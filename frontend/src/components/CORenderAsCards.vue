<template>
  <VContainer grid-list-xl fluid>
    <VLayout row wrap>
      <VFlex v-for="(CO, index) in COs" :key="index" xs3>
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
