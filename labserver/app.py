import cgi
import os
import magic

import panserv
import dirserv

from config import labroot, cachedir

def application(environ, start_response):
    try:
        
        t = 'text/html'
        
        request = environ['REQUEST_URI']
        assert len(request) >= 5 and request[:5] == "/lab/"
        request = request[1:]
        absrequest = os.path.join(labroot, request)
        assert os.path.exists(absrequest)

        if os.path.isdir(absrequest):
            # request is a directory
            source = absrequest
            midtarget = '/tmp/index.md'
            target = os.path.join(cachedir, request, 'index.html')
            try:
                os.makedirs(os.path.split(target)[0])
            except FileExistsError:
                # happens if dir exists already
                pass
            assert dirserv.gen(source, midtarget)[0] == 0
            assert panserv.gen(midtarget, target)[0] == 0

        else:
            # request is a file


            # get file extension
            ft = os.path.splitext(request)[1]

            # handle markdown files
            if ft == '.md':
                source = absrequest
                target = os.path.join(cachedir, request+'.html')
                try:
                    os.makedirs(os.path.split(target)[0])
                except FileExistsError:
                    # happens if dir exists already
                    pass
                assert panserv.gen(source, target)[0] == 0
                
            else:
            	# 2020 12 26: set up as a way to serve static files. required to embed images in html pages.
                mime = magic.Magic(mime=True)
                t = mime.from_file(os.path.join(labroot, request))
                target = os.path.join(labroot, request)

        
        start_response('200 OK', [('Content-Type', t)])
        f = open(target, "rb")
        cont = f.read()
        f.close()
        return cont

    except AssertionError:

        return 0
