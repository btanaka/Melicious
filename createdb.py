import sqlite3
con = sqlite3.connect('melicious.db') # Warning: This file is created in the current directory
con.execute("CREATE TABLE bookmarks (id INTEGER PRIMARY KEY, bookmark char(100) NOT NULL, tags char(100) NOT NULL)")
con.execute("INSERT INTO bookmarks (bookmark,tags) VALUES ('http://python.org', '#python')")