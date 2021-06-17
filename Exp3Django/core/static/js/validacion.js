$(function validarregistro() {
    $("#registro").validate({
        rules: {
            email: {
                required: true,
                email: true
            },
            usuario: "required",
            password: "required",
            password2: {
                required: true,
                equalTo: "#password"
            },
            fecha: "required"
        },
        messages: {
            email: {
                required: 'Ingresa tu correo electrónico',
                email: 'Formato de correo no válido'
            },
            usuario: {
                required: 'Ingresa tu nombre de usuario',
                minlength: 'El usuario debe tener más de 3 caracteres'
            },
            password: {
                required: 'Ingresa una contraseña',
                minlength: 'Debes ingresar mínimo 6 caracteres'
            },
            password2: {
                required: 'Reingresa la contraseña',
                equalTo: 'Las contraseñas ingresadas no coinciden',
                minlength: 'Caracteres insuficientes'
            },
            fecha: {
                required: 'Ingresa tu fecha de nacimiento',
                min: 'Fecha de nacimiento no válida'
            }
        }
    });
});

$(function validaringresot() {
    $("#ingreso").validate({
        rules: {
            codigo: "required"
        },
        messages: {
            codigo: {
                required: 'Ingresa el código del torneo',
                minlength: 'El código debe tener 37 dígitos',
            }
        }
    });
});

$(function validartorneos() {
    $("#datos").validate({
        rules: {
            nombrec: "required",
            nombret: "required",
            equipos: "required",
            fecha: "required",
            hora: "required",
            codigo: "required"
        },
        messages: {
            nombrec: {
                required: 'Ingresa el nombre de quien organiza el torneo',
                minlength: 'El nombre debe tener más de 3 caracteres'
            },
            nombret: {
                required: 'Ingresa el nombre del torneo',
                minlength: 'El nombre del torneo debe tener más de 3 caracteres'
            },
            equipos: {
                required: 'Ingresa cuantos equipos participarán',
                min: 'Debes ingresar como mínimo 2 equipos'
            },
            fecha: {
                required: 'Ingresa la fecha de inicio del torneo',
                min: 'Fecha de inicio del torneo no válida'
            },
            hora: {
                required: 'Ingresa la hora de inicio del torneo',
                min: 'Hora de inicio del torneo no válida'
            },
            codigo: {
                required: 'Debes generar el código del torneo'
            }
        }
    });
});