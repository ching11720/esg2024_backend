# /Project_Management/member

<details>
<summary><code>POST</code> <code><b>/</b></code> <code>(Create an member)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Body
| key      | required | data type | description                              |
| -------- | -------- | --------- | ---------------------------------------- |
| PID      | true     | string    | id of the project                        |
| EID      | true     | string    | the EID of the member                    |
| position | true     | string    |                                          |
##### Responses
| http code    | content-type         | description                        |
| ------------ | -------------------- | ---------------------------------- |
| `201`        | `application/json`   | the detail of the posted member    |
| `400`        | `text/plain`         | `{ message: "client error"}`       |
| `500`        | `text/plain`         | `{ message: "server error"}`       |
</details>

<details>
<summary><code>REVISE</code> <code><b>/{PID}/{EID}</b></code> <code>(Revise an member)</code></summary>

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
| key      | required | data type | description                |
| -------- | -------- | --------- | -------------------------- |
| PID      | true     | string    | id of the project          |
| EID      | true     | string    | the EID of the member      |
| Position | true     | string    | the position of the memeber|
##### Responses
| http code    | content-type | description                                  |
| ------------ | -------------| -------------------------------------        |
| `200`        | `text/plain` | `{'message': 'Member revised successfully!'}`|
| `400`        | `text/plain` | `{ message: "client error"}`                 |
| `404`,       | `text/plain` | `{ message: "Member not found"}`             |
| `500`        | `text/plain` | `{ message: "server error"}`                 |

</details>

<details>
<summary><code>REMOVE</code> <code><b>/{PID}/{EID}</b></code> <code>(Remove an member)</code></summary>

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
| `204`        | `text/plain` | `{ message: "Member deleted successfully!"}`|
| `400`        | `text/plain` | `{ message: "client error"}`                |
| `404`        | `text/plain` | `{ message: "Member not found"}`            |
| `500`        | `text/plain` | `{ message: "server error"}`                |

</details>

<details>
<summary><code>RETRIEVE</code> <code><b>/{PID}/{EID}</b></code> <code>(Retrieve the detail of an member)</code></summary>

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
| http code    | content-type       | description                                 |
| ------------ | ------------------ | ------------------------------------------- |
| `200`        | `application/json` | the detail of the retrieved member          |
| `404`,       | `text/plain`       | `{ message: "Member not found"}`            |
| `500`        | `text/plain`       | `{ message: "server error"}`                |

</details>