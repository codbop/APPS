from django.shortcuts import render, redirect
from core.models import User

def login(request):
    # Sayfa request edildiğinde login penceresi gelsin 
    if request.method == 'GET':
        return render(request, 'login.html')
    # Login html üzerinde POST işlemi yapılırsa htmlde form üzerinden gönderilen
    # parametreler üzerinden işlem yapılsın ve kullanıcı authenticate edilsin.
    # kullanıcı authenticate olursa random_match sayfasına erişebilsin.
    # if request.method == 'POST'
    else:
        # Login parametreleri formdan çekilir 
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            # Kullanıcı tablosunda bu parametrelerle kayıtlı olan bir kullanıcı olup olmadığı
            # kontrol edilir. Eğer var ise sisteme giriş yapılır ve session'da bu parametreler
            # tutulur. Yok ise de kullanıcı yeniden login sayfasına yönlendirilir ve tekrar 
            # doğru parametreleri girene kadar giriş yapması gerekir.
            User.objects.get(username=username, password=password)
            print('Authenticated')
            request.session['is_authenticated'] = True
            return redirect('random_match/')
        except:
            print('Not Authenticated')
        return redirect('/')

def random_match(request):
    if request.session.get('is_authenticated'):
        return render(request, 'random_match.html')
    else:
        return redirect('/')
        



