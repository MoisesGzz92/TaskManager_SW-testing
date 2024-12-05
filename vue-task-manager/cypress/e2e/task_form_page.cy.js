/**
 * @type {Cypress.PluginConfig}
 * This is the test for the main page of the task managervue app
 */
describe('Task Form Page', () => {
    beforeEach(() => {
      // Visit the Task Form Page
      cy.visit('http://localhost:8080/task/create');
    });

    it('should add a new task', () => {
      const taskName = 'Test Task';
      const taskDescription = 'This is a test task description.';

      // Fill in the task name
      cy.get('input[aria-label="Task Name"]').type(taskName);

      // Fill in the task description
      cy.get('textarea[aria-label="Description"]').type(taskDescription);

      // Click the Create Task button
      cy.get('button[type="submit"]').click();

      // Verify that the task was created successfully
      // You can check for a success message or verify the task appears in the task list
      cy.url().should('eq', 'http://localhost:8080/'); // Check if redirected to the home page
      cy.contains(taskName).should('be.visible'); // Check if the task name is visible on the home page
    });

    it('should show an error if task name is missing', () => {
      // Click the Create Task button without filling in the form
      cy.get('button[type="submit"]').click();

      // Verify that an error message is displayed
      cy.get('.v-alert').should('be.visible').and('contain', 'Task name is required');
    });
  });
