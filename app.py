#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from database import Database
from models.post import Post

Database.initialize()

post = Post.from_mongo('60bb58501eef4b0d91bf2808158f808d')

__import__("pprint").pprint(post)