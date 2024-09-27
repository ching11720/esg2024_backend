# /project_management/daily_record

<details>
<summary><code>POST</code> <code><b>/</b></code> <code>(Create a daily record)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Body
| key                | required | data type | description                                         |
| ------------------ | -------- | --------- | --------------------------------------------------- |
| PID                | true     | string    | the id of the project                               |
| PN                 | true     | string    | the part number of the product                      |
| date               | true     | date      | the date of the daily record                        |
| runtime            | false    | float     | equipment runtime of that day, unit: hr             |
| amount             | true     | float     | the amount of material used that day                |
| unit               | true     | string    | the unit of material                                |
##### Responses
| http code    | content-type         | description                        |
| ------------ | -------------------- | ---------------------------------- |
| `201`        | `application/json`   | `{'message': 'Record added successfully!','data': {'dailyID':(int),'PID': (str), 'PN': (str), 'date': (str), 'runtime': (float), 'amount': (float), 'unit': (str)}}`|
| `400`        | `text/plain`         | `{'Error': error massage}`         |
| `500`        | `text/plain`         | `{'Error': 'server error'}`        |
</details>

<details>
<summary><code>PUT</code> <code><b>/{PID}/{date}</b></code> <code>(Raise a requirement of revising a daily record)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key  | required | data type | description                    |
| ---- | -------- | --------- | ------------------------------ |
| PID  | true     | string    | the id of the project          |
| date | true     | date      | the date of the daily record   |
##### Body
| key                | required | data type | description                              |
| ------------------ | -------- | --------- | ---------------------------------------- |
| PID                | true     | string    | the id of the project                    |
| PN                 | true     | string    | the part number of the product           |
| date               | true     | date      | the date of the daily record             |
| runtime            | false    | float     | equipment runtime of that day, unit: hr  |
| amount             | false    | float     | the amount of material used that day     |
| unit               | false    | string    | the unit of material                     |
##### Responses
| http code    | content-type       | description                                   |
| ------------ | ------------------ | --------------------------------------------- |
| `200`        | `application/json` | `{'message': 'Record updated successfully!', 'data': {'PID': (str), 'PN': (str), 'date': (str), 'runtime': (float), 'amount': (float), 'unit': (str)}}` |
| `400`        | `text/plain`       | `{'Error': 'client error'}`                   |
| `404`        | `text/plain`       | `{'Error': 'Record not found'}`               |
| `500`        | `text/plain`       | `{'Error': 'server error'}`                   |

</details>

<details>
<summary><code>GET</code> <code><b>/{PID}/{date}</b></code> <code>(Retrieve the detail of a daily records)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key  | required | data type | description                         |
| ---- | -------- | --------- | ----------------------------------- |
| PID  | true     | string    | the id of the project               |
| date | true     | date      | the date of the daily record        |
##### Responses
| http code    | content-type       | description                                 |
| ------------ | ------------------ | ------------------------------------------- |
| `200`        | `application/json` | the list of daily records (form: `{'PID': (str), 'PN': (str), 'date': (str), 'runtime': (float), 'amount': (float), 'unit': (str)}`) |
| `400`        | `text/plain`       | `{'Error': 'client error'}`                 |
| `404`        | `text/plain`       | `{'Error': 'Record not found'}`             |
| `500`        | `text/plain`       | `{'Error': 'server error'}`                 |

</details>

