from n1d import N1D

def main():
    print(N1D(-1, 2))  # [1.0, 0.0]
    print(N1D(0, 2))   # [0.5, 0.5]
    print(N1D(1, 2))   # [0.0, 1.0]

    print(N1D(-1, 3))  # [1.0, 0.0, 0.0]
    print(N1D(0, 3))   # [0.0, 1.0, 0.0]
    print(N1D(1, 3))   # [0.0, 0.0, 1.0]

if __name__ == "__main__":
    main()
