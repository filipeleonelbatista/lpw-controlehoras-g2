/* // Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal 
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
} */

window.onload=function(){
           
    $("#cnpj").keydown(function(){
        try {
            $("#cnpj").unmask();
        } catch (e) {}
        
        var tamanho = $("#cnpj").val().length;
        
        if(tamanho <= 14){
            $("#cnpj").mask("99.999.999/9999-99");
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });

    $("#hrInicio").keydown(function(){
        try {
            $("#hrInicio").unmask();
        } catch (e) {}
        
        var tamanho = $("#hrInicio").val().length;
        
        if(tamanho <= 5){
            $("#hrInicio").mask("99:99");
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });

    $("#hrFim").keydown(function(){
        try {
            $("#hrFim").unmask();
        } catch (e) {}
        
        var tamanho = $("#hrFim").val().length;
        
        if(tamanho <= 5){
            $("#hrFim").mask("99:99");
        }
        
        // ajustando foco
        var elem = this;
        setTimeout(function(){
            // mudo a posição do seletor
            elem.selectionStart = elem.selectionEnd = 10000;
        }, 0);
        // reaplico o valor para mudar o foco
        var currentValue = $(this).val();
        $(this).val('');
        $(this).val(currentValue);
    });
    
        }
    