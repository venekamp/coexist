<template>
  <VApp>
    <AppNavigation v-if="auth"></AppNavigation>

    <div :class="embeddedContent()">
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
  },
  computed: {
    auth() {
      return this.$store.state.hasAuthenticatedUser;
    }
  },
  methods: {
    embeddedContent() {
      if (this.$store.state.hasAuthenticatedUser) {
        return 'content';
      }

      return '';
    }
  }
};
</script>

<style scoped lang="stylus">
.content
  padding: 3vw
</style>
