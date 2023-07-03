let footer = `<div class="footer-contenido">
<ul class="social">
    <li><a href="https://www.facebook.com/groups/comunidadcodoacodo" target="_blank" <i
            class="fa-brands fa-facebook"></i>Facebook pagina principal</a></li>
    <li><a href="https://www.youtube.com/playlist?list=PLcVi00zZjeQMyFrPgp0fXzi7A5H0v1vCo" target="_blank"
            <i class="fa-brands fa-youtube"></i>Youtube curso codo</a> </li>
    <li><a href="https://github.com/NicolasPergolani/TPOCODO.git" target="_blank" <i
            class="fa-brands fa-github"></i>Repositorio del TPO</a> </li>
</ul>
</div>
<div class="bottom">
<p> Copyright & Diseño<span style="color:#0e0f10
"> Grupo 6 de Codo a Codo</span></p>


</div>
<a href="https://www.flaticon.com/free-icons/plus" title="plus icons">Plus icons created by Freepik -
Flaticon</a>`;

document.getElementById("idFooter").innerHTML = footer

let header = `  <a href="Index.html"> <div class="logo"> Noticiero para Viajeros </div></a> 
<div class="hamburger">
    <div class="line"></div>
    <div class="line"></div>
    <div class="line"></div>
</div>
<nav class="nav-bar">
<ul>
<li>
    <a href="Index.html">Inicio</a>
</li>
<li>
    <a href="nosotros.html">Nosotros</a>
</li>
<li>
    <a href="iniciarSesion.html">Login</a>
</li>
<li>
<<<<<<< HEAD
    <a href="indexCrud.html">Nuestros Destinos </a>
=======
    <a href="indexCrud.html">Viaja con Nosotros</a>
>>>>>>> 3760d4f63de488aeb8cc07dabbde634077a9e0a4
</li>
</ul>
</nav>`

document.getElementById("idHeader").innerHTML = header;

hamburger = document.querySelector(".hamburger");
hamburger.onclick = function () {
    navBar = document.querySelector(".nav-bar");
    navBar.classList.toggle("active");

}
