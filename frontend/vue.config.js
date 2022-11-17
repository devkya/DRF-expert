const { defineConfig } = require('@vue/cli-service');
module.exports = defineConfig({
	transpileDependencies: ['vuetify'],

	outputDir: 'dist',
	publicPath: '/',
	assetsDir: 'static',

	// devServer: {
	// 	proxy: 'http://localhost:8000',
	// },

	pages: {
		home: {
			entry: 'src/pages/Home.js',
			template: 'public/index.html',
			filename: 'home.html',
			title: 'home.html',
		},
	},
});
