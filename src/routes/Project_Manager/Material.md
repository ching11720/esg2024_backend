# /Project_Management/Material

<details>
<summary><code>POST</code> <code><b>/</b></code> <code>(Create a material)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Body
| key                | required | data type | description                              |
| ------------------ | -------- | --------- | ---------------------------------------- |
| PID                | true     | string    | id of the project                        |
| MID                | true     | string    | id of the material                       |
| amount             | true     | int       | amount of the material                   |
| unit               | true     | string    | the unit of the material                 |
##### Responses
| http code    | content-type         | description                        |
| ------------ | -------------------- | ---------------------------------- |
| `200`        | `application/json`   | `{ message: 'Material added successfully!', data: the detail of the material }`  |
| `400`        | `text/plain`         | `{ message: "client error"}`       |
| `500`        | `text/plain`         | `{ message: "server error"}`       |
</details>

<details>
<summary><code>REVISE</code> <code><b>/{PID}/{MID}</b></code> <code>(Revise a material)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key    | required | data type | description                |
| ------ | -------- | --------- | -------------------------- |
| PID    | true     | string    | id of the project          |
| MID    | true     | string    | id of the material         |
##### Body
| key    | required | data type | description                |
| ------ | -------- | --------- | -------------------------- |
| PID    | true     | string    | id of the project          |
| MID    | true     | string    | id of the material         |
| amount | true     | int       | the amount of the material |
| unit   | true     | number    | the unit of the material   |
##### Responses
| http code    | content-type | description                                   |
| ------------ | -------------| -------------------------------------         |
| `200`        | `text/plain` | `{ message: "Material updated successfully!"}`|
| `400`        | `text/plain` | `{ message: "client error"}`                  |
| `404`        | `text/plain` | `{ message: "Material not found"}`            |
| `500`        | `text/plain` | `{ message: "server error"}`                  |

</details>

<details>
<summary><code>RETRIEVE</code> <code><b>/{PID}/{MID}</b></code> <code>(Retrieve the detail of an material)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key  | required | data type | description           |
| ---- | -------- | --------- | --------------------- |
| PID  | true     | string    | id of the project     |
| MID  | true     | string    | id of the material    |
##### Responses
| http code    | content-type       | description                                 |
| ------------ | ------------------ | ------------------------------------------- |
| `200`        | `application/json` | the detail of the retrieved material        |
| `404`        | `text/plain`       | `{ message: "Material not found"}`          |
| `500`        | `text/plain`       | `{ message: "server error"}`                |

</details>