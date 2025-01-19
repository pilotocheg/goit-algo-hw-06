# goit-algo-hw-06

## Завдання 2

Маємо такий вивід у консоль (початкова вершина - Київ):

```shell
Результат обходу в ширину:
['Kyiv', 'Poltava', 'Lviv', 'Vinnytsia', 'Chernihiv', 'Odesa', 'Kharkiv', 'Sumy', 'Uzhorod', 'Mykolaiv', 'Dnipro', 'Zaporizhzhia', 'Mariupol'] 

Результат обходу в глибину:
['Kyiv', 'Lviv', 'Uzhorod', 'Vinnytsia', 'Odesa', 'Mykolaiv', 'Zaporizhzhia', 'Dnipro', 'Kharkiv', 'Poltava', 'Sumy', 'Chernihiv', 'Mariupol']
```

Бачимо що результат для обох обходів різний. Це пов'язано з тим що обхід в ширину спочатку проходиться по найближчих сусідах заданої вершини і далі збільшує радіус обходу. А обхід в глибину йде вглиб рекурсивно поки не дійде до кінця гілки, а потім повертається назад і продовжує обхід.
