newsComponent = {
    data() {
        return {
            news: [],
            totalPages: null,

            pageLimit: 6,
            page: 1,
            pages: []
        }
    },
    computed: {
    },
    methods: {
        async fetchNews() {
            try {
                const response = await axios.get(`https://7trans.by/api/v1/news`, {
                    params: {page: this.page},
                    headers: {'Accept-Language': this.language}
                });
                this.news = response.data.results;
                this.totalPages = Math.ceil(response.data.count / this.pageLimit);
            } catch (e) {
            }
        },
        getCountOfPages () {
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
            this.getCountOfPages();
            this.fetchNews();
        },
        getArticleUrl(articleId) {
            return `http://7trans.by/news/${articleId}/`
        }
    },
    mounted() {
        this.fetchNews();
        this.getCountOfPages();
    },
    template: `
    <div class="list_news__box">
        <a
        v-for="(article, idx) in news"
        :key="article.id"
        :href="getArticleUrl(article.id)"
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
        </a>
    </div> <!--__box-->
    <div class="list_news__pagination pagination _flex">
        <div class="pagination__link page_back" @click="changePage('previous')">??????????</div>
        <ul class="pagination__numbers">
            <li
                v-for="pageNumber in numberOfPages"
                :key="pageNumber"
                :class="{'_active': page === pageNumber}"
                @click="changePage(pageNumber)"
                class="pagination__item"
                >{{ pageNumber }}</li>
        </ul>
        <div class="pagination__link page_next" @click="changePage('next')">????????????</div>
    </div>
    `
}