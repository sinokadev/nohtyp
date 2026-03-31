import sys
import os

def run_reversed_yp():
    if len(sys.argv) < 2:
        print("Usage: python nohtyp.py <filename.yp>")
        return

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return
    
    if not file_path.lower().endswith('.yp'):
        print("Error: Only .yp files are supported.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            source_code = ""
            for line in lines:
                content = line.rstrip('\n\r')
                source_code += content[::-1] + "\n"
            
            exec(source_code)

    except Exception as e:
        print(f"Runtime Error: {e}")

if __name__ == "__main__":
    run_reversed_yp()
