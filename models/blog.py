import datetime
import uuid
from models.post import Post
from database import Database

class Blog(object):
    def __init__(self, author, title, description, id_=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id_ is None else id_

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date (DDMMYYYY), blank == today: ")
        post = Post(blog_id=self.id,
                title=title,
                content=content,
                author=self.author,
                date=datetime.datetime.strptime(date, "%d%m%Y"))
        post.save_to_mongo()

    def get_posts(self):
        Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection="blogs",
                        data=self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def get_from_mongo(cls, id):
        blog_data = Database.find_one(collection="blog",
                                        query={'id': id})
        return cls(blog_data['author'],
                    title=blog_data['title'],
                    description=blog_data['description'],
                    id_=blog_data['id'])
