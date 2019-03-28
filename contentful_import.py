import random
import pickle
from objects.review import Review
from objects.location import Location
import contentful_management
import pprint

import os
CLIENT_ID = "CFPAT-575c4a976867c13f14b4ae41fb51061900f18a04304086d56a5db291d850a10c" #os.environ["CLIENT"]
SPACE_ID =  "3yc8cq6akrvk" #os.environ["SPACEID"]

def makeContentfulObject(pythonObject,content_type):
    """
    Takes a python object and turns it into a dictionary that will satisfy a contentful object
    """
    contentfulObject = {}
    contentfulObject["content_type_id"] = str(content_type)

    fields = {}
    for i in pythonObject.__dict__:
        fields[str(i)] = {
            'en-US': str(eval("pythonObject."+str(i)))
        }

    contentfulObject['fields'] = fields

    return contentfulObject

def postToContentful(python_object,content_type):
    client = contentful_management.Client(
        CLIENT_ID
    )
    space = client.spaces().find(SPACE_ID)


    thisPost = makeContentfulObject(python_object,content_type)


    if content_type == 'review':
        id = python_object.review_id
    elif content_type == 'location':
        id = python_object.location_id

    new_entry = client.entries(space.id,'master').create(
        id,
        thisPost
    )


def makeLocationObjects():
    # content_types = client.content_types(SPACE_ID).all()
    client = contentful_management.Client(
        CLIENT_ID
    )

    # content_type = client.content_types(SPACE_ID,'master').find('review')
    # entries = space.entries().all()
    space = client.spaces().find(SPACE_ID)
    reviews = client.content_types(SPACE_ID,'master').find('review')
    locations = client.content_types(SPACE_ID,'master').find('location')

    all_reviews = reviews.entries().all()

    review_locations = {}
    for review in all_reviews:
        if review.location_id not in review_locations:
            review_locations[review.location_id] = []

        review_locations[review.location_id].append(review.review_id)

    for location_id, reviews_by_location in review_locations.items():
        first_review = reviews.entries().find(reviews_by_location[0])
        newLocation = Location(
                        name = first_review.location_name,
                        location_id = first_review.location_id,
                        placetype_name = first_review.location_placetype,
                        # image_url = getImageURLByLocationId(location_id))
                        image_url = '/static/images/' + str(first_review.location_id) + '.jpg')
        postToContentful(newLocation,'location')

        #### add review links
        location_entry = locations.entries().find(location_id)

        review_links =[]
        for review_id in reviews_by_location:
            new_link = {
              "sys": {
                "type": "Link",
                "linkType": "Entry",
                "id": review_id
              }
            }
            review_links.append(new_link)

        location_entry.reviews = review_links
        location_entry.save()


        location_entry.location_preview = newLocation.getReviewPreviewContentful(first_review.content)
        location_entry.save()


def makeReviewObjects():
    pickle_file = 'data/london.pkl'
    data = pickle.load(open(pickle_file, 'rb'))

    data = pickle.load(open(pickle_file, 'rb'))
    data = data.sample(frac=1, random_state=137)

    for row in data.iterrows():
        item = row[1]
        thisReview = Review(
                            location_name =  item.location_name,
                            location_id = item.location_id,
                            location_placetype = item.location_placetype,
                            review_id=item.review_id,
                            member_id=item.member_id,
                            username=item.member_username,
                            content=item.review_text,
                            rating=item.review_rating,
                            date=item.date)

        postToContentful(thisReview,'review')


def setToPublished():
    client = contentful_management.Client(
        CLIENT_ID
    )
    space = client.spaces().find(SPACE_ID)
    reviews = client.content_types(SPACE_ID,'master').find('review')
    locations = client.content_types(SPACE_ID,'master').find('location')

    all_reviews = reviews.entries().all()
    all_locations = locations.entries().all()

    for item in all_reviews:
        item.publish()

    for item in all_locations:
        item.publish()



# def getImageURLByLocationId(location_id):
#     client = contentful_management.Client(
#         CLIENT_ID
#     )
#     # space = client.spaces().find(SPACE_ID,'master')
#     assets = client.assets(SPACE_ID,"master").all()
#
#     # assets = space.assets().all()
#     for item in assets:
#         if item.title == location_id:
#             return item.url()

def seeData():
    client = contentful_management.Client(
        CLIENT_ID
    )
    space = client.spaces().find(SPACE_ID)
    reviews = client.content_types(SPACE_ID,'master').find('review')
    locations = client.content_types(SPACE_ID,'master').find('location')
    these_reviews = (locations.entries().find("236350").reviews)

    thisLocation = locations.entries().find("236350")
    for item in thisLocation.reviews:
        print(item.id)




def main():
    # makeReviewObjects()
    # makeLocationObjects()
    # setToPublished()
    # print(getImageURLByLocationId("1215838"))
    # addImages()

if __name__ == '__main__':
    main()
