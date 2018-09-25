from flask import Flask, render_template
import pickle
import random


class Location:
    def __init__(self, name, placetype_name, reviews,
                 image_url, location_id=None):
        self.name = name
        self.placetype_name = placetype_name
        self.article_url = '/article/' + str(location_id)
        self.reviews = reviews
        self.image_url = image_url
        self.ta_url = "https://tripadvisor.com/" + str(location_id)

    def addReview(self, review_obj):
        self.reviews.append(review_obj)
        self.review_preview = self.getReviewPreview()

    def getReviewPreview(self):
        r = self.reviews[0].content
        if len(r) < 290:
            return r
        else:
            plus = r[270:].find(" ")
            preview = r[0:270+plus]
            return preview + "..."

    def __str__(self):
        return (self.name + ' has ' + str(len(self.reviews)) + ' reviews.')


class Review:
    def __init__(self, review_id, member_id, username, content, rating, date):
        self.review_id = review_id
        self.member_id = member_id
        self.username = username.replace(" ", "")
        self.member_url = "https://tripadvisor.com/members/"+str(self.username)
        self.content = content
        self.rating = self.getBubbleImg(rating)
        self.date = date
        self.date_string = self.getDateString(date)

    def getBubbleImg(self, rating):
        url = "http://www.tripadvisor.com/img/cdsi/img2/ratings/traveler/s" + str(rating)[0] + ".0-MCID-5.svg"
        return url

    def getDateString(self, date):
        months = ['January', 'February', 'March', 'April',
                  'May', 'June', 'July', 'August', 'September',
                  'October', 'November', 'December']
        date = date.split('-')
        return (months[int(date[0])-1] + " " + str(date[1]))


def makeData(pickle_file='data/london.pkl'):
    """ Returns a dictionary with (key:value) as (location_id:location object) """
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


def getRandomLocation(locations):
    return random.choice(list(locations))


app = Flask(__name__)
locations = makeData()


@app.route('/')
@app.route('/home')
@app.route('/article')
def index():
    col1 = []
    col2 = []
    col3 = []
    columns = [col1, col2, col3]

    for i, location in enumerate(locations.values()):
        columns[i % 3].append(location)
    #
    # for i in range(len(locations.keys())):
    #     columns[i % 3].append(locations[i])

    return render_template('index.html', col1=columns[0],
                           col2=columns[1], col3=columns[2])


@app.route('/restaurants')
def restaurants():
    return render_template('placetype.html',
                           placetype='Restaurants', feed=filter_list('restaurant'))


@app.route('/hotels')
def hotels():
    return render_template('placetype.html',
                           placetype='Hotels', feed=filter_list('hotel'))


@app.route('/attractions')
def attractions():
    return render_template('placetype.html',
                           placetype='Attractions', feed=filter_list('attraction'))


@app.route('/article/<locationid>')
def article(locationid=None):
    # import pdb; pdb.set_trace()
    this = locations.get(int(locationid))

    return render_template('article.html', location=this)


@app.errorhandler(404)
def page_not_found(e):
    link = "/article/" + str(getRandomLocation(locations))
    return render_template('404.html', link=link), 404


def filter_list(placetype_name):
    result = []
    for location in locations.values():
        if location.placetype_name == placetype_name:
            result.append(location)
    return result

if __name__=='__main__':
    app.run()
