<template>
	<v-app>
		<MenuBar></MenuBar>>
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
};
</script>
