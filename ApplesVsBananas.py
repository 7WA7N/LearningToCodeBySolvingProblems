apple_threepoint = 3 * int(input('Enter Number of Three Point Shots by Apples: '))
apple_twopoint = 2 * int(input('Enter Number of Two Point Shots by the Apples: '))
apple_onepoint = 1 * int(input('Enter Number of One Point Free Throws by the Apples: '))
banana_threepoint = 3 * int(input('Enter Number of Three Point Shots by Bananas: '))
banana_twopoint = 2 * int(input('Enter Number of Two Point Shots by the Bananas: '))
banana_onepoint = 1 * int(input('Enter Number of One Point Free Throws by the Bananas: '))

apple_total = apple_threepoint + apple_onepoint + apple_twopoint
banana_total = banana_threepoint + banana_onepoint + banana_twopoint

if apple_total > banana_total:
    print(f'Apples have won the game by {apple_total - banana_total} points.')
elif banana_total > apple_total:
    print(f'Bananas have won the game by {banana_total - apple_total} points.')
elif banana_total == apple_total:
    print('Game has resulted in a draw.')
