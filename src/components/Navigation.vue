<template>
    <div>
        <v-toolbar app dark></v-toolbar>
        <v-navigation-drawer app clipped permanent dark width="175">
            <v-list>
                <v-list-tile v-for="link in links" :key="link.text" router :to="link.route">
                    <v-list-tile-content>
                        <v-list-tile-title class="white--text">
                            {{ link.text }}
                        </v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </v-list>
        </v-navigation-drawer>
    </div>
</template>

<script>
export default {
    data() {
        return {
            links: [
                { text: 'Fran Tasks', route: '/tasks' },
                { text: 'My Drive', route: '/mydrive' },
                { text: 'Shared with me', route: '/sharedwithme' },
                { text: 'Shared with others', route: '/sharedwithothers' },
            ]
        };
    },
};
</script>


<style scoped>

</style>
