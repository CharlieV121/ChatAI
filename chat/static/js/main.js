$(document).autoboxOn('textarea');
$('#textarea-id').trigger('focus');
$('#button-send-id').on('click',sendMessage);


$('.trash-button').on('click', (e)=>{
    console.log(e)
    if(e.target.tagName==="I") $(e.target).parent().parent().parent().remove()
    else $(e.target).parent().parent().remove()
})

function sendMessage(){
    const textarea = $('#textarea-id')
    let req = textarea.val();
    if(req.trim() === "") return
    textarea.val("");
    textarea[0].rows = 1;
    
    addResult(req, false)
}


function addResult(m,type){
    $(".historial-list").html( $(".historial-list").html() + addRequest(m))
    $(".historial-list li:last").html($(".historial-list li:last").html() + addResponse("Bienvenido"))
     
    scrollToTop();
}

function addRequest(m){
    return (`
    <li class="historial-list-item">
        <div class="item-container">
            <button id="button-clear-id" class="trash-button" title="borrar"> <i class="fa fa-trash"></i> </button>
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
            <div class="trash-button"></div>
            <div class="message-container">
                <div class="image"><img width="40px" height="40px" src="../static/img/system.jpg"/></div>
                <div class="content"><pre class="message">${m}</pre></div>
            </div>
        </div>
    `);
}


function showLoading(id,enable){
    if(enable===true){
        $(`#${id}`).removeAttr("hidden")
    }else{
        $(`#${id}`).attr("hidden","")
    }
}
function scrollToTop(){
    const historial = $('.historial-list');
    historial.animate({
        scrollTop:historial[0].scrollHeight
    }, 500) 
}

function disableButton(id,disable){
    $(`#${id}`).prop("disabled",disable)
}

