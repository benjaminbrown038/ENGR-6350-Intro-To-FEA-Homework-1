from b1d import B1D

def main():
    print(B1D(-1, 2))  # [-0.5, 0.5]
    print(B1D(0, 2))   # [-0.5, 0.5]
    print(B1D(1, 2))   # [-0.5, 0.5]
    print(B1D(0.0, 3)) # [ -0.5, 0.0, 0.5 ]

if __name__ == "__main__":
    main()
