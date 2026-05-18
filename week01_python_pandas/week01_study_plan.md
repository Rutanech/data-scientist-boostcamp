# Week 1 Study Plan: Python and pandas

เป้าหมายของ Week 1 ไม่ใช่จำคำสั่งให้ได้ทั้งหมด แต่คือเริ่มคิดแบบคนทำงานกับข้อมูล:

1. โหลดข้อมูลได้
2. สำรวจข้อมูลเป็น
3. เลือกและกรองข้อมูลได้
4. คำนวณ column ใหม่ได้
5. สรุปข้อมูลด้วย `groupby` ได้
6. แปลงผลลัพธ์เป็น insight สั้น ๆ ได้

## Day 1: รู้จักข้อมูลและ pandas

เวลาเรียนประมาณ 2 ชั่วโมง

### Concept

- DataFrame คือ ตารางข้อมูล
- row คือ 1 record หรือ 1 รายการ
- column คือ ตัวแปรหรือคุณสมบัติของข้อมูล
- pandas คือ library ที่ใช้จัดการข้อมูลแบบตาราง

### ทำใน notebook

- import pandas
- อ่านไฟล์ `simple_sales.csv`
- ใช้ `head()`, `shape`, `info()`, `describe()`

### แบบฝึก

1. Dataset นี้มีกี่ rows และกี่ columns?
2. column ไหนเป็นตัวเลข?
3. column ไหนเป็นข้อความ?
4. `describe()` บอกอะไรเกี่ยวกับ `quantity` และ `unit_price`?

### Learning log

เขียน 3 บรรทัด:

- วันนี้รู้แล้วว่า DataFrame คืออะไร
- คำสั่งที่ใช้สำรวจข้อมูลมีอะไรบ้าง
- ยังงงเรื่องอะไร

## Day 2: เลือก กรอง และเรียงข้อมูล

### Concept

งาน data analyst/data scientist ส่วนใหญ่เริ่มจากคำถามง่าย ๆ เช่น:

- ขอเฉพาะข้อมูลของ Bangkok
- ขอเฉพาะสินค้า Electronics
- เรียง order จากยอดขายมากไปน้อย

### ทำใน notebook

- เลือกบาง columns
- filter rows ด้วยเงื่อนไข
- sort values

### แบบฝึก

1. แสดงเฉพาะ columns: `order_id`, `region`, `product`
2. กรองเฉพาะ region = `Bangkok`
3. กรองเฉพาะ category = `Electronics`
4. เรียงข้อมูลจาก `unit_price` สูงไปต่ำ
5. หา order ที่ quantity มากกว่า 5

## Day 3: คำนวณ column ใหม่

### Concept

ข้อมูลดิบมักยังตอบคำถามธุรกิจไม่ได้ทันที เราต้องสร้าง metric เพิ่ม เช่น:

- gross sales = จำนวนชิ้น x ราคาต่อหน่วย
- discount amount = ยอดก่อนลด x ส่วนลด
- net sales = ยอดก่อนลด - ส่วนลด

### ทำใน notebook

- สร้าง `gross_sales`
- สร้าง `discount_amount`
- สร้าง `net_sales`

### แบบฝึก

1. order ไหนมียอด `gross_sales` สูงที่สุด?
2. order ไหนได้ส่วนลดมากที่สุด?
3. ค่าเฉลี่ย `net_sales` ต่อ order คือเท่าไร?
4. total `net_sales` ทั้งหมดคือเท่าไร?

## Day 4: สรุปข้อมูลด้วย groupby

### Concept

`groupby` คือเครื่องมือสำคัญมาก ใช้ตอบคำถามแบบ “สรุปตามกลุ่ม” เช่น:

- ยอดขายตาม region
- ยอดขายตาม category
- จำนวนชิ้นขายตาม product
- ยอดขายตามประเภทลูกค้า

### ทำใน notebook

- groupby region
- groupby category
- groupby product
- groupby customer_type

### แบบฝึก

1. region ไหนยอดขายสุทธิมากที่สุด?
2. category ไหนยอดขายสุทธิมากที่สุด?
3. product ไหนขายได้จำนวนชิ้นมากที่สุด?
4. customer type ไหนสร้างยอดขายสุทธิมากกว่า?
5. region + category คู่ไหนทำยอดขายสูงที่สุด?

## Day 5: Mini Project

### งานหลัก

ทำ mini project จากไฟล์ `week01_mini_project.md`

### สิ่งที่ต้องส่งท้ายสัปดาห์

- notebook ที่รันได้ครบ
- learning log ที่มี insight อย่างน้อย 5 ข้อ
- ตอบคำถาม project ได้ด้วย pandas
- สรุปเป็นภาษาง่าย ๆ ว่าจากข้อมูลนี้ธุรกิจควรรู้อะไร
