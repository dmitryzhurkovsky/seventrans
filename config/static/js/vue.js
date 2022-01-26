const config = {
    delimiters: ["[[", "]]"],
    methods: {
        redirectToPage(endPoint) {
            if (endPoint === 'news') {
                window.open(`https://7trans.by/news`);
            } else if (endPoint === 'about') {
                window.open(`https://7trans.by/about`);
            }
        }
    }
}

const app = Vue.createApp(config)

app.component('language-tumbler', languageTumblerComponent)
app.component('news', newsComponent)
app.component('services', servicesComponent)


const vm = app.mount('#app')