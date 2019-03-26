class Location:
    def __init__(self,
                name = '',
                location_id = '',
                placetype_name = '',
                # reviews = '',
                image_url = ''):
        self.name = name
        self.location_id = location_id
        self.placetype_name = placetype_name
        self.article_url = '/article/' + str(location_id)
        # self.reviews = reviews
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

    def getReviewPreviewContentful(self,review):
        r = review
        if len(r) < 290:
            return r
        else:
            plus = r[270:].find(" ")
            preview = r[0:270+plus]
            return preview + "..."

    def __str__(self):
        return (self.name + ' has ' + str(len(self.reviews)) + ' reviews.')
