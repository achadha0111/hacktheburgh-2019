<template>
    <div>

        <!-- Search Field -->
        <div class = "md-layout">
            <div class="md-layout-item"></div>
            <div class="md-layout-item">
                <md-field>
                    <md-input id= "search" placeholder= "Search for your film"
                              v-model="filmString"
                              @keyup.enter.native="startSearch"></md-input>
                </md-field>
            </div>
            <div class="md-layout-item"></div>
        </div>

        <!-- Search Button -->
        <div class="button">
            <div class="md-layout" :class="`md-alignment`">

                <div class="md-layout-item" style="margin-bottom:20px;">
                    <md-button class="md-raised search-btn"
                               v-on:click="startSearch">Learn and Chill</md-button>
                </div>

            </div>
        </div>

        <!-- Preloader -->
        <!--<div class="preloader">-->
            <!--<div class="md-layout md-gutter" :class="`md-alignment-${vertical}-${horizontal}`">-->
                <!--<div class="md-layout-item">-->
                    <!--<bar-loader class="custom-class" :loading="loading" :size="150" :sizeUnit="px"></bar-loader>-->
                <!--</div>-->
            <!--</div>-->
        <!--</div>-->

        <!-- Movie Result -->

        <div v-for="movie in movieResult" class="results col-lg-10 col-md-offset-2 col-md-8">
            <md-card class="md-primary" flex md-with-hover md-elevation="15" style="margin-bottom:20px;">
                <md-card-header>
                    <div class="md-title">{{movie.title}}</div>
                    <div class="md-subhead" style="font-weight:bold;">
                        Runtime: {{ movie.runtime }} <br>
                    </div>
                </md-card-header>
                <md-card-content>
                    {{movie.overview}}
                </md-card-content>
            </md-card>
        </div>

        <!-- Video Results -->
        <div>
            <md-card v-for="video in results" class="md-primary col-md-3 videos" flex md-with-hover md-elevation="15">
                <md-card-header>
                    <div class="md-title">{{video.title}}</div>
                    <div class="md-subhead" style="font-weight:bold;">
                        Runtime: {{ video.runtime }} <br>
                    </div>
                </md-card-header>
                <md-card-content>
                    {{video.overview}}
                </md-card-content>
            </md-card>
        </div>
    </div>



</template>

<script>

    // import PacmanLoader from '@saeris/vue-spinners'


    export default {
        name: 'search',
        data: () => ({
            movieResult: [],
            results: [],
            filmString: '',
            loading: false
        }),

        methods: {
            startSearch: function() {
                this.loading=true;
                console.log("Button pressed");
                setTimeout(this.fetchDummyResults, 2000);
                this.movieResult = [{
                  "title": "Green Book",
                  "overview": "A world renowed composer of colour decides to embark on a concert tour to the Southern" +
                  "American states during the heights of racial segregation.",
                  "runtime": 145
                }];
                this.filmString = '';
            },

            fetchDummyResults: function() {
                this.results = [
                    {
                        "title": "Differential Equations",
                        "overview": "This video covers basics about differential equations.",
                        "runtime": 200
                    },
                    {
                        "title": "Macroeconomics",
                        "overview": "Basics of Macroeconomics",
                        "runtime": 200
                    },
                    {
                        "title": "Macroeconomics",
                        "overview": "Basics of Macroeconomics",
                        "runtime": 200
                    },
                    {
                        "title": "Macroeconomics",
                        "overview": "Basics of Macroeconomics",
                        "runtime": 200
                    },
                    {
                        "title": "Macroeconomics",
                        "overview": "Basics of Macroeconomics",
                        "runtime": 200
                    },
                    {
                        "title": "Macroeconomics",
                        "overview": "Basics of Macroeconomics",
                        "runtime": 200
                    },
                    {
                        "title": "Macroeconomics",
                        "overview": "Basics of Macroeconomics, covers topics like Inflation, Philips Curve " +
                        "and Income Inequality.",
                        "runtime": 200
                    }
                ]
            }
        }
    }

</script>

<style scoped>

    .search-btn {
        background: #092962;
        color: white;
    }
    #search {
        text-align: center;
        color: black;
        font-size: 20px;
        border: 1px solid black;
        background-color: none;
        border-radius: 3px;
        height:50px;
    }



    .videos {
        width: 320px;
        margin: 4px;
        display: inline-block;
        vertical-align: top;
    }

</style>