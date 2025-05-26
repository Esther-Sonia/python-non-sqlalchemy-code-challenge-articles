class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            pass
        else:
            self._title = value
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        self._magazine = value


class Author:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            pass
        else:
            self._name = value
    
    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        author_magazines = []
        for article in self.articles():
            if article.magazine not in author_magazines:
                author_magazines.append(article.magazine)
        return author_magazines
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        if not self.articles():
            return None
        
        categories = []
        for magazine in self.magazines():
            if magazine.category not in categories:
                categories.append(magazine.category)
        return categories


class Magazine:
    all_magazines = []
    
    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine.all_magazines.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    
    def contributors(self):
        authors = []
        for article in self.articles():
            if article.author not in authors:
                authors.append(article.author)
        return authors
    
    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]
    
    def contributing_authors(self):
        author_counts = {}
        
        for article in self.articles():
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        
        prolific_authors = [author for author, count in author_counts.items() if count > 2]
        
        return prolific_authors if prolific_authors else None
    
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        
        magazine_counts = {}
        
        for article in Article.all:
            magazine = article.magazine
            if magazine in magazine_counts:
                magazine_counts[magazine] += 1
            else:
                magazine_counts[magazine] = 1
        
        if not magazine_counts:
            return None
        
        top_magazine = max(magazine_counts.keys(), key=lambda mag: magazine_counts[mag])
        return top_magazine