class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    def __repr__(self) -> str:
        return f"Article(author = {self.author}, magazine={self.magazine}, title={self.title})"

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if type(value) == str and len(value) >= 5 and len(value) <= 50:
            self._title = value

        
class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in Article.all if article.author == self})

    def add_article(self, magazine, title):
        return Article(author=self, magazine=magazine, title=title)

    def topic_areas(self):
        topics_list = list({magazine.category for magazine in self.magazines()})
        if len(topics_list) > 0:
            return topics_list
        else:
            return None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            print("Name can not be changed")
        elif type(name) != str:
            print("Name must be of type string")
        elif len(name) <= 0:
            print("Name must be longer than 0 characters")
        else:
            self._name = name
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in Article.all if article.magazine == self})

    def article_titles(self):
        titles_list = list({article.title for article in self.articles()})
        if len(titles_list) > 0:
            return titles_list
        else:
            return None

    def contributing_authors(self):
        contributors_list = [article.author for article in Article.all if article.magazine == self]
        sorted_list = sorted(contributors_list, key=lambda author: author.name)
        i = 0
        contributing_authors = []
        for author in sorted_list:
            if sorted_list[i] == sorted_list[i + 1]:
                contributing_authors.append(author)
        
        if len(contributing_authors) > 0:
            return contributing_authors
        else:
            return None



    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) == str and len(value) >= 2 and len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if type(value) == str and len(value) > 0:
            self._category = value