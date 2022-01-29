languageTumblerComponent = {
    methods: {
      changeLanguage(language) {
          this.$emit('changeLanguage', language)
      }
    },
    props: ['language'],
    template:
        `
    <div class="header__language language _flex">
        <div class="language__box">
            <div
                @click="changeLanguage('ru')"
                    :class="{'_active': language === 'ru'}"
                    class="language__item _flex"
            >RU</div>
            <div
                    @click="changeLanguage('en')"
                    :class="{'_active': language === 'en'}"
                    class="language__item _flex"
            >EN</div>
        </div>
        
    </div>
    `
}