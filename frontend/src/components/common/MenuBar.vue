<template>
	<div>
		<v-app-bar color="#494949" fixed app>
			<v-icon class="px-3" dark large>mdi-basketball</v-icon>
			<!-- <v-toolbar-title class="font-weight-bold text-h5" style="color: #fbbd28">
				VUE - DJANGO DevKya WEB
			</v-toolbar-title> -->
			<v-spacer></v-spacer>
			<!-- display breakpoint -->
			<!-- display lg down -->
			<v-menu rounded offset-y>
				<template v-slot:activator="{ attrs, on }">
					<v-app-bar-nav-icon
						class="hidden-lg-and-up"
						v-bind="attrs"
						v-on="on"
						dark
					></v-app-bar-nav-icon>
				</template>

				<v-list>
					<v-list-item v-for="(item, index) in menu" :key="index" link>
						<v-list-item-title v-text="item.title"></v-list-item-title>
					</v-list-item>
				</v-list>
			</v-menu>

			<!-- display lg up -->
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
						:style="active ? 'color: #fbbd28' : undefined"
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
				{ icon: 'HOME', title: 'HOME', to: '' },
				{ icon: 'BLOG', title: 'BLOG', to: '' },
				{ icon: 'IAM', title: 'IAM', to: '' },
				{ icon: 'ADMIN', title: 'ADMIN', to: '' },
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
