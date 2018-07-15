<template>
    <div class="faunaCreate">
    <h2 v-on:click="addForm = !addForm">{{title}}</h2>
		<form v-show="addForm">
			<input type="hidden" name="id" v-model="item._id"/>
			Basic name <input type="text" name="name" v-model="item._name"/><br/>
			Taxonomy classification <input name="classification" v-model="item._classification"/><br/>
			Indigenous name <input name="indigenous" v-model="item._indigenous"/><br/>
			Image file <input name="image" v-model="item._image"/><br/>
			Additional notes <textarea name="notes" v-model="item._notes"></textarea><br/>
			<button v-if="item.update" @click.prevent="updateCreature" type="button" name="button">UPDATE</button>
			<button v-else="item.update" @click.prevent="addCreature" type="button" name="button">ADD</button>
			<br/>
		</form>
    </div>
</template>
<script>
// placeholder="Basic name" 
	import axios from 'axios'
	export default {
		name: "fauna_create",
		props: {
			item:{
				type: Object
			}
		},
		mounted(){
			// console.log(this.item);
		},
		data() {
			return {
				title: "Display Info",
				_id: "",
				_name: "",
				_classification: "",
				_indigenous: "",
				_image: "",
				_notes: "",
				addForm: false,
				update: false,
			}
		},
		methods: {
			updateCreature(){
				var postData = {
					id: this.item._id,
					name: this.item._name,
					classification: this.item._classification,
					indigenous: this.item._indigenous,
					image: this.item._image,
					notes: this.item._notes
				}

				var router=this.$router;
				axios.post('http://127.0.0.1:8000/motherscnotes/faunapost/' + postData.id, postData)
				.then((response) => {
					// console.log(response);
					if (response.statusText == "OK") {
						// Refresh and hide form
						console.log("Update");
						console.log(response.data);
						this.resetFields();
						router.push("fauna");
					} else {
						console.log("error");
						console.log(response.data);
						alert("Error in post");
					}
				})
			},
			addCreature() {
				var postData = {
					name: this.item._name,
					classification: this.item._classification,
					indigenous: this.item._indigenous,
					image: this.item._image,
					notes: this.item._notes
				}
				var router = this.$router;
				axios.post('http://127.0.0.1:8000/motherscnotes/faunaadd/', postData)
				.then((response) => {
					// console.log(response);
					if (response.statusText == "Created") {
						// Refresh and hide form
						console.log("Created");
						console.log(response.data);
						this.resetFields();
						router.push("fauna");
					} else {
						console.log("error");
						console.log(response.data);
						alert("Error in post");
					}
				});
			},
			resetFields() {
				return {
					_id: "",
					_name: "",
					_classification: "",
					_indigenous: "",
					_image: "",
					_notes: "",
				}
			}
		}
	}
</script>
