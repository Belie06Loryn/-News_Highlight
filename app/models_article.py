class Article:
    """
    Article class to define all objects that we are going to use
    """
    def __init__(self, id, name, author, title, description, url, urlToImage, publishedAt, content):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content