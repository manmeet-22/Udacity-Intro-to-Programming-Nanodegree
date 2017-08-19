import webbrowser

class Movie() :
    """ Contains Movie class that contains movie_title, movie_storyline, poster_image, trailer_youtube, movie_release_date"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]   

    #this is the init function
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_release_date) :
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date

    #This function opens the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
