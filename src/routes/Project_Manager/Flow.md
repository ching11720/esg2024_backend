# /project_management/flow

<details>
<summary><code>GET</code> <code><b>/{PID}</b></code> <code>(Get a flow of a project)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key | required | data type | description                           |
| --- | -------- | --------- | ------------------------------------- |
| PID | true     | string    | the pid which is wanted to be posed   |
##### Responses
| http code    | content-type         | description                                |
| ------------ | -------------------- | ------------------------------------------ |
| `200`        | `text/plain`         | `{'data': {'PID': (str), 'flow': (json)}}` |
| `401`        | `text/plain`         | `{'Error': 'PID is invalid'}`              |
| `500`        | `text/plain`         | `{'Error': 'server error'}`                |
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
| key                | required | data type | description                              |
| ------------------ | -------- | --------- | ---------------------------------------- |
| `{ST.{EQM...}.{MAT...}.{Description} -> ST.{EQM...}.{MAT}.{Description} ...}(string)` | true     | json | ---------------------------------------- |
##### Responses
| http code    | content-type | description                              |
| ------------ | -------------| ---------------------------------------- |
| `200`        | `text/plain` | `{'message': "Flow added successfully!", 'data': {'PID': (str), 'flow': (json)}}` |
| `400`        | `text/plain` | `{'Error': error massage}`               |
| `401`        | `text/plain` | `{'Error': 'PID is invalid'}`            |
| `500`        | `text/plain` | `{'Error': 'server error'}`              |

</details>