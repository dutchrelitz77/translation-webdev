# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426082219.727653
_enable_loop = True
_template_filename = '/Users/dutchrelitz77/Dropbox/byu/winter_2015/IS_542/HW/HW10_AjaxFileUpload/code/test_dmp/homepage/templates/tabledemo.html'
_template_uri = 'tabledemo.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['main_center_content2', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def main_center_content2():
            return render_main_center_content2(context._locals(__M_locals))
        initial_page = context.get('initial_page', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_center_content2'):
            context['self'].main_center_content2(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_center_content2(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main_center_content2():
            return render_main_center_content2(context)
        initial_page = context.get('initial_page', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n    \t<h1>Table Demo</h1>\n        <p>Below is a paginated table</p>\n    </div>\n\n    <div id=\'table_container\' data-page=\'')
        __M_writer(str( initial_page ))
        __M_writer('\'>\n    \tTables goes here.\n    </div>\n\n    <div id=\'button_container\'>\n    \t<button id="prev_page_button" class="btn btn-default" type="submit">&larr; Previous Page</button>\n    \t<button id="next_page_button" class="btn btn-default" type="submit">Next Page &rarr;</button>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Tabledemo')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "tabledemo.html", "filename": "/Users/dutchrelitz77/Dropbox/byu/winter_2015/IS_542/HW/HW10_AjaxFileUpload/code/test_dmp/homepage/templates/tabledemo.html", "line_map": {"67": 3, "27": 0, "52": 5, "37": 1, "73": 3, "42": 3, "59": 5, "60": 11, "61": 11, "79": 73}}
__M_END_METADATA
"""
