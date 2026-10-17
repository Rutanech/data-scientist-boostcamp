# Week 5 Mini Project — Customer Churn Prediction

## โจทย์

บริษัท Telecom ต้องการลดจำนวนลูกค้าที่เลิกใช้บริการ (Customer Churn)  
ให้คุณสร้าง Machine Learning Model เพื่อทำนายว่าลูกค้าคนไหน "มีแนวโน้มจะเลิกใช้บริการ"

---

## Dataset: `churn_data.csv`

| Column | Description |
|--------|-------------|
| `customer_id` | รหัสลูกค้า |
| `tenure` | จำนวนเดือนที่เป็นลูกค้า |
| `monthly_charges` | ค่าบริการรายเดือน (บาท) |
| `total_charges` | ค่าบริการสะสม (บาท) |
| `num_services` | จำนวนบริการที่ใช้ |
| `contract_type` | ประเภทสัญญา (month-to-month, one_year, two_year) |
| `paperless_billing` | ใช้ใบแจ้งหนี้อิเล็กทรอนิกส์ (1=ใช่, 0=ไม่ใช่) |
| `churn` | เลิกใช้บริการ (1=ใช่, 0=ไม่ใช่) ← **Target** |

---

## Steps

### Step 1: Data Overview
- โหลดข้อมูลและดู shape, dtypes, describe()
- ตรวจสอบ missing values
- ดู distribution ของ target variable (churn)

### Step 2: EDA
- ดูว่า tenure สัมพันธ์กับ churn ยังไง?
- ลูกค้าที่ monthly_charges สูงมีแนวโน้ม churn มากกว่าไหม?
- contract_type ไหนมี churn rate สูงสุด?

### Step 3: Feature Engineering
- Encode `contract_type` เป็นตัวเลข (Label Encoding หรือ One-Hot)
- เลือก features ที่จะใช้

### Step 4: Model Training
- สร้างโมเดลอย่างน้อย 2 ตัว: Logistic Regression, Decision Tree, หรือ Random Forest
- แบ่ง train/test 80/20

### Step 5: Model Evaluation
- วัดผลด้วย accuracy
- ดู confusion matrix
- เปรียบเทียบโมเดล

### Step 6: Business Recommendation
- โมเดลไหนดีที่สุด? เพราะอะไร?
- Feature ไหนส่งผลต่อ churn มากที่สุด?
- บริษัทควรทำอะไรกับข้อมูลนี้?

---

## Deliverable

ส่วน Mini Project ใน `week05_ml_basics.ipynb`:
- ครอบคลุมทุก Step ข้างต้น
- มี markdown อธิบายแต่ละขั้นตอน
- มีกราฟประกอบ (อย่างน้อย 2 กราฟ)
- มี business recommendation 2-3 ข้อ
