<script setup>
    import navbar from '@/components/client/navbar.vue'
    import downBar from '@/components/client/footer.vue'
</script>

<template>
    <navbar />

    <div class="view">
      <div class="container p-4">
        <h3 class="fw-bolder">{{this.name}}</h3>
        <p>{{this.price}} Руб</p>
        <p>{{this.description}}</p>
      </div>

    </div>

    <downBar />
</template>


<style scoped>
  .view {
    margin-top: 88px;
  }
</style>

<script>
    import baseURL from "@/config"

    export default {
        data() {
            return {
                foodNumber: null,
                name: null,
                price: 0,
                description: ''
            }
        },
        mounted() {
            let path = this.$route.path
            this.foodNumber = path.substring(path.lastIndexOf('/') + 1, path.length)

            this.getData(this.foodNumber)
                .then((data) => {
                    console.log(data)
                    this.name = data.name
                    this.price = data.price
                    this.description = data.description
                })
        },
        methods: {
          async getData(foodNumber) {
            const response = await fetch(`${baseURL}/api/food/${foodNumber}`, {
              method: "GET",
              mode: "cors"
            });
            if (!response.ok) {
                window.location.href = "/"
            }
            const jsonData = await response.json();
            return jsonData
          }
        }
    }
</script>