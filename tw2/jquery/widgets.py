from base import jQueryJSLink, jQueryCSSLink, jQueryPluginJSLink, jQueryPluginCSSLink
import defaults

jquery_js = jQueryJSLink()

####
####
#### JQuery plugins
####
####

# SwitchView
jswitchview_js = jQueryPluginJSLink(name=defaults._switchview_name_, version=defaults._switchview_version_)
jswitchview_css = jQueryPluginCSSLink(name=defaults._switchview_name_, version=defaults._switchview_version_)
jswitchview = jQueryJSLink(resources=[jswitchview_js, jswitchview_css])

#Jcrop
jcrop_css = jQueryPluginCSSLink(name=defaults._jcrop_name_, version=defaults._jcrop_version_)
jcrop_js = jQueryPluginJSLink(name=defaults._jcrop_name_, version=defaults._jcrop_version_)

# The usable piece, I couldn't figure out a better way to do dependencies
jcrop = jQueryJSLink(resources = [jcrop_js, jcrop_css])


####
####
#### Jquery enabled widgets
####
####

jnullable_js = jQueryPluginJSLink(name=defaults._nullable_name_, version=defaults._nullable_version_)

import tw2.forms.widgets
import tw2.core as twc

class NullableSelectionField(tw2.forms.widgets.SelectionField):
    input_class = 'nullable'
    title_text = twc.Param("Text to use as the tool tip for each radio button", default="Select an option, or click a selected option to deselect it.")
    resources = [jquery_js, jnullable_js]

    def prepare(self):
        super(NullableSelectionField, self).prepare()
        #Add the input_class value to the class list
        for opt in self.options:
            opt[0]['class'] = self.input_class
            opt[0]['title'] = self.title_text

class NullableRadioButtonList(NullableSelectionField, tw2.forms.widgets.RadioButtonList): pass

class NullableRadioButtonTable(NullableSelectionField, tw2.forms.widgets.RadioButtonTable):
    """TODO: Fix the prepare path"""
    pass

