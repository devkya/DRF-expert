<template>
	<div>
		<v-app-bar color="#494949" clipped-right app>
			<v-icon class="px-5" dark large>mdi-basketball</v-icon>
			<v-toolbar-title class="font-weight-bold text-h5" style="color: #fbbd28">
				VUE - DJANGO WEB
			</v-toolbar-title>
			<v-spacer></v-spacer>
			<!-- display breakpoint -->
			<!-- display lg down -->

			<v-app-bar-nav-icon
				class="hidden-lg-and-up"
				@click.stop="drawer = !drawer"
				dark
			>
			</v-app-bar-nav-icon>

			<!-- display lg up -->
			<v-slide-group class="hidden-md-and-down">
				<v-slide-item
					v-for="(item, index) in menu"
					:key="index"
					v-slot="{ active, toggle }"
				>
					<v-btn
						id="menu-btn"
						class="elevation-0 px-5"
						:input-value="active"
						v-model="menu"
						:style="active ? 'color: #fbbd28' : undefined"
						@click="
							toggle();
							$emit('menuChg', item.to);
						"
						plain
						dark
					>
						{{ item.title }}
					</v-btn>
				</v-slide-item>
			</v-slide-group>
		</v-app-bar>

		<v-navigation-drawer
			v-model="drawer"
			clipped
			right
			temporary
			:style="{ top: $vuetify.application.top + 'px', zIndex: 4 }"
			app
		>
			<v-list rounded>
				<v-list-item
					class="pa-3"
					v-for="(item, index) in menu"
					:key="index"
					link
					@click="$emit('menuChg', item.to)"
				>
					<v-list-item-icon>
						<v-icon>{{ item.icon }}</v-icon>
					</v-list-item-icon>

					<v-list-item-content>
						<v-list-item-title>{{ item.title }}</v-list-item-title>
					</v-list-item-content>
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
				{ icon: 'mdi-home', title: 'HOME', to: 'home' },
				{ icon: 'mdi-web', title: 'BLOG', to: 'posts' },
				{ icon: 'mdi-account-circle', title: 'IAM', to: 'iam' },
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
