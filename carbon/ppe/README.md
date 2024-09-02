# /ppe/source

<details>
<summary><code>POST</code> <code><b>/</b></code> <code>(Create a source)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Body
| key                | required | data type | description                                 |
| ------------------ | -------- | --------- | ------------------------------------------- |
| name               | true     | string    | name of the equipment                       |
| amount             | true     | int       | amount of the equipment                     |
| unit               | true     | number    | the unit of the equipment                   |
| purchase_date      | ture     | date      | the day the equipment is purchased          |
| disposal_date      | true     | date      | the day the equipment should be disposed    |
| age                | true     | int       | the age of the equipment (unit: yr)         |
| SID                | true     | string    | id of the supplier                          |
| factor             | false    | float     | the emission factor of the equipment        |
| form               | false    | string    | the emission form of the equipment          |
| category           | false    | string    | the emission category of the equipment      |
| status             | true     | int       | =1, if it's equipment. =2, if it's material |
##### Responses
| http code    | content-type         | description                        |
| ------------ | -------------------- | ---------------------------------- |
| `201`        | `application/json`   | `{'message': 'Source added successfully!', 'data': {'SRID':(str),'name':(str),'amount':(int),'unit':(str),'purchase_date':(str),'disposal_date':(str),'age':(int),'factor':(float),'form':(str),'category':(str),'status':(int)}}`|
| `400`        | `text/plain`         | `{'source_add_errors': error massage(str),'supply_add_errors': error massage(str)}`       |
| `500`        | `text/plain`         | `{'Error': "server error"}`       |
</details>

<details>
<summary><code>DELETE</code> <code><b>/{SRID}</b></code> <code>(Delete a source)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key  | required | data type | description         |
| ---- | -------- | --------- | ------------------- |
| SRID | true     | string    | id of the equipment |
##### Responses
| http code    | content-type | description                                     |
| ------------ | -------------| ----------------------------------------------- |
| `204`        | `text/plain` | `{'message': "Source deleted successfully!"}`   |
| `404`        | `text/plain` | `{'Error': 'Source not found'}`                 |
| `500`        | `text/plain` | `{'Error': "server error"}`                     |

</details>

<details>
<summary><code>GET</code> <code><b>/{SRID}</b></code> <code>(Retrieve the detail of a source)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Path Parameters
| key      | required   | data type | description           |
| -------- | ---------- | --------- | --------------------- |
| SRID     | true       | string    | id of the source      |
##### Responses
| http code    | content-type       | description                                 |
| ------------ | ------------------ | ------------------------------------------- |
| `200`        | `application/json` | `{'SRID':(str),'name':(str),'amount':(int),'unit':(str),'purchase_date':(str),'disposal_date':(str),'age':(int),'factor':(float),'form':(str),'category':(str),'status':(int)}` |
| `404`        | `text/plain`       | `{'Error': 'Source not found'}`             |
| `500`        | `text/plain`       | `{'Error': "server error"}`                 |

</details>

# /ppe/equipment

<details>
<summary><code>GET</code> <code><b>/{}</b></code> <code>(Get all equipments)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Responses
| http code    | content-type         | description                             |
| ------------ | -------------------- | --------------------------------------- |
| `200`        | `application/json`   | the list of all equipments (form: `{'SRID':(str),'name':(str),'amount':(int),'unit':(str),'purchase_date':(str),'disposal_date':(str),'age':(int),'factor':(float),'form':(str),'category':(str),'status':(int)}`) |
| `500`        | `text/plain`         | `{'Error': 'server error'}`            |
</details>

# /ppe/material

<details>
<summary><code>GET</code> <code><b>/{}</b></code> <code>(Get all materials)</code></summary>

<br />

##### Headers
| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |
##### Responses
| http code    | content-type         | description                             |
| ------------ | -------------------- | --------------------------------------- |
| `200`        | `application/json`   | the list of all materials (form: `{'SRID':(str),'name':(str),'amount':(int),'unit':(str),'purchase_date':(str),'disposal_date':(str),'age':(int),'factor':(float),'form':(str),'category':(str),'status':(int)}`)  |
| `500`        | `text/plain`         | `{'Error': 'server error'}`            |
</details>

# /ppe/disposal

<details>
<summary><code>GET</code> <code><b>/disposal</b></code> <code>(Retrieve the disposal list that the equipments should be diposed within next half year)</code></summary>

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
| `200`        | `application/json`   | the sorted(by date) list of disposed equipment (form: `{'SRID':(str),'name':(str),'amount':(int),'unit':(str),'purchase_date':(str),'disposal_date':(str),'age':(int),'factor':(float),'form':(str),'category':(str),'status':(int)}`) |
| `205`        | `text/plain`         | `{'message': 'No disposal item recently'}`     |
| `500`        | `text/plain`         | `{'Error': 'server error'}`                    |

</details>

# /ppe/repair_log

<details>
<summary><code>POST</code> <code><b>/{}</b></code> <code>(Post a repair)</code></summary>

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
| SRID  | true     | string    | id of the equipment               |
| Date  | true     | string    | the date the repairment is posted |
| notes | false    | string    | the notes of repairment           |
##### Responses
| http code    | content-type          | description                                    |
| ------------ | --------------------- | ---------------------------------------------- |
| `201`        | `application/json`    | `{'message': "Repair log added successfully!", data: {'SRID': (str), 'date': (str), 'note': (str)}}` |
| `400`        | `text/plain`          | `{'Error': error massage}`                   |
| `500`        | `text/plain`          | `{'Error': 'server error'}`                   |

</details>

<details>
<summary><code>GET</code> <code><b>/{}</b></code> <code>(Retrieve the repair logs of all equipment)</code></summary>

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
| `200`        | `application/json`   | the list of repair log (form: `{'SRID': (str), 'date': (str), 'note': (str)}`)  |
| `500`        | `text/plain`         | `{'Error': 'server error'}`   |
</details>