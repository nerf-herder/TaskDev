<template>
  <div class="main-element">
    <!--div>This is VueJS text.</div>
    <div>API TEXT: {{ api_data }}</div-->
    <Navigation />
  </div>
</template>

<script>
import Navigation from './components/Navigation';

export default {
  name: 'CatchAll',
  components: {
    Navigation,
  },
  data() {
    return {
      api_data: '',
    };
  },
  created() {
    this.$http.get('/api/task/').then((resp) => {
      this.api_data = resp.data;
      console.log(this.api_data[0].list);
    }).catch((err) => {
      this.api_data = 'API FAILED';
      console.log(err);
    });
  },
};
</script>

<style scoped>

</style>
