"""
Entrypoint xử lý nhập/xuất chuẩn (StdIn / StdOut) cho bài toán
Sắp xếp điểm số tuyển sinh Đại học FPT bằng QuickSort.
"""
import sys
from quicksort import sort_candidates

def main():
    try:
        raw_text = sys.stdin.read().strip()
        if not raw_text:
            return

        tokens = raw_text.split()
        if not tokens:
            return

        n = int(tokens[0])
        candidate_tokens = tokens[1:]

        # Mỗi thí sinh gồm đúng 2 token: mã thí sinh và điểm số
        candidates = []
        for i in range(min(n, len(candidate_tokens) // 2)):
            cid = candidate_tokens[i * 2]
            score = float(candidate_tokens[i * 2 + 1])
            candidates.append((cid, score))

        sort_candidates(candidates)

        # Định dạng output: Mỗi dòng gồm Mã thí sinh và Điểm số làm tròn 2 chữ số thập phân
        output_lines = [f"{cid} {score:.2f}" for cid, score in candidates]
        sys.stdout.write("\n".join(output_lines) + "\n")
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")

if __name__ == "__main__":
    main()
