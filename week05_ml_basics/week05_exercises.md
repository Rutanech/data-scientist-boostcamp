# Week 5 Exercises — Machine Learning Basics

## Part 1: Concepts (ตอบเป็น markdown ใน notebook)

**Q1.** Supervised Learning ต่างจาก Unsupervised Learning อย่างไร? ยกตัวอย่างอย่างละ 2 กรณีการใช้งาน

**Q2.** ในโจทย์ต่อไปนี้ อะไรคือ Features และอะไรคือ Target?
- ทำนายราคาบ้านจากขนาด ทำเล จำนวนห้อง
- ทำนายว่าลูกค้าจะเลิกใช้บริการหรือไม่ จากอายุ ยอดซื้อ ความถี่การใช้งาน

**Q3.** ทำไมต้องแบ่ง Train และ Test set? ถ้าไม่แบ่งจะเกิดอะไรขึ้น?

---

## Part 2: Regression (แก้โค้ดใน notebook)

**Ex 2.1** โหลด `churn_data.csv` และสำรวจข้อมูล (shape, dtypes, head)

**Ex 2.2** สร้าง Linear Regression เพื่อทำนาย `monthly_charges` จาก `tenure` และ `num_services`
- แบ่ง train/test 80/20
- วัดผลด้วย MAE และ R²
- Plot กราฟ Actual vs Predicted

**Ex 2.3** ทดลองเพิ่ม feature อื่น ๆ แล้วดูว่า R² เปลี่ยนไปยังไง

---

## Part 3: Classification (แก้โค้ดใน notebook)

**Ex 3.1** สร้าง Logistic Regression เพื่อทำนาย `churn` (0 = ยังอยู่, 1 = เลิกใช้)
- ใช้ features: `tenure`, `monthly_charges`, `num_services`
- วัดผลด้วย accuracy และ confusion matrix

**Ex 3.2** สร้าง Decision Tree และเปรียบเทียบกับ Logistic Regression

**Ex 3.3** สร้าง Random Forest และเปรียบเทียบกับสองโมเดลก่อน

**Ex 3.4** ดู feature importance ของ Random Forest — feature ไหนสำคัญที่สุด?

---

## Part 4: Business Thinking

**Q4.** ถ้าโมเดลทำนาย churn ได้ accuracy 82% ถือว่าดีหรือไม่? มีข้อจำกัดอะไรบ้าง?

**Q5.** ถ้าคุณเป็น Data Scientist ของบริษัท Telecom จะใช้ผลจากโมเดลนี้ยังไง? เสนอ action 2-3 อย่าง
