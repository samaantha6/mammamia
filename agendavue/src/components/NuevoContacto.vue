<template>
    <section id="nuevo">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <h2>Añadir contacto</h2>
            <hr class="star-primary" />
          </div>
        </div>
        <div class="row">
          <div class="col-lg-8 col-lg-offset-2">
            <form @submit.prevent="addContact">
              <div class="form-group">
                <label>Nombre</label>
                <input
                  v-model="contacto.nombre"
                  type="text"
                  class="form-control"
                  placeholder="Nombre"
                />
              </div>
              <div class="form-group">
                <label>Email</label>
                <input
                  v-model="contacto.email"
                  type="email"
                  class="form-control"
                  placeholder="Email"
                />
              </div>
              <div class="form-group">
                <label>Teléfono</label>
                <input
                  v-model="contacto.telefono"
                  type="tel"
                  class="form-control"
                  placeholder="Teléfono"
                />
              </div>
              <button type="submit" class="btn btn-success btn-lg">
                Añadir
              </button>
            </form>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    name: "NuevoContacto",
    data() {
      return {
        contacto: {
          nombre: "",
          email: "",
          telefono: "",
        },
      };
    },
    methods: {
      addContact() {
        console.log("Contacto añadido:", this.contacto);
        // Aquí puedes añadir la lógica para guardar el contacto
      },
    },
  };
  </script>
  
  <style scoped>
  /* Estilos personalizados */
  </style>