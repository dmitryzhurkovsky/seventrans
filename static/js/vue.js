const config = {
    delimiters: ["[[", "]]"],
    methods: {
        redirectToPage(endPoint) {
            if (endPoint === 'news') {
                window.open(`http://7trnas.by/news`);
            } else if (endPoint === 'about') {
                window.open(`http://7trnas.by/about`);
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