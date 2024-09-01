# /Project_Management/material

<details>
<summary><code>PUT</code> <code><b>/{PID}/{SRID}</b></code> <code>(Revise a material)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key    | required | data type | description                |
| ------ | -------- | --------- | -------------------------- |
| PID    | true     | string    | id of the project          |
| SRID   | true     | string    | id of the material         |
##### Body
| key    | required | data type | description                |
| ------ | -------- | --------- | -------------------------- |
| PID    | true     | string    | id of the project          |
| SRID   | true     | string    | id of the material         |
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
<summary><code>GET</code> <code><b>/{PID}/{SRID}</b></code> <code>(Retrieve the detail of an material)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key  | required | data type | description           |
| ---- | -------- | --------- | --------------------- |
| PID  | true     | string    | id of the project     |
| SrID | true     | string    | id of the material    |
##### Responses
| http code    | content-type       | description                                 |
| ------------ | ------------------ | ------------------------------------------- |
| `200`        | `application/json` | the detail of the retrieved material        |
| `404`        | `text/plain`       | `{ message: "Material not found"}`          |
| `500`        | `text/plain`       | `{ message: "server error"}`                |

</details>