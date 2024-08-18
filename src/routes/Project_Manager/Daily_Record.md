# /Project_Management/daily_record

<details>
<summary><code>POST</code> <code><b>/</b></code> <code>(Create a daily record)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Body
| key                | required | data type | description                              |
| ------------------ | -------- | --------- | ---------------------------------------- |
| PID                | true     | string    | the id of the project                    |
| SRID               | true     | string    | the id of the source                     |
| date               | true     | date      | the date of the daily record             |
| runtime            | false    | float     | equipment runtime of that day, unit: hr  |
| amount             | false    | float     | the amount of material used that day     |
| unit               | false    | string    | the unit of material                     |
##### Responses
| http code    | content-type         | description                        |
| ------------ | -------------------- | ---------------------------------- |
| `201`        | `application/json`   | `{'message': 'Record added successfully!','data': the detail of revised daily record}`|
| `400`        | `text/plain`         | `{ message: "client error"}`       |
| `500`        | `text/plain`         | `{ message: "server error"}`       |
</details>

<details>
<summary><code>PUT</code> <code><b>/{PID}/{date}</b></code> <code>(Revise a daily record)</code></summary>

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
| SRID               | true     | string    | the id of the source                     |
| date               | true     | date      | the date of the daily record             |
| runtime            | false    | float     | equipment runtime of that day, unit: hr  |
| amount             | false    | float     | the amount of material used that day     |
| unit               | false    | string    | the unit of material                     |
##### Responses
| http code    | content-type       | description                                 |
| ------------ | ------------------ | ------------------------------------------- |
| `200`        | `application/json` | the detail of revised daily record          |
| `400`        | `text/plain`       | `{ message: "client error"}`                |
| `404`        | `text/plain`       | `{ message: "Record not found"}`            |
| `500`        | `text/plain`       | `{ message: "server error"}`                |

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
| `200`        | `application/json` | the detail of the daily record              |
| `404`        | `text/plain`       | `{ message: "Record not found"}`            |
| `500`        | `text/plain`       | `{ message: "server error"}`                |

</details>