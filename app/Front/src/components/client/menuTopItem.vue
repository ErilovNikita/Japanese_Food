<script setup>
    import foodModal from '@/components/modal/food.vue' 
</script>

<template>
    <foodModal 
        :number = this.number
        :name = this.name
        :price = this.price
        :description = this.description
        :photo = this.photo
    />
    <div class="item-bloc col-6 col-md-6 col-lg-4 col-xl-3" data-bs-toggle="modal" :data-bs-target="'#food-' + this.number">
        <div class="item shadow">
            <div class="image text-center">
                <img v-if="this.photo" :src="this.photo">
                <img v-if="!this.photo" src="@/assets/image/no_image_food.png">
            </div>
            
            <h5 class="fw-bold">{{this.name}}</h5>
            <p class="text-muted fw-light">{{this.description}}</p>
            <div class="row">
                <div class="col-6">
                    <h5 class="fw-bolder">{{this.price}} ₽</h5>
                </div>
                <div class="col-6 text-end">
                    <h5><font-awesome-icon :icon="['fas', 'cart-shopping']" style="color: rgb(214, 0, 212); margin-right: 10px;" /></h5>
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

<style scoped>
.item-bloc {
    padding: 10px;
}
.item {
    padding: 35px;
    border-radius: 14px;
    transition: .3s;
    background-color: white;
}
.image {
    padding: 20px;
}
.image > img {
    max-height: 150px;
    height: 100%;
}
.item:hover {
    cursor: pointer;
    transform: scale(1.04);
    /* background-color: rgb(238, 238, 238); */
}
</style>