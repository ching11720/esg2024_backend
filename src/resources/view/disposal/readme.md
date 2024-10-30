# /resource/disposal

<details>
<summary><code>GET</code> <code><b>/</b></code> <code>(Retrieve the disposal list that the resources should be diposed within next half year)</code></summary>

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

| http code | content-type       | description                                                                                                                                                                                                                          |
| --------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `200`     | `application/json` | the sorted(by date) list of disposed resource (form: `{'RID':(str),'name':(str),'amount':(int),'unit':(str),'purchase_date':(str),'disposal_date':(str),'age':(int),'factor':(float),'form':(str),'category':(str),'status':(int)}`) |
| `205`     | `text/plain`       | `{'message': 'No disposal item recently'}`                                                                                                                                                                                           |
| `500`     | `text/plain`       | `{'Error': 'server error'}`                                                                                                                                                                                                          |

</details>
