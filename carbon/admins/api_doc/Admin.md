# Login

#### /login
| method | input                                                | output                                            |                 |
| ------ | ---------------------------------------------------- | ------------------------------------------------- | --------------- |
| POST   | {"username": "022020112701", "password": "UgNMKDNg"} | {"success": True, "JWT": "", "first_login": True} |                 |
                                                  

#### /login/revise_password
| method | input                                                | output            |                            |
| ------ | ---------------------------------------------------- | ----------------- | -------------------------- |
| POST   | {"UID": "", "old_password": "", "newPw": ""}         | {'success': True} | revise the user's password |

# Admin

#### /admins/user/
|         | method | input                                                | output            |                            |
|-------- | ------ | ---------------------------------------------------- | ----------------- | -------------------------- |
| /create | POST   | {"UID": "", "old_password": "", "newPw": ""}         | {'success': True} |                            |

#### /admins/assign_access
| method | input                              | output            |                                     |
| ------ | ---------------------------------- | ----------------- | ----------------------------------- |
| PUT    | {"name": "", "access": ""}         | {'success': True} | access: admin, member or RO(string) |

#### /admins/project
|         | method | input                         | output                                     |                            |
|-------- | ------ | ----------------------------- | ------------------------------------------ | -------------------------- |
| /create | POST   | {"projectName":"", "PMID":""} | {'projectName': "", 'PID': "", 'PMID': ""} |                            |

#### /admins/employee

|           | method   | input                         | output                                     |                            |
|---------- | -------- | ----------------------------- | ------------------------------------------ | -------------------------- |
| /create   | POST     | {"name":"", "gender":1, "phone":"", "email":"", "nation":"", "PID":""} | {'success': True, 'EID': ""}| gender: 1 or 2(int), email: @xxx.com |
| /delete   | DELETE   | {"EID":"", "region":"", "nation": "", "name": "", "PID": ""} | {'name': "", 'gender': "", 'phone': "", 'email': "", 'nation': "", 'status': 1} | inputs can be none |
| /retrieve | GET      | {"EID":"", "region":"", "nation": "", "name": "", "PID": ""} | {'name': "", 'gender': "", 'phone': "", 'email': "", 'nation': "", 'status': 1} | inputs can be none |
| /revise   | PUT      | {"EID":""} | {'success': True} |                            |