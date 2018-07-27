<template>
    <div class="itemCRUD">
		<div style="margin:auto; width:50%;">
		<h2 v-on:click="addForm = !addForm">{{title}}</h2>
		<form v-show="addForm">
			<table>
				<input-field v-for="(categ,inc) in item.categFields" v-if="categ != 'id' && categ != 'notes'" v-bind:inpVal="item[categ]" v-bind:categ="categ" v-on:inputData="getValues" :key="inc"></input-field>
			</table>
			<table>
				<tr>
					<td>Additional notes</td>
					<td>
						<textarea name="notes" rows="6" cols="50" v-model="item.notes"></textarea>
						<input type="hidden" name="id" v-model="item.id"/>
					</td>
				</tr>
				<tr>
					<td></td>
					<td>
						<button v-if="item.update" @click.prevent="updateItem" type="button" name="button">UPDATE</button>
						<button v-else="item.update" @click.prevent="addItem" type="button" name="button">ADD</button>
					</td>
				</tr>
			</table>
		</form>
		</div>
    </div>
</template>
<script>
	import axios from 'axios'
	import InputField from './InputField.vue'
	export default {
		components: {
			"input-field": InputField
		},
		name: "item_form",
		props: {
			item:{
				type: Object
			},
			compCateg:{
				type: String
			},
		},
		mounted(){
			// console.log(this.item);
		},
		updated(){
			// console.log(this.compCateg);
		},
		data() {
			return {
				title: "Display Info",
				addForm: false,
				update: false,
				formValues: {},
			}
		},
		methods: {
			updateItem(){
				this.formValues['id'] = this.item.id;
				this.formValues['notes'] = this.item.notes;
				var router=this.$router;
				axios.post('http://127.0.0.1:8000/motherscnotes/post/' + this.compCateg + '/' + this.formValues.id, this.formValues)
				.then((response) => {
					// console.log(response);
					if (response.statusText == "OK") {
						// Refresh and hide form
						console.log("Update");
						console.log(response.data);
						this.resetFields();
						router.push("/");
					} else {
						console.log("error");
						console.log(response.data);
						alert("Error in post");
					}
				})
			},
			addItem() {
				this.formValues['notes'] = this.item.notes;
				var router = this.$router;
				axios.post('http://127.0.0.1:8000/motherscnotes/add/' + this.compCateg + '/', this.formValues)
				.then((response) => {
					// console.log(response);
					if (response.statusText == "Created") {
						// Refresh and hide form
						console.log("Created");
						console.log(response.data);
						this.resetFields();
						router.push("/");
					} else {
						console.log("error");
						console.log(response.data);
						alert("Error in post");
					}
				});
			},
			resetFields() {
				return {
				};
			},
			getValues(data) {
				// console.log("Passed to parent", data);
				var property = data[0];
				var value = data[1];
				this.formValues[property] = value;
				// console.log(this.formValues);
			}
		}
	}
</script>
