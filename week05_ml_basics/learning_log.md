# Learning Log — Week 5: Machine Learning Basics

**วันที่:** 2026-05-23

---

## สิ่งที่เรียนในสัปดาห์นี้

### Concepts ที่เข้าใจแล้ว

- **Supervised vs Unsupervised Learning** — Supervised มี label (คำตอบ) ให้โมเดลเรียน เช่น ทำนาย churn / Unsupervised ไม่มี label ต้องหา pattern เอง เช่น Clustering
- **Features & Target** — X คือข้อมูล input, y คือสิ่งที่ต้องการทำนาย
- **Train/Test Split** — สำคัญมาก ถ้าไม่แบ่งโมเดลจะ "จำ" ข้อมูลแทนที่จะ "เรียน"
- **Linear Regression** — ทำนายตัวเลขต่อเนื่อง วัดด้วย MAE และ R²
- **Logistic Regression** — ชื่อ Regression แต่จริง ๆ ใช้ทำ Classification ทำนาย 0 หรือ 1
- **Decision Tree** — ตัดสินใจแบบ if-else เป็นต้นไม้ อ่านง่าย แต่ overfit ง่ายถ้า max_depth ไม่กำหนด
- **Random Forest** — รวม Decision Tree หลายต้น ผลลัพธ์มาจากเสียงส่วนใหญ่ แม่นกว่า tree เดี่ยว
- **scikit-learn workflow** — `.fit()` → `.predict()` → `accuracy_score()` → จบ!

### โค้ดที่ใช้บ่อย

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(accuracy_score(y_test, y_pred))
```

---

## ผลลัพธ์ Mini Project

**Dataset:** churn_data.csv (500 ลูกค้า Telecom, churn rate ~18%)

| โมเดล | Accuracy |
|---|---:|
| Logistic Regression | ดูใน notebook |
| Decision Tree | ดูใน notebook |
| Random Forest | สูงสุด ✅ |

**Key Insight:**
- ลูกค้าที่ tenure สั้น (< 12 เดือน) มีความเสี่ยง churn สูงกว่ามาก
- Month-to-month contract มี churn rate สูงสุด
- Random Forest ดีที่สุดเพราะรวม tree หลายต้น ลด variance ได้

---

## สิ่งที่ยังงงอยู่ / ต้องเรียนต่อ

- [ ] Confusion matrix: precision vs recall ต่างกันยังไง และเลือกใช้เมื่อไหร่?
- [ ] Overfitting หมายความว่าอะไรชัด ๆ และแก้ยังไง?
- [ ] Feature scaling (StandardScaler) จำเป็นไหมสำหรับ Random Forest?

→ Week 6 จะตอบคำถามเหล่านี้ทั้งหมด!

---

## สิ่งที่ภูมิใจ

- สร้าง ML model ได้ครบ 3 ตัว ตั้งแต่ต้นจนจบ
- เข้าใจ business context และ recommend action ได้
- Notebook clean และอ่านง่าย

---

## Next Steps

- เริ่ม Week 6: Model Evaluation & Feature Engineering
- ทบทวน precision/recall และ ROC-AUC
- Commit งานลง GitHub ✅
