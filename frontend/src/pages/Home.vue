<template>
	<v-app>
		<MenuBar @menuChg="scrollTo"></MenuBar>
		<v-main>
			<router-view ref="ContentComponent" :menu="menu" />
		</v-main>
		<Footer></Footer>
	</v-app>
</template>

<script>
import MenuBar from '@/components/common/MenuBar.vue';
import Footer from '@/components/common/Footer.vue';
export default {
	name: 'Home',
	components: { MenuBar, Footer },
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
