<template>
  <VContainer grid-list-md text-cs-center fluid>
    <VLayout row>
      <VFlex v-for="(CO, index) in COs" :key="index">
        <COCard :CO="CO"></COCard>
      </VFlex>
    </VLayout>
  </VContainer>
</template>

<script>
import COCard from '../components/COCard';

export default {
  props: ['COs'],
  components: {
    COCard
  }
};
</script>

<style scope lang="stylus">
</style>
