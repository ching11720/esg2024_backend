# /project_management/member

<details>
<summary><code>GET</code> <code><b>/{}</b></code> <code>(Get all employees)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Responses

| http code | content-type       | description                                                                                                                                          |
| --------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `200`     | `application/json` | the list of all employees (form: `{'EID': (str), 'name': (str), 'gender': (int), 'email': (str), 'phone': (str), 'nation': (str), 'status': (int)}`) |
| `500`     | `text/plain`       | `{'Error': 'server error'}`                                                                                                                          |

</details>

<details>
<summary><code>POST</code> <code><b>/</b></code> <code>(Create an member)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Body

| key         | required | data type | description                                                                    |
| ----------- | -------- | --------- | ------------------------------------------------------------------------------ |
| PID         | true     | string    | id of the project                                                              |
| EID         | true     | string    | the EID of the member                                                          |
| position    | true     | string    |                                                                                |
| role_on_sys | true     | string    | what content can this employee access in the system (admin, member, read_only) |

##### Responses

| http code | content-type       | description                                                                                                           |
| --------- | ------------------ | --------------------------------------------------------------------------------------------------------------------- |
| `201`     | `application/json` | `{'message': 'Member added successfully!','data': {'EID': (str), 'PID': (str), position: (str),'role_on_sys':(str)}}` |
| `400`     | `text/plain`       | `{'Error': error massage}`                                                                                            |
| `500`     | `text/plain`       | `{'Error': 'server error'}`                                                                                           |

</details>

<details>
<summary><code>PUT</code> <code><b>/{PID}/{EID}</b></code> <code>(Revise an member)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Path Parameters

| key | required | data type | description           |
| --- | -------- | --------- | --------------------- |
| PID | true     | string    | id of the project     |
| EID | true     | string    | the EID of the member |

##### Body

| key         | required | data type | description                                                                    |
| ----------- | -------- | --------- | ------------------------------------------------------------------------------ |
| PID         | true     | string    | id of the project                                                              |
| EID         | true     | string    | the EID of the member                                                          |
| position    | true     | string    |                                                                                |
| role_on_sys | true     | string    | what content can this employee access in the system (admin, member, read_only) |

##### Responses

| http code | content-type | description                                                                                                                |
| --------- | ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| `200`     | `text/plain` | `{'message': 'Member updated successfully!', 'data': {'EID': (str), 'PID': (str), 'position': (str),'role_on_sys':(str)}}` |
| `400`     | `text/plain` | `{'Error': 'client error'}`                                                                                                |
| `404`,    | `text/plain` | `{'Error': 'Member not found'}`                                                                                            |
| `500`     | `text/plain` | `{'Error': 'server error'}`                                                                                                |

</details>

<details>
<summary><code>DELETE</code> <code><b>/{PID}/{EID}</b></code> <code>(Remove an member)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Path Parameters

| key | required | data type | description           |
| --- | -------- | --------- | --------------------- |
| PID | true     | string    | id of the project     |
| EID | true     | string    | the EID of the member |

##### Responses

| http code | content-type | description                                 |
| --------- | ------------ | ------------------------------------------- |
| `204`     | `text/plain` | `'message': 'Member deleted successfully!'` |
| `404`     | `text/plain` | `{'Error': 'Member not found'}`             |
| `500`     | `text/plain` | `{'Error': 'server error'}`                 |

</details>

<details>
<summary><code>GET</code> <code><b>/{PID}/{EID}</b></code> <code>(Retrieve the detail of an member)</code></summary>

<br />only for admin

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Path Parameters

| key | required | data type | description           |
| --- | -------- | --------- | --------------------- |
| PID | true     | string    | id of the project     |
| EID | true     | string    | the EID of the member |

##### Responses

| http code | content-type       | description                                                           |
| --------- | ------------------ | --------------------------------------------------------------------- |
| `200`     | `application/json` | `{'EID': (str), 'PID': (str), 'position': (str),'role_on_sys':(str)}` |
| `404`,    | `text/plain`       | `{'Error': 'Member not found'}`                                       |
| `500`     | `text/plain`       | `{'Error': 'server error'}`                                           |

</details>

<details>
<summary><code>GET</code> <code><b>/{PID}</b></code> <code>(Retrieve the detail of all member in specific project)</code></summary>

<br />only for admin

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Path Parameters

| key | required | data type | description       |
| --- | -------- | --------- | ----------------- |
| PID | true     | string    | id of the project |

##### Responses

| http code | content-type       | description                                                                                                                                  |
| --------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `200`     | `application/json` | the list of employee (form: `{'EID': (str), 'name': (str), 'PID': (str), 'gender': (int), 'email': (str), 'phone': (str), 'nation': (str)}`) |
| `404`,    | `text/plain`       | `{'Error': "There's no member in this project"}`                                                                                             |
| `500`     | `text/plain`       | `{'Error': 'server error'}`                                                                                                                  |

</details>
