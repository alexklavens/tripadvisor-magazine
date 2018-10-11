# TripAdvisor Magazine

## About

TripAdvisor Magazine is a magazine-style publication. It's content: the most well-written reviews on TripAdvisor.

There are millions of reviews on TripAdvisor, often containing a few sentences of praise or frustration.
But among those millions, there are some beautiful, compelling, and lengthy travel essays!

## Who

TripAdvisor Magazine is a product I built with a group for TripAdvisor's
summer intern hackathon.

* Alex Klavens -- Data Analytics Intern
* Mihir Ranha -- Data Science Intern
* Jonathan Tseng -- Software Engineering Intern
* Chloe Smith -- Product Management Intern

## Data and Population

We analyzed all reviews of currently-open hotels, restaurants, and attractions in London.

We used TripAdvisor's internal databases and APIs, rather than public-facing ones.

We make the assumption that this project, at any scale, should not depend on real-time data gathering and language processing. Analyzing all reviews -- even just for London -- takes a while! The content is not likely to drastically change at any given moment. See below...

We decided to run database querries and execute NLP offline and store our final results in a way that we could easily process on our server.

In a larger-scale version of this project, this should be done automatically on a reoccuring basis.

## Natural Language Processing

How did we define "good" or "high-quality" writing?

Our NLP algorithm analyzed each review for features such as sentiment, spelling accuracy, word complexity, and more.

We also placed some manual filters in the image of editorial submission standards: a minimum word count, a minimum rating, etc.

## The Web App

We built a Flask application to serve TripAdvisor Magazine

## Which Locations and Reviews Are Eligible?

We used London as our test-case. But for whatever geographic scope, we analyze every hotel, restaurant, or attraction review for any open (not permanently closed) location.

## No APIs

TripAdvisor does have public-facing APIs, but we were unfamiliar with the limitations of that interface. Using internal databases allowed us to access review and location data in a more holistic way. These databases are also what we had been using for our normal jobs all summer.


We recognize that a large-scale implementation of this project would involve adjustments to allow for regularly scheduled NLP-based content decisions.

We used internal databases to pull review and location data. This project only covers one city, but even that involved sorting through every review

## Deployment

During the hackathon, we hosted the application on our laptops. 

Now, its deployed on a Heroku server that uses this github repository as its source

## Future Project Ideas

Ideally, this project is entirely independent of access to internal databases. It is possible that one could conduct a similar data gathering process using their public-facing APIs. However, our project depended on internal datasets and the company's database server power to access that information in a reasonable amount of time.
