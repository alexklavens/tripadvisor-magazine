# TripAdvisor Magazine

[TripAdvisor Magazine](https://tripadvisor-magazine.herokuapp.com) is a web-based magazine-style publication that identifies high quality travel reviews with [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing) and features them as articles.

There are millions of reviews on TripAdvisor, often containing a few sentences of praise or frustration. But among those millions, there are some beautiful, compelling, and lengthy travel essays!

TripAdvisor Magazine is a new form of travel media. Its content comes from a non-editorial context, one where a consumer experience is featured in the context of a business profile.

__UPDATE: The current version of TripAdvisor Magazine uses Contentful as its CMS. Though the data behind the current project has not changed and will not change, I altered this project to learn about how to integrate a formal CMS.__

## The Magazine and Its Content

Many of the articles in TripAdvisor Magazine truly are incredible. All are original reviews that were identified as the best of the best. None of the content has been manipulated (no editing, no punctuation fixes, etc.). Here are a few examples of my favorites:

__This piece on the [Charles Dickens Museum](https://tripadvisor-magazine.herokuapp.com/article/188889)__ is the story of someone who rediscovered some of their favorite childhood literature.
> "More than any other London attraction, I felt a knot of excitement in my stomach as I turned into Doughty St. and made my way to No. 48. And there it was; standing unadorned except for two discrete signs proclaiming its famous former occupant."

Here's a piece on the [Vanilla Black](https://tripadvisor-magazine.herokuapp.com/article/1215838) restaurant. It's incredibly descriptive of both experience and food.

And here's __[a piece on Buckingham Palace](https://tripadvisor-magazine.herokuapp.com/article/187549)__ about someone whose experience was greatly enhanced by the location's handicap accessiblity.

Just to be clear: not every article in TripAdvisor Magazine is going to win a Pulitzer! Our NLP algorithm was not perfect. There are some examples of frightening capitalization. But please go read through some of them!

## Who, What, When

TripAdvisor Magazine is a product I built with a group for TripAdvisor's
summer intern hackathon during July 2018.

* Alex Klavens -- Data Analytics Intern
* Mihir Ranha -- Data Science Intern
* Chloe Smith -- Product Management Intern
* Jonathan Tseng -- Software Engineering Intern

## Data and Population

We analyzed all reviews of currently-open hotels, restaurants, and attractions in London.

We used TripAdvisor's internal databases and APIs, rather than public-facing ones.

We make the assumption that this project, at any scale, should not depend on real-time data gathering and language processing. Analyzing all reviews -- even just for London -- takes a while!

We decided to run database queries and execute NLP offline and store our final results in a way that we could easily process on our server.

## Natural Language Processing

How did we define "good" or "high-quality" writing?

Our NLP algorithm analyzed each review for features such as sentiment, spelling accuracy, word complexity, and more.

We also placed some manual filters in the image of editorial submission standards: a minimum word count, a minimum rating, etc.

The final product of the language processing was a table where each row was a review. The process exports a Pickle object containing the table as a Pandas DataFrame.

## Contentful Data Import

The new version of TripAdvisor Magazine pulls its data from Contentful. At a real world magazine, an editor might upload articles to their CMS. Now that can theoretically happen with TripAdvisor Magazine.

Rather than manually inputing the data for the existing articles, I used Contentful's content management API to upload individual reviews, and then make articles out of those reviews. The project's images have not been integrated into Contentful. The processes for this can be found in the ```contentful_import.py``` file.

## The Web App

#### Pre-CMS

We built a Flask application to serve TripAdvisor Magazine using Jinja HTML templating. The app unpacks the Pickle object and uses the Pandas dataframe to generate review and location objects. Each location has a unique id, which is also the same id for that business used in TripAdvisor's main databases and website.

The site serves three main types of page templates: a home page featuring previews of all available articles, a template for the three verticals (hotels, restaurants, attractions), and an article template.

#### Current, with the CMS

The Flask app continues to serve TripAdvisor Magazine using Jinja templating. Rather than getting data from a Pickle object, the app makes calls to Contentful's Content Management API.

#### The Article

An 'article' on TripAdvisor Magazine has a one-to-one relationship with businesses featured on the site. In some cases, the NLP algorithm found high-quality reviews for the same business. We put a cap on three reviews per business.

So an article format is as follows:

__headline__: business name

__image__: business image

__reviews__: one to three reviews

__link__: link to the businesses TripAdvisor page

## No APIs

TripAdvisor does have public-facing APIs, but we were unfamiliar with that interface and any possible limitations it might come with. Using internal databases allowed us to access review and location data in a more holistic way. These databases are also what we had been using for our normal jobs all summer.

We recognize that a large-scale implementation of this project would involve adjustments to allow for regularly scheduled NLP-based content decisions.

## Photography

We chose to focus the project on language processing and front-end web development to best display our findings.

There are less than 30 locations featured on TripAdvisor Magazine, so we chose to find photos for each of those manually.

## Deployment

During the hackathon, we hosted the application on our laptops.

After the summer, I deployed TripAdvisor Magazine to a Heroku server that uses this GitHub repository as its source.

## Mobile Web.

The updated version of TripAdvisor Magazine contains small CSS changes that make the website look much prettier on mobile web.

## Future Project Ideas

The next major steps in developing TripAdvisor Magazine are to expand location coverage and to set up continuous NLP execution.

Another next step would be to rebuild the data collection process around what is possible with public-facing APIs.
Ideally, this project would also be entirely independent of access to internal databases. Our project depended on internal datasets and the company's database server power to access that information in a reasonable amount of time.
