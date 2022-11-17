<template>
	<div>
		<v-app-bar clipped-right flat dark app>
			<v-spacer></v-spacer>
		</v-app-bar>

		<v-navigation-drawer clipped right flat dark app>
			<v-list>
				<v-list-item class="px-2">
					<v-list-item-avatar>
						<v-img src="https://randomuser.me/api/portraits/men/11.jpg"></v-img>
					</v-list-item-avatar>

					<v-list-item-title>John Doe</v-list-item-title>
				</v-list-item>
				<v-list-item
					v-for="item in navbarlist"
					:key="item.route"
					:to="item.route"
				>
					<v-list-item-icon>
						<v-icon>{{ item.icon }}</v-icon>
					</v-list-item-icon>
					<v-list-item-content>{{ item.text }}</v-list-item-content>
				</v-list-item>
			</v-list>
		</v-navigation-drawer>
	</div>
</template>
<script>
export default {
	name: 'MenuBar',
	components: {},
	data() {
		return {
			drawer: false,
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
