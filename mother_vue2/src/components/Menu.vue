<template>
  <div class="menuEl">
    <table>
    <tbody>
		<tr v-for="i in Math.ceil(elements.length / 3)" :key="i">
			<td v-for="element in elements.slice((i-1)*3, i*3)">
				<h4 @click.prevent="showCateg($event)">{{element}}</h4>
			</td>
		</tr>
    </tbody>
    </table>
  </div>
</template>
<script>
	import axios from 'axios';
	export default {
		name: "menuEl",
		mounted(){
			axios.get('http://127.0.0.1:8000/motherscnotes/menu/')
			.then((response) => {
				// console.log(response);
				this.elements = response.data.names;
			})
		},
		data() {
			return {
				elements: [],
			}
		},
		methods: {
			showCateg: function(event){
				this.$emit("selectedCateg", event.currentTarget.textContent);
			}
		}
	}
</script>
