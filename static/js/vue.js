const config = {
    delimiters: ["[[", "]]"],
}

const app = Vue.createApp(config)

app.component('lagnuage-tumbler', {
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
})
app.component('news', {
    data() {
        return {
            news: [],
            totalPages: null,
            pageLimit: 6,
            page: 1,
            numberOfPages: []
        }
    },
    computed: {
        getCountOfPages: function () {
            if (this.page === 1) {
                this.numberOfPages = [this.page, this.page + 1, this.page + 2, this.page + 3, this.page + 4];
            } else if (this.page === 2) {
                this.numberOfPages = [this.page - 1, this.page, this.page + 1, this.page + 2, this.page + 3];
            } else if (this.page === this.totalPages) {
                this.numberOfPages = [this.page - 4, this.page - 3, this.page - 2, this.page - 1, this.page];
            } else if (this.page === this.totalPages - 1) {
                this.numberOfPages = [this.page - 3, this.page - 2, this.page - 1, this.page, this.page + 1];
            } else {
                this.numberOfPages = [this.page - 2, this.page - 1, this.page, this.page + 1, this.page + 2];
            }
        }
    },
    methods: {
        async fetchNews() {
            try {
                const response = await axios.get('http://7trans.by/api/v1/news', {
                    params: {page: this.page},
                    headers: {'Accept-Language': this.language}
                });
                this.news = response.data.results;
                this.totalPages = Math.ceil(response.data.count / this.pageLimit);
            } catch (e) {
            }
        },
        changePage(pageNumber) {
            if (pageNumber === 'next' && this.page < this.totalPages) {
                this.page += 1;
            }
            if (pageNumber === 'previous' && this.page > 1) {
                this.page -= 1;
            }
            if (typeof pageNumber === 'number') {
                this.page = pageNumber;
            }
            this.fetchNews();
        },
    },

    mounted() {
        this.fetchNews()
    },
    template: `
    <div class="list_news__box">
        <div 
        v-for="article, idx in news" 
        :key="article.id"
        class="list_news__item"
    >
        <div class="list_news__img">
            <img :src="article.img_url" alt="">
        </div>

        <div class="list_news__description">
            <div class="one_news__date one_news__item">{{ article.publish_date }}</div>
            <div class="one_news__title one_news__item">{{ article.title }}</div>
            <div class="one_news__text one_news__item">{{ article.preview_body }}</div>
        </div>
    </div>
    </div> <!--__box-->
    <div class="list_news__pagination pagination _flex">
        <div class="pagination__link page_back" @click="changePage('previous')">Назад</div>
        <ul class="pagination__numbers">
            <li 
                v-for="pageNumber in numberOfPages"
                :key="page"
                :class="{'_active': page === pageNumber}"
                @click="changePage(pageNumber)"
                class="pagination__item"
                >{{ pageNumber }}</li>
        </ul>
        <div class="pagination__link page_next" @click="changePage('next')">Вперед</div>
    </div>
    `
})

const vm = app.mount('#app')