from database import Database

class Post:
    def __init__(self, blog_id, title, content, author, date, id_):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = id_

    def save_to_mongo(self):
        Database.insert(collection='posts',
                self.json())

    def json(self):
        return {
                'id': self.id,
                'blog_id': self.blog_id, 
                'author': self.author,
                'content': self.content,
                'title': self.title,
                'created_date': self.created_date
                }

    @staticmethod
    def from_mongo(id_):
        """Given ID, return content.

        :param id: ID of the post
        :returns data: Content from the post ID

        """
        return Database.find_one(collection='posts', query={'id': id_})

    @staticmethod
    def from_blog(id_):
        return [post for post in Database.find('posts', query={'blog_id': id_})]
