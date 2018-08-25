#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from database import Database
from models.post import Post

Database.initalize()

post = Post()
post2 = Post()
post2.content = "Some different content"

print(post.content)
print(post2.content)
