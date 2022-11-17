<template>
	<div>
		<v-app-bar color="#494949" fixed app>
			<v-icon class="px-3" dark large>mdi-basketball</v-icon>
			<!-- <v-toolbar-title class="font-weight-bold text-h5" style="color: #fbbd28">
				VUE - DJANGO DevKya WEB
			</v-toolbar-title> -->
			<v-spacer></v-spacer>
			<!-- display breakpoint -->
			<v-app-bar-nav-icon class="hidden-lg-and-up" dark></v-app-bar-nav-icon>
			<v-slide-group class="hidden-lg-and-down">
				<v-slide-item
					v-for="(item, index) in menu"
					:key="index"
					v-slot="{ active, toggle }"
				>
					<v-btn
						id="menu-btn"
						class="elevation-0 px-5"
						:input-value="active"
						:style="
							active ? 'color: #fbbd28' : 'background-color : transparent'
						"
						@click="toggle"
						plain
						dark
						>{{ item.title }}</v-btn
					>
				</v-slide-item>
			</v-slide-group>
		</v-app-bar>
	</div>
</template>
<script>
export default {
	name: 'MenuBar',
	components: {},
	data() {
		return {
			menu: [
				{ icon: 'HOME', title: 'HOME' },
				{ icon: 'BLOG', title: 'BLOG' },
				{ icon: 'IAM', title: 'IAM' },
				{ icon: 'ADMIN', title: 'ADMIN' },
			],
		};
	},
	setup() {},
	created() {},
	mounted() {},
	unmounted() {},
	methods: {},
};
</script>
<style scoped>
#menu-btn::before {
	background-color: transparent !important;
}
</style>
