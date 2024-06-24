from functools import wraps
from django.http import HttpResponseForbidden
from core.models import UserRole


# this checks the request user role is in the specified list of Roles in the
# allowed_roles list. If not return forbiddon (403)
def has_permission(allowed_roles: list[int]):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):

            if request.user.is_authenticated:
                user_role: int = UserRole.objects.get(user_id=request.user.id).userrole
                if int(user_role) in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponseForbidden(
                        "You don't have permission to access this resource"
                    )

        return _wrapped_view

    return decorator
