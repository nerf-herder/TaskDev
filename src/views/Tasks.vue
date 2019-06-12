<template>
    <div class="Tasks">
        <v-app>
            <Navigation />
            <v-content app class="pt-0">
                <v-container>
                    <v-flex justify-start xs1 class="mx-2">
                        <h1>Tasks</h1>
                    </v-flex>
                    <v-layout row wrap>
                        <v-flex xs12 md6 class="pa-3">
                            <!-- Urgent and Important -->
                            <v-card>
                                <v-card-title class="error py-1"></v-card-title>
                                <v-card-title align-center justify-space-between class="py-1">
                                    
                                    <v-flex xs9>
                                        <h3 class="error--text">Urgent & Important</h3>
                                    </v-flex>
                                    <v-flex xs2>
                                        <NewTask v-on:new-task="createTask" v-bind:cat="'uandi'"/>
                                    </v-flex>
                                    
                                </v-card-title>
                                <v-card-text column justify-center>
                                    <draggable class="list-group" :list="tasks.UandI" group="people" @change="log">
                                        <transition-group>
                                            <v-list class="list-group-item" v-for="(item, i) in tasks.UandI" :key="i">
                                                <TaskItem 
                                                    v-on:edit-task="editTask" 
                                                    v-on:del-task="deleteTask" 
                                                    v-bind:json="item"/>
                                            </v-list>
                                        </transition-group>
                                    </draggable>
                                </v-card-text>
                            </v-card>
                        </v-flex>
                        
                        <v-flex xs12 md6 class="pa-3">
                            <!-- Urgent -->
                            <v-card>
                                <v-card-title class="warning py-1"></v-card-title>
                                <v-card-title align-center justify-space-between class="py-1">
                                    
                                    <v-flex xs9>
                                        <h3 class="warning--text">Urgent</h3>
                                    </v-flex>
                                    <v-flex xs2>
                                        <NewTask v-on:new-task="createTask" v-bind:cat="'urgent'"/>
                                    </v-flex>
                                    
                                </v-card-title>
                                <v-card-text column justify-center>
                                    <draggable class="list-group" :list="tasks.Urgent" group="people" @change="log">
                                        <transition-group>
                                            <v-list class="list-group-item" v-for="(item, i) in tasks.Urgent" :key="i">
                                                <TaskItem 
                                                    v-on:edit-task="editTask" 
                                                    v-on:del-task="deleteTask" 
                                                    v-bind:json="item"/>
                                            </v-list>
                                        </transition-group>
                                    </draggable>
                                </v-card-text>
                            </v-card>
                        </v-flex>
                    </v-layout>
                    <v-layout row wrap>
                        <v-flex xs12 md6 class="pa-3">
                            <!-- Important -->
                            <v-card>
                                <v-card-title class="info py-1"></v-card-title>
                                <v-card-title align-center justify-space-between class="py-1">
                                    
                                    <v-flex xs9>
                                        <h3 class="info--text">Important</h3>
                                    </v-flex>
                                    <v-flex xs2>
                                        <NewTask v-on:new-task="createTask" v-bind:cat="'important'"/>
                                    </v-flex>
                                    
                                </v-card-title>
                                <v-card-text column justify-center>
                                    <draggable class="list-group" :list="tasks.Important" group="people" @change="log">
                                        <transition-group>
                                            <v-list class="list-group-item" v-for="(item, i) in tasks.Important" :key="i">
                                                <TaskItem 
                                                    v-on:edit-task="editTask" 
                                                    v-on:del-task="deleteTask" 
                                                    v-bind:json="item"/>
                                            </v-list>
                                        </transition-group>
                                    </draggable>
                                </v-card-text>
                            </v-card>
                        </v-flex>
                        <v-flex xs12 md6 class="pa-3">
                            <!-- Other -->
                            <v-card>
                                <v-card-title class="grey py-1"></v-card-title>
                                <v-card-title align-center justify-space-between class="py-1">
                                    
                                    <v-flex xs9>
                                        <h3 class="grey--text">Other</h3>
                                    </v-flex>
                                    <v-flex xs2>
                                        <NewTask v-on:new-task="createTask" v-bind:cat="'other'"/>
                                    </v-flex>
                                    
                                </v-card-title>
                                <v-card-text column justify-center>
                                    <draggable class="list-group" :list="tasks.Other" group="people" @change="log">
                                        <transition-group>
                                            <v-list class="list-group-item" v-for="(item, i) in tasks.Other" :key="i">
                                                <TaskItem 
                                                    v-on:edt-task="editTask" 
                                                    v-on:del-task="deleteTask" 
                                                    v-bind:json="item"/>
                                            </v-list>
                                        </transition-group>
                                    </draggable>
                                </v-card-text>
                            </v-card>
                        </v-flex>
                    </v-layout>
                </v-container>
            </v-content>
        </v-app>
    </div>
</template>

