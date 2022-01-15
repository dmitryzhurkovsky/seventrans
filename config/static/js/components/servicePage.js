servicePage = {
    data() {
        return {
            service: null
        }
    },
    methods: {
        async fetchService(id) {
            try {
                const response = await axios.get(`http://localhost:8000/api/v1/services/${id}`, {
                    headers: {'Accept-Language': this.language}
                });
                this.service = response.data.results;
            } catch (e) {
            }
        },
    },
    template: `
        <div class="service">
            <span class="service__name">{{ service.title }}</span>
            <span class="service__text">{{ service.content }}</span>
            <<img src="service.img" alt="">
        </div>
    `
}