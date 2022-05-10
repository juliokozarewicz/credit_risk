from pymongo import MongoClient


def copy_db():
    client = MongoClient('mongodb://localhost:27017')

    client.drop_database('credit_risk')

    db_copy = list(client['db_credit_risk_bkp']['credit_risk'].find())

    collection_reinsert = client['credit_risk']['credit_risk']

    collection_reinsert.insert_many(db_copy)


copy_db()
