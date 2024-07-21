let bancos = 15;
let alumnos = 15;
let mensaje;

function alcanzanLosBancos(){
    if (bancos >= alumnos){
        mensaje = "Van a alcanzar los bancos"
    } else {
        mensaje = "No van a alcanzar los bancos"
    }
}

console.log(mensaje)