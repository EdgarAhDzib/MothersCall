<template>
	<tr>
		<td>{{inp_title[categ]}}</td><td><input type="text" v-bind:name="categ" v-bind:value="inpVal" v-on:keyup="sendData($event.currentTarget.name, $event.currentTarget.value)" v-bind:placeholder="categ"/></td>
	</tr>
</template>
<script>
	export default {
		name: "input_template",
		props: {
			categ: {
				type: String
			},
			inpVal: {
				type: String
			},
		},
		mounted() {
			// console.log(this.categ);
		},
		data() {
			return {
				inp_title: {
					name: "Given name",
					image: "Image file",
					relatives: "Family relatives",
					village: "Village setting",
					elder: "Elder reincarnation",
					indigenous: "Indigenous name",
					classification: "Taxonomy classification",
					chap_num: "Tentative number",
				},
			}
		},
		methods: {
			sendData: function(name, value){
				// console.log(name, value);
				var data = [name, value]
				this.$emit("inputData", data);
			}
		}
	}
</script>
