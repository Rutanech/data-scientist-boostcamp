# Week 4 Mini Project: Ecommerce SQL Analysis

ลองสวมบทบาทเป็น Data Analyst ของบริษัท ecommerce เล็ก ๆ ที่เพิ่งเปิดมา 1-2 ปี หัวหน้าฝ่ายการตลาดเดินมาถามคำถามต่อไปนี้ ภารกิจคือใช้ SQL ดึงคำตอบจาก `ecommerce.db` แล้วเขียนสรุปเป็น business summary ให้หัวหน้าอ่าน

## คำถามทางธุรกิจที่ต้องตอบ

1. **Revenue overview** — Revenue รวมของบริษัทเท่าไหร่ (เฉพาะ order ที่ `status = 'completed'`) แยกตามเดือนเป็นอย่างไร
2. **Top customers** — ใครคือ 10 ลูกค้าที่ใช้จ่ายมากที่สุด แต่ละคนซื้อกี่ครั้ง ใช้จ่ายเฉลี่ยต่อ order เท่าไหร่
3. **Top products & categories** — สินค้าและ category ไหนทำ revenue เยอะที่สุด
4. **Country performance** — ประเทศไหนคือตลาดที่ใหญ่ที่สุด และมีศักยภาพรองลงมาคือประเทศไหน
5. **Cancellation / refund** — ออเดอร์ที่ถูก cancel หรือ refund คิดเป็นกี่ % และมี category ใดที่มี rate สูงผิดปกติไหม
6. **Repeat customer** — กี่ % ของลูกค้าซื้อมากกว่า 1 ครั้ง (repeat rate)
7. **Customer segmentation** — แบ่งลูกค้าเป็น High / Medium / Low value (ใช้ CASE WHEN) แต่ละกลุ่มมีกี่คน และสร้าง revenue รวมเท่าไหร่

## Deliverables

1. ไฟล์ `week04_sql_analysis.sql` — รวม query ทั้งหมดที่ใช้ ตั้งชื่อ comment ให้ชัดว่าแต่ละ block ตอบคำถามข้อไหน
2. ไฟล์ `week04_sql_summary.md` — Business summary 1 หน้า ประกอบด้วย
   - 5-7 insight ที่สำคัญ
   - ตารางสรุป (markdown table) ที่จำเป็น
   - คำแนะนำ 2-3 ข้อให้ฝ่ายการตลาด
3. (ตัวเลือก) Notebook เพิ่มเติมที่ visualize ผลด้วย matplotlib/seaborn

## เกณฑ์ที่ดี

- Query อ่านง่าย ใช้ alias, จัด indent
- Insight อ้างอิงตัวเลขจริงจาก query ไม่ใช่เดา
- Recommendation ตอบ "แล้วบริษัทควรทำอะไรต่อ" ได้ ไม่ใช่แค่บอกตัวเลข
- ไม่ลืม edge case เช่น order ที่ถูก cancel ไม่ควรนับใน revenue

## Stretch goals (ทำได้ถ้ามีเวลา)

- ทำ cohort analysis เบื้องต้น: เปรียบเทียบลูกค้าที่ signup ในแต่ละไตรมาส ว่าเฉลี่ยใช้จ่ายต่างกันไหม
- เขียน query หา "products often bought together" (สินค้า 2 รายการที่อยู่ใน order เดียวกันบ่อยที่สุด)
- ลอง export ผลจาก SQL เป็น pandas DataFrame แล้ววาดกราฟ
