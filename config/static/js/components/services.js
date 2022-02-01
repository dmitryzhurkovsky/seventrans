servicesComponent = {
    data() {
        return {
            services: null
        }
    },
    props: ['language'],
    methods: {
        async fetchServices() {
            try {
                const response = await axios.get(`http://localhost:8000/api/v1/services/`, {
                    // headers: {'Accept-Language': this.language}
                });
                this.services = response.data.results;
            } catch (e) {
            }
        },
        getServiceUrl(serviceId) {
            return `https://7trans.by/services/${serviceId}/`
        }
    },
    mounted() {
        this.fetchServices();
    },
    template: `
         <div class="uslugi__box">
            <a
                v-for="(service, idx) in services"
                :key="service.id"
                :href="getServiceUrl(service.id)"
                class="uslugi__item usluga"
            >
                <div class="usluga__img">
                    <img :src="service.img" alt="">
                </div>
                <div class="usluga__textbox">
                    <h4 v-html="service.title" class="usluga__title"></h4>
                    <div v-if="language === ru" class="usluga__description">{{ service.preview_ru }}</div>
                    <div v-else class="usluga__description">{{ service.preview_en }}</div>
                </div>
            </a>
         </div>
    `
}