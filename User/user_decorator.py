from django.shortcuts import redirect


def user_login(function):
    def wrap(self, request, *args, **kwargs):
        try:
            if request.session.get('userid'):
                return function(self, request, *args, **kwargs)
            else:
                return redirect('/user/login/')
        except Exception as e:
            return redirect('/user/login/')
    return wrap
