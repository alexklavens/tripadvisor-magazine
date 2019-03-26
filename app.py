from flask import Flask, render_template
import pickle
import random
from objects.location import Location
from objects.review import Review
from objects.generate_data_set import LocationData
import contentful_management
import random



app = Flask(__name__)
# location_data = LocationData('data/london.pkl')


client = contentful_management.Client(
    'CFPAT-575c4a976867c13f14b4ae41fb51061900f18a04304086d56a5db291d850a10c'
)
space = client.spaces().find("3yc8cq6akrvk")
locations = client.content_types('3yc8cq6akrvk','master').find('location')
reviews = client.content_types('3yc8cq6akrvk','master').find('location')

@app.route('/')
@app.route('/home')
@app.route('/article')
def index():
    """Sets up homepage """
    col1 = []
    col2 = []
    col3 = []
    columns = [col1, col2, col3]

    for i, location in enumerate(locations.entries().all()):
        columns[i % 3].append(location)

    return render_template('index.html', col1=columns[0],
                           col2=columns[1], col3=columns[2])


@app.route('/article/<locationid>')
def article(locationid=None):
    this_location = locations.entries().find(locationid)

    return render_template('article.html', location=this_location,reviews=reviews)



"""
The following three endpoints ask the data source for a list of article
filtered by placetype.

For example, /restaurants gets us only restaurant locations
"""


@app.route('/restaurants')
def restaurants():

    """ Filter by restaurants, display vertical """

    return render_template('placetype.html',
                           placetype='Restaurants', feed=locations.entries().all())


@app.route('/hotels')
def hotels():
    """ Filter by hotels, display vertical """

    return render_template('placetype.html',
                           placetype='Hotels', feed=locations.entries().all())


@app.route('/attractions')
def attractions():
    """ Filter by hotels, display vertical """

    return render_template('placetype.html',
                           placetype='Attractions', feed=locations.entries().all())



@app.errorhandler(404)
def page_not_found(e):
    location_ids = [item.id  for item in locations.entries().all()]
    random.shuffle(location_ids)

    link = "/article/" + location_ids[0]
    return render_template('404.html', link=link), 404


if __name__ == '__main__':
    app.run()
