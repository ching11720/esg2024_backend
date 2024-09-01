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
| SRID               | true     | string    | id of the source                         |
| amount             | true     | int       | amount of the source                     |
| unit               | true     | string    | the unit of the source                   |
##### Responses
| http code    | content-type         | description                        |
| ------------ | -------------------- | ---------------------------------- |
| `200`        | `application/json`   | `{'message': 'Usage added successfully!','data': {'PID': (str), 'SRID': (str), 'amount': (int), 'unit': (str)}}` |
| `400`        | `text/plain`         | `{'Error': error massage}`         |
| `500`        | `text/plain`         | `{'Error': 'server error'}`        |
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