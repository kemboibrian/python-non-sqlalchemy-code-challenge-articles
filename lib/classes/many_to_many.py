class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.__class__.all.append(self)
      
      
class Author:
    all = []
    
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name
        self.__class__.all.append(self)
        
    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = {article.magazine.category for article in Article.all if article.author == self}
        return list(categories) if categories else None


class Magazine:
    all = []    

    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Magazine category must be a non-empty string.")
        self._name = name
        self._category = category
        self.__class__.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Magazine category must be a non-empty string.")
        self._category = value
        
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
         return list(set(article.author for article in self.articles()))
     
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None
    
    def contributing_authors(self):
        author_article_count = {}
        for article in self.articles():
            author_name = article.author.name
            if author_name in author_article_count:
                author_article_count[author_name] += 1
            else:
                author_article_count[author_name] = 1
                
        authors = [author for author in self.contributors() if author_article_count[author.name] > 2]
        return authors if authors else None
