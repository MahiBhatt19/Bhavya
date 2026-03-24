def create_transaction(tx, sender, receiver, amount, timestamp):
    query = """
    MERGE (a:Account {id: $sender})
    MERGE (b:Account {id: $receiver})
    CREATE (a)-[:TRANSACTED {
        amount: $amount,
        timestamp: $timestamp
    }]->(b)
    """
    tx.run(query, sender=sender, receiver=receiver, amount=amount, timestamp=timestamp)
