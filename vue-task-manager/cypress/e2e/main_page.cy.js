/**
 * @type {Cypress.PluginConfig}
 * This is the test for the main page of the task managervue app
 */
describe('TaskManager Main Page Tests', () => {
    beforeEach(() => {
        // Navigate to the landing page
        cy.visit('http://localhost:8080');
    });

    it('should display the "create new task" button and redirect to the create task page', () => {
        // Check if the create button is visible
        cy.get('#create-task-btn').should('be.visible');

        // Click the create button and verify redirection
        // to the create task page
        cy.get('#create-task-btn').click();
        cy.url().should('eq', 'http://localhost:8080/task/create');
    });
});
