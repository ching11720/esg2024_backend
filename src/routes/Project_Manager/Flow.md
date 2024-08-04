# /Project_Management/Flow

<details>
<summary><code>PUT</code> <code><b>/{PID}</b></code> <code>(Put a flow of a project)</code></summary>

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
| `201`        | `text/plain`         | `{'message': 'Flow added successfully!', 'data': serializer.data}` |
| `400`        | `text/plain`         | `{ message: "client error"}`       |
| `404`        | `text/plain`         | `{ message: "PID is invalid"}`     |
| `500`        | `text/plain`         | `{ message: "server error"}`       |
</details>

<details>
<summary><code>REVISE</code> <code><b>/{PID}</b></code> <code>(Revise the flow of a project)</code></summary>

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
| http code    | content-type | description                           |
| ------------ | -------------| ------------------------------------- |
| `200`        | `text/plain` | `{ message: "success"}`               |
| `400`        | `text/plain` | `{ message: "client error"}`       |
| `404`        | `text/plain` | `{ message: "PID is invalid"}`        |
| `500`        | `text/plain` | `{ message: "server error"}`          |

</details>