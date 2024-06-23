from functools import wraps
from django.http import HttpResponseForbidden
from core.models import UserRole


def has_permission(permtocheck: list[int]):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):

            if request.user.is_authenticated:
                user_role: int = UserRole.objects.get(user_id=request.user.id).userrole
                if int(user_role) in permtocheck:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponseForbidden(
                        "You don't have permission to access this resource"
                    )

        return _wrapped_view

    return decorator
