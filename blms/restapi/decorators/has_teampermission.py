from functools import wraps
from django.http import HttpResponseForbidden
from core.models import UserRole, Team


def has_teampermission():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):

            if request.user.is_authenticated:
                user_role: int = UserRole.objects.get(user_id=request.user.id)
                if user_role and int(user_role.userrole) == UserRole.COACH:
                    # In UserRole if role in Coach then object_id is the primary
                    # key from Coach table for this coach
                    teamid = kwargs.get("pk")
                    if Team.objects.get(pk=teamid).coach.id == user_role.object_id:
                        return view_func(request, *args, **kwargs)
                    else:
                        return HttpResponseForbidden(
                            "You don't have permission to access this team details"
                        )

        return _wrapped_view

    return decorator
