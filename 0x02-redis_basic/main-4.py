#!/usr/bin/python3
"""
    main-4
"""
import redis


get_page = __import__('web').get_page
print(get_page("http://slowwly.robertomurray.co.uk"))
