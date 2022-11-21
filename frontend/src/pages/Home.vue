<template>
	<v-app>
		<MenuBar @move-to="test(menu)"></MenuBar>>
		<v-main>
			<router-view />
		</v-main>
	</v-app>
</template>

<script>
import MenuBar from '@/components/common/MenuBar.vue';
export default {
	name: 'Home',
	components: { MenuBar },
	data: () => ({
		//
	}),
	methods: {
		test(menu) {
			console.log('test()...', menu);
		},
	},
};
</script>
