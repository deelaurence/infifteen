# core/context_processors.py
def user_name(request):
    if request.user.is_authenticated:
        print(request.user.first_name)
        return {'name': request.user.first_name}
    return {}
