servicesComponent = {
    data() {
        return {
            services: null
        }
    },
    methods: {
        async fetchServices() {
            try {
                const response = await axios.get(`http://7trans.by/api/v1/services`, {
                    headers: {'Accept-Language': this.language}
                });
                this.services = response.data.results;
            } catch (e) {
            }
        },
        getServiceUrl(serviceId) {
            return `http://7trans.by/services/${serviceId}/`
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
                    <img src="service.img.url" alt="">
                </div>
                <div class="usluga__textbox">
                    <h4 class="usluga__title">{{ service.title }}</h4>
                    <div class="usluga__description">
                        {{ service.content }}
                    </div>
                </div>
            </a>
         </div>
    `
}