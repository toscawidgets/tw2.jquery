from tw2.core.testbase.base import WidgetTest
import tw2.jquery.widgets as twjqwidgets

class TestjQueryJS(WidgetTest):
    widget = twjqwidgets.jquery_js
    attrs = {}
    params = {}
    expected = """
<script type="text/javascript" src="/resources/tw2.jquery/static/jquery/1.4.4/jquery.js"></script>
"""

