import sqlite3
from bottle import route, run, SimpleTemplate, template, debug, request, static_file, error
import re

#
# show all bookmarks
#
@route('/') # also make this the default route
@route('/list/all')
def listall():

    # get bookmarks
    conn = sqlite3.connect('melicious.db')
    c = conn.cursor()
    c.execute("SELECT bookmark, tags FROM bookmarks")
    result = c.fetchall()
    c.close()

    # get tags
    conn = sqlite3.connect('melicious.db')
    t = conn.cursor()
    t.execute("SELECT DISTINCT tags FROM bookmarks")
    tags = t.fetchall()
    t.close()
    output = template('list_all_template', rows=result, tagrows=tags)
    return output

#
# add a bookmark
# TODO This is now handled with a jquery reveal. Remove this route if
# it becomes an orphan.
#
@route('/add')
def add(action="form"):
    return template ('add_template', action=action)

#
# save the new bookmark
#
@route('/new', method='GET')
def new_item():
	bookmark = request.GET.get('bookmark', '').strip()
	tags = request.GET.get('tags', '').strip()
	conn = sqlite3.connect('melicious.db')
	c = conn.cursor()
	c.execute("INSERT INTO bookmarks (bookmark,tags) VALUES (?,?)", (bookmark, tags))
	new_id = c.lastrowid
	conn.commit()
	c.close()
	#return '<p>The new bookmark was inserted into the database, the ID is %s</p>' % new_id
	output = template('save_complete_template', dbsaid='The new bookmark was inserted into the database, the ID is %s' % new_id)
	return output

#
# delete a bookmark
#
@route('/delete/:url', method='GET')
def del_row(url):
	#return "i will delete %s " % url #debug
        #change triple colon back to slash 
        p = re.compile(':::')
        slash = p.sub( '/', url)
	conn = sqlite3.connect('melicious.db')
	c = conn.cursor()
	query = "DELETE FROM bookmarks WHERE bookmark like '%%%s';" % slash.strip()
	c.execute(query)
	conn.commit()
	c.close()
	return '<p>Bookmark for %(url)s deleted! <a href="/">continue</a></p>' % {"url": slash}
	#return '<p>Bookmark for %(url)s deleted! %(query)s <a href="/">continue</a></p>' % {"url": slash, "query": query} #debug

#
# 404
#
#@error(404)
#def error404(error):
#    return 'Nothing here, sorry. <a href="/">home</a>'


#
# run like the wind
#
debug(True) # turn off in production
#run(host='localhost', port=8080) # production
run(reloader=True, host='localhost', port=8080) #test

