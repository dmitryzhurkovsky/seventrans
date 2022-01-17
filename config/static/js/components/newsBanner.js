newsBannerComponent = {
    data() {
        return {
            news: null,
            language: this.getCookie('django_language'),
        }
    },
    methods: {
        async fetchThreeNews() {
            try {
                const response = await axios.get(`http://7trans.by/api/v1/news`, {
                    params: {page_size: 3},
                    headers: {'Accept-Language': this.language}
                });
                this.news = response.data.results;
            } catch (e) {
            }
        },
        getArticleUrl(articleId) {
            return `http://7trans.by/news/${articleId}/`
        }
    },
    mounted() {
        this.fetchThreeNews();
    },
    template: `
    <div class="news__body">
        <div 
        v-for="(article, idx) in news"
        :key="article.id"
        class="news__block"
        >
            <a :href="getArticleUrl(article.id)" class="one_news__block">
                <div class="one_news__img">
                    <img :src="article.img_url" alt="Новости">
                </div>
                <div class="one_news__description  mt-20">
                    <div class="one_news__date one_news__item">{{ article.publish_date }}</div>
                    <div class="one_news__title one_news__item">{{ article.title }}</div>
                    <div class="one_news__text one_news__item">{{ article.preview_body }}</div>
                </div>
            </a>
        </div>

        <a href="http://7trans.by/news" class="one_news__btn">
            <button
             v-if="this.language='ru'"
             class="btn btn-arrow"
             >Смотреть все новости
                <img src="img/arr_wh.svg" width="26" alt="">
            </button>
            <button
             v-if="this.language='en'"
             class="btn btn-arrow"
             >See all news
                <img src="img/arr_wh.svg" width="26" alt="">
            </button> 
        </a>
    </div> <!-- ..body-->
    `
}