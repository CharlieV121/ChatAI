$(document).autoboxOn('textarea');
$('#textarea-id').trigger('focus');
$('#button-send-id').on('click',sendMessage);


$('#button-clear-id').on('click', (e)=>{
    list_msg = []
    $('.historial-list-item').each((i,e)=>{
        console.log(i)
        list_msg.push($(e).attr("id"))
    })
    console.log(list_msg)
    if(list_msg.length > 0){
        $.ajax({
            url: '/delete/',
            type: 'POST',
            data: { data: JSON.stringify(list_msg)},
            success: function(res) {
                if(res.result == "ok"){
                    alert("Historial borrado correctamente")
                }
                $(".historial-list").html('')
            },
            error: function(xhr, status, error) {
                $(".historial-list").html('')
            }, 
            timeout: 60000 // 20 segundos de espera
        });
    }
})

function sendMessage(){
    const textarea = $('#textarea-id')
    let req = textarea.val();
    if(req.trim() === "") return
    textarea.val("");
    textarea[0].rows = 1;
    $.ajax({
        url: '/message/',
        type: 'POST',
        data: {req},
        success: function(d) {
            addResult(d.data.res, true)
            if(d.id != "0") $('.historial-list li:last').attr('id',d.id)
        },
        error: function(xhr, status, error) {
            error = error === "timeout" ? ": Tiempo de espera excedido":""
            addResult(`Ocurrió un error procesando tu consulta${error}`, true)
        }, 
        timeout: 20000
    });

    addResult(req, false)
}

spinner = ()=>{
    return(`<div class="loading">
        <div class="spinner-container">
            <div id="spinner1">
                <div class="spinner-border" role="status"></div>
            </div>
        </div>
    </div>`)
}

function addResult(m,type){
    if(type){$(".loading").remove()}

    if(type) $(".historial-list li:last").html($(".historial-list li:last").html() + addResponse(m))
    else $(".historial-list").html( $(".historial-list").html() + addRequest(m) + spinner())
     
    $('#textarea-id').prop("disabled",!type)
    $('#button-send-id').prop("disabled",!type)
    $('#button-clear-id').prop("disabled",!type)

    type? $('#textarea-id').trigger('focus') : void(0)
    showLoading(!type)
    scrollToTop();
}

function addRequest(m){
    return (`
    <li class="historial-list-item">
        <div class="item-container">
            <div class="message-container">
                <div class="image"><img width="40px" height="40px" src="../static/img/user.png"/></div>
                <div class="content"><pre class="message">${m}</pre></div>
            </div>
        </div>
    </li>`);
}

function addResponse(m){
    return (`
        <div class="item-container">
            <div class="message-container">
                <div class="image"><img width="40px" height="40px" src="../static/img/system.jpg"/></div>
                <div class="content"><pre class="message">${m}</pre></div>
            </div>
        </div>
    `);
}


function showLoading(enable){
    if(enable===true){
        $(`.loading`).addClass("flex")
    }else{
        $(`.loading`).removeClass("flex")
    }
}
function scrollToTop(){
    const historial = $('.historial-list');
    historial.animate({
        scrollTop:historial[0].scrollHeight
    }, 500) 
}

