from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    if request.method == 'POST':
        room_code = request.POST.get('room_code')
        username=request.POST.get('username')
        return redirect(f'/chat/{room_code}/?user={username}')
    return render(request, 'home.html')

def chat(request,room_code):
    context={'room_code':room_code,'user':request.GET.get('user')}
    print(context)
    return render(request, 'chat.html',context)