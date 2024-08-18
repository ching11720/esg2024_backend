# /Project_Management/flow

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
| PID | true     | string    | the pid which is wanted to be posed |
##### Body
| key                | required | data type | description                              |
| ------------------ | -------- | --------- | ---------------------------------------- |
| `{ST.{EQM...}.{MAT...}.{Description} -> ST.{EQM...}.{MAT}.{Description} ...}(string)` | true     | json | ---------------------------------------- |
##### Responses
| http code    | content-type         | description                        |
| ------------ | -------------------- | ---------------------------------- |
| `201`        | `text/plain`         | `{'data': the detail of the flow}` |
| `400`        | `text/plain`         | `{ message: "client error"}`       |
| `401`        | `text/plain`         | `{ message: "PID is invalid"}`     |
| `500`        | `text/plain`         | `{ message: "server error"}`       |
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
| `200`        | `text/plain` | `{ message: "Flow added successfully!"}` |
| `400`        | `text/plain` | `{ message: "client error"}`             |
| `401`        | `text/plain` | `{ message: "PID is invalid"}`           |
| `500`        | `text/plain` | `{ message: "server error"}`             |

</details>