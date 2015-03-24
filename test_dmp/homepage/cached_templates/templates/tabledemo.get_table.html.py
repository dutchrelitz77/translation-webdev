# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426124684.548023
_enable_loop = True
_template_filename = '/Users/dutchrelitz77/Dropbox/byu/winter_2015/IS_542/HW/HW10_AjaxFileUpload/code/test_dmp/homepage/templates/tabledemo.get_table.html'
_template_uri = 'tabledemo.get_table.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        table = context.get('table', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        table = context.get('table', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        __M_writer(str( table ))
        __M_writer('\n    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "52": 3, "53": 5, "54": 5, "27": 0, "60": 54, "45": 3}, "source_encoding": "ascii", "filename": "/Users/dutchrelitz77/Dropbox/byu/winter_2015/IS_542/HW/HW10_AjaxFileUpload/code/test_dmp/homepage/templates/tabledemo.get_table.html", "uri": "tabledemo.get_table.html"}
__M_END_METADATA
"""
