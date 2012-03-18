from django import template
from django.utils.safestring import mark_safe

register = template.Library()
def make_html_list(value, autoescape=None):
    """Break a string down based on newline characters and for each line, enclose it in the <li> and </li> without the <ul> and </ul> tags. 
           Similar to the unordered_list filter but not requiring a list"""
    #paras = ['<li>%s</li>' % p.strip().replace('\n', '<br/>') for p in paras]
    html = []
    value_len = len(value)
    
    for i, item in enumerate(value):
        item_class = ''
        if i == (value_len - 1):
            item_class = ' class="last"'
        item_html = '<li%(class)s>%(item)s</li>' % { 'class': item_class, 'item' : item }
        
        html.append(item_html)
    return mark_safe('\n\n'.join(html))
make_html_list.is_safe = True
make_html_list.needs_autoescape = True
register.filter('html_list', make_html_list)