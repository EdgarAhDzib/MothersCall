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
				<td v-bind:id="element.id" @click="review($event)"><a href="#formTop">Edit</a></td>
				<td v-bind:id="element.id" @click="delItem($event)">Delete</td>
			</tr>
		</tbody>
		</table>
    </div>
    <div class="itemFormDiv" style="float:left;width:70%;">
		<a id="formTop">
			<add-item v-if="addForm" v-bind:subjFields="subjFields" v-bind:compCateg="category" v-on:refreshCateg="refresh"></add-item>
			<update-item v-if="updateForm" :key="item.id" v-bind:item="item" v-bind:compCateg="category" v-bind:itemNum="item.id" v-on:refreshCateg="refresh"></update-item>
		</a>
    </div>
  </div>
</template>
<script>
	import axios from 'axios';
	import AddItem from "../components/AddItem.vue";
	import UpdateItem from "../components/UpdateItem.vue";
	import Menu from "../components/Menu.vue";
	export default {
		components: {
			"menu-div": Menu,
			"add-item": AddItem,
			"update-item": UpdateItem,
		},
		name: "mainVue",
		created(){
			axios.get('http://127.0.0.1:8000/motherscnotes/view/' + this.category + '/')
			.then((response) => {
				// console.log(response);
				this.elements = response.data;
			});
			axios.get('http://127.0.0.1:8000/motherscnotes/getfields/' + this.category + '/')
			.then((response) => {
				// console.log(response.data);
				this.subjFields = response.data;
			});
		},
		data() {
			return {
				elements: [],
				item: {
					item: "",
					categFields: {},
					notes: "",
				},
				category: "fauna",
				title: "Fauna",
				addForm: true,
				updateForm: false,
				subjFields: [],
			}
		},
		methods: {
			review: function(event){
				axios.get('http://127.0.0.1:8000/motherscnotes/get/' + this.category+ '/' + event.currentTarget.id)
				.then((response) => {
					this.addForm = false;
					this.updateForm = true;
					// Reset item and all its field, to prevent passing fields from previous item's model
					this.item = {
						item: "",
						categFields: {},
						notes: "",
					};
					for (var property in response.data) {
						if (property == "id") {
							this.item.id = response.data[property];
						} else {
							this.item.categFields[property] = response.data[property];
						}
					}
					this.item.compCateg = this.category;
				});
			},
			delItem: function(event){
				var conf = confirm("Delete this entry?");
				if (conf) {
					axios.delete('http://127.0.0.1:8000/motherscnotes/delete/' + this.category + '/' + event.currentTarget.id)
					.then((response) => {
						// console.log(response);
						this.refresh(this.category);
					});
				} else {
					return false;
				}
			},
			showTitle: function(categTitle){
				this.title = categTitle;
				var newCateg = categTitle.toLowerCase();
				this.category = newCateg;
				axios.get('http://127.0.0.1:8000/motherscnotes/view/' + this.category + '/')
				.then((response) => {
					// console.log(response);
					this.elements = response.data;
				});
				axios.get('http://127.0.0.1:8000/motherscnotes/getfields/' + this.category + '/')
				.then((response) => {
					// console.log(response.data);
					this.addForm = true;
					this.updateForm = false;
					this.subjFields = response.data;
				});
			},
			refresh: function(menuCateg){
				this.showTitle(menuCateg);
				this.item = {
					id: "",
					categFields: {},
					notes: "",
				},
				this.addForm = true;
				this.updateForm = false;
				this.subjFields = [];
			},
		}
	}
</script>
