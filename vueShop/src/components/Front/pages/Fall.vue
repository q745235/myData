<template>
  <div>
    <loading :active.sync="isLoading"></loading>
    <iframe
      width="743"
      height="418"
      src="https://www.youtube.com/embed/oykrSEJcCW0"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
  </div>
</template>
<script>
export default {
  data() {
    return {
      status: {
        loadingItem: "",
      },
      isLoading: false,
    };
  },
};
</script>

<style lang="scss">
  iframe{
    margin-top: 50px;

  }
</style>