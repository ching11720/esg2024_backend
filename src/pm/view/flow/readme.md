# /project_management/flow

flow's form example: `[
    {"step": 1, "equipments": [{"PN": "06xxxx", "amount": 1, "unit": "unit"}], "materials": [{"PN": "06xxxx", "amount": 1, "unit": "kg"}], "description": "Initial setup and preparation"}, 
    {"step": 2, .....}]`

<details>
<summary><code>GET</code> <code><b>/{PID}</b></code> <code>(Get a flow of a project)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Path Parameters

| key | required | data type | description                         |
| --- | -------- | --------- | ----------------------------------- |
| PID | true     | string    | the pid which is wanted to be posed |

##### Responses

| http code | content-type | description                      |
| --------- | ------------ | -------------------------------- |
| `200`     | `text/plain` | `{'PID': (str), 'flow': (json)}` |
| `401`     | `text/plain` | `{'Error': 'PID is invalid'}`    |
| `500`     | `text/plain` | `{'Error': 'server error'}`      |

</details>

<details>
<summary><code>PUT</code> <code><b>/{PID}</b></code> <code>(Revise or add a flow of a project)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Path Parameters

| key | required | data type | description                           |
| --- | -------- | --------- | ------------------------------------- |
| PID | true     | string    | the pid which is wanted to be revised |

##### Body

| key  | required | data type | description                           |
| ---- | -------- | --------- | ------------------------------------- |
| PID  | true     | string    | the pid which is wanted to be revised |
| flow | true     | json      | the flow of the project               |

##### Responses

| http code | content-type | description                                                                       |
| --------- | ------------ | --------------------------------------------------------------------------------- |
| `200`     | `text/plain` | `{'message': "Flow added successfully!", 'data': {'PID': (str), 'flow': (json)}}` |
| `400`     | `text/plain` | `{'Error': error massage}`                                                        |
| `401`     | `text/plain` | `{'Error': 'PID is invalid'}`                                                     |
| `500`     | `text/plain` | `{'Error': 'server error'}`                                                       |

</details>
