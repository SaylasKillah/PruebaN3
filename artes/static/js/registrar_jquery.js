$(document).ready(function () {
    $("#btnRegistrar").click(function () {
        var nombre = $("#txtNombre").val()
        var apellido = $("#txtApellido").val()
        var password = $("#txtPassword").val()
        var correo = $("#txtCorreo").val()
        var matchFound = false;

        var objeto = {
            nombre: nombre,
            apellido: apellido,
            password: password,
            correo: correo
        }
        $.ajax({
            type: 'GET',
            url: 'https://6462e26d7a9eead6fad8bcbf.mockapi.io/usuario',
            beforeSend: function(){
                $("#capa").html("<p>Registrando usuario...</p>")
            },
            error:function(){},
            success: function(data){
                $.each(data, function(index, obj) {
                    if (obj.correo === correo) {
                        matchFound = true;
                    }
                });
                if (matchFound) {

                    $("#capa").html("<p>El usuario: "+objeto.correo+" ya existe</p>")

                } else {
                    $.ajax({
                        type: 'POST',
                        data: objeto,
                        url: 'https://6462e26d7a9eead6fad8bcbf.mockapi.io/usuario',
                        beforeSend: function(){
                            $("#capa").html("<p>Registrando usuario...</p>")
                        },
                        error: function(xhr, status, error){
                            console.log(error)
                        },
                        success: function(data){
                            $("#capa").html("<p>Registrado exitosamente!!</p>")
                        }
                    })
                }
            }
        })
    })
    $("#btnIniciarsesion").click(function () {
        var nombre = $("#txtNombre").val()
        var password = $("#txtPassword").val()

        var objeto = {
            nombre: nombre,
            password: password
        }
        $.ajax({
            type: 'GET',
            url: 'https://6462e26d7a9eead6fad8bcbf.mockapi.io/usuario',
            beforeSend: function(){
                $("#capa").html("<p>Iniciando Sesion...</p>")
            },
            error:function(){},
            success: function(data){
                $.each(data, function(index, obj) {
                    if (obj.nombre === nombre && obj.password === password) {
                        matchFound = true;
                    }
                });
                if (matchFound) {
                    $("#capa").html("<p>La combinacion del usuario y contraseña coinciden.</p>")

                    $("#capa").append("<p>Usuario: "+objeto.nombre+"</p>")

                } else {
                    $("#capa").html("<p>La combinacion del usuario y contraseña no coinciden... crea una cuenta!!</p>")
                }
            }
        })
    })
})