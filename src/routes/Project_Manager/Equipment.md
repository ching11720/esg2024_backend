# /Project_Management/equipment

<details>
<summary><code>GET</code> <code><b>/</b></code> <code>(Get all equipments)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Body
| key                | required | data type | description                              |
| ------------------ | -------- | --------- | ---------------------------------------- |
| PID                | true     | string    | id of the project                        |
| SRID               | true     | string    | id of the equipment                      |
| amount             | true     | int       | amount of the equipment                  |
| unit               | true     | string    | the unit of the equipment                |
##### Responses
| http code    | content-type         | description                             |
| ------------ | -------------------- | --------------------------------------- |
| `200`        | `application/json`   | `{ data: the detail of the equipment }` |
| `500`        | `text/plain`         | `{ message: "server error"}`            |
</details>

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
| SRID               | true     | string    | id of the equipment                      |
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
<summary><code>Delete</code> <code><b>/{PID}/{SRID}</b></code> <code>(Remove an eqiupment)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key  | required | data type | description         |
| ---- | -------- | --------- | ------------------- |
| PID  | true     | string    | id of the project   |
| SRID | true     | string    | id of the equipment |
##### Responses
| http code    | content-type | description                                     |
| ------------ | -------------| ----------------------------------------------- |
| `204`        | `text/plain` | `{ message: "equipment deleted successfully!"}` |
| `404`        | `text/plain` | `{ message: "Equipment not found"}`             |
| `500`        | `text/plain` | `{ message: "server error"}`                    |

</details>

<details>
<summary><code>GET</code> <code><b>/{PID}/{SRID}</b></code> <code>(Retrieve the detail of an equipment)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key  | required | data type | description           |
| ---- | -------- | --------- | --------------------- |
| PID  | true     | string    | id of the project     |
| SRID  | true     | string    | id of the equipment   |
##### Responses
| http code    | content-type       | description                                 |
| ------------ | ------------------ | ------------------------------------------- |
| `200`        | `application/json` | the detail of the retrieved equipment       |
| `404`        | `text/plain`       | `{ message: "Equipment not found"}`         |
| `500`        | `text/plain`       | `{ message: "server error"}`                |

</details>