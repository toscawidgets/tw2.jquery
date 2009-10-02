from tw2.core import Widget
from base import jQueryJSLink, jQueryCSSLink, jQueryPluginJSLink, jQueryPluginCSSLink
import defaults

jquery_js = jQueryJSLink()


#Jcrop
jcrop_css = jQueryPluginCSSLink(name=defaults._jcrop_name_, version=defaults._jcrop_version_)
jcrop_js = jQueryPluginJSLink(name=defaults._jcrop_name_, version=defaults._jcrop_version_)

# The usable piece, I couldn't figure out a better way to do dependencies
jcrop = jQueryJSLink(resources = [jcrop_js, jcrop_css])
