# /project_management/usage

<details>
<summary><code>POST</code> <code><b>/</b></code> <code>(Create an usage of source)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Body

| key    | required | data type | description                    |
| ------ | -------- | --------- | ------------------------------ |
| PID    | true     | string    | id of the project              |
| PN     | true     | string    | the part number of the product |
| amount | true     | int       | amount of the source           |
| unit   | true     | string    | the unit of the source         |

##### Responses

| http code | content-type       | description                                                                                                    |
| --------- | ------------------ | -------------------------------------------------------------------------------------------------------------- |
| `200`     | `application/json` | `{'message': 'Usage added successfully!','data': {'PID': (str), 'PN': (str), 'amount': (int), 'unit': (str)}}` |
| `400`     | `text/plain`       | `{'Error': error massage}`                                                                                     |
| `500`     | `text/plain`       | `{'Error': 'server error'}`                                                                                    |

</details>

<details>
<summary><code>Delete</code> <code><b>/{PID}/{PN}</b></code> <code>(Remove usage of a source)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Path Parameters

| key | required | data type | description                    |
| --- | -------- | --------- | ------------------------------ |
| PID | true     | string    | id of the project              |
| PN  | true     | string    | the part number of the product |

##### Responses

| http code | content-type | description                                  |
| --------- | ------------ | -------------------------------------------- |
| `204`     | `text/plain` | `{'message': 'Usage deleted successfully!'}` |
| `404`     | `text/plain` | `{'Error': 'Usage not found'}`               |
| `500`     | `text/plain` | `{'Error': 'server error'}`                  |

</details>

<details>
<summary><code>PUT</code> <code><b>/{PID}/{PN}</b></code> <code>(Revise usage of source)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Path Parameters

| key | required | data type | description                    |
| --- | -------- | --------- | ------------------------------ |
| PID | true     | string    | id of the project              |
| PN  | true     | string    | the part number of the product |

##### Body

| key    | required | data type | description                    |
| ------ | -------- | --------- | ------------------------------ |
| PID    | true     | string    | id of the project              |
| PN     | true     | string    | the part number of the product |
| amount | true     | int       | amount of the source           |
| unit   | true     | string    | the unit of the source         |

##### Responses

| http code | content-type | description                                                                                                       |
| --------- | ------------ | ----------------------------------------------------------------------------------------------------------------- |
| `200`     | `text/plain` | `{'message': 'Usage updated successfully!', 'data': {'PID': (str), 'PN': (str), 'amount': (int), 'unit': (str)}}` |
| `400`     | `text/plain` | `{'Error': 'client error'}`                                                                                       |
| `404`     | `text/plain` | `{'Error': 'Usage not found'}`                                                                                    |
| `500`     | `text/plain` | `{'Error': 'server error'}`                                                                                       |

</details>

<details>
<summary><code>GET</code> <code><b>/{PID}/{PN}</b></code> <code>(Retrieve the detail of usage)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Path Parameters

| key | required | data type | description                    |
| --- | -------- | --------- | ------------------------------ |
| PID | true     | string    | id of the project              |
| PN  | true     | string    | the part number of the product |

##### Responses

| http code | content-type       | description                                                                  |
| --------- | ------------------ | ---------------------------------------------------------------------------- |
| `200`     | `application/json` | `{'PID': (str), 'PN': (str), 'name': (str), 'amount': (int), 'unit': (str)}` |
| `404`     | `text/plain`       | `{'Error': 'Usage not found'}`                                               |
| `500`     | `text/plain`       | `{'Error': 'server error'}`                                                  |

</details>
