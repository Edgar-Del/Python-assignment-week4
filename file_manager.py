#!/usr/bin/env python3
"""
File Read & Write Challenge with Error Handling Lab
==================================================

"""

import os
import sys
from typing import Optional


class FileManager:
    """A class to handle file operations with comprehensive error handling."""
    
    def __init__(self):
        self.supported_extensions = ['.txt', '.py', '.md', '.csv']
    
    def get_filename_from_user(self) -> str:
        """Get filename from user input with validation."""
        while True:
            try:
                filename = input("\nEnter the filename to read (or 'quit' to exit): ").strip()
                
                if filename.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    sys.exit(0)
                
                if not filename:
                    print("Filename cannot be empty. Please try again.")
                    continue
                
                return filename
                
            except (EOFError, KeyboardInterrupt):
                print("\n\nGoodbye!")
                sys.exit(0)
    
    def validate_file(self, filename: str) -> tuple[bool, str]:
        """Validate if the file exists and can be read."""
        if not os.path.exists(filename):
            return False, f"File '{filename}' does not exist."
        
        if not os.path.isfile(filename):
            return False, f"'{filename}' is not a file (it might be a directory)."
        
        if not os.access(filename, os.R_OK):
            return False, f"File '{filename}' exists but cannot be read (permission denied)."
        
        # Check file size
        try:
            file_size = os.path.getsize(filename)
            if file_size == 0:
                return False, f"File '{filename}' is empty."
            if file_size > 10 * 1024 * 1024:  # 10MB limit
                return False, f"File '{filename}' is too large ({file_size / (1024*1024):.1f}MB)."
        except OSError:
            return False, f"Cannot access file '{filename}' properties."
        
        return True, f"File '{filename}' is valid and ready to read."
    
    def read_file_content(self, filename: str) -> tuple[bool, str, Optional[str]]:
        """Read file content with error handling."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                return True, f"Successfully read '{filename}' ({len(content)} characters)", content
                
        except UnicodeDecodeError:
            # Try with different encodings
            encodings = ['latin-1', 'cp1252', 'iso-8859-1']
            for encoding in encodings:
                try:
                    with open(filename, 'r', encoding=encoding) as file:
                        content = file.read()
                        return True, f"Successfully read '{filename}' with {encoding} encoding ({len(content)} characters)", content
                except UnicodeDecodeError:
                    continue
            
            return False, f"Cannot read '{filename}' - unsupported file encoding.", None
            
        except PermissionError:
            return False, f"Permission denied when reading '{filename}'.", None
        except OSError as e:
            return False, f"OS error when reading '{filename}': {e}", None
        except Exception as e:
            return False, f"Unexpected error when reading '{filename}': {e}", None
    
    def modify_content(self, content: str, filename: str) -> str:
        """Modify the file content with various transformations."""
        print(f"\n🔧 Modifying content from '{filename}'...")
        
        # Apply various modifications
        modified_content = content
        
        # Add header with file info
        header = f"# Modified version of: {filename}\n"
        header += f"# Original length: {len(content)} characters\n"
        header += f"# Modification timestamp: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        header += "=" * 50 + "\n\n"
        
        modified_content = header + modified_content
        
        # Count and display statistics
        lines = content.split('\n')
        words = content.split()
        chars = len(content)
        
        stats = f"\nFile Statistics:\n"
        stats += f"   Lines: {len(lines)}\n"
        stats += f"   Words: {len(words)}\n"
        stats += f"   Characters: {chars}\n"
        stats += f"   Average words per line: {len(words)/len(lines):.1f}\n"
        
        print(stats)
        
        return modified_content
    
    def write_modified_file(self, original_filename: str, modified_content: str) -> tuple[bool, str]:
        """Write modified content to a new file."""
        # Generate output filename
        name, ext = os.path.splitext(original_filename)
        output_filename = f"{name}_modified{ext}"
        
        # Ensure unique filename
        counter = 1
        while os.path.exists(output_filename):
            output_filename = f"{name}_modified_{counter}{ext}"
            counter += 1
        
        try:
            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write(modified_content)
            
            return True, f"Successfully wrote modified content to '{output_filename}'"
            
        except PermissionError:
            return False, f"Permission denied when writing to '{output_filename}'"
        except OSError as e:
            return False, f"OS error when writing to '{output_filename}': {e}"
        except Exception as e:
            return False, f"Unexpected error when writing to '{output_filename}': {e}"
    
    def display_file_preview(self, content: str, max_lines: int = 10) -> None:
        """Display a preview of the file content."""
        lines = content.split('\n')
        
        print(f"\nFile Preview (showing first {min(max_lines, len(lines))} lines):")
        print("-" * 50)
        
        for i, line in enumerate(lines[:max_lines]):
            line_num = i + 1
            preview = line[:80] + "..." if len(line) > 80 else line
            print(f"{line_num:3d}: {preview}")
        
        if len(lines) > max_lines:
            print(f"      ... and {len(lines) - max_lines} more lines")
        
        print("-" * 50)
    
    def run(self):
        """Main program loop."""
        print("File Manager - Read, Modify & Write Challenge")
        print("=" * 50)
        print("This program will:")
        print("• Read a file you specify")
        print("• Show you a preview of its contents")
        print("• Create a modified version")
        print("• Save the modified version to a new file")
        print("• Handle any errors gracefully")
        
        while True:
            try:
                # Get filename from user
                filename = self.get_filename_from_user()
                
                # Validate file
                is_valid, validation_message = self.validate_file(filename)
                print(validation_message)
                
                if not is_valid:
                    continue
                
                # Read file content
                success, read_message, content = self.read_file_content(filename)
                print(read_message)
                
                if not success:
                    continue
                
                # Display file preview
                self.display_file_preview(content)
                
                # Ask user if they want to proceed
                proceed = input("\nDo you want to create a modified version? (y/n): ").strip().lower()
                if proceed not in ['y', 'yes', '']:
                    print("⏭Skipping modification.")
                    continue
                
                # Modify content
                modified_content = self.modify_content(content, filename)
                
                # Write modified file
                write_success, write_message = self.write_modified_file(filename, modified_content)
                print(write_message)
                
                if write_success:
                    print(f"Success! Your modified file has been created.")
                    
                    # Ask if user wants to see the modified file
                    show_modified = input("\nWould you like to see the modified file? (y/n): ").strip().lower()
                    if show_modified in ['y', 'yes']:
                        self.display_file_preview(modified_content, 15)
                
                # Ask if user wants to process another file
                another = input("\nProcess another file? (y/n): ").strip().lower()
                if another not in ['y', 'yes', '']:
                    print("Thanks for using File Manager!")
                    break
                    
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"\nAn unexpected error occurred: {e}")
                print("Let's try again...")
                continue

def main():
    """Main entry point."""
    try:
        file_manager = FileManager()
        file_manager.run()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
    except Exception as e:
        print(f"\nFatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
