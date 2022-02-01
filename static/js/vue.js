const config = {
    data() {
        return {
            language: this.getCookie('django_language') ? this.getCookie('django_language') : this.changeLanguage('ru')
        }
    },
    delimiters: ["[[", "]]"],
    methods: {
        redirectToPage(endPoint) {
            if (endPoint === 'news') {
                window.location.href = `https://7trans.by/news`;
            } else if (endPoint === 'about') {
                window.location.href = `https://7trans.by/about`;
            }
        },
        getCookie(cookieName) {
            let name = cookieName + "=";
            let decodedCookie = decodeURIComponent(document.cookie);
            let ca = decodedCookie.split(';');
            for (let i = 0; i < ca.length; i++) {
                let c = ca[i];
                while (c.charAt(0) == ' ') {
                    c = c.substring(1);
                }
                if (c.indexOf(name) == 0) {
                    return c.substring(name.length, c.length);
                }
            }
            return "";
        },
        setCookie(cookieName, cookieValue, exDays) {
            const d = new Date();
            d.setTime(d.getTime() + (exDays * 24 * 60 * 60 * 1000));
            let expires = "expires=" + d.toUTCString();
            document.cookie = cookieName + "=" + cookieValue + ";" + expires + ";path=/";
        },
        changeLanguage(language) {
            this.language = language
            this.setCookie('django_language', language, 1);
            this.setCookie('language', language, 1);
            location.reload();
        }
    }
}

const app = Vue.createApp(config)

app.component('language-tumbler', languageTumblerComponent)
app.component('news', newsComponent)
app.component('services', servicesComponent)


const vm = app.mount('#app')