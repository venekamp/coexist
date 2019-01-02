<template>
  <VContainer grid-list-md text-cs-center fluid>
    <VLayout row>
      <VFlex xs6 v-for="(CO, index) in COs" :key="index">
        <VCard class="card">
          <VCardMedia class="card-media">
            <VImg :src="CO.logo" contain height="100px"></VImg>
          </VCardMedia>

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
      </VFlex>
    </VLayout>
  </VContainer>
</template>

<script>
export default {
  props: ['COs']
};
</script>

<style scope lang="stylus">
.card
  width: 24ex

.card-media
  padding: 0 1em

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
  border: 1px solid #bbb
</style>
