test ={
    "ok": True,
    "channel": {
        "id": "C024BE91L",
        "name": "fun",

        "created": 1360782804,
        "creator": "U024BE7LH",

        "is_archived": False,
        "is_general": False,
        "is_member": True,
        "is_starred": True,

        "members": [ "dan" ],

        "topic": { ... },
        "purpose": { ... },

        "last_read": "1401383885.000061",
        "latest": { ... },
        "unread_count": 0,
        "unread_count_display": 0
    }
}

swag = (test["channel"])
print (swag["members"])
