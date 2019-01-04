<template>
  <VHover>
    <VCard
      slot-scope="{ hover }"
      :class="`elevation-${hover ? 12 : 2}`"
      @click="CardSelected(CO.id)"
      class="card"
    >
      <div class="card-image">
        <VImg :src="CO.logo" contain height="100px">

        </VImg>
      </div>

      <VCardTitle primary-title class="subheading font-weight-medium">
        {{ CO.name }}
      </VCardTitle>

      <hr class="card-element-separator" />

      <VCardText>
        <VContainer fluid pa-0>
          <VLayout row>
            <VFlex xs12 class="card-description">
              {{ CO.description }}
            </VFlex>
          </VLayout>

          <VLayout row>
            <VFlex xs6 class="font-weight-medium card-date-label">
              <div>start date:</div>
              <div>end date:</div>
            </VFlex>
            <VFlex xs6 class="font-italic">
              <div>{{ CO.start }}</div>
              <div>{{ CO.end }}</div>
            </VFlex>
          </VLayout>

        </VContainer>
      </VCardText>
    </VCard>
  </VHover>
</template>

<script>
export default {
  props: ['CO'],
  methods: {
    CardSelected(id) {
      console.log(id + ': card clicked.');
    }
  }
};
</script>

<style scoped lang="stylus">
.card
  width: 24ex
.card:hover
  cursor: pointer

.card-image
  padding: 1em 1em 0

.card-description
  color: #484850
  font-size: 13px
  height: 7.5em
  overflow: auto
  margin-bottom: 1ex

.card-date-label
  color: #444

.card-element-separator
  margin 0 1em
  border: 1px solid #b8b8b8
</style>
