

/* Seçim yapıldığında post requesti ajax ile atılacak */
$(document).ready(function() {

    /* Döküman ilk açıldığında önce 1.bloğa oyun yerleştirilmeli sonra ikinci bloğa
    oyun yerleştirilmeli bu yüzden randomize butonunu sayfa ilk açıldığında disable ediyoruz. */
    document.getElementById('randomize').disabled=true;
    $('#select-app').change(function(){

        /* Uygulama idsine erişebilmek için datalist üzerinde option taglerine bu şekilde
        bir filtreleme yapıldı. Çünkü normal value değerleri html üzerinde gözükmekte.
        Bize lazım olan gözükmeyen id değerleri. */
        var val = $(this).val();
        var app_id = $('#datalistOptions option').filter(function() {
            return this.value == val;
        }).data('value');
        $.ajax({
            type: "POST",
            dataType: "json",
            url:window.location.href,
            data: {'app_id':app_id, 'action':'select_app'},
            success: function(data)
            {

                /* imajları htmlye basmak için {% static %} yerine direk dosya dizin yapısı kullanıldı (../static/images/icons/
                gibi) çünkü static yapısı özel django karakterleri içermekte (% veya {} gibi) ve innerhtml bu karakterler
                server tarafında basıldığı için htmlye django karakterleri olarak geçirilemiyor sadece string olarak
                geçiyorlar */
                
                var html_1 = `<div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
                <div class="carousel-inner"><div class="carousel-item active"><img src="../static/images/icons/` 
                + data.icon + `" class="d-block w-100" alt="..." style="height:415px;"></div>`;
                var html_2 = '';
                for(const ss of data.ss_list) {
                    html_2 +=
                    `<div class="carousel-item">
                    <img src="../static/images/ss/` + ss + `" class="d-block w-100" alt="..." style="height:415px;">
                    </div>`;
                }
                html_3 = `</div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                    </button>
                </div>`
                var new_html = html_1 + html_2 + html_3;
                document.getElementById('carousel-1').innerHTML = new_html;

                /* Oyun seçimi yapıldığında ve birinci bloğa oyun yerleştirildiğinde artık 2.bloğa
                oyun yerleştirilebilir. Bu yüzden randomize butonunu oyun seçtiken sonra aktif ediyoruz. */
                document.getElementById('randomize').disabled=false;
            },
            
        })
    });
    $('#randomize').click(function(){

        /* uygulama idsi random geleceği için burada id çekmemize gerek yok.
        Diğer işlemler bir önceki aksiyonla hemen hemen aynı olacak*/

        $.ajax({
            type: "POST",
            dataType: "json",
            url:window.location.href,
            data: {'action':'randomize'},
            success: function(data)
            {

                /* imajları htmlye basmak için {% static %} yerine direk dosya dizin yapısı kullanıldı (../static/images/icons/
                gibi) çünkü static yapısı özel django karakterleri içermekte (% veya {} gibi) ve innerhtml bu karakterler
                server tarafında basıldığı için htmlye django karakterleri olarak geçirilemiyor sadece string olarak
                geçiyorlar */
                var html_1 = `<div id="carouselExampleControls2" class="carousel slide" data-bs-ride="carousel">
                <div class="carousel-inner"><div class="carousel-item active"><img src="../static/images/icons/` 
                + data.icon + `" class="d-block w-100" alt="..." style="height:415px;"></div>`;
                var html_2 = '';
                for(const ss of data.ss_list) {
                    html_2 +=
                    `<div class="carousel-item">
                    <img src="../static/images/ss/` + ss + `" class="d-block w-100" alt="..." style="height:415px;">
                    </div>`;
                }
                html_3 = `</div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls2" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls2" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                    </button>
                </div>`
                var new_html = html_1 + html_2 + html_3;
                document.getElementById('carousel-2').innerHTML = new_html;
            },
            
        })
    })
});

