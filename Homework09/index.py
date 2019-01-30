import codeskulptor
codeskulptor.set_timeout(20)


def gen_all_sequences(outcomes, length):
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):

    hand_score = []
    for dice_value in hand:
        hand_score.append(hand.count(dice_value) * dice_value)
    return max(hand_score)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    possible_hands = []

    value = 0

    possible_rolls = (gen_all_sequences(
        (range(1, (num_die_sides + 1))), num_free_dice))

    for roll in possible_rolls:
        possible_hands.append(held_dice + roll)

    for hand in possible_hands:
        value += (float(score(hand)) / len(possible_hands))

    return value


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.


    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    all_holds_set = set([()])
    for dice_value in hand:
        hold_set = all_holds_set.copy()
        for hold in hold_set:
            temp = list(hold)
            temp.append(dice_value)
            tempp = sorted(temp)
            all_holds_set.add(tuple(temp))

    return all_holds_set


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_holds = gen_all_holds(hand)
    max_value = 0.0
    best_hold = ()
    for held_dice in all_holds:
        num_free_dice = len(hand) - len(held_dice)
        value = expected_value(held_dice, num_die_sides, num_free_dice)
        if value > max_value:
            best_hold = held_dice
            max_value = value
    return (max_value, best_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print("Best strategy for hand", hand, "is to hold", hold,
          "with expected score", hand_score)


run_example()
