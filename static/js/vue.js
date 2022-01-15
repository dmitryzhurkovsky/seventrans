const config = {
    delimiters: ["[[", "]]"],
}

const app = Vue.createApp(config)

app.component('language-tumbler', languageTumbler)
app.component('news', news)
app.component('service-page', servicePage)


const vm = app.mount('#app')