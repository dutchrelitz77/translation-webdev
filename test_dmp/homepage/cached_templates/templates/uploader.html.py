# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1426772502.678297
_enable_loop = True
_template_filename = '/home/justin/Dropbox/BYU/Winter_2015/IS_542/HW/HW10_AjaxFileUpload/code/test_dmp/homepage/templates/uploader.html'
_template_uri = 'uploader.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'main_center_content2']


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
        def title():
            return render_title(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def main_center_content2():
            return render_main_center_content2(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 3
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_center_content2'):
            context['self'].main_center_content2(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('Translation Home Page')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_center_content2(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def main_center_content2():
            return render_main_center_content2(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n    <div class="content">\n        <h1>Upload a file!</h1>\n        <p>Fill out the form below to upload a file to the server</p>\n    </div>\n\n    <div class="content_main">\n        <form method=\'POST\'>\n            <table>\n                ')
        # SOURCE LINE 14
        __M_writer(str( form ))
        __M_writer('\n            </table>\n            <input type=\'submit\'/>\n        </form>\n        <br>\n        <div class="progress bar" style=\'display: none;\'>\n            <div class="progress-bar progress-bar-success progress-bar-striped" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width: 0%">\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


