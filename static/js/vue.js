const config = {
    delimiters: ["[[", "]]"],
    methods: {
        redirectToPage(endPoint) {
            if (endPoint === 'news') {
                window.open(`${this.url}/news`);
            } else if (endPoint === 'about') {
                window.open(`${this.url}/about`);
            }
        }
    }
}

const app = Vue.createApp(config)

app.component('language-tumbler', languageTumblerComponent)
app.component('news', newsComponent)
app.component('services', servicesComponent)
app.component('news-banner', newsBannerComponent)


const vm = app.mount('#app')