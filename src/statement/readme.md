# /statement

<details>
<summary><code>GET</code> <code><b>/project</b></code> <code>(Retrieve all project id and name in company)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Body

| key  | required | data type | description             |
| ---- | -------- | --------- | ----------------------- |
| PID  | true     | string    | the id of the project   |
| name | true     | string    | the name of the project |

##### Responses

| http code | content-type       | description                                                                          |
| --------- | ------------------ | ------------------------------------------------------------------------------------ |
| `200`     | `application/json` | the list of daily records (form: `{'PID': (str), 'PName': (str), 'PN_name': (str)}`) |
| `500`     | `text/plain`       | `{'Error': 'get project api error'}`                                                 |

</details>

<details>
<summary><code>GET</code> <code><b>/</b></code> <code>(Retrieve the detail of a daily records to make statement)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Path Parameters

| key | required | data type | description           |
| --- | -------- | --------- | --------------------- |
| PID | true     | string    | the id of the project |

##### Responses

| http code | content-type       | description                                                                                                                                                            |
| --------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `200`     | `application/json` | the list of daily records (form: `{'PName': (str), 'PN_name': (str), 'date': (str), 'runtime': (float), 'amount': (float), 'unit': (str), 'current_factor': (float)}`) |
| `404`     | `text/plain`       | `{'Error': 'PID is invalid'}`                                                                                                                                          |
| `500`     | `text/plain`       | `{'Error': 'statement api error'}`                                                                                                                                     |

</details>
