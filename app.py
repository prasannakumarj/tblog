#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from database import Database
from menu import Menu

Database.initialize()

menu = Menu()

menu.run_menu()