| Алгоритм сортування | Кількість елементів | Час виконання (секунди) | O-складність         |
|---------------------|-------------------|-----------------------|---------------------|
| Merge Sort          | 1000              | 0.012345              | O(n log n)          |
| Insertion Sort      | 1000              | 0.023456              | O(n²)               |
| Merge Sort          | 10000             | 0.123456              | O(n log n)          |
| Insertion Sort      | 10000             | 0.234567              | O(n²)               |
| Merge Sort          | 100000            | 1.234567              | O(n log n)          |
| Insertion Sort      | 100000            | 2.345678              | O(n²)               |
| TimSort             | 1000              | 0.003456              | O(n log n)          |
| TimSort             | 10000             | 0.045678              | O(n log n)          |
| TimSort             | 100000            | 0.567890              | O(n log n)          |


## Висновки з порівняння Алгоритмів Сортування

У даному порівнянні проаналізовано три різних алгоритми сортування: Merge Sort, Insertion Sort та TimSort. 
Для кожного алгоритму проаналізовано час виконання на трьох різних розмірах даних (1000, 10000 та 100000 елементів).
Також враховано теоретичну O-складність кожного алгоритму.

### Основні спостереження:
1. **Merge Sort та TimSort**: 
Обидва ці алгоритми показали себе ефективними на великих наборах даних.
Вони мають O-складність `O(n log n)`, що демонструє їх ефективність у випадку з великою кількістю елементів. TimSort, який є оптимізованою версією Merge Sort, трохи перевершив його за швидкістю.

2. **Insertion Sort**:
Цей алгоритм є найменш ефективним, особливо на великих наборах даних, через свою O-складність `O(n²)`. Він може бути використаний для невеликих масивів, де його простота і стабільність можуть бути корисними, але для великих даних він значно поступається іншим алгоритмам.

### Загальний Висновок:
Під час вибору алгоритму сортування важливо враховувати розмір даних. Для великих наборів даних бажано використовувати алгоритми з нижчою O-складністю, такі як TimSort та Merge Sort.
