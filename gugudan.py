def gugudan():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")


def print_end(end_message):
    print(end_message)


if __name__ == "__main__":
    gugudan()

    end_message = "This is end."
    print_end(end_message)
