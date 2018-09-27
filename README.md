# TripAdvisor Magazine

## About

TripAdvisor Magazine is a magazine-style publication. It's content: the most well-written reviews on TripAdvisor.

TripAdvisor Magazine is a product I built with a group for TripAdvisor's
summer intern hackathon.

* Alex Klavens -- Data Analytics Intern
* Mihir Ranha -- Data Science Intern
* Jonathan Tseng -- Software Engineering Intern
* Chloe Smith -- Product Management Intern

My mom *loves* writing reviews on TripAdvisor. She takes the time to write throughough, informative, and helpful reviews.

I thought that amongst the millions of travel reviews already on TripAdvisor, there must be some examples of incredibly high-quality writing, and that TripAdvisor users might .


## Data and Population

We make the assumption that this project, at any scale, should not depend on real-time data gathering and language processing.

We decided to run database querries and execute NLP offline and store our final results in a way that we could easily process on our server.

In a larger-scale version of this project, this should be done automatically on a reoccuring basis.




## Natural Language Processing

## The CMS

## Which Locations and Reviews Are Eligible?

We used London as our test-case. But for whatever geographic scope, we analyze every hotel, restaurant, or attraction review for any open (not permanently closed) location.

## No APIs

TripAdvisor does have public-facing APIs, but we were unfamiliar with the limitations of that interface. Using internal databases allowed us to access review and location data in a more holistic way. These databases are also what we had been using for our normal jobs all summer.


We recognize that a large-scale implementation of this project would involve adjustments to allow for regularly scheduled NLP-based content decisions.

We used internal databases to pull review and location data. This project only covers one city, but even that involved sorting through every review



## Future Project Ideas

Ideally, this project is entirely independent of access to internal databases. It is possible that one could conduct a similar data gathering process using their public-facing APIs. However, our project depended on internal datasets and the company's database server power to access that information in a reasonable amount of time.
