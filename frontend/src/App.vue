<template>
  <VApp>
    <AppNavigation></AppNavigation>

    <div class="content">
      <RouterView></RouterView>
    </div>

  </VApp>
</template>

<script>
import AppNavigation from './components/AppNavigation';

export default {
  name: 'App',
  components: {
    AppNavigation
  },
  data() {
    return {
      //
    };
  }
};
</script>

<style scoped lang="stylus">
.content
  padding: 3vw
</style>
