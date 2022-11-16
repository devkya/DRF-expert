const { defineConfig } = require('@vue/cli-service');
const FileManagerPlugin = require('filemanager-webpack-plugin');

module.exports = defineConfig({
	transpileDependencies: ['vuetify'],
	// build output setting
	outputDir: 'dist',
	publicPath: '/',
	assetsDir: 'static',

	// devServer proxy & static setting
	devServer: {
		proxy: 'http://localhost:8000',
	},
	pages: {
		index: {
			template: 'public/home.html',
			filename: 'home.html',
			title: 'home.html',
		},
	},

	// filemanager setting
	configureWebpack: {
		plugins: [
			new FileManagerPlugin({
				events: {
					onStart: {
						delete: [
							{ source: '../backend/templates/', options: { force: true } },
							{ source: '../backend/static/', options: { force: true } },
						],
						mkdir: ['../backend/templates/', '../backend/static/'],
					},
					onEnd: {
						copy: [
							{ source: './dist/static', destination: '../backend/static/' },
							{ source: './dist/*.html', destination: '../backend/templates/' },
						],
					},
				},
			}),
		],
	},
});
