<template>
    <section id="contactos">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <h2>Contactos</h2>
            <hr class="star-primary" />
          </div>
        </div>
        <div class="row">
          <div class="col-xs-4"><h4>Nombre</h4></div>
          <div class="col-xs-4"><h4>Email</h4></div>
          <div class="col-xs-3"><h4>Teléfono</h4></div>
        </div>
        <div class="row">
          <div class="col-xs-4">
            <p>John Doe</p>
          </div>
          <div class="col-xs-4">
            <p>john.doe@deusto.es</p>
          </div>
          <div class="col-xs-3">
            <p>555555555</p>
          </div>
          <div class="col-xs-1">
            <button class="btn btn-danger btn-sm">
              <span class="glyphicon glyphicon-remove"></span>
            </button>
          </div>
        </div>
        <div>
          <div class="row">
            <div class="col-xs-12">
              <p>No se ha encontrado ningún contacto.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    name: "AgendaContactos",
  };
  </script>
  
  <style scoped>
  /* Añade estilos si es necesario */
  </style>