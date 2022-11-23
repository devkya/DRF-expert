<template>
	<v-container>
		<v-card class="my-5 py-5 px-8" min-height="500px">
			<v-row class="mt-5">
				<v-col cols="12">
					<h1 class="text-center">I AM</h1>
				</v-col>
			</v-row>
			<v-row algin="center" justify="center">
				<v-col lg="4" md="12" sm="12" class="mb-5">
					<v-img
						src="@/assets/images/profile.jpg"
						alt="profile"
						class="rounded-circle mx-auto mb-5"
						max-height="250px"
						max-width="250px"
					></v-img>
					<h2 class="text-center">devKya</h2>
					<h3 class="text-center font-weight-light">
						Vue & Django Web Programmer
					</h3>
					<div class="text-center">
						<v-btn
							class="mx-5 mt-3"
							v-for="(item, idx) in icons"
							:key="idx"
							icon
						>
							<v-icon large>
								{{ item }}
							</v-icon>
						</v-btn>
					</div>
				</v-col>
				<v-col lg="8" md="0" sm="0">
					<h2>(주)LG 팜한농 SI 프로젝트 대시보드 개발</h2>
					<h3 class="font-weight-light">
						MsSql DB에 들어오는 실시간 데이터를 반영하고, 대시보드 형태로
						사용자가 각 공장별, 태그별 현황을 파악함.
					</h3>
					<br />
					<br />
					<h2>(주)XpertINC CSound App Web</h2>
					<h3 class="font-weight-light">
						Smart Glasses에서 사용되는 C-Sound App의 사용자 정보와 라이센스를 볼
						수 있는 ADMIN PAGE 개발
					</h3>
					<br />
					<br />
					<h2>OAS를 사용한 Web 인터페이스</h2>
					<h3 class="font-weight-light">
						(주)XpertINC & (주)팜한농 프로젝트로, SI Tool(OAS)의 라이브 데이터를
						받아 탱크의 레벨링을 결정하는 Web Page 개발
					</h3>
					<br />
					<br />
				</v-col>
			</v-row>
		</v-card>
	</v-container>
</template>
<script>
export default {
	name: 'HomeIam',
	components: {},
	data() {
		return {
			icons: ['mdi-facebook', 'mdi-twitter', 'mdi-instagram'],
		};
	},
	setup() {},
	created() {},
	mounted() {},
	unmounted() {},
	methods: {},
};
</script>
