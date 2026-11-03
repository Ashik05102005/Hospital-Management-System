from django.shortcuts import redirect

class LoginMiddleware :
    def __init__(self , get_response):
        self.get_response = get_response
    def __call__(self, request):
        if request.path == '/test/' and not request.user.is_authenticated:

            return redirect('login')
        response = self.get_response(request)
        return response