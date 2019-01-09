<template>
  <div class="text-xs-center">
    <v-dialog v-model="dialog" persistent width="75ex">
      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
          In order to continue, you'll need to log in first
        </v-card-title>

        <v-card-text>
          <div class="subheading mb-3">
            If you would like to use coexist, you must provide an identity. A number
            of sources are trusted to provide this identity. You'll be guided through
            that process if you wish to continue and log in. Below are
            a number of things you'll be able to do once logged in. Click on each
            line if you want more information.
          </div>

          <v-expansion-panel focusable>
            <v-expansion-panel-content>
              <div slot="header">
                View and update your personal info
              </div>
              <v-card>
                <v-card-text>
                  coexist keeps info on you once you have logged in. You can
                  review this information and make updated to it.
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
            <v-expansion-panel-content>
              <div slot="header">
                View and manage collaboration membership
              </div>
              <v-card>
                <v-card-text>
                  Join or leave collaborations ans view the members. Weather
                  or not this applies to the collaborations depends on its
                  confiuration.
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
            <v-expansion-panel-content>
              <div slot="header">
                Change collaboration settings
              </div>
              <v-card>
                <v-card-text>
                  You can manage collaborations you are an administror of.
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            dark
            color="orange darken-2"
            to="/help"
          >
            Help
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            @click="Login()"
          >
            Log in
          </v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dialog: true,
      info: []
    };
  },
  methods: {
    Login() {
      const apiMethod = this.$store.state.apiBaseURL + '/ffff';
      console.log('api: ' + apiMethod);
      this.$axios
        .get('https://api.coindesk.com/v1/bpi/currentprice.json')
        .then(response => (this.info = response.data.bpi))
        .catch(error => console.log(error));
      this.dialog = false;
    }
  }
};
</script>

<style scoped lang="stylus">
</style>
