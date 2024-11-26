# /statement

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
