# /resource/create

<details>
<summary><code>POST</code> <code><b>/</b></code> <code>(Create a resource)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Body

| key           | required | data type | description                                 |
| ------------- | -------- | --------- | ------------------------------------------- |
| PN            | true     | string    | PPN of the resource                         |
| name          | true     | string    | name of the resource                        |
| amount        | true     | int       | amount of the resource                      |
| unit          | true     | number    | the unit of the resource                    |
| purchase_date | ture     | date      | the day the resource is purchased           |
| disposal_date | true     | date      | the day the resource should be disposed     |
| age           | true     | int       | the age of the resource (unit: yr)          |
| SID           | true     | string    | id of the supplier                          |
| factor        | false    | float     | the emission factor of the resource         |
| form          | false    | string    | the emission form of the resource           |
| category      | false    | string    | the emission category of the resource       |
| status        | true     | int       | =1, if it's equipment. =2, if it's material |

##### Responses

| http code | content-type       | description                                                                                                                                                                                                                                    |
| --------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `201`     | `application/json` | `{'message': 'Resource added successfully!', 'data': {'RID':(str),'name':(str),'PN':(str),'amount':(int),'unit':(str),'purchase_date':(str),'disposal_date':(str),'age':(int),'factor':(float),'form':(str),'category':(str),'status':(int)}}` |
| `400`     | `text/plain`       | `{'Error': error massage}`                                                                                                                                                                                                                     |
| `500`     | `text/plain`       | `{'Error': "server error"}`                                                                                                                                                                                                                    |

</details>

# /resource/retrieve

<details>
<summary><code>DELETE</code> <code><b>/{RID}</b></code> <code>(Delete a resource)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Path Parameters

| key | required | data type | description        |
| --- | -------- | --------- | ------------------ |
| RID | true     | string    | id of the resource |

##### Responses

| http code | content-type | description                                     |
| --------- | ------------ | ----------------------------------------------- |
| `204`     | `text/plain` | `{'message': "Resource deleted successfully!"}` |
| `404`     | `text/plain` | `{'Error': 'Resource not found'}`               |
| `500`     | `text/plain` | `{'Error': "server error"}`                     |

</details>

<details>
<summary><code>GET</code> <code><b>/{RID}</b></code> <code>(Retrieve the detail of a resource, no matter it is disposed or not)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Path Parameters

| key | required | data type | description        |
| --- | -------- | --------- | ------------------ |
| RID | true     | string    | id of the resource |

##### Responses

| http code | content-type       | description                                                                                                                                                                               |
| --------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `200`     | `application/json` | `{'RID':(str),'name':(str),'PN':(str),'amount':(int),'unit':(str),'purchase_date':(str),'disposal_date':(str),'age':(int),'factor':(float),'form':(str),'category':(str),'status':(int)}` |
| `404`     | `text/plain`       | `{'Error': 'Source not found'}`                                                                                                                                                           |
| `500`     | `text/plain`       | `{'Error': "server error"}`                                                                                                                                                               |

</details>
