<template>
  <v-app>
    <!-- Header Section -->
    <v-app-bar color="primary" class="px-4">
      <v-btn color="white" variant="text" @click="goBack">
        <v-icon>mdi-arrow-left</v-icon>
        Back
      </v-btn>
      <v-spacer></v-spacer>
    </v-app-bar>

    <!-- Main Content Section -->
    <v-main>
      <v-container class="pa-6">
        <v-card class="mx-auto" max-width="600">
          <v-card-title class="text-h5 pa-4">
            Create New Task
          </v-card-title>

          <v-card-text>
            <v-form @submit.prevent="submitTask" ref="form">
              <v-text-field
                v-model="task.name"
                label="Task Name"
                :rules="[v => !!v || 'Task name is required']"
                required
                class="mb-4"
              ></v-text-field>

              <v-textarea
                v-model="task.description"
                label="Description"
                :rules="[v => !!v || 'Description is required']"
                required
                class="mb-4"
              ></v-textarea>

              <v-card-actions class="pa-0">
                <v-spacer></v-spacer>
                <v-btn
                  color="primary"
                  type="submit"
                  :loading="loading"
                >
                  Create Task
                </v-btn>
              </v-card-actions>
            </v-form>
          </v-card-text>
        </v-card>

        <!-- Error Alert -->
        <v-alert
          v-if="error"
          type="error"
          class="mt-4"
          variant="tonal"
          closable
        >
          {{ error }}
        </v-alert>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const form = ref(null)
const loading = ref(false)
const error = ref(null)

const task = ref({
  name: '',
  description: ''
})

const submitTask = async () => {
  const { valid } = await form.value.validate()

  if (!valid) return

  loading.value = true
  error.value = null

  try {
    await axios.post('http://127.0.0.1:5000/task', task.value)
    router.push('/')
  } catch (err) {
    error.value = err.response?.data?.message || 'Failed to create task'
  } finally {
    loading.value = false
  }
}

const goBack = () => {
  router.push('/')
}
</script>

<style scoped>
/* Override Vuetify default styles */
:deep(.v-text-field .v-input__details) {
  padding-inline-start: 0;
}

:deep(.v-textarea .v-input__details) {
  padding-inline-start: 0;
}

:deep(.v-card-title) {
  border-bottom: 1px solid rgba(0, 0, 0, 0.12);
}
</style>
