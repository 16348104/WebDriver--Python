function myfun() {
    //var myDate = new Date();
    // $('textarea').val('shijian:'myDate.toLocaleDateString());
    // $('textarea').val(myDate.innerHTML = Date());
    document.getElementById('nrStr').value = new Date().toLocaleDateString();
    document.getElementById('nrStr').value = ('11233');

    setTimeout(function(){ alert("Hello"); }, 3000);

    var audio = document.getElementById('mp3');
    audio.play();
}