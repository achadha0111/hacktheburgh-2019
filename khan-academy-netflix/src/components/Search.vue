<template>
    <div>

        <div class = "md-layout">
            <div class="md-layout-item"></div>
            <div class="md-layout-item">
                <md-field>
                    <md-input id= "search" placeholder= "Search for your film" v-model="filmString"></md-input>
                </md-field>
            </div>
            <div class="md-layout-item"></div>
        </div>

        <div class="button">
            <div class="md-layout" :class="`md-alignment-${vertical}-${horizontal}`">

                <div class="md-layout-item" style="margin-bottom:20px;">
                    <md-button class="md-raised search-btn">Learn and Chill</md-button>
                </div>

            </div>
        </div>

    </div>


</template>

<script>



    export default {
        name: 'search',
        data: () => ({
            results: {},
            filmString: ''
        })
    }

</script>

<style scoped>
    #search {
        text-align: center;
        color: black;
        font-size: 20px;
        border: 1px solid black;
        background-color: none;
        border-radius: 3px;
        height:50px;
    }

</style>