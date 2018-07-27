<template>
  <div class="displayDiv">
	<div><menu-div v-on:selectedCateg="showTitle"></menu-div></div>
    <h1>Mother's Call {{title}}</h1>
    <div style="float:left;width:30%;">
		<table>
		<tbody v-for="element in elements" :key="element.id">
			<tr>
				<td>
					<h4>{{element.name}}</h4>
				</td>
				<td><em>{{element.indigenous}}</em></td>
				<td v-bind:id="element.id" @click="review($event)">Edit</td>
				<td v-bind:id="element.id" @click="delItem($event)">Delete</td>
			</tr>
		</tbody>
		</table>
    </div>
    <div class="itemFormDiv" style="float:left;width:70%;">
		<item-form v-bind:item="item" v-bind:compCateg="category"></item-form>
    </div>
  </div>
</template>
<script>
	import axios from 'axios';
	import ItemForm from "../components/ItemForm.vue";
	import Menu from "../components/Menu.vue";
	export default {
		components: {
			"item-form": ItemForm,
			"menu-div": Menu
		},
		name: "mainVue",
		created(){
			// console.log(this.category);
			axios.get('http://127.0.0.1:8000/motherscnotes/view/' + this.category + '/')
			.then((response) => {
				// console.log(response);
				this.elements = response.data;
			});
			axios.get('http://127.0.0.1:8000/motherscnotes/getfields/' + this.category + '/')
			.then((response) => {
				// console.log(response.data);
				this.item.categFields = response.data;
			});
		},
		data() {
			return {
				elements: [],
				item: {},
				category: "fauna",
				title: "",
			}
		},
		methods: {
			review: function(event){
				axios.get('http://127.0.0.1:8000/motherscnotes/get/' + this.category+ '/' + event.currentTarget.id)
				.then((response) => {
					for (var property in response.data) {
						this.item[property] = response.data[property]; // restore "_"+ property
					}
					this.item.update = true;
					// this.item.showForm = true;
				});
			},
			delItem: function(event){
				console.log(event.currentTarget.id);
				var conf = confirm("Delete this entry?");
				if (conf) {
					axios.delete('http://127.0.0.1:8000/motherscnotes/delete/' + this.category + '/' + event.currentTarget.id)
					.then((response) => {
						console.log(response);
					});
				} else {
					return false;
				}
			},
			showTitle: function(categTitle){
				this.title = categTitle;
				var newCateg = categTitle.toLowerCase();
				this.category = newCateg;
				this.item = {};
				axios.get('http://127.0.0.1:8000/motherscnotes/view/' + this.category + '/')
				.then((response) => {
					// console.log(response);
					this.elements = response.data;
				});
				axios.get('http://127.0.0.1:8000/motherscnotes/getfields/' + this.category + '/')
				.then((response) => {
					// console.log(response.data);
					this.item.categFields = response.data;
				});
			},
		}
	}
</script>
