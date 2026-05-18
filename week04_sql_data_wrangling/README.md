# Week 4: SQL & Data Wrangling

ยินดีต้อนรับสู่สัปดาห์ที่ 4 ของ Data Scientist Boostcamp ครับ สัปดาห์นี้เราจะเริ่มใช้ภาษา SQL ซึ่งเป็นภาษาหลักของคนทำงานกับข้อมูลในบริษัทจริง ๆ ทั้ง Data Analyst, Data Scientist, Data Engineer ใช้ SQL ทุกวัน เป้าหมายของสัปดาห์นี้คือดึงข้อมูล รวมข้อมูลจากหลายตาราง และคำนวณ business metric ได้ด้วย SQL

## เป้าหมายของสัปดาห์

- เขียน SQL query อ่านง่ายและถูกต้องได้
- ใช้ SELECT, WHERE, GROUP BY, JOIN, subquery, CASE WHEN, window function พื้นฐาน
- รู้จัก SQL + pandas workflow สำหรับงาน Data Science
- ตอบคำถามทางธุรกิจจาก ecommerce database ได้

## โครงสร้างของสัปดาห์ (5 วัน)

| Day | หัวข้อ |
|-----|--------|
| 1 | SELECT, WHERE, ORDER BY, LIMIT (วันนี้) |
| 2 | GROUP BY, Aggregate functions, HAVING |
| 3 | JOIN: INNER, LEFT, RIGHT |
| 4 | Subquery, CASE WHEN, Window functions |
| 5 | Mini project: ecommerce analysis + business summary |

## ไฟล์ในโฟลเดอร์นี้

- `ecommerce.db` — ฐานข้อมูล SQLite จำลอง (customers, products, orders, order_items)
- `build_ecommerce_db.py` — สคริปต์สร้าง DB ใหม่ (ถ้าอยาก reset)
- `week04_sql_analysis.ipynb` — notebook หลักของสัปดาห์ (Day 1 พร้อมใช้แล้ว)
- `week04_study_plan.md` — แผนเรียนรายวัน
- `week04_exercises.md` — แบบฝึกหัด
- `week04_mini_project.md` — โจทย์ mini project
- `week04_checklist.md` — checklist ก่อนข้ามสัปดาห์
- `learning_log.md` — สมุดบันทึกการเรียน

## Schema ของ ecommerce database

```
customers
├── customer_id      INTEGER PK
├── first_name       TEXT
├── last_name        TEXT
├── email            TEXT
├── city             TEXT
├── country          TEXT
└── signup_date      TEXT (YYYY-MM-DD)

products
├── product_id       INTEGER PK
├── product_name     TEXT
├── category         TEXT
├── price            REAL
└── cost             REAL

orders
├── order_id         INTEGER PK
├── customer_id      INTEGER FK -> customers
├── order_date       TEXT (YYYY-MM-DD)
└── status           TEXT  (completed / cancelled / refunded / pending)

order_items
├── order_item_id    INTEGER PK
├── order_id         INTEGER FK -> orders
├── product_id       INTEGER FK -> products
├── quantity         INTEGER
└── unit_price       REAL
```

ข้อมูลโดยประมาณ: customers ~50 คน, products 20 รายการ, orders ~110 รายการ, order_items ~280 แถว

## วิธีเริ่ม Day 1

1. เปิด `week04_sql_analysis.ipynb` ใน Jupyter / VS Code
2. รันเซลล์ตามลำดับ (Shift+Enter)
3. ทำแบบฝึกหัดท้าย notebook ก่อนข้ามไปวันถัดไป
4. จดสิ่งที่เรียนรู้ลง `learning_log.md`
