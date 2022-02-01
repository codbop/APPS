# APPS
APPS Mulakat Projesi

Dockerfile eklendi. Dockerfile içerisine sanal makine oluşturulması için gerekli komutlar yazıldı. 

Örnek olarak Dockerfile içerisindeki komutlar

****************************************************************
****************************************************************
FROM python:3.9.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
****************************************************************
****************************************************************

Bu komutlar çalıştırılarak proje için sanal ortam kolay bir şekilde oluşturulmuş olur ve proje ayağa kalkmış olur.

Bu komutların işletilmesi commands.txt dosyasında verilen terminal komutları ile sağlanmaktadır. Sırasıyla;

docker build --tag python-django . 
docker run --publish 8000:8000 python-django

komutları yazılır. İlk komut üstteki komutları işleterek proje için sanal bir ortam oluşturur. Ardından ikinci komut 8000 portu üzerinde cmd
çalıştırma komutunu uygular ve uygulamayı sanal ortamda publish eder. Docker masaüstü uygulaması üzerinden bu sanal makine kolaylıkla görünür hale
gelir ve uygulama üzerinden istenildiği gibi makine çalıştırılıp durdurulabilir.

**NOT: Projeye toplam olarak yaklaşık _2,5-3_ gün arası gibi bir süre harcandı.**
