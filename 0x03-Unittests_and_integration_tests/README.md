# Project 0x03: Unittests and Integration Tests

Welcome to Project 0x03: Unittests and Integration Tests! In this project, we will dive into the world 
of unit testing and integration testing to ensure the reliability and functionality of the code. 
Below are the details of the project, including concepts, resources, requirements, and tasks:

## Concepts Covered:

### Unit Testing:

Unit testing is the process of testing that a particular function returns expected results for different sets of inputs.
It focuses on testing the logic defined inside the tested function and should only test standard inputs and corner cases.
Key aspects include using mock objects to simulate behavior, testing the function in isolation, and ensuring expected 
outcomes for various inputs.

### Integration Testing:

Integration testing aims to test a code path end-to-end, including interactions between different parts of your code.
It involves testing the integration of various components to ensure they work together as expected.
### Mocking:

Mocking is the process of simulating the behavior of complex components, such as network requests or database calls,
 to isolate the unit of code being tested.
It allows you to replace external dependencies with mock objects to control their behavior during testing.
## Resources:

- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/39623882/how-to-mock-a-readonly-property-with-mock)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)


## Tasks:

### 0. Parameterize a unit test

- Implement unit tests for `utils.access_nested_map` function.
- Test different inputs using `@parameterized.expand`.
- Ensure that the function returns the expected result for each input.

### 1. Parameterize a unit test

- Implement unit tests for `utils.access_nested_map_exception` function.
- Use `assertRaises` context manager to test that a `KeyError` is raised for specific inputs.
- Verify that the exception message is as expected.

### 2. Mock HTTP calls

- Implement unit tests for `utils.get_json` function.
- Use `unittest.mock.patch` to mock `requests.get`.
- Ensure that the mocked `get` method is called with the expected argument and returns a known payload.

### 3. Parameterize and patch

- Implement unit tests for `utils.memoize` decorator.
- Use `unittest.mock.patch` to mock a method.
- Verify that the method is called only once when calling a property twice.

### 4. Parameterize and patch as decorators

- Implement unit tests for `client.GithubOrgClient` class.
- Use `@patch` decorator to mock `get_json` method.
- Use `@parameterized.expand` decorator to parametrize the test with different org examples.

### 5. Mocking a property

- Implement unit tests for `GithubOrgClient._public_repos_url` method.
- Use `patch` as a context manager to mock `GithubOrgClient.org`.
- Verify that the result of `_public_repos_url` is as expected based on the mocked payload.

### 6. More patching

- Implement unit tests for `GithubOrgClient.public_repos` method.
- Use `@patch` as a decorator to mock `get_json`.
- Use `patch` as a context manager to mock `GithubOrgClient._public_repos_url`.
- Test that the list of repos is what you expect from the chosen payload.

### 7. Parameterize

- Implement unit tests for `GithubOrgClient.has_license` method.
- Parametrize the test with different inputs and expected returned values.

### 8. Integration test: fixtures

- Implement integration tests for `GithubOrgClient.public_repos` method.
- Use fixtures from `fixtures.py` to mock external requests.
- Parameterize the test class with fixtures using `@parameterized_class`.

### 9. Integration tests

- Implement integration tests for `GithubOrgClient.public_repos` method.
- Ensure that the method returns the expected results based on the fixtures.
- Implement tests for `GithubOrgClient.public_repos` with the `license` argument and verify the results.


