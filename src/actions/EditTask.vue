<template>
    <div>
        <v-list-tile v-bind:data-reveal-id="'edit' + json.id">Edit</v-list-tile>
        <v-card v-bind:id="'edit' + json.id" class="reveal-modal small" data-reveal>
            <v-card-title class="headline pb-0">
                <v-flex xs11>
                    Edit Task
                </v-flex>
                <v-flex xs1>
                    <v-btn icon @click="closeDialog">
                        <v-icon class="grey--text">clear</v-icon>
                    </v-btn>
                </v-flex>
            </v-card-title>
            <v-spacer dark></v-spacer>
            <v-card-text>
                <v-form v-model="valid">
                    <v-container class="pt-0">
                        <v-layout>
                            <v-flex xs12>
                                <!-- Description -->
                                <v-text-field class="pt-0" v-model="editTask.description" :rules="desc" :counter="30" required></v-text-field>
                            </v-flex>
                        </v-layout>
                        <v-layout>
                            <v-flex xs6>
                                <!-- Application -->
                                <select v-model="editTask.appselect">
                                    <option disabled value="">Application</option>
                                    <option v-for="(item, i) in applist" :key="i">
                                        {{ item.title }}
                                    </option>
                                </select>
                            </v-flex>
                            <v-flex xs6>
                                <!-- Priority -->
                                <select v-model="editTask.priorityselect">
                                    <option disabled value="">Priority</option>
                                    <option v-for="(item, i) in prioritylist" :key="i">
                                        {{ item.title }}
                                    </option>
                                </select>
                            </v-flex>
                        </v-layout>
                        <v-layout>
                            <v-flex xs6>
                                <!-- Dat and Time -->
                                <datetime 
                                    v-model="editTask.dateselect" 
                                        :use12-hour="true" 
                                        type="datetime" 
                                        placeholder="Due Date"></datetime>
                            </v-flex>
                            <v-flex xs6>
                                <!-- Call to Action -->
                                <select v-model="editTask.actionselect">
                                    <option disabled value="">Call to Action</option>
                                    <option v-for="(item, i) in actionlist" :key="i">
                                        {{ item.title }}
                                    </option>
                                </select>
                            </v-flex>
                        </v-layout>
                    </v-container>
                </v-form>
            </v-card-text>
            <v-card-actions>
                <v-container>
                    <v-layout>
                        <v-flex xs12>
                            <v-btn class="primary" @click="editThisTask">Accept</v-btn>
                        </v-flex>
                    </v-layout>
                </v-container>
            </v-card-actions>
        </v-card>
    </div>
</template>

<script>
import uuid from 'uuid';

export default {
    name: 'EditTask',
    props: {
        json: Object,
        edTask: Object
    },
    methods: {
        closeDialog() {
            // Reset form
            
            this.editTask = {
                description: this.json.description,
                appselect: this.json.application,
                priorityselect: this.json.category,
                dateselect: new Date(this.json.due).toISOString(),
                actionselect: this.json.action,
                completed: this.json.completed,
                id: this.json.id
                
            }
            $('#edit' + this.json.id).foundation('reveal', 'close');
        },
        editThisTask() {
            const edittedTask = {
                description: this.editTask.description,
                category: this.editTask.priorityselect,
                application: this.editTask.appselect,
                due: new Date(this.editTask.dateselect).toLocaleString('en-US'),
                completed: this.editTask.completed,
                action: this.editTask.actionselect,
                id: this.editTask.id
            }
            console.log(edittedTask)
            this.$emit('edit-task', edittedTask);
            $('#edit' + this.json.id).foundation('reveal', 'close');
        }
    },
    data() {
        return {
            valid: false,
            editTask: {
                description: this.json.description,
                appselect: this.json.application,
                priorityselect: this.json.category,
                dateselect: new Date(this.json.due).toISOString(),
                actionselect: this.json.action,
                completed: this.json.completed,
                id: this.json.id
            },
            desc: [
                v => !!v || 'Description is required',
                v => v.length <= 30 || 'Description must be less than 30 characters'
            ],
            applist: [
                { title: 'Fran Hire' },
                { title: 'Fran Jobs' },
                { title: 'Fran Train' },
                { title: 'Sales Analytics' }
            ],
            prioritylist: [
                { title: 'Urgent and Important' },
                { title: 'Urgent' },
                { title: 'Important' },
                { title: 'Other' }
            ],
            actionlist: [
                { title: 'Email' },
                { title: 'Call' },
                { title: 'Text' },
                { title: 'Meeting' }
            ]
        }
    }
}
</script>

<style scoped>
    .reveal-modal {
        padding: 0px;
    }

    .f-dropdown {
        width: auto !important;
        border: none !important;
    }

    select {
        font-size: 18px;
    }
</style>


