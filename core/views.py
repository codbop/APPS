from django.shortcuts import render, redirect
from core.models import User, SampleApps
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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

@csrf_exempt
def random_match(request):
    if request.method == 'GET':
        if request.session.get('is_authenticated'):
            """ Eğer sayfa üzerinde get metodu çağrılmışsa blokta henüz bir oyun
            gözükmemesi gerektiğinden yani önce kullanıcı bir oyun seçmesi ve sonra
            blokta bir oyun gözükmesi gerektiğinden isCarouselEmpty boolean değişkeni
            tanımlanmış olup bu değişkenin boolean değerine göre bloğa oyun yerleştirile-
            cektir. Bu da post metodunda bu değişkenin False olarak gönderilmesi ile sağlana
            caktır. """
            context = {
                'apps':SampleApps.objects.all(),
                'isCarouselEmpty':False
            }
            return render(request, 'random_match.html', context)
        else:
            return redirect('/')
    # Eğer sayfa üzerinde post requesti atılmış ise burası çalışır
    else:
        # Eğer sistemde mevcut olan bir uygulama adı girilmişse buradan uygulama 
        # sorgulanıp döndürülür. Mevcut olmayan bir uygulma girilmiş ise de herhangi
        # bir işlem yapılmaz.
        if request.POST.get('app_id'):
            app_id = request.POST.get('app_id')
            # Seçilen uygulamayı post edilen id ile veritabanı üzerinden
            # sorgulatıyoruz ve bu uygulmaya ait gerekli screenshotların hepsini
            # veritabanından sorgulatıp response olarak döndürüyoruz.
            app = SampleApps.objects.get(id=app_id)
            ss = app.Screenshots.all()
            # Uygulamaya ait screenshotları veritabanında sorgulatıp liste olarak elde ettik
            # liste içerisinde tuplelar var ise ve biz böyle bir yapı ile tupleı toplar isek
            # flatten edilmiş bir tuple elde ederiz ve bu tupleı listeye dönüştürerek istediğimiz
            # screenshotları tek bir liste içerisinde elde edebiliriz.
            ss_list = list(sum(ss.values_list('file_name'),()))
            print(ss_list)
            # Responseu ajaxa döndürüyoruz ve ayrıca screenshotların yanında oyunun ana görselini de
            # response olarak döndürüyoruz.
            return JsonResponse({'ss_list':ss_list,
                                'icon':app.icon})


        



