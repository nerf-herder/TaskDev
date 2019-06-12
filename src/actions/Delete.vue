<template>
    <div>
        <v-list-tile v-bind:data-reveal-id="json.action + json.id">
            Delete
        </v-list-tile>
        <v-card v-bind:id="json.action + json.id" class="reveal-modal tiny" data-reveal>
            <v-card-title>
                <p>Are you sure you want to delete this?</p>
            </v-card-title>
            <v-card-actions>
                <v-layout>
                    <v-btn small class="primary" @click="deleteTask">
                        Accept
                    </v-btn>
                    <v-btn small class="error" v-model="json" @click="closeDialog">
                        Cancel
                    </v-btn>
                </v-layout>
            </v-card-actions>
        </v-card>
    </div>
</template>

<script>
export default {
    name: 'Delete',
    props: ["json"],
    methods: {
        closeDialog() {
            $('#' + this.json.action + this.json.id).foundation('reveal', 'close');
        },
        deleteTask() {
            this.$emit('delete-task', this.json);
            $('#' + this.json.action + this.json.id).foundation('reveal', 'close');
        }
    }
}
</script>
