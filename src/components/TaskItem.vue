<template>

    <!-- Use v-list for tasks, then a card -->
    
        <v-card hover>
            <v-card-title>
                    <!-- Completed -->
                    <v-flex xs1>
                        <input type="checkbox" v-model="json.completed">
                    </v-flex>
                    <!-- App -->
                    <v-flex xs2>
                        <v-chip v-if="this.taskItems.application === 'Fran Hire'">Hire</v-chip>
                        <v-chip v-else-if="this.taskItems.application == 'Fran Jobs'">Jobs</v-chip>
                        <v-chip v-else-if="this.taskItems.application == 'Fran Train'">Train</v-chip>
                        <v-chip v-else-if="this.taskItems.application === 'Sales Analytics'">Sales</v-chip>
                        <v-chip v-else>Error</v-chip>
                    </v-flex>
                    <!-- Description -->
                    <v-flex xs7 class="grey--text">
                        <h4 class="black--text">{{ this.taskItems.description }}</h4>
                        {{ this.taskItems.due }}
                    </v-flex>
                    <!-- Call to Action -->
                    <v-flex xs1>
                        <v-layout align-content-center>
                            <v-btn icon v-if="this.taskItems.action == 'Email'" class="info"><v-icon>email</v-icon></v-btn>
                            <v-btn icon v-else-if="this.taskItems.action == 'Call'" class="info"><v-icon>call</v-icon></v-btn>
                            <v-btn icon v-else-if="this.taskItems.action == 'Text'" class="info"><v-icon>textsms</v-icon></v-btn>
                            <v-btn icon v-else-if="this.taskItems.action == 'Meeting'" class="info"><v-icon>meeting_room</v-icon></v-btn>
                            <v-btn icon v-else class="info">Error</v-btn>
                        </v-layout>
                            
                    </v-flex>
                    <!-- Edit or Delete -->
                    <v-flex xs1>
                        <v-btn icon class="grey--text" v-bind:data-dropdown="'drop' + json.id">
                            <v-icon>more_vert</v-icon>
                        </v-btn>
                        <v-list v-bind:id="'drop' + json.id" class="f-dropdown" data-dropdown-content>
                            <v-list-tile>
                                <EditTask v-on:edit-task="edtTask" v-bind:json="this.taskItems"/>
                            </v-list-tile>
                            <v-list-tile>
                                <Delete v-on:delete-task="$emit('del-task', json)" v-bind:json="this.taskItems"/>
                            </v-list-tile>
                        </v-list>
                    </v-flex>
               
            </v-card-title>
        </v-card>
   

    
</template>

<script>
import EditTask from '../actions/EditTask';
import Delete from '../actions/Delete';
import draggable from 'vuedraggable';

export default {
    name: 'TaskItem',
    props: ["json"],
    methods: {
        edtTask(ed) {
            this.taskItems = ed;
            this.$emit('edt-task', ed);
        }
    },
    data() {
        return {
            menu: [
                { title: 'Edit' },
                { title: 'Delete' },
            ],
            taskItems: this.json
        }
    },
    components: {
        EditTask,
        Delete,
        draggable,
    }
}
</script>

<style scoped>

    .f-dropdown {
        width: auto !important;
        border: none;
    }

    button:hover {
        background-color: lightgrey;
    }

</style>

