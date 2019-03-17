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


        <h1 class="title-text col-md-12" v-if="movieNotFound" style="color: darkred"> Sorry, couldn't find that film. </h1>

        <!-- Movie Result -->


        <div v-for="movie in movieResult" class="results col-lg-12 col-md-12 col-xs-12">
            <md-card class="md-primary" flex md-with-hover md-elevation="15" style="margin-bottom:20px;">
                <md-card-header>
                    <div class="md-title">{{movie.title}}</div>
                    <div class="md-subhead" style="font-weight:bold;">
                        Runtime: {{ movie.duration }} minutes <br>
                    </div>
                </md-card-header>
                <md-card-media md-medium>
                    <img v-bind:src=movie.image>
                </md-card-media>
                <md-card-content>
                    {{movie.overview}}
                </md-card-content>
            </md-card>
        </div>

        <h2 class="snarky-text col-md-12" v-if="results.length > 0"> {{messageString}} </h2>
        <!-- Video Results -->
        <div>
            <md-card v-for="video in results" class="md-primary col-md-3 videos" flex md-with-hover md-elevation="15">
                <md-card-header>
                    <div class="md-title">{{video.title}}</div>
                    <div class="md-subhead" style="font-weight:bold;">
                        Runtime: {{ Math.round(video.video_duration_minutes) }} minutes <br>
                    </div>
                </md-card-header>
                <md-card-media md-medium>
                    <img v-bind:src=video.thumbnail>
                </md-card-media>
                <!--<md-card-content>-->
                    <!--{{video.overview}}-->
                <!--</md-card-content>-->
                <md-card-actions>
                    <md-button v-bind:href=video.youtube_url target="_blank">View Video</md-button>
                </md-card-actions>
            </md-card>
        </div>
    </div>



</template>

<script>

    // import PacmanLoader from '@saeris/vue-spinners'

    //import BarLoader from '@saeris/vue-spinners'

    import axios from 'axios';

    export default {
        name: 'search',
        data: () => ({
            movieResult: [],
            results: [],
            filmString: '',
            movieNotFound: false,
            messageString: ''
        }),

        methods: {
            startSearch: function() {

                this.results = [];
                this.movieResult = [];
                this.movieNotFound = false;

                this.fetchResults(this.filmString);

                this.filmString = '';

            },

            fetchResults: function (movieTitle) {
                axios.get(`https://7cd2c27b.ngrok.io/getVideoSuggestions/${movieTitle}`)
                    .then(response => {

                        let video_suggestions = response["data"]["video_suggestions"];

                        for (let categoryIndex = 0; categoryIndex < video_suggestions.length; categoryIndex++) {
                            for (let videoIndex  = 0;
                                 videoIndex < video_suggestions[categoryIndex]["video_list"].length; videoIndex++) {

                                let videoObject = video_suggestions[categoryIndex]["video_list"][videoIndex];

                                videoObject["youtube_url"] =
                                    `https://www.youtube.com/watch?v=${videoObject["youtube_id"]}`;

                                this.results.push(video_suggestions[categoryIndex]["video_list"][videoIndex]);
                            }
                        }

                        this.movieResult = response["data"]["movie_result"];

                        if (this.movieResult.length === 0) {
                            this.movieNotFound = true;
                        }

                        this.messageString = this.selectGreeting(this.movieResult[0]["title"],
                            this.movieResult[0]["duration"], this.results);

                    })
            },

            selectGreeting: function (movie_title, duration, video_list) {
                let titleString  = `topics ranging from ${video_list[0].title} to ${video_list[Math.floor(Math.random()*video_list.length)].title}`;
                let greetings = [
                    `Are you sure your date is going to prefer ${movie_title} over ${titleString}?`,
                    `You really want to spend ${duration} minutes watching ${movie_title} when
                    you could have learnt about ${titleString}.`,
                    `There now, is ${movie_title} really the best choice for your career prospects?`,
                    `Remember this day, mate! You could have learnt about ${titleString} but you chose to
                    spend time on ${movie_title} of all possible things!`
                ];

                let randomGreetingIndex = Math.floor(Math.random()*greetings.length);

                return greetings[randomGreetingIndex];
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

    .snarky-text {
        font-size: 50px;
        line-height: 50px
    }

    md-progress-spinner {
        margin: 24px;
        z-index: 10000;
    }

</style>