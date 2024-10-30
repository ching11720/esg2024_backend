# /project_management/daily_record

<details>
<summary><code>POST</code> <code><b>/</b></code> <code>(Create a daily record)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Body

| key     | required | data type | description                             |
| ------- | -------- | --------- | --------------------------------------- |
| PID     | true     | string    | the id of the project                   |
| PN      | true     | string    | the part number of the product          |
| date    | true     | date      | the date of the daily record            |
| runtime | false    | float     | equipment runtime of that day, unit: hr |
| amount  | true     | float     | the amount of material used that day    |
| unit    | true     | string    | the unit of material                    |

##### Responses

| http code | content-type       | description                                                                                                                                                                                                                                                     |
| --------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `201`     | `application/json` | `{'message': 'Record added successfully!','data': {'dailyID':(int), 'PID': (str), 'PN': (str), 'date': (str), 'runtime': (float), 'amount': (float), 'unit': (str), 'created_by': (str), 'created_date': (str), 'modified_by': (str), 'modified_date': (str)}}` |
| `400`     | `text/plain`       | `{'Error': error massage}`                                                                                                                                                                                                                                      |
| `500`     | `text/plain`       | `{'Error': 'server error'}`                                                                                                                                                                                                                                     |

</details>

<details>
<summary><code>PUT</code> <code><b>/{PID}/{date}</b></code> <code>(Raise a requirement of revising a daily record)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Path Parameters

| key  | required | data type | description                  |
| ---- | -------- | --------- | ---------------------------- |
| PID  | true     | string    | the id of the project        |
| date | true     | date      | the date of the daily record |

##### Body

| key            | required | data type | description                                  |
| -------------- | -------- | --------- | -------------------------------------------- |
| dailyID_origin | true     | string    | the ID of the record that you want to modify |
| PID            | true     | string    | the id of the project                        |
| PN             | true     | string    | the part number of the product               |
| date           | true     | date      | the date of the daily record                 |
| runtime        | false    | float     | equipment runtime of that day, unit: hr      |
| amount         | false    | float     | the amount of material used that day         |
| unit           | false    | string    | the unit of material                         |

##### Responses

| http code | content-type       | description                                                                                                                                                                                                                                                            |
| --------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `200`     | `application/json` | `{'message': 'Record updated successfully!', 'data': {'dailyID_modified':(int), 'dailyID_origin':(int), 'PID': (str), 'PN': (str), 'date': (str), 'runtime': (float), 'amount': (float), 'unit': (str), 'created_by': (str), 'created_date': (str), 'status': (int)}}` |
| `400`     | `text/plain`       | `{'Error': 'client error'}`                                                                                                                                                                                                                                            |
| `404`     | `text/plain`       | `{'Error': 'Record not found'}`                                                                                                                                                                                                                                        |
| `500`     | `text/plain`       | `{'Error': 'server error'}`                                                                                                                                                                                                                                            |

</details>

<details>
<summary><code>GET</code> <code><b>/{PID}/{date}</b></code> <code>(Retrieve the detail of a daily records)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Path Parameters

| key  | required | data type | description                  |
| ---- | -------- | --------- | ---------------------------- |
| PID  | true     | string    | the id of the project        |
| date | true     | date      | the date of the daily record |

##### Responses

| http code | content-type       | description                                                                                                                          |
| --------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `200`     | `application/json` | the list of daily records (form: `{'PID': (str), 'PN': (str), 'date': (str), 'runtime': (float), 'amount': (float), 'unit': (str)}`) |
| `400`     | `text/plain`       | `{'Error': 'client error'}`                                                                                                          |
| `404`     | `text/plain`       | `{'Error': 'Record not found'}`                                                                                                      |
| `500`     | `text/plain`       | `{'Error': 'server error'}`                                                                                                          |

</details>
