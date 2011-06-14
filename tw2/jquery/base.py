from tw2.core.params import Param
from tw2.core import CSSLink, DirLink, JSLink, js_function
from version import JSLinkMixin

import defaults

class jQueryLinkMixin(JSLinkMixin):
    name = 'jquery'
    dirname = defaults._dirname_
    basename = defaults._basename_
    version = defaults._version_
    url_base = defaults._url_base_

    modname = 'tw2.jquery'

class jQueryJSLink(JSLink, jQueryLinkMixin):
    pass
class jQueryCSSLink(jQueryLinkMixin, CSSLink):
    extension = 'css'

class jQueryPluginLinkMixin(jQueryLinkMixin):
    dirname =   Param('(string) Specify the directory path for the given file, relative to the "static" folder some substitutions are allowed. Default: %s' % defaults._plugin_dirname_, default=defaults._plugin_dirname_)
    basename =  Param('(string) Specify the basename for the given file. Default: %s' % defaults._plugin_basename_, default=defaults._plugin_basename_)
    subdir = Param('(string) Specify the subdirectory that this link is found in.  Default: %s' % defaults._plugin_subdir_, default=defaults._plugin_subdir_)

    @property
    def substitutions(self):
        subs = super(jQueryPluginLinkMixin, self).substitutions
        subs.update(dict(subdir=self.subdir))
        return subs

class jQueryPluginJSLink(JSLink, jQueryPluginLinkMixin):
    subdir = 'js'

class jQueryPluginCSSLink(jQueryPluginLinkMixin, CSSLink):
    subdir = 'css'
    extension = 'css'

jquery_js = jQueryJSLink()
jQuery = js_function('jQuery')
