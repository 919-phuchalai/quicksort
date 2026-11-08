import sys
from quicksort import sort_numbers

def main():
    try:
        input_data = sys.stdin.read().split()
        if not input_data:
            sys.stdout.write("-1\n")
            return
        
        n = int(input_data[0])
        elements = [int(x) for x in input_data[1:]]
        
        # Kiểm tra tính toàn vẹn dữ liệu: số lượng phần tử phải khớp với N
        if n < 0 or len(elements) != n:
            sys.stdout.write("-1\n")
            return
            
        sort_numbers(elements)
        sys.stdout.write(" ".join(map(str, elements)) + "\n")
    except Exception:
        sys.stdout.write("-1\n")

if __name__ == "__main__":
    main()
