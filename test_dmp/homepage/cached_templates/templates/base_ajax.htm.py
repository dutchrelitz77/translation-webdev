# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426082220.258902
_enable_loop = True
_template_filename = '/Users/dutchrelitz77/Dropbox/byu/winter_2015/IS_542/HW/HW10_AjaxFileUpload/code/test_dmp/homepage/templates/base_ajax.htm'
_template_uri = 'base_ajax.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \n\n')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  Sub-templates should place their ajax content here.\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "base_ajax.htm", "filename": "/Users/dutchrelitz77/Dropbox/byu/winter_2015/IS_542/HW/HW10_AjaxFileUpload/code/test_dmp/homepage/templates/base_ajax.htm", "line_map": {"33": 7, "34": 10, "35": 10, "36": 14, "41": 19, "42": 22, "43": 22, "61": 55, "16": 6, "49": 17, "18": 0, "55": 17, "27": 4, "28": 6, "29": 7}}
__M_END_METADATA
"""
