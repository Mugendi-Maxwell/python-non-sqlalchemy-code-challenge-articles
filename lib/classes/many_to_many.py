class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        if not isinstance(title, str):
            raise TypeError("Title must be of type str")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters, inclusive")

        self._author = author
        self._magazine = magazine
        self._title = title

        # Adding the article to the author's and magazine's records
        author.add_article(self)
        magazine.add_article(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise TypeError("author must be an instance of Author")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        self._magazine = new_magazine

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def add_article(self, article):
        if not isinstance(article, Article):
            raise TypeError("article must be an instance of Article")
        self._articles.append(article)

    @property
    def articles(self):
        return self._articles

    def magazines(self):
        #  magazines for which the author has written articles
        return list({article.magazine for article in self._articles})

    def topic_areas(self):
        #  categories from the articles' magazines
        return list({article.magazine.category for article in self._articles})





class Magazine:
    #
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        self._name = name

        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = category

        self._articles = []

        # Appending this magazine instance to the class-level `all_magazines` list
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    @property
    def articles(self):
        return self._articles

    def add_article(self, article):
        if not isinstance(article, Article):
            raise TypeError("Must be an instance of Article")
        self._articles.append(article)

    def contributors(self):
        # Returning unique list of authors for this magazine
        return list({article.author for article in self._articles})

    def article_titles(self):
        # Returning list of article titles
        return [article.title for article in self._articles]

    @classmethod
    def top_publisher(cls):
        
        if not cls.all_magazines:
            return None
        return max(cls.all_magazines, key=lambda magazine: len(magazine.articles))


# tesing output
author1 = Author("Mark Goldbrigde")
author2 = Author("Mark Twain")

magazine1 = Magazine("London post", "sports")
magazine2 = Magazine("Big think", "Science")

article1 = Article(author1, magazine1, "The Art of code")
article2 = Article(author1, magazine2, "The Science of Storytelling")
article3 = Article(author2, magazine1, "London is blue")


print("Articles by Mark Goldbridge:")
for article in author1.articles:
    print(article.title)

print("\nMagazines Mark Goldbridge has written for:")
for magazine in author1.magazines():
    print(magazine.name)

print("\nArticles in sports:")
for title in magazine1.article_titles():
    print(title)

print("\nContributors to London post:")
for contributor in magazine1.contributors():
    print(contributor.name)


print("\nTopic areas by Mark Goldbridge:")
for topic in author1.topic_areas():
    print(topic)


print("\nMagazine with the most articles:")
print(Magazine.top_publisher().name)
