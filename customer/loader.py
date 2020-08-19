# def render_to_string(template_name, context=None, request=None, using=None):
#     """
#     Load a template and render it with a context. Return a string.

#     template_name may be a string or a list of strings.
#     """
#     if isinstance(template_name, (list, tuple)):
#         template = select_template(template_name, using=using)
#     else:
#         template = get_template(template_name, using=using)
#     return template.render(context, request)