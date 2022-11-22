<template>
	<v-container>
		<v-row class="mt-3" align="center" jusify="center">
			<v-col cols="12">
				<h1 class="text-center">Post List</h1>
			</v-col>
		</v-row>
		<v-row>
			<v-col cols="4" v-for="n in 6" :key="n">
				<v-card class="ma-3" max-height="500">
					<v-img
						height="250"
						src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
					></v-img>

					<v-card-title class="py-3">Post Title</v-card-title>
					<v-row align="center" justify="center">
						<v-col cols="5">
							<v-card-text class="text-center">Category</v-card-text>
						</v-col>
						<v-col cols="4">
							<v-card-text>
								5<v-icon color="red">mdi-cards-heart</v-icon>
							</v-card-text>
						</v-col>
						<v-spacer></v-spacer>
					</v-row>

					<v-card-text>
						<div>post summary description</div>
					</v-card-text>
				</v-card>
			</v-col>
			<v-row>
				<v-col>
					<v-pagination v-model="page" :length="5" class="py-5"></v-pagination>
				</v-col>
			</v-row>

			<!-- <v-col cols="4">
				<v-card class="mx-auto" max-width="374">
					<v-img
						height="250"
						src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
					></v-img>

					<v-card-title>Cafe Badilico</v-card-title>

					<v-card-text>
						<v-row align="center" class="mx-0">
							<v-rating
								:value="4.5"
								color="amber"
								dense
								half-increments
								readonly
								size="14"
							></v-rating>

							<div class="grey--text ms-4">4.5 (413)</div>
						</v-row>

						<div class="my-4 text-subtitle-1">$ • Italian, Cafe</div>

						<div>
							Small plates, salads & sandwiches - an intimate setting with 12
							indoor seats plus patio seating.
						</div>
					</v-card-text>
				</v-card>
			</v-col> -->
		</v-row>
	</v-container>
</template>
<script>
export default {
	name: 'HomePostList',
	components: {},
	data() {
		return {};
	},
	setup() {},
	created() {},
	mounted() {},
	unmounted() {},
	methods: {},
};
</script>
