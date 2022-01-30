/* Seçim yapıldığında post requesti ajax ile atılacak */
$(document).ready(function() {
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
            data: {'app_id':app_id},
            success: function(data)
            {
                /* imajları htmlye basmak için {% static %} yerine direk dosya dizin yapısı kullanıldı (../static/images/icons/
                gibi) çünkü static yapısı özel django karakterleri içermekte (% veya {} gibi) ve innerhtml bu karakterler
                server tarafında basıldığı için htmlye django karakterleri olarak geçirilemiyor sadece string olarak
                geçiyorlar */
                console.log(data.icon);
                var html_1 =  `<div class="carousel-item active"><img src="../static/images/icons/` + data.icon + `" 
                        class="d-block w-100" alt="..." style="height:450px;"></div>`;
                var html_2 = '';
                for(const ss of data.ss_list) {
                    html_2 +=
                    `<div class="carousel-item">
                    <img src="../static/images/ss/` + ss + `" class="d-block w-100" alt="..." style="height:450px;">
                    </div>`;
                }
                var new_html = html_1 + html_2;
                console.log(new_html);
                document.getElementById('carousel-1').innerHTML = new_html;
            },
            
        })
    });
});

