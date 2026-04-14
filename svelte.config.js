import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';


const dev = "production" === "development";

const config = {

	preprocess: vitePreprocess(),

	kit: {
		adapter: adapter({
		    pages: "docs",
		    assets: "docs"
		}),
		paths: {
		    base: dev ? "" : "/bike-share-toronto",
		}
	}
};

export default config;