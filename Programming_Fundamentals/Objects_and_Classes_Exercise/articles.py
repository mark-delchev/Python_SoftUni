class Article:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, content):
        self.content = content

    def change_author(self, author):
        self.author = author

    def rename(self, title):
        self.title = title

    def __repr__(self):
        return f"{self.title} - {self.content}: {self.author}"


article = Article(
    "Highest Recorded Temperature",
    "Temperatures across Europe are unprecedented, according to scientists.",
    "Ben Turner"
)
article.edit(
    "Syracuse, a city on the coast of the Italian island of Sicily, registered temperatures of 48.8 degrees Celsius"
)
article.rename(
    "Temperature in Italy"
)
article.change_author(
    "B. T."
)
print(article)
