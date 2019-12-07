function validar(){
var nombre,apellido,correo,usuario,clave,telefono;
nombre = document.getElementById("nombre").value;
apellidos = document.getElementById("apellidos").value;
correo = document.getElementById("correo").value;
usuario = document.getElementById("usuario").value;
clave = document.getElementById("clave").value;
telefono = document.getElementById("telefono").value;

if(nombre == "" || apellidos == "" || correo == "" || usuario == "" || clave == ""|| telefono == ""){ 
alert("Todos los campos son obligatorios"); 
return false;
}
else if(nombre.length>30){
alert("El nombre es muy largo");
return false;
}
else if(apellidos.length>80){
alert("Los apellidos es muy largo");
return false;
}
else if(correo.length>100){
alert("El correo es muy largo");
return false;
}
else if(usuario.length>20)|| clave.length>20){
alert("El usuario y la clave solo deben tener 20 caracteres como maximo");
return false;
}
else if(telefono.length>100){
alert("El telefono es muy largo");
return false;