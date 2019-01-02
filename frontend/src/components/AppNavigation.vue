<template>
  <VToolbar height=80 dark color="primary">
    <VMenu :nudge-bottom="54">

      <VToolbarTitle slot="activator">
        <div class="font-weight-bold">
          <span>{{ currentCO }}</span>
        </div>
        <div class="subheading font-weight-light">
          <span>
            Gerben Venekamp ―
          </span>
          <span class="role">
            {{ role }}<VIcon dark size="20">expand_more</VIcon>
          </span>
        </div>
      </VToolbarTitle>

<!--
      <VToolbar dark dense flat color="secondary">
        <VToolbarTitle>Choose role</VToolbarTitle>
      </VToolbar>
-->
      <div class="role-menu-title">
        Choose role
      </div>

      <VList>
        <VListTile v-for="role in roles" :key="role" @click="gerben(role)">
          <VListTileTitle v-text="role"></VListTileTitle>
        </VListTile>
      </VList>

    </VMenu>

    <VSpacer></VSpacer>

    <VToolbarItems>
      <VTabs slot="extensions" right icons-and-text aling-with-title color="primary">
        <VTab key="messages" to="/messages" replace ripple>
          Messages
          <VBadge right color="red">
            <span slot="badge">2</span>
            <VIcon>mail</VIcon>
          </VBadge>
        </VTab>
        <VTab key="home" to="/" replace ripple>
           Home
          <VIcon>home</VIcon>
        </VTab>
        <VTab key="profile" to="/profile" replace ripple>
          Profile
          <VIcon>person</VIcon>
        </VTab>
        <VTab key="settings" to="/settings" replace ripple>
          Settings
          <VIcon>settings</VIcon>
        </VTab>
      </VTabs>
    </VToolbarItems>
  </VToolbar>
</template>

<script>
export default {
  name: 'AppNavigation',
  data: () => ({
    roles: ['Platform admin', 'CO admin', 'User'],
    role: 'User'
  }),
  computed: {
    user: {
      get() {
        return 'Gerben Venekamp';
      }
    },
    currentCO: {
      get() {
        return 'Research Cloud';
      }
    }
  },
  methods: {
    gerben: function(message) {
      this.role = message;
    }
  }
};
</script>

<style scoped lang="stylus">
.role-menu-title
  color: white
  background-color: #47afcd
  font-size: 14pt
  font-weight: 500
  padding: 2px
  padding-left: 10px
</style>
