<template>
  <div>
    <v-toolbar flat dark color="primary justify-center">
      <v-toolbar-title>
        coexist help
      </v-toolbar-title>
    </v-toolbar>

    <v-layout>
      <v-flex xs12 sm8 offset-sm2>
        <v-card class="mt-5" max-width="75ex">
          <v-card-title primary-title>
            <div>
              <h3 class="heqadline mb-0">
                What is coexist?
              </h3>
              <div>
                coexist is a group and identidy management system based
                on federated identities.
              </div>
            </div>
          </v-card-title>

          <v-divider></v-divider>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn flat color="orange" @click="back()">Back</v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
export default {
  methods: {
    back() {
      window.history.back();
    }
  }
};
</script>

<style scoped lang="stylus">
</style>
