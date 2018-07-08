<template>
  <div class="fauna">
    <h1>Fauna of Mother's Call</h1>
    <div class="addCreature">
		<fauna-form></fauna-form>
    </div>
    <div v-for="animal in fauna" :key="animal.id">
		<h3>{{animal.name}} : <em>{{animal.indigenous}}</em></h3>
    </div>
  </div>
</template>
<script>
	import axios from 'axios';
	import FaunaForm from "./FaunaForm.vue";
	// This is throwing an "unexpected require" error
	// var FaunaForm = require('./FaunaForm');
	export default {
		components: {
			"fauna-form": FaunaForm
		},
		name: "fauna",
		mounted(){
			axios.get('http://127.0.0.1:8000/motherscnotes/fauna')
			.then((response) => {
				console.log(response);
				this.fauna = response.data;
			})
		},
		data() {
			return {
				fauna: [],
			}
		}
	}
</script>
