<template>
  <div class="fauna">
    <h1>Fauna of Mother's Call</h1>
    <div class="addCreature">
		<fauna-form></fauna-form>
    </div>
    <table>
    <tbody v-for="animal in fauna" :key="animal.id">
		<tr><td><h4>{{animal.name}}</h4></td><td><em>{{animal.indigenous}}</em></td><td v-bind:id="animal.id" @click="review($event)">Edit</td></tr>
    </tbody>
    </table>
  </div>
</template>
<script>
	import axios from 'axios';
	import FaunaForm from "../components/FaunaForm.vue";
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
		},
		methods: {
			review: function(event){
				// console.log(event.currentTarget.id);
				axios.get('http://127.0.0.1:8000/motherscnotes/faunaget/' + event.currentTarget.id)
				.then((response) => {
					console.log(response);
				});
			}
		}
	}
</script>
