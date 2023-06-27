
$.validator.addMethod("terminaPor", function(value, element, parametro){
    if(value.endswith(parametro)) {
        return true;
    }

    return false;

}, "Debe terminar por {0}")

$("#formulario_contacto").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 3,
            maxlength: 30
        },
        apellidopa: {
            required: true,
        },
        apellidoma: {
            required: true,
        },
        rut: {
            required: true,
        },
        direccion: {
            required: true,
        },
        email: {
            required: true,
            email: true,
            number: true,
        },
        telefono: {
            required: true,
            number: true,
        },
        genero: {
            required: true,

        },
        caja: {
            required: true,

        },
    }
})

$("#enviar").click(function() {
    let nombre = $("#nombre").val()
    let apellidopa = $("#apellidopa").val()
    let apellidoma = $("#apellidoma").val()
    let rut = $("#rut").val()
    let direccion = $("#direccion").val()
    let email = $("#email").val()
    let telefono = $("#telefono").val()
    let genero = $("#genero").val()
    let caja = $("#caja").val()

    console.log(nombre)
    console.log(apellidopa)
    console.log(apellidoma)
    console.log(rut)
    console.log(direccion)
    console.log(email)
    console.log(telefono)
    console.log(genero)
    console.log(caja)

})