# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426082358.091198
_enable_loop = True
_template_filename = '/Users/dutchrelitz77/Dropbox/byu/winter_2015/IS_542/HW/HW10_AjaxFileUpload/code/test_dmp/homepage/templates/photos.html'
_template_uri = 'photos.html'
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
        images = context.get('images', UNDEFINED)
        def main_center_content2():
            return render_main_center_content2(context._locals(__M_locals))
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
        images = context.get('images', UNDEFINED)
        def main_center_content2():
            return render_main_center_content2(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n        <h1>Photo Gallery</h1>\n        <p>Below is a photo gallery of popular Natural Parks around America</p>\n        <p>Hover over each picture to show the name of the National Park associated with each picture</p>\n    </div>\n\n    <div class="photos">          \n')
        for image in images:
            __M_writer('            <a href="/static/images/')
            __M_writer(str( image.imageSource ))
            __M_writer('" download><img class="gallery-icon" src = "/static/images/')
            __M_writer(str( image.imageSource ))
            __M_writer('"></a>\n            <p class="picture-title hidden">')
            __M_writer(str( image.title ))
            __M_writer('</p>\n')
        __M_writer('    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Translation Home Page')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "photos.html", "filename": "/Users/dutchrelitz77/Dropbox/byu/winter_2015/IS_542/HW/HW10_AjaxFileUpload/code/test_dmp/homepage/templates/photos.html", "line_map": {"64": 14, "65": 14, "66": 15, "59": 5, "68": 17, "37": 1, "42": 3, "80": 3, "67": 15, "52": 5, "86": 80, "74": 3, "27": 0, "60": 13, "61": 14, "62": 14, "63": 14}}
__M_END_METADATA
"""
