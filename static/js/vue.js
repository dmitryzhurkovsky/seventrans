const config = {
    delimiters: ["[[", "]]"],
}

const app = Vue.createApp(config)

app.component('news', {
    data() {
        return {
            news: [],
            totalPages: null,
            pageLimit: 6,
            page: 1,
        }
    },
    methods: {
        async fetchNews() {
            try {
                const response = await axios.get('http://7trans.by/api/v1/news', {params: {page: this.page}});
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
            <img src="article.img_url" alt="">
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
                v-for="pageNumber in totalPages"
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