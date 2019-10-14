$("#formulario1").validate({
        rules: {
            "txtNombre": {
                required: true,
                minlength: 5
            },
            "txtRut": {
                required: true,
                minlength: 10
            },
            "txtEmail": {
                required: true,
                email: true
            },
            "txtTelefono": {
                required: true
            },
            "txtRegion": {
                required: true
            },
            "comunas": {
                required: true
            },
            "txtVivienda": {
                required: true
            },
            "bday": {
                required: true
            }
        }, //---> fin de reglas
        messages: {
            "txtNombre": {
                required: "Te falto el nombre!!!",
                minlength: "Min. CINCO caracteres"
            },
            "txtEmail": {
                required: "Te falto el email",
                email: "NO tiene el formato email"
            },
            "txtRut": {
                required: "Te falto el rut"
            },
            "regiones": {
                required: "Te faltó la región"
            },

            "txtTelefono": {
                required: "Te faltó el telefono"
            },
            "txtVivienda": {
                required: "Te faltó la vivienda"
            },
            "bday": {
                required: "Te faltó la fecha de nacimiento"
            }
        } //--> fin de mensajes 
    } //--> final del objeto json

);