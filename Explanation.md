### Bonus 1: 
To include the "priority" field, need to extend the
logic in calculate_total_grade to consider the priority.

### Bonus 2: 
To handle the delay in new website appearances, 
you might want to introduce a mechanism to simulate the passage
of time. For instance, you can add a timestamp field to the
websites and update it periodically based on the elapsed time
since the last update. The calculate_total_grade function can
then consider this timestamp when computing the seniority parameter. Keep in mind that this is a simulation,
and in a real-world scenario, need to use a scheduler (change the time)
or a time-based trigger in your database system.

### 3. Explanations and Assumptions

#### 3.1 Database Assumptions

- The database system (simulator Data Base, MySQL, PostgreSQL, e.g.) is assumed to be properly configured and accessible during testing.
- The structure of the database tables (products, websites, search_engine_ranking, etc.) adheres to the expected schema.

#### 3.2 API Endpoint Assumptions

- The provided API endpoints (`insertNewSiteIntoSearchEngineDb`, `getSearchTermOptions`, etc.) are assumed to be fully functional.
- The API responses adhere to the specified format and provide accurate information.

#### 3.3 Ranking Calculation Assumptions

- The ranking calculation logic is assumed to be implemented correctly based on the specified parameters (seniority, keywords, references, priority).
- The ranking mechanism considers all relevant parameters and updates rankings accordingly.

#### 3.4 Test Data Assumptions

- Test data for insertion and ranking scenarios are assumed to represent a realistic scenario.
- The generated test data includes diverse cases to cover a wide range of scenarios.

#### 3.5 System State Assumptions

- The system is assumed to be in a stable state before the execution of each test scenario.
- No ongoing maintenance or other disruptive activities are expected during the testing phase.

#### 3.6 Test Environment Assumptions

- The test environment is assumed to mimic the production environment closely.
- Scheduler jobs (update ranking, insert data) are assumed to run as scheduled without interruptions.

#### 3.7 API Response Handling

- When testing API endpoints, it's assumed that proper error handling is implemented for scenarios such as invalid requests, server unavailability, or no data found.

#### 3.8 Priority Field in Ranking

- The priority field in the ranking mechanism is assumed to be implemented correctly.
- The impact of priority on the total grade is assumed to be reflected accurately in the ranking.

#### 3.9 Performance Assumptions

- The performance of the system is assumed to be within acceptable limits during both normal and stress testing scenarios.
- Stress tests are assumed to provide insights into system behavior under load.



### If you have more time to improve the project, there are several aspects you can consider:

1. **Add Data Bases:** Create and run DB on local docker and use them.

2. **DataGeneration:** Use the Fake library to generate test data

3. **Unit Testing:** Enhance your unit tests to cover more edge cases and scenarios. Make sure to test different combinations of parameters and prioritize the tests based on critical functionality.

4. **Integration Testing:** Consider creating integration tests that cover the interaction between different components of your system. For example, you can simulate the full process of updating the ranking, from inserting new products to updating the ranking table.

5. **Refactor and Code Quality:** Review your code for any areas that can be refactored to improve readability and maintainability. Ensure adherence to coding standards and best practices.

6. **Logging:** Expand logging in your application. Ensure that log messages are helpful for debugging and troubleshooting. You can log more details during critical processes or when exceptions occur.

7. **Error Handling:** Implement robust error handling mechanisms. Make sure that your application gracefully handles unexpected situations and provides meaningful error messages.

8. **Documentation:** Enhance code documentation, including docstrings for functions and classes. Document any assumptions, limitations, or dependencies. Consider using a documentation tool like Sphinx to generate documentation from docstrings.

9. **Performance Optimization:** If you identify performance bottlenecks, consider optimizing critical sections of your code. Use profiling tools to identify areas that can be improved, and apply appropriate optimizations.

10. **Security Considerations:** Review your code for potential security vulnerabilities. Ensure that you are handling user inputs securely, validating data, and protecting against common security issues.

11. **Scalability:** Consider how your application might scale as the data volume increases. Optimize database queries, and explore options for caching or database indexing if necessary.

12. **Code Review:** If you are working in a team, conduct code reviews to get feedback from other developers. Code reviews can help identify potential issues, ensure consistency, and share knowledge among team members.

13. **Automated Build and Deployment:** Implement automated build and deployment processes. This can include using tools like Jenkins, Travis CI, or GitHub Actions to automate testing and deployment workflows.

14. **Continuous Integration/Continuous Deployment (CI/CD):** Set up CI/CD pipelines to automate the testing and deployment of your application. This ensures that changes are automatically validated and deployed in a controlled manner.





