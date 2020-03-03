import pymongo


def test_assertion():
    # GIVEN a variable
    a = 1
    # WHEN checking if integer

    # THEN assert it is a integer
    assert isinstance(a, int)


def test_mongodb():
    # GIVEN a client
    client = pymongo.MongoClient()
    # WHEN creating a database and inserting into collection
    db = client.test
    post = {"name": "Me"}
    db.person.insert_one(post)
    # THEN assert the doc is there
    res = db.person.find_one()
    assert res["name"] == post["name"]
