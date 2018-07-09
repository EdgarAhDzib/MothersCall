<template>
    <div class="faunaCreate">
    <h2 v-on:click="addForm = !addForm">{{title}}</h2>
		<form v-show="addForm">
			<input v-model="creatureName" name="name" placeholder="Basic name"/><br/>
			<input v-model="creatureClass" name="classification" placeholder="Taxonomy classification"/><br/>
			<input v-model="creatureIndigenous" name="indigenous" placeholder="Indigenous name"/><br/>
			<input v-model="creatureImage" name="image" placeholder="Image file"/><br/>
			<textarea v-model="creatureDesc" name="notes"></textarea><br/>
			<button @click.prevent="addCreature" type="button" name="button">ADD</button>
			<br/>
		</form>
    </div>
</template>
<script>
	import axios from 'axios'
	export default {
		name: "fauna_create",
		mounted(){
		},
		data() {
			return {
				title: "Add Creature",
				creatureName: "",
				creatureClass: "",
				creatureIndigenous: "",
				creatureImage: "",
				creatureDesc: "",
				addForm: false,
			}
		},
		methods: {
			addCreature(){
				var data = {
					name: this.creatureName,
					classification: this.creatureClass,
					indigenous: this.creatureIndigenous,
					image: this.creatureImage,
					notes: this.creatureDesc
				}
				var router=this.$router;
				// console.log(data);
				axios.post('http://127.0.0.1:8000/motherscnotes/faunapost/', data)
				.then((response) => {
					// console.log(response);
					if (response.statusText == "Created") {
						// Refresh and hide form
						this.data();
						router.push("fauna");
					} else {
						console.log("error " + response.data);
						alert("Error in post");
					}
				})
			}
		}
	}
</script>
