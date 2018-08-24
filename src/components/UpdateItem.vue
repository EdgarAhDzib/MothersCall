<template>
    <div class="itemCRUD">
		<div style="margin:auto; width:50%;">
		<h2>{{title}}</h2>
		<form>
			<table>
				<input-field v-for="(categ, propertyName, inc) in item.categFields" v-model="propertyName" :ref="propertyName" v-if="propertyName != 'notes'" v-bind:inpVal="categ" v-bind:categ="propertyName" v-on:inputData="getValues" :key="inc"></input-field>
			</table>
			<table>
				<tr>
					<td>Additional notes</td>
					<td>
						<textarea name="notes" rows="6" cols="50" v-model="item.categFields.notes"></textarea>
						<input type="hidden" name="id" v-model="item.id"/>
					</td>
				</tr>
				<tr>
					<td></td>
					<td>
						<button @click.prevent="updateItem" type="button" name="button">UPDATE</button>
					</td>
				</tr>
			</table>
		</form>
		</div>
		<div v-if="item.categFields.image">
			<img v-bind:src="imgUrl" style="width:400px;"/>
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
				type: Object,
				categFields: {
					type: Object
				}
			},
			compCateg:{
				type: String
			},
			itemNum:{
				type: Number
			},
		},
		data() {
			return {
				title: "Display Info",
				formValues: {},
				imgUrl: "",
			}
		},
		mounted() {
			if (this.item.categFields.hasOwnProperty("image")) {
				this.imgUrl = "static/images/" + this.item.categFields.image;
			}
		},
		methods: {
			updateItem(){
				this.formValues['id'] = this.item.id;
				this.formValues['notes'] = this.item.categFields.notes;
				// Name is always required for 'save' method in Django, so it must be passed as default field
				this.formValues['name'] = this.item.categFields.name;
				// console.log(this.formValues);
				var router=this.$router;
				axios.post('motherscnotes/post/' + this.compCateg + '/' + this.formValues.id, this.formValues)
				.then((response) => {
					// console.log(response);
					if (response.statusText == "OK") {
						// Refresh and hide form
						this.resetFields();
					} else {
						console.log("error");
						console.log(response.data);
						alert("Error in post");
					}
				});
			},
			resetFields() {
				this.$emit("refreshCateg", this.compCateg);
			},
			getValues(data) {
				var property = data[0];
				var value = data[1];
				this.formValues[property] = value;
			},
		}
	}
</script>
