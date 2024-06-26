from django.shortcuts import redirect
from django.urls import reverse

#class AdminUserMiddleware:
 #   def __init__(self, get_response):
  #      self.get_response = get_response
#
 #   def __call__(self, request):
  #      if request.path.startswith('/admin/'):
   #         if not request.user.is_superuser:
    #            #return redirect('some_other_view')
     #           return redirect('/')
      #  return self.get_response(request)
