from models.calculate import Calculate


def main() -> None:
    score: int = 0
    play(score)


def play(score: int) -> None:
    difficulty: int = int(input('Insert the difficulty level (1, 2, 3, 4): '))

    calc: Calculate = Calculate(difficulty)

    print('Insert the result for the following operation: ')
    calc.show_operation()

    result: int = int(input())

    if calc.check_result(result):
        score += 1
        print(f'You have {score} pts')

    continuar: int = int(input('Want to continue? (1 - Yes, 0 - No): '))

    if continuar:
        play(score)
    else:
        print(f'You finished the game with {score} pts')


if __name__ == '__main__':
    main()
