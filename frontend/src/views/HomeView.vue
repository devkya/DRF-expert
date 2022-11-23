<template>
	<div>
		<Home-Img ref="home"></Home-Img>
		<Home-Post-List ref="posts"></Home-Post-List>
		<Home-Iam ref="iam"></Home-Iam>
	</div>
</template>

<script>
import HomeImg from '@/components/home/HomeImg.vue';
import HomePostList from '@/components/home/HomePostList.vue';
import HomeIam from '@/components/home/HomeIam.vue';

export default {
	components: { HomeImg, HomePostList, HomeIam },
	data() {
		return {};
	},
	props: {},
	setup() {},
	created() {},
	mounted() {},
	unmounted() {},
	watched: {},
	computed: {},
	methods: {
		scrollTo(menu) {
			if (menu == 'home') {
				this.$vuetify.goTo(0);
			}
			this.$vuetify.goTo(this.$refs[menu]);
		},
	},
};
</script>
