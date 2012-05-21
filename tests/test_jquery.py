from nose.tools import eq_
import tw2.core as twc

def request_local_tst():
    global _request_local, _request_id
#    if _request_id is None:
#        raise KeyError('must be in a request')
    if _request_local == None:
        _request_local = {}
    try:
        return _request_local[_request_id]
    except KeyError:
        rl_data = {}
        _request_local[_request_id] = rl_data
        return rl_data

twc.core.request_local = request_local_tst
_request_local = {}
_request_id = 'whatever'

def setUp():
    twc.core.request_local = request_local_tst
    twc.core.request_local()['middleware'] = twc.make_middleware()


def test_jquery_resource():
    from tw2.jquery import jquery_js
    the_link = '/resources/tw2.jquery/static/jquery/1.7.1/jquery.js'
    eq_(jquery_js.req().link, the_link)

def test_jquery_js_function():
    from tw2.jquery import jQuery
    eq_(str(jQuery('foo')), 'jQuery("foo")')

def test_jquery_script_name():
    twc.core.request_local()['middleware'] = \
        twc.make_middleware(script_name='/lol')
    from tw2.jquery import jquery_js
    twc.core.request_local()['middleware'].script_name = '/lol'
    the_link = '/lol/resources/tw2.jquery/static/jquery/1.7.1/jquery.js'
    eq_(jquery_js.req().link, the_link)

def test_jquery_external():
    from tw2.jquery import jquery_js
    jquery_js.external = True
    the_link = 'http://ajax.googleapis.com/ajax/libs/jquery/1.7.1//jquery.js'
    eq_(jquery_js.req().link, the_link)

def test_jquery_custom():
    from tw2.jquery import jquery_js
    the_link = "/foo/bar/jquery.js"
    jquery_js.link = the_link
    eq_(jquery_js.req().link, the_link)
