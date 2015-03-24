# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1426772501.0800786
_enable_loop = True
_template_filename = '/home/justin/Dropbox/BYU/Winter_2015/IS_542/HW/HW10_AjaxFileUpload/code/test_dmp/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'main_title', 'message', 'main_center_content2', 'main_left_content']


# SOURCE LINE 4
from django_mako_plus.controller import static_files 

# SOURCE LINE 35
import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def main_left_content():
            return render_main_left_content(context._locals(__M_locals))
        def main_center_content2():
            return render_main_center_content2(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def message():
            return render_message(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def main_title():
            return render_main_title(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        # SOURCE LINE 4
        __M_writer('\n')
        # SOURCE LINE 5
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <head>\n    <meta charset="UTF-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n\n    <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 14
        __M_writer('</title>\n    \n')
        # SOURCE LINE 17
        __M_writer('    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/jquery.min.js"></script>\n    <script src="')
        # SOURCE LINE 18
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/jquery-ui.js"></script>\n    <script src="')
        # SOURCE LINE 19
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/plugins/jquery.enablepopout.js"></script>\n\n\n    <!-- Latest compiled and minified CSS for bootstrap -->\n    <link rel="stylesheet" href="')
        # SOURCE LINE 23
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/styles/bootstrap/bootstrap.min.css">\n    <link rel="stylesheet" href="')
        # SOURCE LINE 24
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/styles/bootstrap/bootstrap-theme.min.css">\n\n    <!-- Stylesheet for the datetimepicker -->\n    <link rel="stylesheet" href="')
        # SOURCE LINE 27
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/datetimepicker-master/jquery.datetimepicker.css">\n\n    <!-- This is used for the shortcut icon -->\n    <link rel="shortcut icon" href="http://worldwater.byu.edu/template/img/favicon.ico">\n\n')
        # SOURCE LINE 33
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n\n    ')
        # SOURCE LINE 35
        __M_writer('\n  </head>\n  <body>\n\n    <nav class="navbar navbar-default navbar-fixed-top">\n      <div class="container-fluid byu">\n        <!-- Brand and toggle get grouped for better mobile display -->\n        <div class="navbar-header">\n          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n            <span class="sr-only">Toggle navigation</span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n          </button>\n          <a class="navbar-brand" href="#">\n            <img alt=\'Brand Logo\' src=\'')
        # SOURCE LINE 50
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/pics/logo2.png\'>\n          </a>\n          <p class="navbar-text" style=\'font-size="2em;\'>BYU World Water Project</p>\n        </div>\n\n        <!-- Collect the nav links, forms, and other content for toggling -->\n        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n          <ul class="nav navbar-nav">\n            <li><a href="/homepage/index/">Home Page</a></li>\n            <li><a href="/homepage/photos/">Photos</a></li>\n            <li><a href="/homepage/tabledemo/">Table</a></li>\n            <li><a href="/homepage/uploader/">File Upload</a></li>\n          </ul>\n          <ul class="nav navbar-nav navbar-right">\n            <li><a href="#">HydroServer Lite</a></li>\n            <li class="dropdown">\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Your Account <span class="caret"></span></a>\n              <ul class="dropdown-menu" role="menu">\n                <li><a href="#">Profile</a></li>\n                <li><a href="#">Admin</a></li>\n                <li><a href="#">Change Password</a></li>\n                <li class="divider"></li>\n                <li><a href="#">Log Out</a></li>\n              </ul>\n            </li>\n          </ul>\n        </div><!-- /.navbar-collapse -->\n      </div><!-- /.container-fluid -->\n    </nav>\n\n    <header>\n      <h1>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_title'):
            context['self'].main_title(**pageargs)
        

        # SOURCE LINE 81
        __M_writer('</h1>\n    </header>\n\n    <div class="alert">\n        <div class="message-content">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'message'):
            context['self'].message(**pageargs)
        

        # SOURCE LINE 86
        __M_writer("\n        </div>\n    </div>\n\n    <main>\n  \t\t<div id = 'main_left_content'>\n            <div id = 'main_left_content_menu'>\n                <li><a href='#'>Item One</a></li>\n                <li><a href='#'>Item Two</a></li>\n                <li><a href='#'>Item Three</a></li>\n                <li><a href='#'>Item Four</a></li>\n                ")
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_left_content'):
            context['self'].main_left_content(**pageargs)
        

        # SOURCE LINE 97
        __M_writer("\n            </div>\n  \t\t</div>\n\n  \t\t<div id = 'main_center_content'>\n  \t\t\t")
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_center_content2'):
            context['self'].main_center_content2(**pageargs)
        

        # SOURCE LINE 104
        __M_writer('\n        <br>\n  \t\t</div>\n\n    </main>\n\n    <footer>\n      <p>Copyright: Coding Engineers, LLC | ')
        # SOURCE LINE 111
        __M_writer(str( datetime.datetime.now().strftime("%b-%Y") ))
        __M_writer('</p>\n    </footer>\n  \n    <!-- Latest compiled and minified JavaScript -->\n    <script src="')
        # SOURCE LINE 115
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/bootstrap/bootstrap.min.js"></script>\n\n    <script src="')
        # SOURCE LINE 117
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/functions.js"></script>\n    <script src="')
        # SOURCE LINE 118
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/datetimepicker-master/jquery.datetimepicker.js"></script>\n    <script src="')
        # SOURCE LINE 119
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/plugins/bootstrap-filestyle.min.js"></script>\n\n')
        # SOURCE LINE 122
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main_title():
            return render_main_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def message():
            return render_message(context)
        __M_writer = context.writer()
        # SOURCE LINE 86
        __M_writer('<div id="not-empty"></div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_center_content2(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main_center_content2():
            return render_main_center_content2(context)
        __M_writer = context.writer()
        # SOURCE LINE 102
        __M_writer('\n          Site content goes here sub-templates.\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main_left_content():
            return render_main_left_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


