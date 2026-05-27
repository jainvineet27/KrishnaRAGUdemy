import sys
def main(load_type: str = 'full'):
    print("Hello from krishnaikragudemy!")
    print('this is vineet...')


if __name__ == "__main__":
    load_type = sys.argv[1] if len(sys.argv) > 1 else "full"
    print(f"Loading with type: {load_type}")
    main(load_type)
