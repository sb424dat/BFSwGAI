def last_transactions(user_transactions: list, transaction: str, max: int
= 3) -> list: #A
    """
    Adds a transaction to the list of user transactions and returns the
    updated list.
    :param max_length: Maximum transactions to keep
    :param user_transactions: List of current transactions
    :param transaction: New transaction
    :return: Updated list of transactions
    """
    if len(user_transactions) + 1 >= max:
        user_transactions.pop(0)
    #B
    #B
    user_transactions.append(transaction)#C
    return user_transactions#D

