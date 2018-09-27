from flask import Flask, render_template
import pickle
import random
from objects.location import Location
from objects.review import Review
from objects.generate_data_set import LocationData


app = Flask(__name__)
location_data = LocationData('data/london.pkl')

@app.route('/')
@app.route('/home')
@app.route('/article')
def index():
    """Sets up homepage """
    col1 = []
    col2 = []
    col3 = []
    columns = [col1, col2, col3]

    for i, location in enumerate(location_data.locations.values()):
        columns[i % 3].append(location)

    return render_template('index.html', col1=columns[0],
                           col2=columns[1], col3=columns[2])




@app.route('/article/<locationid>')
def article(locationid=None):
    """
    Individual POI articles.

    At minimum, one review will populate as content
    """

    # For debugging....
    # import pdb; pdb.set_trace()

    this_location = location_data.getArticle(locationid)

    return render_template('article.html', location=this_location)



"""
The following three endpoints ask the data source for a list of article
filtered by placetype.

For example, /restaurants gets us only restaurant locations
"""

@app.route('/restaurants')
def restaurants():

    """ Filter by restaurants, display vertical """

    return render_template('placetype.html',
                           placetype='Restaurants', feed=location_data.filter_list('restaurant'))


@app.route('/hotels')
def hotels():
    """ Filter by hotels, display vertical """

    return render_template('placetype.html',
                           placetype='Hotels', feed=location_data.filter_list('hotel'))


@app.route('/attractions')
def attractions():
    """ Filter by hotels, display vertical """

    return render_template('placetype.html',
                           placetype='Attractions', feed=location_data.filter_list('attraction'))



@app.errorhandler(404)
def page_not_found(e):
    """ 404 error will return a link to a randomly chosen article """

    link = "/article/" + str(location_data.getRandomLocation())
    return render_template('404.html', link=link), 404


if __name__ == '__main__':
    app.run()
