# Week 4 Exercises

แบบฝึกหัดของสัปดาห์ที่ 4 แบ่งตามวัน ทำในเซลล์ของ `week04_sql_analysis.ipynb` หรือเขียนแยกเป็นไฟล์ `.sql` ก็ได้

> เคล็ดลับ: ลองคิดคำตอบในหัวก่อนเขียน query แล้วเปรียบเทียบกับผลที่ได้จริงเสมอ จะช่วยให้พัฒนาเร็วขึ้นมาก

---

## Day 1 — SELECT, WHERE, ORDER BY, LIMIT

ใช้ตาราง `customers` และ `products`

1. แสดง `customer_id`, `first_name`, `last_name`, `country` ของทุกคน
2. แสดงลูกค้าเฉพาะที่อยู่ประเทศ Thailand
3. แสดงลูกค้าที่อยู่ Bangkok หรือ Chiang Mai (ใช้ `IN`)
4. แสดงรายชื่อ `country` ที่ไม่ซ้ำกัน (ใช้ `DISTINCT`)
5. แสดงสินค้าทั้งหมด เรียงจากราคาแพงไปถูก
6. แสดงสินค้าที่ราคาอยู่ระหว่าง 500–2000 บาท (ใช้ `BETWEEN`)
7. แสดงสินค้า category Electronics ที่ราคาน้อยกว่า 2000 บาท เรียงราคาจากน้อยไปมาก
8. หาสินค้าที่ชื่อมีคำว่า "Pen" หรือ "Pencil" (ใช้ `LIKE`)
9. แสดงลูกค้าที่ลงทะเบียนหลังวันที่ 2024-06-30 (ใช้เปรียบเทียบสตริงวันที่)
10. แสดงสินค้า 5 อันดับที่ "กำไรต่อชิ้น" (price - cost) สูงสุด — สร้าง column ใหม่ใน SELECT

### โจทย์ challenge (ไม่บังคับ)

- แสดงลูกค้าที่อยู่ในประเทศที่ขึ้นต้นด้วย "T" (Thailand, Taiwan) เรียงตาม `signup_date` จากเก่าสุดไปใหม่สุด 10 คนแรก

---

## Day 2 — GROUP BY, Aggregate, HAVING

1. นับจำนวนลูกค้าต่อ `country`
2. นับจำนวนสินค้าต่อ `category` พร้อมราคาเฉลี่ย
3. ราคาสูงสุดและต่ำสุดของสินค้าในแต่ละ category
4. หา category ที่มีสินค้า "มากกว่า 3 ชิ้น" (ใช้ HAVING)
5. นับจำนวน order ต่อ `status`
6. นับจำนวน order ต่อเดือน (ใช้ `strftime('%Y-%m', order_date)`)

---

## Day 3 — JOIN

1. ดึง order ทั้งหมดพร้อมชื่อลูกค้า (orders + customers)
2. คำนวณ revenue ต่อ order (sum ของ quantity * unit_price) — ใช้ orders + order_items
3. คำนวณ revenue ต่อ category (orders + order_items + products) เฉพาะ status = 'completed'
4. หา top 5 ลูกค้าตาม revenue รวม
5. หาสินค้าที่ "ไม่เคยถูกสั่งเลย" (LEFT JOIN + WHERE IS NULL)

---

## Day 4 — Subquery, CASE WHEN, Window

1. หาลูกค้าที่ใช้จ่ายมากกว่าค่าเฉลี่ยรวม (subquery)
2. สร้าง column `customer_tier`:
   - High: total revenue >= 5000
   - Medium: 1000 <= total revenue < 5000
   - Low: < 1000
3. จัดอันดับลูกค้าตาม revenue ภายในแต่ละประเทศ (`RANK() OVER (PARTITION BY country ORDER BY revenue DESC)`)
4. คำนวณ running total ของ revenue รายเดือน
5. หา percent ของ revenue ที่ลูกค้าแต่ละคนสร้าง เทียบกับ revenue ทั้งหมด

---

## เช็คหลังทำเสร็จ

- เขียน query ได้ในครั้งแรกโดยไม่ดูตัวอย่างกี่ข้อ?
- ข้อไหนติด ให้กลับไปอ่าน notebook ส่วนที่เกี่ยวข้องอีกครั้ง
- สิ่งที่ติดบ่อยให้จดลง `learning_log.md`
