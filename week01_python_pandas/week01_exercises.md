# Week 1 Exercises

ใช้ dataset: `../data/simple_sales.csv`

ให้ทำใน `week01_python_pandas.ipynb` หรือสร้าง notebook ใหม่ชื่อ `week01_extra_practice.ipynb`

## Part 1: สำรวจข้อมูล

1. อ่านไฟล์ CSV ด้วย pandas
2. แสดง 5 แถวแรก
3. แสดง 5 แถวท้าย
4. เช็กจำนวน rows และ columns
5. เช็กชนิดข้อมูลของแต่ละ column
6. ดู summary statistics ของ columns ตัวเลข

## Part 2: เลือก columns

1. แสดงเฉพาะ `order_id`
2. แสดงเฉพาะ `region` และ `product`
3. แสดงเฉพาะ `quantity`, `unit_price`, `discount`
4. แสดง 10 แถวแรกของ columns: `order_date`, `region`, `category`, `product`

## Part 3: Filter rows

1. แสดงเฉพาะ order จาก `Bangkok`
2. แสดงเฉพาะ order จาก `Chiang Mai`
3. แสดงเฉพาะ category = `Electronics`
4. แสดงเฉพาะ quantity มากกว่า 5
5. แสดงเฉพาะ discount มากกว่า 0
6. แสดงเฉพาะ region = `Bangkok` และ category = `Office`

## Part 4: Sort values

1. เรียงข้อมูลตาม `unit_price` จากมากไปน้อย
2. เรียงข้อมูลตาม `quantity` จากมากไปน้อย
3. เรียงข้อมูลตาม `discount` จากมากไปน้อย
4. หลังสร้าง `net_sales` แล้ว ให้เรียงตาม `net_sales` จากมากไปน้อย

## Part 5: Calculated columns

สร้าง columns เหล่านี้:

- `gross_sales` = `quantity` * `unit_price`
- `discount_amount` = `gross_sales` * `discount`
- `net_sales` = `gross_sales` - `discount_amount`

จากนั้นตอบ:

1. total gross sales เท่าไร?
2. total discount amount เท่าไร?
3. total net sales เท่าไร?
4. net sales เฉลี่ยต่อ order เท่าไร?
5. order ไหน net sales สูงที่สุด?

## Part 6: Groupby

ตอบด้วย pandas:

1. net sales รวมตาม region
2. net sales รวมตาม category
3. quantity รวมตาม product
4. net sales รวมตาม customer_type
5. net sales เฉลี่ยตาม category
6. จำนวน order ตาม region
7. net sales รวมตาม region และ category

## Part 7: เขียน insight

เลือกผลลัพธ์ 5 ข้อ แล้วเขียนเป็นภาษาคน เช่น:

- Bangkok มียอดขายสุทธิสูงที่สุด แปลว่าตลาดหลักของข้อมูลชุดนี้อยู่ที่ Bangkok
- Electronics เป็นหมวดที่สร้างรายได้มากที่สุด แม้จำนวน order ไม่ได้เยอะที่สุด

ไม่ต้องใช้ประโยคยาว ขอให้อ่านแล้วเข้าใจว่า “ตัวเลขนี้แปลว่าอะไร”
