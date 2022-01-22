languageTumblerComponent = {
    data() {
        return {
            language: this.getCookie('django_language'),
        }
    },
    methods: {
        changeLanguage(language) {
            this.language = language
            this.setCookie('django_language', language, 1);
            this.setCookie('language', language, 1);
            location.reload();
        },

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