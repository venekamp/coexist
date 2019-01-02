<template>
  <VContainer grid-list-md text-cs-center fluid>
    <VLayout row>
      <VFlex xs6 v-for="(CO, index) in COs" :key="index">
        <VCard>
          <VResponsive :aspect-ratio="5/3">
            <VImg :src="CO.logo"></VImg>

            <VCardTitle primary-title class="subheading font-weight-medium">
              {{ CO.name }}
            </VCardTitle>

            <VCardText>
              <div class="description">
                {{ CO.description }}
              </div>
              <div>
                <span class="font-weight-medium datelabel">start date:</span>
                <span class="font-italic">{{ CO.start }}</span>
              </div>
              <div>
                <span class="font-weight-medium datelabel">end date:</span>
                <span class="font-italic">{{ CO.end }}</span>
              </div>
            </VCardText>
          </VResponsive>
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
.description
  color: #484850

.datelabel
  color: #444
</style>
