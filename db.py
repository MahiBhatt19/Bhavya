from neo4j import GraphDatabase

URI = "bolt://localhost:7687"

driver = GraphDatabase.driver(URI)

def get_session():
    return driver.session()
