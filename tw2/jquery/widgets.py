from base import jQueryJSLink, jQueryCSSLink, jQueryPluginJSLink, jQueryPluginCSSLink
import defaults

jquery_js = jQueryJSLink()

# SwitchView
jswitchview_js = jQueryPluginJSLink(name=defaults._switchview_name_, version=defaults._switchview_version_)
jswitchview_css = jQueryPluginCSSLink(name=defaults._switchview_name_, version=defaults._switchview_version_)
jswitchview = jQueryJSLink(resources=[jswitchview_js, jswitchview_css])

#Jcrop
jcrop_css = jQueryPluginCSSLink(name=defaults._jcrop_name_, version=defaults._jcrop_version_)
jcrop_js = jQueryPluginJSLink(name=defaults._jcrop_name_, version=defaults._jcrop_version_)

# The usable piece, I couldn't figure out a better way to do dependencies
jcrop = jQueryJSLink(resources = [jcrop_js, jcrop_css])
