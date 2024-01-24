def echo(text: str, repetitions: int = 3) -> str:
    result = []
    for i in range(repetitions, 0, -1):
        result.append(text[-i:])
    return '\n'.join(result) + '\n.'

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))