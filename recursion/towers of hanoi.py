"""
Wrire a recursive function for towers of hanoi
"""


def towers_of_hanoi(n: int, from_rode: str, to_rode: str, aux_rode: str) -> None:
    if n == 0:
        return

    towers_of_hanoi(n-1, from_rode, aux_rode, to_rode)
    print(f"disk - {n}, from rode {from_rode} to rode {to_rode}")
    towers_of_hanoi(n-1, aux_rode, to_rode, from_rode)


N = 4
towers_of_hanoi(N, 'A', 'C', 'B')
