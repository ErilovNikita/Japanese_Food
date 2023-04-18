<template>
    <div class="modal fade" :id="'food-'+ this.number" tabindex="-1">
      <div class="modal-dialog shadow">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="row h-100">
              <div class="col-12 col-md-7 text-center">
                <img :src="this.photo" class="h-100">
              </div>
              <div class="col-12 col-md-5">
                <div class="d-flex h-100 flex-column">
                  <div class="mt-4">
                    <h4 class="fw-bold">{{this.name}}</h4>
                    <p class="text-muted">{{this.description}}</p>
                  </div>
                  <div class="footer mt-auto">
                    <div class="row w-100">
                      <div class="col-6">
                        <h4 class="fw-bold">{{this.price}} ₽</h4>
                        <p class="fw-bold">225 гр.</p>
                      </div>
                      <div class="col-6 text-end">
                        <button type="button" class="btn btn-outline-success">В корзину</button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
          </div>
        </div>
      </div>
    </div>
</template>

<script>
  export default {
    props: ['name','price','description', 'number', 'photo'],
    methods: {
    }
  }
</script>

<style>
.modal-dialog {
  margin-top: 300px;
  max-height: 100% !important;
  max-width: 70% !important;
}
.modal-content {
  height: 400px;
}
.modal-header {
  position: relative;
  z-index: 1000;
}
.modal-content,
.modal-footer,
.modal-header {
  border: none !important;
}
.modal-body {
  margin-top: -50px;
}
.modal-body > div > div > div:nth-of-type(2){
  padding-top: 50px;
}
</style>