#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from database import Database
# from models.post import Post
from models.blog import Blog

Database.initialize()

blog = Blog(author="Santosh",
        title="Sample title",
        description="Sample description")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts)