# Week 4 Checklist

เช็คก่อนข้ามไปสัปดาห์ที่ 5 ครับ ถ้าตอบ "ยัง" หรือ "งง" ในข้อไหน ให้กลับไปทบทวนเฉพาะข้อนั้นก่อน

## SQL พื้นฐาน

- [ ] อธิบายลำดับการเขียน SQL ได้: `SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ... LIMIT`
- [ ] รู้ว่า `WHERE` กับ `HAVING` ต่างกันอย่างไร
- [ ] ใช้ `LIKE`, `IN`, `BETWEEN`, `IS NULL` ได้ถูกสถานการณ์
- [ ] ใช้ `DISTINCT` ได้และรู้ว่ามันทำอะไร
- [ ] ใช้ `ORDER BY ... DESC`, `LIMIT` ได้

## Aggregation

- [ ] ใช้ `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` ได้
- [ ] ใช้ `GROUP BY` หลายคอลัมน์ได้
- [ ] ใช้ alias (`AS`) ให้ผลลัพธ์อ่านง่าย
- [ ] เข้าใจว่าทำไม `SELECT category, name, AVG(price) FROM products GROUP BY category` ถึงไม่ make sense

## JOIN

- [ ] เขียน `INNER JOIN` 2 ตารางได้
- [ ] เขียน `LEFT JOIN` 2 ตาราง และเข้าใจว่าทำไมบางแถวมี NULL
- [ ] Join 3 ตารางขึ้นไปได้ (เช่น orders + order_items + products)
- [ ] หา "สินค้าที่ไม่เคยถูกสั่ง" ด้วย LEFT JOIN + IS NULL ได้

## Advanced

- [ ] เขียน subquery ใน `WHERE` ได้
- [ ] ใช้ `CASE WHEN` เพื่อสร้าง column ใหม่ได้
- [ ] ใช้ window function พื้นฐาน เช่น `ROW_NUMBER()`, `RANK()`, `SUM() OVER (PARTITION BY ...)` ได้

## SQL + pandas

- [ ] โหลด query result เข้า pandas DataFrame ได้ (`pd.read_sql`)
- [ ] รู้ว่าเมื่อไรควรทำงานบน SQL และเมื่อไรควรย้ายไปทำใน pandas

## Business thinking

- [ ] ตอบ business question ด้วย SQL ได้อย่างน้อย 5 ข้อ
- [ ] เขียน business summary 1 หน้าได้ (mini project)
- [ ] อธิบาย insight ได้โดยไม่ใช้ศัพท์เทคนิค

## House-keeping

- [ ] commit งานสัปดาห์ที่ 4 ขึ้น GitHub แล้ว
- [ ] อัปเดต `learning_log.md` ของสัปดาห์นี้แล้ว
