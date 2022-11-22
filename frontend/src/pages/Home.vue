<template>
	<v-app>
		<MenuBar @menuChg="scrollTo"></MenuBar>
		<v-main>
			<router-view ref="ContentComponent" :menu="menu" />
		</v-main>
	</v-app>
</template>

<script>
import MenuBar from '@/components/common/MenuBar.vue';
export default {
	name: 'Home',
	components: { MenuBar },
	data: () => ({
		menu: '',
		//
	}),
	methods: {
		scrollTo(menu) {
			this.$refs.ContentComponent.scrollTo(menu);
		},
	},
};
</script>
