from base import jQueryJSLink, jQueryCSSLink, jQueryPluginJSLink, jQueryPluginCSSLink
import defaults

jquery_js = jQueryJSLink()


#Jcrop
jcrop_js = jQueryPluginJSLink(name=defaults._jcrop_name_, version=defaults._jcrop_version_)
jcrop_css = jQueryPluginCSSLink(name=defaults._jcrop_name_, version=defaults._jcrop_version_, additional_files = ['Jcrop.gif'])
