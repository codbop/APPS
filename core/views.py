from django.shortcuts import render, redirect
from core.models import User, SampleApps, Document
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from core.forms import DocumentForm
from PIL import Image

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
            return redirect('/random_match/')
        except:
            print('Not Authenticated')
        return redirect('/')

@csrf_exempt
def random_match(request):
    if request.method == 'GET':
        if request.session.get('is_authenticated'):
            """ Sayfa ilk yüklendiğinde htmldeki dropdowna uygulamalar yüklenmelidir.
            Bu yüzden get metodu çağrıldığında veritabanından uygulamaları çekiyoruz
            ve context içerisinde htmlye gönderiyoruz."""
            context = {
                'apps':SampleApps.objects.all(),
            }
            return render(request, 'random_match.html', context)
        else:
            return redirect('/')

    # Eğer sayfa üzerinde post requesti atılmış ise burası çalışır
    else:

        # Eğer sistemde mevcut olan bir uygulama adı girilmişse buradan uygulama 
        # sorgulanıp döndürülür. Mevcut olmayan bir uygulma girilmiş ise de herhangi
        # bir işlem yapılmaz. Ayrıca bir uygulama seçilmiş ise bu aksiyon uygulama seçme aksiyonudur.
        # Yani 1. bloğa yerleştirme aksiyonudur. Bu yüzden aksiyon parametresi de kontrol edilmektedir.
        if request.POST.get('app_id') and request.POST.get('action') == 'select_app':
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

            # Responseu ajaxa döndürüyoruz ve ayrıca screenshotların yanında oyunun ana görselini de
            # response olarak döndürüyoruz.
            return JsonResponse({'ss_list':ss_list,
                                'icon':app.icon})

        # Aksiyon randomize ise ikinci bloğa yerleştirme işlemidir. Bu yüzden bu blok çalışır.
        elif request.POST.get('action') == 'randomize':

            # Burada da birinci bloğa yerleştirmek için yapılan işlemlerin benzerleri yapılacak.
            # Tek fark id'nin random olarak üretilmesi ve bir önceki id'nin mevcut id'ye eşit olmaması

            # Veritabanından uygulamaları rastgele sıralarız ve ilk kaydı döndürürüz. Böylece 
            # rastgele bir oyun elde etmiş oluruz. 
            # NOT!!: Bu metod çok performanslı değildir ancak veritabanında şuan çok az sayıda
            # kayıt bulunduğundan kullanılmasında sakınca görülmemiştir.

            # Ayrıca random olarak veritabanından çekilen oyun bir önceki oyuna eşit olmayıncaya
            # kadar yeniden üretilir ki bir önceki oyundan farklı bir oyun elde edilsin. 
            app = SampleApps.objects.order_by("?").first()
            while app.id == request.session.get('is_same'):
                app = SampleApps.objects.order_by("?").first()
            
            # while fonksiyonundan çıkıldığında is_same parametresi mevcut uygulama ile güncellenir
            # böylece bir sonraki uygulama üretilirken bir sonraki uygulama da bu uygulama ile
            # karşılaştırılır. Ve bu işlem bu şekilde devam eder ve böylece aynı oyunu hiçbir zaman
            # elde etmemiş oluruz. Güncellemeyi sessiona kaydederek yapıyoruz.
            request.session['is_same'] = app.id

            # Geri kalan işlemler bir önceki aksiyonda uygulanan işlemler ile aynı olacaktır.
            ss = app.Screenshots.all()   
            ss_list = list(sum(ss.values_list('file_name'),())) 

            return JsonResponse({'ss_list':ss_list,
                    'icon':app.icon})

# Görselin yükleneceği sayfa
def webp(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # imaj verileri veritabanına yüklendikten ve imaj mediaya yüklendikten sonra
            # kayıt işlemini yapıyoruz.
            Document.objects.last().description
            return redirect('/webp/')
    else:
        # Authenticate kontrolünü yine yapıyoruz get yaparken
        if request.session.get('is_authenticated'):
            form = DocumentForm()
        else:
            return redirect('/')
    return render(request, 'webp.html', {'form':form})


