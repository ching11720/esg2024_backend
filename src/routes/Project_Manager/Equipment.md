# /Project_Management/Equipment

<details>
<summary><code>POST</code> <code><b>/</b></code> <code>(Create an equipment)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Body
| key                | required | data type | description                              |
| ------------------ | -------- | --------- | ---------------------------------------- |
| PID                | true     | string    | id of the project                        |
| EQID               | true     | string    | id of the equipment                      |
| amount             | true     | int       | amount of the equipment                  |
| unit               | true     | string    | the unit of the equipment                |
##### Responses
| http code    | content-type         | description                        |
| ------------ | -------------------- | ---------------------------------- |
| `200`        | `application/json`   | `{ message: 'Equipment added successfully!', data: the detail of the equipment }` |
| `400`        | `text/plain`         | `{ message: "client error"}`       |
| `500`        | `text/plain`         | `{ message: "server error"}`       |
</details>

<details>
<summary><code>REMOVE</code> <code><b>/{PID}/{EID}</b></code> <code>(Remove an eqiupment)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key  | required | data type | description         |
| ---- | -------- | --------- | ------------------- |
| PID  | true     | string    | id of the project   |
| EQID | true     | string    | id of the equipment |
##### Responses
| http code    | content-type | description                                     |
| ------------ | -------------| ----------------------------------------------- |
| `204`        | `text/plain` | `{ message: "equipment deleted successfully!"}` |
| `404`        | `text/plain` | `{ message: "Equipment not found"}`             |
| `500`        | `text/plain` | `{ message: "server error"}`                    |

</details>

<details>
<summary><code>RETRIEVE</code> <code><b>/{PID}/{EID}</b></code> <code>(Retrieve the detail of an equipment)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key  | required | data type | description           |
| ---- | -------- | --------- | --------------------- |
| PID  | true     | string    | id of the project     |
| EID  | true     | string    | id of the equipment   |
##### Responses
| http code    | content-type       | description                                 |
| ------------ | ------------------ | ------------------------------------------- |
| `200`        | `application/json` | the detail of the retrieved equipment       |
| `404`        | `text/plain`       | `{ message: "Equipment not found"}`         |
| `500`        | `text/plain`       | `{ message: "server error"}`                |

</details>