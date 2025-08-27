#!/usr/bin/env python3
"""
Test script to demonstrate the File Manager program
"""

import os
import subprocess
import sys

def test_file_creation():
    """Test that all required files exist."""
    required_files = [
        'file_manager.py',
        'sample_text.txt',
        'requirements.txt',
        'README.md'
    ]
    
    print("🔍 Checking required files...")
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} missing")
            return False
    return True

def test_python_syntax():
    """Test that the main program has valid Python syntax."""
    print("\n🔍 Checking Python syntax...")
    try:
        with open('file_manager.py', 'r') as f:
            compile(f.read(), 'file_manager.py', 'exec')
        print("✅ Python syntax is valid")
        return True
    except SyntaxError as e:
        print(f"❌ Syntax error: {e}")
        return False

def test_sample_file():
    """Test that the sample file can be read."""
    print("\n🔍 Testing sample file...")
    try:
        with open('sample_text.txt', 'r') as f:
            content = f.read()
            if len(content) > 0:
                print(f"✅ Sample file readable ({len(content)} characters)")
                return True
            else:
                print("❌ Sample file is empty")
                return False
    except Exception as e:
        print(f"❌ Error reading sample file: {e}")
        return False

def run_demo():
    """Run a quick demo of the program."""
    print("\n🚀 Running program demo...")
    print("Note: This will start the interactive program.")
    print("You can test it with 'sample_text.txt' or press Ctrl+C to exit.")
    
    try:
        # Run the program
        result = subprocess.run([sys.executable, 'file_manager.py'], 
                              input=b'sample_text.txt\ny\ny\nn\n', 
                              timeout=30)
        print(f"\n✅ Demo completed with exit code: {result.returncode}")
    except subprocess.TimeoutExpired:
        print("\n⏰ Demo timed out (this is normal for interactive programs)")
    except KeyboardInterrupt:
        print("\n👋 Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Demo error: {e}")

def main():
    """Main test function."""
    print("🧪 File Manager Program Test Suite")
    print("=" * 40)
    
    # Run all tests
    tests = [
        test_file_creation,
        test_python_syntax,
        test_sample_file
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The program is ready to use.")
        print("\nTo run the program:")
        print("python3 file_manager.py")
        
        # Ask if user wants to run demo
        try:
            run_demo_choice = input("\n🤔 Would you like to run a quick demo? (y/n): ").strip().lower()
            if run_demo_choice in ['y', 'yes']:
                run_demo()
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
    else:
        print("❌ Some tests failed. Please check the issues above.")

if __name__ == "__main__":
    main()
