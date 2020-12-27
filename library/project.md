# the library

browse, search, and download books via a browser.

frontend: browser ui. user makes an AJAX request to the backend, which returns json containing the list of relevant resources.

backend: user requests either a book or information about books. the file is returned, or, json containing the information
the appropriate way to serve static files seems to be invoking uwsgi with --static-map /data=data, for example. 

storage: sql database stores filename (md5), title, author, and tags.

