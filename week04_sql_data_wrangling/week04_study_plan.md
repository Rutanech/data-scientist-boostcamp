# Week 4 Study Plan: SQL & Data Wrangling

สัปดาห์นี้เป็นสัปดาห์ที่ "เรียนภาษาใหม่" ครั้งแรกของคอร์ส อย่ารีบ ให้เน้นเขียน query เยอะ ๆ เพราะ SQL เก่งขึ้นจากการเขียน ไม่ใช่จากการอ่าน

## Day 1: SELECT, WHERE, ORDER BY, LIMIT

### เรียนเรื่อง

- โครงสร้าง SQL query เบื้องต้น
- การเลือก column ด้วย `SELECT`
- การกรองแถวด้วย `WHERE`
- ตัวดำเนินการ: `=`, `!=`, `>`, `<`, `>=`, `<=`, `AND`, `OR`, `NOT`, `LIKE`, `IN`, `BETWEEN`, `IS NULL`
- การเรียงด้วย `ORDER BY` (ASC / DESC)
- การจำกัดผลลัพธ์ด้วย `LIMIT`
- รู้จักคำสั่ง `DISTINCT`

### ทำ

- เชื่อมต่อ `ecommerce.db` ผ่าน sqlite3 ใน notebook
- ดู schema และข้อมูลตัวอย่างจากทุกตาราง
- เขียน query ตอบคำถาม เช่น "ลูกค้าจากประเทศไทยมีกี่คน?", "สินค้า Electronics ที่ราคาต่ำกว่า 1000 บาทมีอะไรบ้าง?"
- ทำแบบฝึกหัด Day 1 ใน `week04_exercises.md` ทั้งหมด

## Day 2: GROUP BY, Aggregate, HAVING

### เรียนเรื่อง

- Aggregate functions: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- `GROUP BY` หลายระดับ
- `HAVING` ต่างกับ `WHERE` อย่างไร
- การใช้ alias (`AS`)

### ทำ

- หายอดขายรวมต่อ category
- หาจำนวนลูกค้าต่อประเทศ
- หา product ที่ขายดี top 5
- สรุปข้อแตกต่างของ `WHERE` กับ `HAVING` ลง learning log

## Day 3: JOIN

### เรียนเรื่อง

- INNER JOIN, LEFT JOIN, RIGHT JOIN (SQLite ไม่มี RIGHT JOIN ตรง ๆ แต่ logic เหมือนกัน)
- การ join หลายตาราง
- การใช้ alias เพื่ออ่านง่าย
- ระวังกรณี duplicate หลัง join

### ทำ

- Join orders + customers เพื่อหาว่าใครเป็นคนสั่ง
- Join orders + order_items + products เพื่อคำนวณ revenue ต่อ order
- หา top 5 customers ตาม revenue
- หาสินค้าที่ไม่เคยถูกสั่ง (เทคนิค LEFT JOIN + IS NULL)

## Day 4: Subquery, CASE WHEN, Window functions

### เรียนเรื่อง

- Subquery ใน `WHERE`, `FROM`, `SELECT`
- `CASE WHEN ... THEN ... ELSE ... END`
- Window functions: `ROW_NUMBER`, `RANK`, `SUM() OVER (PARTITION BY ...)`
- เมื่อไรควรใช้ window function แทน group by

### ทำ

- จัดอันดับลูกค้าตาม revenue ภายในแต่ละประเทศ (RANK + PARTITION BY)
- สร้าง column "customer tier" ด้วย CASE WHEN (High / Medium / Low)
- คำนวณ running total ของยอดขายรายเดือน

## Day 5: Mini Project

ทำ mini project ใน `week04_mini_project.md` และสรุปเป็น business summary

ผลลัพธ์ที่ควรได้:

- ไฟล์ `week04_sql_analysis.sql` ที่รวม query สำคัญทั้งหมด
- `week04_sql_summary.md` สรุป business insight 5-7 ข้อ พร้อม recommendation
- commit ขึ้น GitHub

---

ตอนจบสัปดาห์ลองถามตัวเองว่า:

- ถ้าหัวหน้าให้ตาราง 3 ตาราง แล้วถามว่า "revenue เดือนนี้เท่าไหร่ แยกตาม category" เขียน SQL ได้ในไม่เกิน 5 นาทีไหม
- อ่าน query ของคนอื่นแล้วเข้าใจไหมว่าเขาตอบคำถามอะไร
