<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { jwtDecode } from "jwt-decode";

const router = useRouter()
const perfil = ref(0)
const nombre = ref('')

onMounted(() => {
    const token = localStorage.getItem('token');

    if (token) {
        //const decodedToken = jwt_decode(token)
        const decodedToken = jwtDecode(token)
        perfil.value = decodedToken.sub.perfil_id
        nombre.value = decodedToken.sub.nombre
    } else {
        // Si no hay token, redirigir al login
        router.push('/login')
    }
})

// Función de logout que limpia el localStorage y redirige al login
const logout = () => {
    localStorage.clear()
    router.push('/login')
}
</script>

<template>
    <div class="container">
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">EcoTourism</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
                    aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarText">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li v-show="perfil === 1" class="nav-item">
                            <a class="nav-link" href="/usuarios-list">Usuarios</a>
                        </li>
                        <li v-show="perfil === 2 | perfil === 3" class="nav-item">
                            <a class="nav-link" href="/sitios-list">Sitios</a>
                        </li>
                        <li v-show="perfil === 2 | perfil === 3" class="nav-item">
                            <a class="nav-link" href="/equipo-list">Equipo</a>
                        </li>
                        <!--
                        <li v-show="perfil === 2 | perfil === 3" class="nav-item">
                            <a class="nav-link" href="/comentarios-list">Comentarios</a>
                        </li>-->
                        <li v-show="perfil === 2 | perfil === 3" class="nav-item">
                            <a class="nav-link" href="/preguntasfrecuentes-list">Preguntas frecuentes</a>
                        </li>
                        <li>
                            <a class="nav-link" @click="logout" href="#"><i class="bi bi-box-arrow-right"></i>Salir</a>
                        </li>
                    </ul>
                    <span class="navbar-text">
                        Bienvenido(a) <span>{{ nombre }}</span>!!!
                    </span>
                </div>
            </div>
        </nav>
    </div>
    <div class="imagenes d-flex flex-row flex-wrap justify-content-evenly">
        <img src="/img/buenaventura1.png" class="rounded float-start" alt="Puente de Tierra" srcset="">
        <img src="/img/buenaventura2.png" class="rounded float-end" alt="San Cipriano" srcset="">
    </div>
</template>

<style scoped>
.nav-link i {
    padding-right: 7px;
}

.nav-link:hover {
    border-bottom: 1px solid gray;
}

.navbar-text span {
    font-weight: bold;
}

img {
    max-width: 700px;
}
.imagenes{
    margin-top: 5rem;
}
</style>