<template>
    <router-view></router-view>
</template>

<script>
import Index from '@/components/Index'

export default {
  name: 'App',
  components: {
    Index
  }
}
</script>

<style>
  *{
    padding: 0;
    margin: 0;
  }
</style>
