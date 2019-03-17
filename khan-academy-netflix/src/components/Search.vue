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

    export default {
        name: 'search',
        data: () => ({
            movieResult: [],
            results: [],
            filmString: '',
            loading: true
        }),

        methods: {
            startSearch: function() {
                this.loading=true;
                console.log("Button pressed");
                setTimeout(this.fetchDummyResults, 3000);
                this.loading = false;
                this.filmString = '';
            },

            fetchDummyResults: function() {
                this.movieResult = [{
                    "title": "Green Book",
                    "overview": "A world renowed composer of colour decides to embark on a concert tour to the Southern" +
                    "American states during the heights of racial segregation.",
                    "runtime": 145
                }];

                let results = [
                    {
                        "category_title": "Revision of shapes, estimation, simple operations, large numbers",
                        "video_list": [
                            {
                                "youtube_id": "dZPOCU10TqY",
                                "title": "Comparing place values",
                                "video_duration_seconds": 150,
                                "video_duration_minutes": 2.5,
                                "thumbnail": "https://cdn.kastatic.org/googleusercontent/UeoUCyGT5cfqKeKbBy9qB0zjrjH8pGVclFAjM_YCziuite9sUNJc6bo7ojpP5wq_NUuT5Hl8Jd5PKPq_Hg-eS8o"
                            },
                            {
                                "youtube_id": "a_mzIWvHx_Y",
                                "title": "Regrouping numbers into various place values",
                                "video_duration_seconds": 154,
                                "video_duration_minutes": 2.566666666666667,
                                "thumbnail": "https://cdn.kastatic.org/googleusercontent/4x0qCxQCbAC6PJEOwCLn-poltUUlxzi1qaMFFc8T4l-gcOn1PEffQByfc5OrLHcmi9z8HUR5a7IgNChQNBusBQw_"
                            },
                            {
                                "youtube_id": "3Xcae0OGavk",
                                "title": "Comparing whole number place values",
                                "video_duration_seconds": 91,
                                "video_duration_minutes": 1.5166666666666666,
                                "thumbnail": "https://cdn.kastatic.org/googleusercontent/NIolzOHtyZCfKTl5ZgguceSoTRH33t7MUnq6hTWfWD5snH3h0OjSXGaRee4I4edkBQ5_-Orc5PhtARjBq5zBC02R"
                            },
                            {
                                "youtube_id": "PvSx8oJ7PrM",
                                "title": "Place value: comparing same digit in different places",
                                "video_duration_seconds": 160,
                                "video_duration_minutes": 2.6666666666666665,
                                "thumbnail": "https://cdn.kastatic.org/googleusercontent/wMAUn7saTwRYXJRgsRpO4DjxKoX2Vbto35eWiaULaSTvvXSjEWaY8OHZtNvKgcoKaF8ZSEVxtqU1bPHq69KcqLM"
                            }
                        ],
                        "category_duration_seconds": 555,
                        "category_duration_minutes": 9.25
                    },
                    {
                        "category_title": "Angles and unit of measurement for angles",
                        "video_list": [
                            {
                                "youtube_id": "D-EIh7NJvtQ",
                                "title": "Angle measurement & circle arcs",
                                "video_duration_seconds": 457,
                                "video_duration_minutes": 7.616666666666666,
                                "thumbnail": "https://cdn.kastatic.org/googleusercontent/0KlI5SnYF2Zl_e19lMG8GtaXMwQ7292ZKQJZMTxKeMT6lfUgeJmgNXix6SJCpTWemHGaMh8EcWQNlJ8DT5lPJlhubQ"
                            },
                            {
                                "youtube_id": "ALhv3Rlydig",
                                "title": "Acute, right, & obtuse angles",
                                "video_duration_seconds": 332,
                                "video_duration_minutes": 5.533333333333333,
                                "thumbnail": "https://cdn.kastatic.org/googleusercontent/0TrIIisE8BxVp_Bs5Co3G8RXtYcnmx9zu5pR2My5GUcj1JjSm5_G6kkQ4ZMUk0Ln1ry1Q5I7HXnYXTX1BGCdUOnJ"
                            },
                            {
                                "youtube_id": "92aLiyeQj0w",
                                "title": "Measuring angles in degrees",
                                "video_duration_seconds": 502,
                                "video_duration_minutes": 8.366666666666667,
                                "thumbnail": "https://cdn.kastatic.org/googleusercontent/AUN8zIwamVCnRbVrbNkTeBO9SpKe7AxHlEaNRb5uRVice-wM0qmnW-YuL_KiAeC99oc3B1LtSsEEtRXjOhR3PGg5"
                            },
                            {
                                "youtube_id": "B0R3MJOrST0",
                                "title": "Recognizing angles",
                                "video_duration_seconds": 135,
                                "video_duration_minutes": 2.25,
                                "thumbnail": "https://cdn.kastatic.org/googleusercontent/TSOfNlrgBlkSftUPPOoLCmGhIzgd2iNRa8PM7SrelbRsiDTlUhwf-_BJ7ZspSr6-MZhuguc9oZ4TU92ut_4syhM"
                            },
                            {
                                "youtube_id": "2mzuFKCuDg4",
                                "title": "Identifying an angle",
                                "video_duration_seconds": 123,
                                "video_duration_minutes": 2.05,
                                "thumbnail": "https://cdn.kastatic.org/googleusercontent/Pyujn_3Ou49usXWDTBtTWdNBN2dBFOqwP5W7wodNMOEEFI9Rv5la3ecQVq6C28kHk7wC3dE1uD48b22aERBogfE"
                            },
                            {
                                "youtube_id": "dw41PMWek6U",
                                "title": "Measuring angles using a protractor",
                                "video_duration_seconds": 205,
                                "video_duration_minutes": 3.4166666666666665,
                                "thumbnail": "https://cdn.kastatic.org/googleusercontent/fl9JqzAG4AES6K4YGfp4Aj6oDVKRNlLOERnZGNV26NZUICj8syJjkPPaVF371GWAEtBEhbQP1aiI3FbboRuvrd_Htw"
                            },
                            {
                                "youtube_id": "wJ37GJyViU8",
                                "title": "Measuring angles using a protractor 2",
                                "video_duration_seconds": 245,
                                "video_duration_minutes": 4.083333333333333,
                                "thumbnail": "https://cdn.kastatic.org/googleusercontent/El9nQtild7LvphLXXrc_VV8bcM_qv3fChQ23GfLVi38RV8WX7xbkNQPq9lw1aaIfC1dmftEVgaTRBGrhxRbSErKGiw"
                            }
                        ],
                        "category_duration_seconds": 1999,
                        "category_duration_minutes": 33.31666666666667
                    }
                ];

                for (let categoryIndex = 0; categoryIndex < results.length; categoryIndex++) {
                    for (let videoIndex  = 0; videoIndex < results[categoryIndex]["video_list"].length; videoIndex++) {
                        let videoObject = results[categoryIndex]["video_list"][videoIndex];
                        videoObject["youtube_url"] = `https://www.youtube.com/watch?v=${videoObject["youtube_id"]}`
                        this.results.push(results[categoryIndex]["video_list"][videoIndex]);
                    }
                }
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