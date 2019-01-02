<template>
  <VLayout>
    <VCard>
      <VCardTitle class="title">
        <VToolbarSideIcon></VToolbarSideIcon>
          COs you are a member of
      </VCardTitle>
      <CORenderAsCards :COs="COs"></CORenderAsCards>
    </VCard>

    <VCard>
      <VCardTitle class="title">Messages</VCardTitle>
    </VCard>
  </VLayout>
</template>

<script>
import CORenderAsCards from '../components/CORenderAsCards.vue';

export default {
  components: {
    CORenderAsCards
  },
  data: () => ({
    COs: [
      {
        id: 'g-1',
        name: 'UvA Research',
        description: 'UvA Research CO.',
        start: '2018-06-01',
        end: '2019-12-31',
        logo:
          'https://www.reliwerk.nl/wp-content/uploads/2018/07/UVA-logo-880x660-768x576.png'
      },
      {
        id: '17a6c1',
        name: 'Research Cloud',
        description:
          'Enabling cloud providers for researchers. Supports federated authentication.',
        start: '2018-01-01',
        end: '–',
        logo:
          'http://wp.curve.in.th/wp-content/uploads/2015/04/digitalocean-square-logo.png'
      },
      {
        id: '1a',
        name: 'BBMRI',
        description: 'Life science research project.',
        start: '2017-01-01',
        end: '2018-12-31',
        logo: 'https://www.bbmri.nl/sites/bbmri/themes/bbmri/logo.png'
      },
      {
        id: 'f92ea612733',
        name: 'Yoda',
        description:
          'Your data, otherwise known as YODA, is an awesome frontend to iRODS. It provides a portal to iRODS over the command line.',
        start: '2017-05-01',
        end: '2029-09-30',
        logo:
          'https://vignette.wikia.nocookie.net/starwars/images/0/07/Yoda_cartoon.jpg/revision/latest?cb=20050421025718'
      }
    ]
  })
};
</script>

<style scoped lang="stylus">
</style>
