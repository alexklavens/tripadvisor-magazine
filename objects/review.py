class Review:
    def __init__(self,
                location_name = '',
                location_id = '',
                location_placetype = '',
                review_id = '',
                member_id = '',
                username = '',
                content = '',
                rating = '',
                date = ''):
        self.location_name = location_name
        self.review_id = review_id
        self.member_id = member_id
        self.username = username.replace(" ", "")
        self.member_url = "https://tripadvisor.com/members/"+str(self.username)
        self.content = content
        self.rating = rating
        self.rating_img_url = self.getBubbleImg(rating)
        self.date = self.getDateString(date)
        self.location_id = location_id
        self.location_placetype = location_placetype

    def getBubbleImg(self, rating):
        url = "http://www.tripadvisor.com/img/cdsi/img2/ratings/traveler/s" + str(rating)[0] + ".0-MCID-5.svg"
        return url

    def getDateString(self, date):
        months = ['January', 'February', 'March', 'April',
                  'May', 'June', 'July', 'August', 'September',
                  'October', 'November', 'December']
        date = date.split('-')
        return (months[int(date[0])-1] + " " + str(date[1]))