# /project_management/flow
flow's form example: `[
    {"step": 1, "equipments": [{"PN": "06xxxx", "amount": 1, "unit": "unit"}], "materials": [{"PN": "06xxxx", "amount": 1, "unit": "kg"}], "description": "Initial setup and preparation"}, 
    {"step": 2, .....}]`
<details>
<summary><code>GET</code> <code><b>/{PID}</b></code> <code>(Get a flow of a project)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key | required | data type | description                           |
| --- | -------- | --------- | ------------------------------------- |
| PID | true     | string    | the pid which is wanted to be posed   |
##### Responses
| http code    | content-type         | description                                |
| ------------ | -------------------- | ------------------------------------------ |
| `200`        | `text/plain`         | `{'PID': (str), 'flow': (json)}`           |
| `401`        | `text/plain`         | `{'Error': 'PID is invalid'}`              |
| `500`        | `text/plain`         | `{'Error': 'server error'}`                |
</details>

<details>
<summary><code>PUT</code> <code><b>/{PID}</b></code> <code>(Revise or add a flow of a project)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key | required | data type | description                           |
| --- | -------- | --------- | ------------------------------------- |
| PID | true     | string    | the pid which is wanted to be revised |
##### Body
| key  | required | data type | description                              |
| ---- | -------- | --------- | ---------------------------------------- |
| PID  | true     | string    | the pid which is wanted to be revised    |
| flow | true     | json      | the flow of the project                  |
##### Responses
| http code    | content-type | description                              |
| ------------ | -------------| ---------------------------------------- |
| `200`        | `text/plain` | `{'message': "Flow added successfully!", 'data': {'PID': (str), 'flow': (json)}}` |
| `400`        | `text/plain` | `{'Error': error massage}`               |
| `401`        | `text/plain` | `{'Error': 'PID is invalid'}`            |
| `500`        | `text/plain` | `{'Error': 'server error'}`              |

</details>

# /project_management/member

<details>
<summary><code>GET</code> <code><b>/{}</b></code> <code>(Get all employees)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Responses
| http code    | content-type         | description                        |
| ------------ | -------------------- | ---------------------------------- |
| `200`        | `application/json`   | the list of all employees (form: `{'EID': (str), 'name': (str), 'gender': (int), 'email': (str), 'phone': (str), 'nation': (str), 'status': (int)}`) |
| `500`        | `text/plain`         | `{'Error': 'server error'}`        |
</details>

<details>
<summary><code>POST</code> <code><b>/</b></code> <code>(Create an member)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Body
| key         | required | data type | description                                         |
| ----------- | -------- | --------- | --------------------------------------------------- |
| PID         | true     | string    | id of the project                                   |
| EID         | true     | string    | the EID of the member                               |
| position    | true     | string    |                                                     |
| role_on_sys | true     | string    | what content can this employee access in the system (admin, member, read_only) |
##### Responses
| http code    | content-type         | description                        |
| ------------ | -------------------- | ---------------------------------- |
| `201`        | `application/json`   | `{'message': 'Member added successfully!','data': {'EID': (str), 'PID': (str), position: (str),'role_on_sys':(str)}}`    |
| `400`        | `text/plain`         | `{'Error': error massage}`         |
| `500`        | `text/plain`         | `{'Error': 'server error'}`        |
</details>

<details>
<summary><code>PUT</code> <code><b>/{PID}/{EID}</b></code> <code>(Revise an member)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key      | required | data type | description           |
| -------- | -------- | --------- | --------------------- |
| PID      | true     | string    | id of the project     |
| EID      | true     | string    | the EID of the member |
##### Body
| key         | required | data type | description                                         |
| ----------- | -------- | --------- | --------------------------------------------------- |
| PID         | true     | string    | id of the project                                   |
| EID         | true     | string    | the EID of the member                               |
| position    | true     | string    |                                                     |
| role_on_sys | true     | string    | what content can this employee access in the system (admin, member, read_only) |
##### Responses
| http code    | content-type | description                                  |
| ------------ | -------------| -------------------------------------------- |
| `200`        | `text/plain` | `{'message': 'Member updated successfully!', 'data': {'EID': (str), 'PID': (str), 'position': (str),'role_on_sys':(str)}}`|
| `400`        | `text/plain` | `{'Error': 'client error'}`                  |
| `404`,       | `text/plain` | `{'Error': 'Member not found'}`              |
| `500`        | `text/plain` | `{'Error': 'server error'}`                  |

</details>

<details>
<summary><code>DELETE</code> <code><b>/{PID}/{EID}</b></code> <code>(Remove an member)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key      | required | data type | description                              |
| -------- | -------- | --------- | ---------------------------------------- |
| PID      | true     | string    | id of the project                        |
| EID      | true     | string    | the EID of the member                    |
##### Responses
| http code    | content-type | description                                 |
| ------------ | -------------| -------------------------------------       |
| `204`        | `text/plain` | `'message': 'Member deleted successfully!'` |
| `404`        | `text/plain` | `{'Error': 'Member not found'}`             |
| `500`        | `text/plain` | `{'Error': 'server error'}`                 |

</details>

<details>
<summary><code>GET</code> <code><b>/{PID}/{EID}</b></code> <code>(Retrieve the detail of an member)</code></summary>

<br />only for admin

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key      | required | data type | description                              |
| -------- | -------- | --------- | ---------------------------------------- |
| PID      | true     | string    | id of the project                        |
| EID      | true     | string    | the EID of the member                    |
##### Responses
| http code    | content-type       | description                                        |
| ------------ | ------------------ | -------------------------------------------------- |
| `200`        | `application/json` | `{'EID': (str), 'PID': (str), 'position': (str),'role_on_sys':(str)}`  |
| `404`,       | `text/plain`       | `{'Error': 'Member not found'}`                    |
| `500`        | `text/plain`       | `{'Error': 'server error'}`                        |

</details>

<details>
<summary><code>GET</code> <code><b>/{PID}</b></code> <code>(Retrieve the detail of all member in specific project)</code></summary>

<br />only for admin

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key      | required | data type | description                              |
| -------- | -------- | --------- | ---------------------------------------- |
| PID      | true     | string    | id of the project                        |
##### Responses
| http code    | content-type       | description                                       |
| ------------ | ------------------ | ------------------------------------------------- |
| `200`        | `application/json` | the list of employee (form: `{'EID': (str), 'name': (str), 'PID': (str), 'gender': (int), 'email': (str), 'phone': (str), 'nation': (str)}`)              |
| `404`,       | `text/plain`       | `{'Error': "There's no member in this project"}`  |
| `500`        | `text/plain`       | `{'Error': 'server error'}`                       |

</details>

# /project_management/usage

<details>
<summary><code>POST</code> <code><b>/</b></code> <code>(Create an usage of source)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Body
| key                | required | data type | description                              |
| ------------------ | -------- | --------- | ---------------------------------------- |
| PID                | true     | string    | id of the project                        |
| PN                 | true     | string    | the part number of the product           |
| amount             | true     | int       | amount of the source                     |
| unit               | true     | string    | the unit of the source                   |
##### Responses
| http code    | content-type         | description                        |
| ------------ | -------------------- | ---------------------------------- |
| `200`        | `application/json`   | `{'message': 'Usage added successfully!','data': {'PID': (str), 'PN': (str), 'amount': (int), 'unit': (str)}}` |
| `400`        | `text/plain`         | `{'Error': error massage}`         |
| `500`        | `text/plain`         | `{'Error': 'server error'}`        |
</details>

<details>
<summary><code>GET</code> <code><b>/material/{PID}</b></code> <code>(Get all the materials in the specific project)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Body
| key                | required | data type | description                              |
| ------------------ | -------- | --------- | ---------------------------------------- |
| PID                | true     | string    | id of the project                        |
| PN                 | true     | string    | the part number of the product           |
| amount             | true     | int       | amount of the source                     |
| unit               | true     | string    | the unit of the source                   |
##### Responses
| http code    | content-type         | description                        |
| ------------ | -------------------- | ---------------------------------- |
| `200`        | `application/json`   | `{'message': 'Usage added successfully!','data': {'PID': (str), 'PN': (str), 'amount': (int), 'unit': (str)}}` |
| `400`        | `text/plain`         | `{'Error': error massage}`         |
| `500`        | `text/plain`         | `{'Error': 'server error'}`        |
</details>

<details>
<summary><code>Delete</code> <code><b>/{PID}/{PN}</b></code> <code>(Remove usage of a source)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key  | required | data type | description                    |
| ---- | -------- | --------- | ------------------------------ |
| PID  | true     | string    | id of the project              |
| PN   | true     | string    | the part number of the product |
##### Responses
| http code    | content-type | description                                     |
| ------------ | -------------| ----------------------------------------------- |
| `204`        | `text/plain` | `{'message': 'Usage deleted successfully!'}`    |
| `404`        | `text/plain` | `{'Error': 'Usage not found'}`                  |
| `500`        | `text/plain` | `{'Error': 'server error'}`                     |

</details>

<details>
<summary><code>PUT</code> <code><b>/{PID}/{PN}</b></code> <code>(Revise usage of source)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key    | required | data type | description                    |
| ------ | -------- | --------- | ------------------------------ |
| PID    | true     | string    | id of the project              |
| PN     | true     | string    | the part number of the product |
##### Body
| key                | required | data type | description                              |
| ------------------ | -------- | --------- | ---------------------------------------- |
| PID                | true     | string    | id of the project                        |
| PN                 | true     | string    | the part number of the product           |
| amount             | true     | int       | amount of the source                     |
| unit               | true     | string    | the unit of the source                   |
##### Responses
| http code    | content-type | description                                   |
| ------------ | -------------| -------------------------------------         |
| `200`        | `text/plain` | `{'message': 'Usage updated successfully!', 'data': {'PID': (str), 'PN': (str), 'amount': (int), 'unit': (str)}}`|
| `400`        | `text/plain` | `{'Error': 'client error'}`                   |
| `404`        | `text/plain` | `{'Error': 'Usage not found'}`               |
| `500`        | `text/plain` | `{'Error': 'server error'}`                   |

</details>

<details>
<summary><code>GET</code> <code><b>/{PID}/{PN}</b></code> <code>(Retrieve the detail of usage)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key    | required | data type | description                    |
| ------ | -------- | --------- | ------------------------------ |
| PID    | true     | string    | id of the project              |
| PN     | true     | string    | the part number of the product |
##### Responses
| http code    | content-type       | description                                 |
| ------------ | ------------------ | ------------------------------------------- |
| `200`        | `application/json` | `{'PID': (str), 'PN': (str), 'name': (str), 'amount': (int), 'unit': (str)}`       |
| `404`        | `text/plain`       | `{'Error': 'Usage not found'}`             |
| `500`        | `text/plain`       | `{'Error': 'server error'}`                 |

</details>