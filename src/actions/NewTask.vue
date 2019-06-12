<template>
    <div>
        <v-btn small v-bind:data-reveal-id="cat" class="primary--text">+ New Task</v-btn>
        <v-card v-bind:id="cat" class="reveal-modal small" data-reveal>
            <v-card-title class="headline pb-0">
                <v-flex xs11>
                    New Task
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
                                <v-text-field class="pt-0" v-model="newTask.description" :rules="desc" :counter="30" placeholder="  Enter Description..." required></v-text-field>
                            </v-flex>
                        </v-layout>
                        <v-layout>
                            <v-flex xs6>
                                <!-- Application -->
                                <select v-model="newTask.appselect">
                                    <option disabled value="">Application</option>
                                    <option v-for="(item, i) in applist" :key="i">
                                        {{ item.title }}
                                    </option>
                                </select>
                            </v-flex>
                            <v-flex xs6>
                                <!-- Priority -->
                                <select v-model="newTask.priorityselect">
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
                                    v-model="newTask.dateselect" 
                                        :use12-hour="true" 
                                        type="datetime" 
                                        placeholder="Due Date"></datetime>
                            </v-flex>
                            <v-flex xs6>
                                <!-- Call to Action -->
                                <select v-model="newTask.actionselect">
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
                            <v-btn class="primary" @click="createNewTask">Accept</v-btn>
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
    name: 'NewTask',
    props: ["cat"],
    methods: {
        closeDialog() {
            // Clear form
            this.newTask = {
                description: '',
                appselect: '',
                priorityselect: '',
                dateselect: '',
                actionselect: ''
            }
            $('#' + this.cat).foundation('reveal', 'close');
        },
        createNewTask() {
            const createdTask = {
                description: this.newTask.description,
                category: this.newTask.priorityselect,
                application: this.newTask.appselect,
                due: new Date(this.newTask.dateselect).toLocaleString('en-US'),
                completed: false,
                action: this.newTask.actionselect,
                id: uuid.v4()
            }
            console.log(createdTask)
            this.$emit('new-task', createdTask);
            this.closeDialog();
        }
    },
    data() {
        return {
            valid: false,
            newTask: {
                description: '',
                appselect: '',
                priorityselect: '',
                dateselect: '',
                actionselect: ''
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


