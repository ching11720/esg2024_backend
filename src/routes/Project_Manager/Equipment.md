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
<summary><code>Delete</code> <code><b>/{PID}/{SRID}</b></code> <code>(Remove usage of a source)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key  | required | data type | description         |
| ---- | -------- | --------- | ------------------- |
| PID  | true     | string    | id of the project   |
| SRID | true     | string    | id of the source    |
##### Responses
| http code    | content-type | description                                     |
| ------------ | -------------| ----------------------------------------------- |
| `204`        | `text/plain` | `{'message': 'Source deleted successfully!'}`   |
| `404`        | `text/plain` | `{'Error': 'Source not found'}`                 |
| `500`        | `text/plain` | `{'Error': 'server error'}`                     |

</details>

<details>
<summary><code>PUT</code> <code><b>/{PID}/{SRID}</b></code> <code>(Revise usage of source)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key    | required | data type | description                |
| ------ | -------- | --------- | -------------------------- |
| PID    | true     | string    | id of the project          |
| SRID   | true     | string    | id of the source           |
##### Body
| key    | required | data type | description                |
| ------ | -------- | --------- | -------------------------- |
| PID    | true     | string    | id of the project          |
| SRID   | true     | string    | id of the source           |
| amount | true     | int       | the amount of the source   |
| unit   | true     | number    | the unit of the source     |
##### Responses
| http code    | content-type | description                                   |
| ------------ | -------------| -------------------------------------         |
| `200`        | `text/plain` | `{'message': 'Material updated successfully!', 'data': {'PID': (str), 'SRID': (str), 'amount': (int), 'unit': (str)}}`|
| `400`        | `text/plain` | `{'Error': 'client error'}`                   |
| `404`        | `text/plain` | `{'Error': 'Source not found'}`               |
| `500`        | `text/plain` | `{'Error': 'server error'}`                   |

</details>

<details>
<summary><code>GET</code> <code><b>/{PID}/{SRID}</b></code> <code>(Retrieve the detail of usage)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key  | required | data type | description           |
| ---- | -------- | --------- | --------------------- |
| PID  | true     | string    | id of the project     |
| SRID | true     | string    | id of the source      |
##### Responses
| http code    | content-type       | description                                 |
| ------------ | ------------------ | ------------------------------------------- |
| `200`        | `application/json` | `{'PID': (str), 'SRID': (str), 'name': (str), 'amount': (int), 'unit': (str)}`       |
| `404`        | `text/plain`       | `{'Error': 'Source not found'}`             |
| `500`        | `text/plain`       | `{'Error': 'server error'}`                 |

</details>