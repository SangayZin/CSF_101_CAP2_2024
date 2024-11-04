## TEST_README.md - Library Management System Testing Documentation

## Introduction
This document outlines the unit tests that were designed for the Library Management System. The tests primarily check features such, as book borrowing and return processes availability verification book addition, by administrators and managing scenarios where errors occur. The goal of these test cases is to verify that the system behaves correctly under circumstances including situations and limits of operation. 

## Resources Used

1. **Python `unittest` Documentation**  
   - Link: [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)  
   - Justification:I referred to Pythons unittest' module documentation to grasp the structure and necessary methods, for writing test cases in this project since the 'unittest' framework is widely used in Python and considered dependable for this purpose. 

2. **Real Python - Unit Testing in Python**  
   - Link: [Real Python Unit Testing Guide](https://realpython.com/python-testing/)  
   - Justification: Real Python gave me tips, on how to structure test cases and manage interactions effectively which helped me confirm that my test cases were thorough and aligned with Python conventions. 
3. **Stack Overflow Discussions**  
   - Link: [Example of Unit Testing](https://stackoverflow.com/)  
   - Justification: Discussions, on Stack Overflow were really useful for dealing with situations and fixing problems that came up while testing out the systems functionality.It gave some hands on tips on how to set up tests for situations such, as trying to borrow a book thats not available or returning a book that was never borrowed before. 

## Justification for the Resources
The materials were chosen because they are pertinent, to the job and dependable in nature.The `unittest` guide was crucial, for grasping the frameworks core concepts.Real Python provided elucidations and instances that facilitated the application of ideas in my test scenarios.In conclusion.Stack Overflow proved helpful in overcoming obstacles and gaining insight into how others tackled issues. 

## Test Coverage
The test cases created cover a wide range of scenarios within the Library Management System:

1. **Valid Book Borrowing**  
   - Ensures that a user can successfully borrow a book, and the availability status changes accordingly.
   
2. **Invalid Book Borrowing**  
   - Tests the scenario where a user attempts to borrow a book that has already been borrowed.

3. **Valid Book Returning**  
   - Verifies that a user can return a book and the system updates the book’s availability status.

4. **Invalid Book Returning**  
   - Ensures that users cannot return books that were not borrowed or that belong to another user.

5. **Admin Adding Books**  
   - Confirms that an admin user can successfully add new books to the library collection and that they appear in the list of available books.

6. **Boundary and Edge Cases**  
   - Handles cases such as attempting to borrow or return all books, trying to borrow an unavailable book, or returning a book without borrowing it first.

7. **Check available books after borrowing**
   - This test ensures that once a book is borrowed, the system updates the list of available books

8. **Check available books after returning**
   -This test checks if the availability of a book is correctly restored after it is returned, making it available for others.

## Conclusion
This document outlines the resources and methodology used to develop and execute the unit tests for the Library Management System. By utilizing Python's `unittest` framework and following best practices from the provided resources, I was able to validate the core functionalities of the system, covering both typical use cases and edge cases.

