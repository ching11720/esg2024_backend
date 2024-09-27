# /resource/equipment

<details>
<summary><code>GET</code> <code><b>/</b></code> <code>(Get all equipments)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Responses
| http code    | content-type         | description                             |
| ------------ | -------------------- | --------------------------------------- |
| `200`        | `application/json`   | the list of all equipments (object form: `{'RID':(str),'name':(str),'PN':(str),'amount':(int),'unit':(str),'purchase_date':(str),'disposal_date':(str),'age':(int),'factor':(float),'form':(str),'category':(str)}`) |
| `500`        | `text/plain`         | `{'Error': 'server error'}`            |
</details>

# /resource/material

<details>
<summary><code>GET</code> <code><b>/</b></code> <code>(Get all materials)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Responses
| http code    | content-type         | description                             |
| ------------ | -------------------- | --------------------------------------- |
| `200`        | `application/json`   | the list of all materials (form: `{'RID':(str),'name':(str),'PN':(str),'amount':(int),'unit':(str),'purchase_date':(str),'disposal_date':(str),'age':(int),'factor':(float),'form':(str),'category':(str)}`)  |
| `500`        | `text/plain`         | `{'Error': 'server error'}`            |
</details>

# /resource/create

<details>
<summary><code>POST</code> <code><b>/</b></code> <code>(Create a resource)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Body
| key                | required | data type | description                                |
| ------------------ | -------- | --------- | ------------------------------------------ |
| PN                 | true     | string    | PPN of the resource                        |
| name               | true     | string    | name of the resource                       |
| amount             | true     | int       | amount of the resource                     |
| unit               | true     | number    | the unit of the resource                   |
| purchase_date      | ture     | date      | the day the resource is purchased          |
| disposal_date      | true     | date      | the day the resource should be disposed    |
| age                | true     | int       | the age of the resource (unit: yr)         |
| SID                | true     | string    | id of the supplier                         |
| factor             | false    | float     | the emission factor of the resource        |
| form               | false    | string    | the emission form of the resource          |
| category           | false    | string    | the emission category of the resource      |
| status             | true     | int       | =1, if it's resource. =2, if it's material |
##### Responses
| http code    | content-type         | description                        |
| ------------ | -------------------- | ---------------------------------- |
| `201`        | `application/json`   | `{'message': 'Resource added successfully!', 'data': {'RID':(str),'name':(str),'PN':(str),'amount':(int),'unit':(str),'purchase_date':(str),'disposal_date':(str),'age':(int),'factor':(float),'form':(str),'category':(str),'status':(int)}}`     |
| `400`        | `text/plain`         | `{'Error': error massage}`         |
| `500`        | `text/plain`         | `{'Error': "server error"}`        |
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
| key  | required | data type | description         |
| ---- | -------- | --------- | ------------------- |
| RID  | true     | string    | id of the resource  |
##### Responses
| http code    | content-type | description                                     |
| ------------ | -------------| ----------------------------------------------- |
| `204`        | `text/plain` | `{'message': "Resource deleted successfully!"}` |
| `404`        | `text/plain` | `{'Error': 'Resource not found'}`               |
| `500`        | `text/plain` | `{'Error': "server error"}`                     |

</details>

<details>
<summary><code>GET</code> <code><b>/{RID}</b></code> <code>(Retrieve the detail of a resource, no matter it is disposed or not)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key      | required   | data type | description           |
| -------- | ---------- | --------- | --------------------- |
| RID      | true       | string    | id of the resource    |
##### Responses
| http code    | content-type       | description                                 |
| ------------ | ------------------ | ------------------------------------------- |
| `200`        | `application/json` | `{'RID':(str),'name':(str),'PN':(str),'amount':(int),'unit':(str),'purchase_date':(str),'disposal_date':(str),'age':(int),'factor':(float),'form':(str),'category':(str),'status':(int)}` |
| `404`        | `text/plain`       | `{'Error': 'Source not found'}`             |
| `500`        | `text/plain`       | `{'Error': "server error"}`                 |

</details>

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
| http code    | content-type         | description                                    |
| ------------ | -------------------- | ---------------------------------------------- |
| `200`        | `application/json`   | the sorted(by date) list of disposed resource (form: `{'RID':(str),'name':(str),'amount':(int),'unit':(str),'purchase_date':(str),'disposal_date':(str),'age':(int),'factor':(float),'form':(str),'category':(str),'status':(int)}`) |
| `205`        | `text/plain`         | `{'message': 'No disposal item recently'}`     |
| `500`        | `text/plain`         | `{'Error': 'server error'}`                    |

</details>

# /resource/repair_log

<details>
<summary><code>POST</code> <code><b>/</b></code> <code>(Post a repair)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key | required | data type | description         |
| --- | -------- | --------- | ------------------- |
##### Body
| key   | required | data type | description                       |
| ----- | -------- | --------- | --------------------------------- |
| RID  | true     | string    | id of the resource               |
| Date  | true     | string    | the date the repairment is posted |
| notes | false    | string    | the notes of repairment           |
##### Responses
| http code    | content-type          | description                                    |
| ------------ | --------------------- | ---------------------------------------------- |
| `201`        | `application/json`    | `{'message': "Repair log added successfully!", data: {'RID': (str), 'date': (str), 'note': (str)}}` |
| `400`        | `text/plain`          | `{'Error': error massage}`                   |
| `500`        | `text/plain`          | `{'Error': 'server error'}`                   |

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
| http code    | content-type         | description                    |
| ------------ | -------------------- | ------------------------------ |
| `200`        | `application/json`   | the list of repair log (form: `{'RID': (str), 'date': (str), 'note': (str)}`)  |
| `500`        | `text/plain`         | `{'Error': 'server error'}`   |
</details>