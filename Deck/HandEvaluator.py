from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):

    rank_counts = {}
    for card in hand:
        if card.rank in rank_counts:
            rank_counts[card.rank] += 1
        else:
            rank_counts[card.rank] = 1


    counts = []
    for r in rank_counts:
        counts.append(rank_counts[r])


    counts.sort()
    counts = counts[::-1]   # invertir lista

    suit_counts = {}
    for card in hand:
        if card.suit in suit_counts:
            suit_counts[card.suit] += 1
        else:
            suit_counts[card.suit] = 1

    # Verificar si hay flush
    flush = False
    for s in suit_counts:
        if suit_counts[s] >= 5:
            flush = True


    # Lista de ranks sin duplicados
    unique_ranks = []
    for card in hand:
        if card.rank not in unique_ranks:
            unique_ranks.append(card.rank)


    unique_ranks.sort()

    # Ace bajo
    if Rank.ACE in unique_ranks:
        unique_ranks.append(1)

    # Detectar 5 consecutivos
    straight = False
    in_row = 1
    i = 1
    while i < len(unique_ranks):
        if unique_ranks[i] == unique_ranks[i - 1] + 1:
            in_row += 1
            if in_row == 5:
                straight = True
        else:
            in_row = 1
        i += 1

    # ----- Straight Flush -----
    if flush and straight:
        return "Straight Flush"

    # ----- Resto de las jugadas -----
    if counts[0] == 4:
        return "Four of a Kind"

    if counts[0] == 3:
        # Buscar si hay un par
        found_pair = False
        j = 1
        while j < len(counts):
            if counts[j] == 2:
                found_pair = True
            j += 1
        if found_pair:
            return "Full House"

    if flush:
        return "Flush"

    if straight:
        return "Straight"

    if counts[0] == 3:
        return "Three of a Kind"

    # Contar pares
    pair_count = 0
    k = 0
    while k < len(counts):
        if counts[k] == 2:
            pair_count += 1
        k += 1

    if pair_count >= 2:
        return "Two Pair"

    if counts[0] == 2:
        return "One Pair"

    return "High Card"