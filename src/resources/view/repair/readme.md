# /resource/repair_log

<details>
<summary><code>POST</code> <code><b>/</b></code> <code>(Post a repair)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Path Parameters

| key | required | data type | description |
| --- | -------- | --------- | ----------- |

##### Body

| key   | required | data type | description                       |
| ----- | -------- | --------- | --------------------------------- |
| RID   | true     | string    | id of the resource                |
| Date  | true     | string    | the date the repairment is posted |
| notes | false    | string    | the notes of repairment           |

##### Responses

| http code | content-type       | description                                                                                         |
| --------- | ------------------ | --------------------------------------------------------------------------------------------------- |
| `201`     | `application/json` | `{'message': "Repair log added successfully!", data: {'RID': (str), 'date': (str), 'note': (str)}}` |
| `400`     | `text/plain`       | `{'Error': error massage}`                                                                          |
| `500`     | `text/plain`       | `{'Error': 'server error'}`                                                                         |

</details>

<details>
<summary><code>GET</code> <code><b>/repair_log</b></code> <code>(Retrieve the repair logs of all resource)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Path Parameters

| key | required | data type | description         |
| --- | -------- | --------- | ------------------- |
| --- | -------- | --------- | ------------------- |

##### Responses

| http code | content-type       | description                                                                   |
| --------- | ------------------ | ----------------------------------------------------------------------------- |
| `200`     | `application/json` | the list of repair log (form: `{'RID': (str), 'date': (str), 'note': (str)}`) |
| `500`     | `text/plain`       | `{'Error': 'server error'}`                                                   |

</details>
