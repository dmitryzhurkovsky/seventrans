languageTumblerComponent = {
    data() {
        return {
            language: this.getCookie('django_language'),
        }
    },
    methods: {
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
    },
    template:
        `
    <div class="header__language language _flex">
        <div class="language__box">
            <div
                    @click="changeLanguage('ru')"
                    :class="{'_active': this.language === 'ru'}"
                    class="language__item _flex"
            >RU</div>
            <div
                    @click="changeLanguage('en')"
                    :class="{'_active': this.language === 'en'}"
                    class="language__item _flex"
            >EN</div>
        </div>
        
    </div>
    `
}