#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from database import Database
from models.post import Post

post = Post(blog_id="123",
        title="Another great post",
        content="This is some sample content",
        author="Santosh")

post.save_to_mongo()