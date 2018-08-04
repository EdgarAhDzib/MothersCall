<template>
    <div class="itemCRUD">
		<div style="margin:auto; width:50%;">
		<h2>{{title}}</h2>
		<form>
			<table>
				<input-field v-for="(categ,inc) in subjFields" v-if="categ != 'id' && categ != 'notes'" v-bind:inpVal="subjFields[categ]" v-bind:categ="categ" v-on:inputData="getValues" :key="inc"></input-field>
			</table>
			<table>
				<tr>
					<td>Additional notes</td>
					<td>
						<textarea name="notes" rows="6" cols="50" v-model="notes"></textarea>
					</td>
				</tr>
				<tr>
					<td></td>
					<td>
						<button @click.prevent="addItem" type="button" name="button">ADD</button>
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
		name: "add_form",
		props: {
			subjFields:{
				type: Array
			},
			compCateg:{
				type: String
			},
		},
		mounted(){
			// console.log("Add item mounted");
			// console.log(this.subjFields);
		},
		created(){
			// console.log("Add item created");
		},
		data() {
			return {
				title: "Add Entry",
				notes: "",
				formValues: {},
			}
		},
		methods: {
			addItem() {
				this.formValues['notes'] = this.notes;
				var router = this.$router;
				axios.post('http://127.0.0.1:8000/motherscnotes/add/' + this.compCateg + '/', this.formValues)
				.then((response) => {
					// console.log(response);
					if (response.statusText == "Created") {
						// Refresh and hide form
						// console.log("Created");
						// console.log(response.data);
						this.resetFields();
						return false;
						// router.push("/");
					} else {
						console.log("error");
						console.log(response.data);
						alert("Error in post");
					}
				});
			},
			resetFields() {
				console.log("Reset fields");
				// REDO: emit signal to reload the menu page with the current category
				this.$emit("refreshCateg", this.compCateg);
			},
			getValues(data) {
				// console.log("Passed to parent", data);
				var property = data[0];
				var value = data[1];
				this.formValues[property] = value;
				// console.log(this.formValues);
			},
		}
	}
</script>
