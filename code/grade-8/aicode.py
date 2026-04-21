import sys

# aicode.py -- Tower of Hanoi solver (recursive)

def hanoi(n, source='A', target='C', auxiliary='B', moves=None):
    """Return list of moves to solve Tower of Hanoi with n disks.
    Each move is a tuple (from_peg, to_peg)."""
    if moves is None:
        moves = []
    if n <= 0:
        return moves
    hanoi(n - 1, source, auxiliary, target, moves)
    moves.append((source, target))
    hanoi(n - 1, auxiliary, target, source, moves)
    return moves

def print_moves(moves):
    for i, (frm, to) in enumerate(moves, start=1):
        print(f"{i:>3}: move from {frm} -> {to}")
    print(f"\nTotal moves: {len(moves)}")

if __name__ == "__main__":
    try:
        n = int(sys.argv[1]) if len(sys.argv) > 1 else int(input("Number of disks (default 3): ") or 3)
    except ValueError:
        print("Invalid number, using 3.")
        n = 3
    moves = hanoi(n)
    print_moves(moves)