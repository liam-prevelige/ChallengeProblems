# Zack Gottesman, Will McCall, & Liam Prevelige
# Solution to problem 1 of voluntary coding assignment: "A Number Picking Game"

from random import randint


"""
Determine the largest possible minimum score for Alice in a number picking game
Input: List A of even number of integers
Output: Largest number W guaranteed to Alice
"""
def max_W(A):
    n = len(A)

    # Create 2x2 matrices to dynamically store scores and moves for different possibilities of A
    # Table[i][j] represents the respective value for the list of numbers from sublist of A = A[i:j+1]
    scores = [[0 for x in range(n)] for i in range(n)]
    moves = [["" for x in range(n)] for i in range(n)]

    for sub_length in range(n+1):   # every possible length sublist - O(n)
        for i in range(n - sub_length):     # iterate over all possible start index for current sub_length - O(n)
            j = i + sub_length      # every possible end index for sublist of length sub_length
            lr = ll = rr = 0

            # Score for Alice choosing left num and Bob choosing right num, or vice versa
            if i+1 <= j-1 < n:
                lr = scores[i+1][j-1]

            # Score for both Alice and Bob choosing left num
            if i+2 <= j < n:
                ll = scores[i+2][j]

            # Score for both Alice and Bob choosing right num
            if i <= j-2 < n:
                rr = scores[i][j-2]

            # Determine worst possible score for next round depending on left or right pick
            min_gain_l = min(lr, ll)
            min_gain_r = min(lr, rr)

            # Total gain should include worst-case for next round of picking and score of current pick
            total_gain_l = min_gain_l + A[i]
            total_gain_r = min_gain_r + A[j]

            # Compare value of left vs right pick against perfect opponent, choose larger of the two
            if total_gain_l > total_gain_r:
                moves[i][j] = "l"   # left is better, so store this move for sublist A[i:j+1]
                scores[i][j] = total_gain_l
            else:
                moves[i][j] = "r"   # right is better, so store this move for sublist A[i:j+1]
                scores[i][j] = total_gain_r

    return scores[0][n-1], moves    # return best possible score for perfect opponent and the moves for each sublist


"""
Create an interactive number-picking game where a user plays against the computer (Alice).
No matter what moves the user makes, Alice will always have a score >= the best possible score given a perfect opponent.
"""
def interactive_game():
    print("Let's play a number picking game! \n")

    try:
        number_count = int(input("How many numbers do you want to play with (max 20)? \nPlease type an even integer > "
                                 "0: "))
    except Exception as e:  # reached after casting error - input not an integer
        number_count = -1   # default value of -1 will prompt user for input again

    while number_count % 2 != 0 or number_count < 1:    # keep asking for input until even integer greater than 0 given
        print("Oops, please type an even integer!")
        try:
            number_count = int(input("How many numbers do you want to play with (max 50)? \nPlease type an even "
                                     "integer > 0: "))
        except Exception as e:  # reached after casting error - input not an integer
            number_count = -1   # default value of -1 will prompt user for input again

    number_count = int(number_count)
    if number_count > 50:   # set a limit so runtime and gameplay is relatively short
        print("Input exceeds limit - set to maximum number count: 50")
        number_count = 50

    number_arr = [0 for x in range(number_count)]
    for i in range(number_count):
        number_arr[i] = randint(-9, 9)  # use a randomly generated list of integers for game of inputted length

    alice_score, alice_moves = max_W(number_arr)    # get  max score against perfect opponent & moves for Alice
    print("\nLet's get started! Here's the list of numbers to choose from:")
    print(number_arr)
    print("You are playing against Alice, who will get a minimum score of " + str(alice_score))

    i = 0
    j = number_count - 1

    alice_cscore = 0    # score for Alice based on current round
    user_cscore = 0     # score for user (aka Bob) based on current round

    while i < j:    # keep going until no more numbers left to choose (note that i==j is checked below)
        if alice_moves[i][j] == "l":
            print("\nAlice's move. She chooses the leftmost number: " + str(number_arr[i]))
            alice_cscore += number_arr[i]
            i += 1  # number_arr[i] is no longer an option, so increment
        else:
            print("\nAlice's move. She chooses the rightmost number: " + str(number_arr[j]))
            alice_cscore += number_arr[j]
            j -= 1  # number_arr[j] is no longer an option, so increment

        print("Alice's current score: " + str(alice_cscore))
        print("Alice's final score will still equal or exceed: " + str(alice_score))

        print("\nRemaining numbers to choose from: ")
        print(number_arr[i:j+1])

        if i < j:
            user_move = input("\nYour move! Type 'l' to choose left number or 'r' to choose right number: ")

            while user_move != "l" and user_move != "r":
                user_move = input("Invalid selection. Please type 'l' or 'r' for left or right number respectively: ")

            if user_move == "l":
                print("You chose " + str(number_arr[i]))
                user_cscore += number_arr[i]
                i += 1  # number_arr[i] is no longer an option, so increment
            else:
                print("You chose " + str(number_arr[j]))
                user_cscore += number_arr[j]
                j -= 1  # number_arr[j] is no longer an option, so increment

            print("Your current score is " + str(user_cscore))
        else:   # i==j, so only one number left to choose
            print("Your move! Only one number left, so you choose: " + str(number_arr[i]))
            user_cscore += number_arr[i]

    print("\nAlice's final score: " + str(alice_cscore) + " which equals or exceeds " + str(alice_score))
    print("Your final score: " + str(user_cscore))

    if alice_cscore > user_cscore:
        print("Alice wins!")
    elif user_cscore > alice_cscore:
        print("You win!")
    else:
        print("It's a tie!")


interactive_game()
