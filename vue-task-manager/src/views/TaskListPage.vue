<template>
  <div class="task-list">
    <!-- Header -->
    <header class="app-header">
      <div class="header-content">
        <div class="header-left">
          <v-icon
            icon="mdi-checkbox-marked-outline"
            size="32"
            color="white"
            class="header-icon"
          ></v-icon>
          <h1 class="header-title">TaskManager</h1>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <v-container class="py-8">
      <!-- Title and Create Button -->
      <div class="d-flex justify-space-between align-center mb-6">
        <h2 class="text-h4">Tasks</h2>
        <v-btn
          id="create-task-btn"
          color="primary"
          variant="elevated"
          prepend-icon="mdi-plus"
          @click="createTask"
        >
          CREATE NEW TASK
        </v-btn>
      </div>

      <!-- Table Section -->
      <v-card>
        <v-data-table
          id="tasks-table"
          :headers="headers"
          :items="taskList"
          :loading="loading"
          :items-per-page="rowsPerPage"
          class="elevation-1"
        >
          <template v-slot:item="{ item }">
            <tr>
              <td>{{ item.name }}</td>
              <td>{{ item.description }}</td>
              <td class="text-right">
                <div class="d-flex justify-end">
                  <v-btn
                    :id="`edit-task-${item.name}`"
                    color="primary"
                    variant="text"
                    density="comfortable"
                    icon="mdi-pencil"
                    class="mr-2"
                    @click="editTask(item)"
                  ></v-btn>
                  <v-btn
                    :id="`delete-task-${item.name}`"
                    color="error"
                    variant="text"
                    density="comfortable"
                    icon="mdi-delete"
                    @click="deleteTask(item.name)"
                  ></v-btn>
                </div>
              </td>
            </tr>
          </template>

          <!-- No Data Template -->
          <template v-slot:no-data>
            <div id="no-data-message" class="pa-4 text-center">
              No data available
            </div>
          </template>
        </v-data-table>
      </v-card>

      <!-- Info Message -->
      <v-alert
        id="no-tasks-alert"
        v-if="taskList.length === 0 && !loading"
        type="info"
        class="mt-4"
        variant="tonal"
        border="start"
      >
        No tasks available at the moment.
      </v-alert>

      <!-- Edit Dialog -->
      <v-dialog v-model="editDialog" max-width="600px">
        <v-card>
          <v-card-title class="text-h5 pa-4">
            Edit Task
          </v-card-title>

          <v-card-text>
            <v-form ref="editForm" id="edit-task-form">
              <v-text-field
                id="edit-task-name"
                v-model="editedTask.name"
                label="Task Name"
                variant="outlined"
                density="comfortable"
                :rules="[v => !!v || 'Task name is required']"
                required
                class="mb-4"
                data-cy="edit-task-name-input"
              ></v-text-field>

              <v-textarea
                id="edit-task-description"
                v-model="editedTask.description"
                label="Description"
                variant="outlined"
                density="comfortable"
                :rules="[v => !!v || 'Description is required']"
                required
                rows="4"
                data-cy="edit-task-description-input"
              ></v-textarea>
            </v-form>
          </v-card-text>

          <v-card-actions class="pa-4 pt-0">
            <v-spacer></v-spacer>
            <v-btn
              id="cancel-edit-btn"
              color="grey-darken-1"
              variant="text"
              @click="closeEditDialog"
            >
              Cancel
            </v-btn>
            <v-btn
              id="save-edit-btn"
              color="primary"
              variant="elevated"
              :loading="updating"
              @click="updateTask"
            >
              Save
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/api'

const router = useRouter()
const taskList = ref([])
const loading = ref(false)
const rowsPerPage = ref(10)

const headers = [
  { title: 'Task Name', key: 'name', align: 'start' },
  { title: 'Description', key: 'description', align: 'start' },
  { title: 'Actions', key: 'actions', align: 'end', sortable: false },
]

const fetchTasks = async () => {
  loading.value = true
  try {
    const response = await api.get('/tasks')
    if (!response.data || Object.keys(response.data).length === 0) {
      taskList.value = []
    } else if (Array.isArray(response.data)) {
      taskList.value = response.data
    } else {
      taskList.value = Object.values(response.data)
    }
  } catch (error) {
    console.error('Error fetching tasks:', error)
    taskList.value = []
  } finally {
    loading.value = false
  }
}

const createTask = () => {
  router.push('/task/create')
}

const deleteTask = async (name) => {
  try {
    await api.delete(`/task/${name}`)
    await fetchTasks()
  } catch (error) {
    console.error('Error deleting task:', error)
  }
}

// Edit dialog state
const editDialog = ref(false)
const editForm = ref(null)
const updating = ref(false)
const editedTask = ref({
  name: '',
  description: '',
  originalName: '' // To store the original name for the API call
})

const editTask = (task) => {
  editedTask.value = {
    name: task.name,
    description: task.description,
    originalName: task.name // Store original name for API reference
  }
  editDialog.value = true
}

const closeEditDialog = () => {
  editDialog.value = false
  editedTask.value = {
    name: '',
    description: '',
    originalName: ''
  }
}

const updateTask = async () => {
  const { valid } = await editForm.value.validate()

  if (!valid) return

  updating.value = true
  try {
    await api.put(`/task/${editedTask.value.originalName}`, {
      name: editedTask.value.name,
      description: editedTask.value.description
    })
    await fetchTasks()
    closeEditDialog()
  } catch (error) {
    console.error('Error updating task:', error)
  } finally {
    updating.value = false
  }
}

onMounted(() => {
  fetchTasks()
})
</script>

<style scoped>
.task-list {
  min-height: 100vh;
  background-color: #f5f5f5;
}

.app-header {
  background-color: #1976d2;
  padding: 16px 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.header-content {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 16px;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.header-icon {
  margin-right: 4px;
}

.header-title {
  color: white;
  font-size: 24px;
  font-weight: 500;
  margin: 0;
  letter-spacing: 0.5px;
}

:deep(.v-data-table) {
  background-color: white;
}

:deep(.v-data-table-header th) {
  background-color: #f5f5f5 !important;
  color: rgba(0, 0, 0, 0.87) !important;
  font-size: 0.875rem;
  font-weight: 500 !important;
  text-transform: none !important;
}

:deep(.v-data-table-row td) {
  height: 48px;
}

:deep(.v-btn--icon) {
  margin: 0 2px;
}

.edit-dialog-form {
  padding: 20px;
}
</style>
