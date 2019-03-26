############ This module is from an older version of the project. It took in a pickle file
############ with all the data and created python objects to serve to the site.
############ The site now uses the Contentful CMS. The data has not changed,
############ but I altered the project to learn more about CMS integration



# This module exists to transform a pickle object into a python dictionary
# That dictionary will act as the data source for content management


import random
import pickle
from objects.review import Review
from objects.location import Location



class LocationData:

    def __init__(self,pickle_file):
        self.locations = self.makeData(pickle_file)

    def makeData(self,pickle_file):
        """
        Returns a dictionary with
            (key:value) as (location_id:location object)
        """
        data = pickle.load(open(pickle_file, 'rb'))
        data = data.sample(frac=1, random_state=137)
        locations = {}
        for row in data.iterrows():
            item = row[1]
            thisReview = Review(review_id=item.review_id, member_id=item.member_id,
                                username=item.member_username, content=item.review_text,
                                rating=item.review_rating, date=item.date)
            if item.location_id not in locations:
                locations[item.location_id] = Location(name=item.location_name,
                                                       location_id=item.location_id,
                                                       placetype_name=item.location_placetype,
                                                       reviews=[], image_url='/static/images/' + str(item.location_id) + '.jpg')

            locations[item.location_id].addReview(thisReview)

        return locations

    def getArticle(self,locationid):
        return self.locations.get(int(locationid))


    def filter_list(self,placetype_name):
        """
        Returns a filtered list of location objects based on a
        placetype subset of Restaurants, Hotels, or Attractions
        """
        result = []
        for location in self.locations.values():
            if location.placetype_name == placetype_name:
                result.append(location)
        return result


    def getRandomLocation(self):
        return random.choice(list(self.locations))
