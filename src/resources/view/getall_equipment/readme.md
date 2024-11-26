# /resource/equipment

<details>
<summary><code>GET</code> <code><b>/</b></code> <code>(Get all equipments)</code></summary>

<br />

##### Headers

| key | values | description |
| --- | ------ | ----------- |
| --- | ------ | ----------- |

##### Responses

| http code | content-type       | description                                                                                                                                                                                                          |
| --------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `200`     | `application/json` | the list of all equipments (object form: `{'RID':(str),'name':(str),'PN':(str),'amount':(int),'unit':(str),'purchase_date':(str),'disposal_date':(str),'age':(int),'factor':(float),'form':(str),'category':(str)}`) |
| `500`     | `text/plain`       | `{'Error': 'server error'}`                                                                                                                                                                                          |

</details>
