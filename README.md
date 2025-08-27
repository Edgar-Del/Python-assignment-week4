# File Read & Write Challenge with Error Handling Lab 🖋️🧪

## Overview
This Python program demonstrates comprehensive file operations including reading, modifying, and writing files, with robust error handling and user input validation.

## 🎯 Learning Objectives
By completing this assignment, you'll master:
- **File Operations**: Reading from and writing to files
- **Error Handling**: Graceful handling of file-related errors
- **User Input Validation**: Robust input processing
- **Exception Management**: Comprehensive try-catch blocks
- **File System Operations**: File validation and management

## 🚀 Features

### Core Functionality
- **File Reading**: Read files with multiple encoding support
- **Content Modification**: Transform file content with statistics
- **File Writing**: Create modified versions with unique naming
- **Preview System**: Display file contents before processing

### Error Handling
- **File Existence**: Check if files exist before reading
- **Permission Errors**: Handle read/write permission issues
- **Encoding Issues**: Support multiple file encodings
- **Size Validation**: Prevent processing of extremely large files
- **Graceful Recovery**: Continue operation after errors

### User Experience
- **Interactive Interface**: User-friendly command-line interface
- **Input Validation**: Robust filename validation
- **Progress Feedback**: Clear status messages and progress indicators
- **File Statistics**: Display comprehensive file information

## 📁 Project Structure
```
Python-assignment-week4/
├── file_manager.py          # Main program file
├── sample_text.txt          # Sample file for testing
├── requirements.txt         # Dependencies (none required)
└── README.md               # This documentation
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- No external dependencies required

### Running the Program
1. **Clone or download** the project files
2. **Navigate** to the project directory:
   ```bash
   cd Python-assignment-week4
   ```
3. **Run the program**:
   ```bash
   python3 file_manager.py
   ```

## 🎮 How to Use

### Basic Usage
1. **Start the program**: Run `python3 file_manager.py`
2. **Enter filename**: Type the name of a file to process
3. **Review preview**: See the first 10 lines of your file
4. **Confirm modification**: Choose whether to create a modified version
5. **View results**: Check the generated modified file

### Example Session
```
🚀 File Manager - Read, Modify & Write Challenge
==================================================
This program will:
• Read a file you specify
• Show you a preview of its contents
• Create a modified version
• Save the modified version to a new file
• Handle any errors gracefully

📁 Enter the filename to read (or 'quit' to exit): sample_text.txt
✅ File 'sample_text.txt' is valid and ready to read.
✅ Successfully read 'sample_text.txt' (1234 characters)

📖 File Preview (showing first 10 lines):
--------------------------------------------------
  1: Python Programming Fundamentals
  2: 
  3: Welcome to the world of Python programming! This is a sample text file...
  4: 
  5: Key Topics Covered:
  6: 1. Variables and Data Types
  7: 2. Control Structures (if, for, while)
  8: 3. Functions and Methods
  9: 4. File Operations
 10: 5. Error Handling with try-except blocks
--------------------------------------------------

🤔 Do you want to create a modified version? (y/n): y

🔧 Modifying content from 'sample_text.txt'...

📊 File Statistics:
   Lines: 25
   Words: 89
   Characters: 1234
   Average words per line: 3.6

✅ Successfully wrote modified content to 'sample_text_modified.txt'
🎉 Success! Your modified file has been created.
```

## 🔧 Error Handling Examples

### File Not Found
```
�� Enter the filename to read (or 'quit' to exit): nonexistent.txt
❌ File 'nonexistent.txt' does not exist.
```

### Permission Denied
```
📁 Enter the filename to read (or 'quit' to exit): /etc/shadow
❌ File '/etc/shadow' exists but cannot be read (permission denied).
```

### Empty File
```
📁 Enter the filename to read (or 'quit' to exit: empty.txt
❌ File 'empty.txt' is empty.
```

### Large File
```
📁 Enter the filename to read (or 'quit' to exit: huge_file.txt
❌ File 'huge_file.txt' is too large (15.2MB).
```

## 📚 Key Concepts Demonstrated

### 1. File Operations
- **Reading**: `open()`, `read()`, context managers
- **Writing**: `open()`, `write()`, unique filename generation
- **Validation**: File existence, permissions, size checks

### 2. Error Handling
- **Try-Except Blocks**: Comprehensive exception handling
- **Specific Exceptions**: Handle different error types appropriately
- **Graceful Degradation**: Continue operation after errors
- **User Feedback**: Clear error messages and recovery options

### 3. Input Validation
- **User Input**: Safe input handling with validation
- **Filename Validation**: Check file properties before processing
- **Loop Control**: Robust program flow with exit options

### 4. Content Modification
- **Text Processing**: String manipulation and analysis
- **Statistics Generation**: Line, word, and character counting
- **Metadata Addition**: Timestamps and file information

## 🧪 Testing Your Program

### Test Cases
1. **Valid File**: Use `sample_text.txt` to test normal operation
2. **Non-existent File**: Try entering a filename that doesn't exist
3. **Directory**: Try entering a directory name instead of a file
4. **Permission Issues**: Try accessing system files you can't read
5. **Empty File**: Create an empty file and test the validation
6. **Large File**: Test with a file larger than 10MB

### Expected Behaviors
- ✅ **Valid files**: Process successfully with preview and modification
- ❌ **Invalid files**: Display appropriate error messages
- 🔄 **Error recovery**: Continue operation after handling errors
- 🚪 **Clean exit**: Graceful program termination

## 🎓 Learning Outcomes

After completing this assignment, you'll be able to:

### Technical Skills
- **File I/O**: Read, write, and modify files in Python
- **Error Handling**: Implement robust exception handling
- **Input Validation**: Validate user input and file properties
- **String Processing**: Manipulate and analyze text content

### Best Practices
- **Defensive Programming**: Handle edge cases and errors gracefully
- **User Experience**: Provide clear feedback and recovery options
- **Code Organization**: Structure code with classes and methods
- **Documentation**: Write clear, comprehensive code documentation

### Problem Solving
- **Error Analysis**: Identify and categorize different error types
- **Recovery Strategies**: Implement appropriate error recovery mechanisms
- **User Guidance**: Help users understand and resolve issues
- **System Robustness**: Build applications that handle unexpected situations

## 🚀 Advanced Challenges

### Extension Ideas
1. **Multiple File Formats**: Support for JSON, CSV, XML files
2. **Content Filters**: Add options to filter or search content
3. **Batch Processing**: Process multiple files at once
4. **Configuration Files**: Load settings from external files
5. **Logging System**: Add comprehensive logging capabilities
6. **GUI Interface**: Create a graphical user interface

### Code Improvements
1. **Performance Optimization**: Handle very large files efficiently
2. **Memory Management**: Implement streaming for large files
3. **Async Operations**: Add asynchronous file processing
4. **Unit Testing**: Create comprehensive test suites
5. **Type Hints**: Add complete type annotations

## 🤝 Contributing
Feel free to improve this program by:
- Adding new features
- Improving error handling
- Enhancing user interface
- Optimizing performance
- Adding more test cases

## 📄 License
This project is open source and available under the MIT License.

## 🎉 Conclusion
Congratulations! You've completed the File Read & Write Challenge with Error Handling Lab. You now have the skills to build robust, user-friendly applications that handle files efficiently and gracefully manage errors.

**Next Steps**: Try the advanced challenges, experiment with different file types, and apply these concepts to your own projects!