<script>
import draggable from 'vuedraggable';
import Navigation from '../components/Navigation';
import NewTask from '../actions/NewTask';
import TaskItem from '../components/TaskItem';
import uuid from 'uuid';

export default {
    components: {
        draggable,
        Navigation,
        NewTask,
        TaskItem
    },
    $_veeValidate: {
        validator: 'new'
    },
    methods: {
        createTask(createdTask) {
            if (createdTask.category == 'Urgent and Important')
                this.tasks.UandI = [...this.tasks.UandI, createdTask];
            else if (createdTask.category == 'Urgent')
                this.tasks.Urgent = [...this.tasks.Urgent, createdTask];
            else if (createdTask.category == 'Important')
                this.tasks.Important = [...this.tasks.Important, createdTask];
            else
                this.tasks.Other = [...this.tasks.Other, createdTask];
            
            this.$http.post('api/tasks/', this.tasks)
                .then(res => console.log(res.data))
                .catch(err => console.log(err));
        },
        deleteTask(del) {
            if (del.category == 'Urgent and Important')
                this.tasks.UandI = this.tasks.UandI.filter(todo => todo.id !== del.id);
            else if (del.category == 'Urgent')
                this.tasks.Urgent = this.tasks.Urgent.filter(todo => todo.id !== del.id);
            else if (del.category == 'Important')
                this.tasks.Important = this.tasks.Important.filter(todo => todo.id !== del.id);
            else
                this.tasks.Other = this.tasks.Other.filter(todo => todo.id !== del.id);
        },
        editTask(edt) {
            if (edt.category == 'Urgent and Important') {
                var pos = this.tasks.UandI.map(function(e) { return e.id }).indexOf(edt.id);
                this.tasks.UandI[pos] = edt;
            }
            else if (edt.category == 'Urgent') {
                var pos = this.tasks.Urgent.map(function(e) { return e.id }).indexOf(edt.id);
                this.tasks.Urgent[pos] = edt;
            }
            else if (edt.category == 'Important') {
                var pos = this.tasks.Important.map(function(e) { return e.id }).indexOf(edt.id);
                this.tasks.Important[pos] = edt;
            }
            else {
                var pos = this.tasks.Other.map(function(e) { return e.id }).indexOf(edt.id);
                this.tasks.Other[pos] = edt;
            }
        },
        log: function(evt) {
            console.log(evt);

            if (evt.removed) {
                console.log('Update API');
            }
        }
    },
    created() {
        this.$http.get('api/task/')
            .then(res => this.apiTasks = res.data)
            .catch(err => console.log(err));
    },
    data() {
        return {
            showModal: false,
            editable: false,
            isDragging: false,
            delayedDragging: false,
            apiTasks: '',
            tasks: {
                    UandI: [
                    {
                        category: 'Urgent and Important',
                        application: 'Fran Hire',
                        due: new Date('2019-06-10T16:50:00.000Z').toLocaleString('en-US'),
                        completed: true,
                        action: "Text",
                        description: 'This is an example task',
                        id: uuid.v4()
                    },
                    {
                        category: 'Urgent and Important',
                        application: 'Sales Analytics',
                        due: new Date('2019-06-10T16:50:00.000Z').toLocaleString('en-US'),
                        completed: false,
                        action: "Call",
                        description: 'This is an example task',
                        id: uuid.v4()
                    },
                ],
                Important: [
                    {
                        category: 'Important',
                        application: 'Sales Analytics',
                        due: new Date('2019-06-10T16:50:00.000Z').toLocaleString('en-US'),
                        completed: false,
                        action: "Email",
                        description: 'This is an example task',
                        id: uuid.v4()
                    },
                    {
                        category: 'Important',
                        application: 'Fran Jobs',
                        due: new Date('2019-06-10T16:50:00.000Z').toLocaleString('en-US'),
                        completed: true,
                        action: "Meeting",
                        description: 'This is an example task',
                        id: uuid.v4()
                    }
                ],
                Urgent: [
                    {
                        category: 'Urgent',
                        application: 'Fran Hire',
                        due: new Date('2019-06-10T16:50:00.000Z').toLocaleString('en-US'),
                        completed: false,
                        action: "Call",
                        description: 'This is an example task',
                        id: uuid.v4()
                    },
                    {
                        category: 'Urgent',
                        application: 'Fran Train',
                        due: new Date('2019-06-10T16:50:00.000Z').toLocaleString('en-US'),
                        completed: false,
                        action: "Meeting",
                        description: 'This is an example task',
                        id: uuid.v4()
                    }
                ],
                Other: [
                    {
                        category: 'Other',
                        application: 'Sales Analytics',
                        due: new Date('2019-06-10T16:50:00.000Z').toLocaleString('en-US'),
                        completed: false,
                        action: "Call",
                        description: 'This is an example task',
                        id: uuid.v4()
                    }
                ]
            }, // End tasks
        } // End return
    } // End data
}
</script>

<style scoped>

</style>

