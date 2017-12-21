from django.utils.decorators import method_decorator


def class_view_decorator(function_decorator):
    """
    Take decorator and apply to whole class.
    """
    def decorator(view):
        view.dispatch = method_decorator(function_decorator)(view.dispatch)
        return view
    return decorator
