from urllib.parse import urlparse


class UrlParser(object):
    """
        Base Url parser object

    """
    def __init__(self, url):
        self.url = url

    def get_youtube_id(self):
        parse = urlparse(self.url)
        return parse.query.split("=")[1]

    def get_background_image(self):
        youtube_id = self.get_youtube_id()
        # hqdefault => maxresdefault
        return "https://img.youtube.com/vi/{}/hqdefault.jpg".format(youtube_id)

    def __str__(self):
        return "{}".format(self.url)
