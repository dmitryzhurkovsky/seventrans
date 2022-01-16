const config = {
    delimiters: ["[[", "]]"],
}

const app = Vue.createApp(config)

app.component('language-tumbler', languageTumblerComponent)
app.component('news', newsComponent)
app.component('services', servicesComponent)


const vm = app.mount('#app')