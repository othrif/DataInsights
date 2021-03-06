---
title: "DataFrames counting"
date: 2020-04-12T14:41:32+02:00
author: "Othmane Rifki"
type: technical_note
draft: false
---
Most common summary statistics: 
- `.mean()`
- `.std()`
- `.var()`
- `.median()`
- `.mode()`
- `.min()`
- `.max()`
- `.sum()`
- `.quantile()`

### Generate some data


```python
import pandas as pd
import numpy as np
from pandas import Timestamp

mycols = ['store', 'type', 'department', 'date', 'weekly_sales', 'is_holiday']
content = np.array([[1, 'A', 1, Timestamp('2010-02-05 00:00:00'), 24924.5, False],[1, 'B', 1, Timestamp('2010-03-05 00:00:00'), 21827.9, True],[1, 'A', 1, Timestamp('2010-04-02 00:00:00'), 57258.43, False],[1, 'C', 1, Timestamp('2010-05-07 00:00:00'), 17413.94, False],[1, 'C', 1, Timestamp('2010-06-04 00:00:00'), 17558.09, False],[1, 'C', 1, Timestamp('2010-07-02 00:00:00'), 16333.14, False],[1, 'C', 1, Timestamp('2010-08-06 00:00:00'), 17508.41, False],[1, 'B', 1, Timestamp('2010-09-03 00:00:00'), 16241.78, False],[1, 'A', 1, Timestamp('2010-10-01 00:00:00'), 20094.19, True],[1, 'B', 1, Timestamp('2010-11-05 00:00:00'), 34238.88, False],[1, 'C', 1, Timestamp('2010-12-03 00:00:00'), 22517.56, False],[1, 'A', 1, Timestamp('2011-01-07 00:00:00'), 15984.24, False],[1, 'C', 2, Timestamp('2010-02-05 00:00:00'), 50605.27, True],[1, 'A', 2, Timestamp('2010-03-05 00:00:00'), 48397.98, False],[1, 'A', 2, Timestamp('2010-04-02 00:00:00'), 47450.5, False],[1, 'A', 2, Timestamp('2010-05-07 00:00:00'), 47903.01, False],[1, 'A', 2, Timestamp('2010-06-04 00:00:00'), 48754.47, False],[1, 'A', 2, Timestamp('2010-07-02 00:00:00'), 47077.72, False],[1, 'A', 2, Timestamp('2010-08-06 00:00:00'), 50031.73, False],[1, 'A', 2, Timestamp('2010-09-03 00:00:00'), 49015.05, False],[1, 'A', 2, Timestamp('2010-10-01 00:00:00'), 45829.02, False],[1, 'A', 2, Timestamp('2010-11-05 00:00:00'), 46381.43, True],[1, 'A', 2, Timestamp('2010-12-03 00:00:00'), 44405.02, False],[1, 'A', 2, Timestamp('2011-01-07 00:00:00'), 43202.29, False],[1, 'A', 3, Timestamp('2010-02-05 00:00:00'), 13740.12, False],[1, 'A', 3, Timestamp('2010-03-05 00:00:00'), 12275.58, False],[1, 'A', 3, Timestamp('2010-04-02 00:00:00'), 11157.08, False],[1, 'A', 3, Timestamp('2010-05-07 00:00:00'), 9372.8, True],[1, 'A', 3, Timestamp('2010-06-04 00:00:00'), 8001.41, False],[1, 'C', 3, Timestamp('2010-07-02 00:00:00'), 7857.88, True],[1, 'A', 3, Timestamp('2010-08-06 00:00:00'), 26719.02, False],[1, 'A', 3, Timestamp('2010-09-03 00:00:00'), 19081.8, False],[1, 'B', 3, Timestamp('2010-10-01 00:00:00'), 9775.17, False],[1, 'A', 3, Timestamp('2010-11-05 00:00:00'), 9825.22, False],[1, 'A', 3, Timestamp('2010-12-03 00:00:00'), 10856.85, False],[1, 'A', 3, Timestamp('2011-01-07 00:00:00'), 15808.15, False],[1, 'A', 4, Timestamp('2010-02-05 00:00:00'), 39954.04, False],[1, 'A', 4, Timestamp('2010-03-05 00:00:00'), 38086.19, False],[1, 'A', 4, Timestamp('2010-04-02 00:00:00'), 37809.49, False],[1, 'A', 4, Timestamp('2010-05-07 00:00:00'), 37168.34, False],[1, 'A', 4, Timestamp('2010-06-04 00:00:00'), 40548.19, False],[1, 'B', 4, Timestamp('2010-07-02 00:00:00'), 39773.71, False],[1, 'A', 4, Timestamp('2010-08-06 00:00:00'), 40973.88, False],[1, 'A', 4, Timestamp('2010-09-03 00:00:00'), 38321.88, False],[1, 'A', 4, Timestamp('2010-10-01 00:00:00'), 34912.45, False],[1, 'A', 4, Timestamp('2010-11-05 00:00:00'), 37980.55, False],[1, 'A', 4, Timestamp('2010-12-03 00:00:00'), 37110.55, False],[1, 'A', 4, Timestamp('2011-01-07 00:00:00'), 37947.8, False],[1, 'A', 5, Timestamp('2010-02-05 00:00:00'), 32229.38, False],[1, 'A', 5, Timestamp('2010-03-05 00:00:00'), 23082.14, False],[1, 'B', 5, Timestamp('2010-04-02 00:00:00'), 29967.92, False],[1, 'A', 5, Timestamp('2010-05-07 00:00:00'), 19260.44, False],[1, 'A', 5, Timestamp('2010-06-04 00:00:00'), 22932.26, False],[1, 'A', 5, Timestamp('2010-07-02 00:00:00'), 18887.71, False],[1, 'A', 5, Timestamp('2010-08-06 00:00:00'), 16926.17, False],[1, 'A', 5, Timestamp('2010-09-03 00:00:00'), 15390.52, False],[1, 'A', 5, Timestamp('2010-10-01 00:00:00'), 23381.38, False],[1, 'A', 5, Timestamp('2010-11-05 00:00:00'), 23903.81, False],[1, 'A', 5, Timestamp('2010-12-03 00:00:00'), 36472.02, False],[1, 'A', 5, Timestamp('2011-01-07 00:00:00'), 22699.69, False],[1, 'A', 6, Timestamp('2010-02-05 00:00:00'), 5749.03, False],[1, 'A', 6, Timestamp('2010-03-05 00:00:00'), 4221.25, False],[1, 'A', 6, Timestamp('2010-04-02 00:00:00'), 4132.61, False],[1, 'A', 6, Timestamp('2010-05-07 00:00:00'), 7477.7, False],[1, 'A', 6, Timestamp('2010-06-04 00:00:00'), 5484.9, False],[1, 'A', 6, Timestamp('2010-07-02 00:00:00'), 4541.91, False],[1, 'A', 6, Timestamp('2010-08-06 00:00:00'), 4700.38, False],[1, 'A', 6, Timestamp('2010-09-03 00:00:00'), 3553.75, False],[1, 'B', 6, Timestamp('2010-10-01 00:00:00'), 2876.19, False],[1, 'A', 6, Timestamp('2010-11-05 00:00:00'), 5036.99, False],[1, 'A', 6, Timestamp('2010-12-03 00:00:00'), 6356.96, False],[1, 'A', 6, Timestamp('2011-01-07 00:00:00'), 1376.15, False],[1, 'A', 7, Timestamp('2010-02-05 00:00:00'), 21084.08, False],[1, 'A', 7, Timestamp('2010-03-05 00:00:00'), 19659.7, False],[1, 'A', 7, Timestamp('2010-04-02 00:00:00'), 22427.62, False],[1, 'A', 7, Timestamp('2010-05-07 00:00:00'), 20457.62, False],[1, 'A', 7, Timestamp('2010-06-04 00:00:00'), 44563.68, False],[1, 'A', 7, Timestamp('2010-07-02 00:00:00'), 22589.0, False],[1, 'A', 7, Timestamp('2010-08-06 00:00:00'), 21842.57, False],[1, 'A', 7, Timestamp('2010-09-03 00:00:00'), 18005.65, False],[1, 'A', 7, Timestamp('2010-10-01 00:00:00'), 16481.79, False],[1, 'A', 7, Timestamp('2010-11-05 00:00:00'), 19136.58, False],[1, 'A', 7, Timestamp('2010-12-03 00:00:00'), 47406.83, False],[1, 'A', 7, Timestamp('2011-01-07 00:00:00'), 17516.16, False],[1, 'A', 8, Timestamp('2010-02-05 00:00:00'), 40129.01, False],[1, 'A', 8, Timestamp('2010-03-05 00:00:00'), 38776.09, False],[1, 'A', 8, Timestamp('2010-04-02 00:00:00'), 38151.58, False],[1, 'A', 8, Timestamp('2010-05-07 00:00:00'), 35393.78, False],[1, 'A', 8, Timestamp('2010-06-04 00:00:00'), 35181.47, False],[1, 'A', 8, Timestamp('2010-07-02 00:00:00'), 35580.01, False],[1, 'A', 8, Timestamp('2010-08-06 00:00:00'), 34833.35, False],[1, 'A', 8, Timestamp('2010-09-03 00:00:00'), 35562.68, False],[1, 'A', 8, Timestamp('2010-10-01 00:00:00'), 34658.25, False],[1, 'A', 8, Timestamp('2010-11-05 00:00:00'), 36182.58, False],[1, 'A', 8, Timestamp('2010-12-03 00:00:00'), 36222.74, False],[1, 'A', 8, Timestamp('2011-01-07 00:00:00'), 36599.46, False],[1, 'A', 9, Timestamp('2010-02-05 00:00:00'), 16930.99, False],[1, 'A', 9, Timestamp('2010-03-05 00:00:00'), 24064.7, False],[1, 'A', 9, Timestamp('2010-04-02 00:00:00'), 25435.02, False],[1, 'A', 9, Timestamp('2010-05-07 00:00:00'), 27588.34, False]])
df = pd.DataFrame(content, columns=mycols)
df['frac_sales'] = df['weekly_sales']*np.random.rand()
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>store</th>
      <th>type</th>
      <th>department</th>
      <th>date</th>
      <th>weekly_sales</th>
      <th>is_holiday</th>
      <th>frac_sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>A</td>
      <td>1</td>
      <td>2010-02-05</td>
      <td>24924.5</td>
      <td>False</td>
      <td>11757.6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>B</td>
      <td>1</td>
      <td>2010-03-05</td>
      <td>21827.9</td>
      <td>True</td>
      <td>10296.9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>A</td>
      <td>1</td>
      <td>2010-04-02</td>
      <td>57258.4</td>
      <td>False</td>
      <td>27010.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>C</td>
      <td>1</td>
      <td>2010-05-07</td>
      <td>17413.9</td>
      <td>False</td>
      <td>8214.67</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>C</td>
      <td>1</td>
      <td>2010-06-04</td>
      <td>17558.1</td>
      <td>False</td>
      <td>8282.67</td>
    </tr>
  </tbody>
</table>
</div>



### Drop duplicates with `.drop_duplicates()`


```python
df.drop_duplicates(subset='type')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>store</th>
      <th>type</th>
      <th>department</th>
      <th>date</th>
      <th>weekly_sales</th>
      <th>is_holiday</th>
      <th>frac_sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>A</td>
      <td>1</td>
      <td>2010-02-05</td>
      <td>24924.5</td>
      <td>False</td>
      <td>11757.6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>B</td>
      <td>1</td>
      <td>2010-03-05</td>
      <td>21827.9</td>
      <td>True</td>
      <td>10296.9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>C</td>
      <td>1</td>
      <td>2010-05-07</td>
      <td>17413.9</td>
      <td>False</td>
      <td>8214.67</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.drop_duplicates(subset=['type','is_holiday'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>store</th>
      <th>type</th>
      <th>department</th>
      <th>date</th>
      <th>weekly_sales</th>
      <th>is_holiday</th>
      <th>frac_sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>A</td>
      <td>1</td>
      <td>2010-02-05</td>
      <td>24924.5</td>
      <td>False</td>
      <td>11757.6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>B</td>
      <td>1</td>
      <td>2010-03-05</td>
      <td>21827.9</td>
      <td>True</td>
      <td>10296.9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>C</td>
      <td>1</td>
      <td>2010-05-07</td>
      <td>17413.9</td>
      <td>False</td>
      <td>8214.67</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>B</td>
      <td>1</td>
      <td>2010-09-03</td>
      <td>16241.8</td>
      <td>False</td>
      <td>7661.72</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1</td>
      <td>A</td>
      <td>1</td>
      <td>2010-10-01</td>
      <td>20094.2</td>
      <td>True</td>
      <td>9479.02</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1</td>
      <td>C</td>
      <td>2</td>
      <td>2010-02-05</td>
      <td>50605.3</td>
      <td>True</td>
      <td>23872</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_unique = df.drop_duplicates(subset=['type','is_holiday'])
```

### Count with `.value_counts()`


```python
df_unique['type'].value_counts()
```




    C    2
    A    2
    B    2
    Name: type, dtype: int64




```python
df_unique['type'].value_counts(sort=True)
```




    C    2
    A    2
    B    2
    Name: type, dtype: int64




```python
df_unique['type'].value_counts(normalize=True)
```




    C    0.333333
    A    0.333333
    B    0.333333
    Name: type, dtype: float64



### Grouping with `.groupby()`


```python
df.groupby('type')['weekly_sales'].min()
```




    type
    A    1376.15
    B    2876.19
    C    7857.88
    Name: weekly_sales, dtype: float64



Example of how much the syntax gets simplified with `.groupby()`


```python
# Calc total weekly sales
sales_all = df["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = df[df["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = df[df["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = df[df["type"] == "C"]["weekly_sales"].sum()

print('all=', sales_all)
print('A ', sales_A)
print('B ', sales_B)
print('C ', sales_C)
```

    all= 2629115.29
    A  2324619.4500000007
    B  154701.55
    C  149794.29



```python
df.groupby('type')['weekly_sales'].sum()
```




    type
    A    2324619.45
    B     154701.55
    C     149794.29
    Name: weekly_sales, dtype: float64




```python
print('A ', sales_A/sales_all)
print('B ', sales_B/sales_all)
print('C ', sales_C/sales_all)
```

    A  0.8841831542503412
    B  0.05884167597686444
    C  0.056975169772794564



```python
df.groupby("type")["weekly_sales"].sum()/df['weekly_sales'].sum()
```




    type
    A    0.884183
    B    0.058842
    C    0.056975
    Name: weekly_sales, dtype: float64



#### Multiple categories


```python
df.groupby(['type','is_holiday'])['weekly_sales'].sum()
```




    type  is_holiday
    A     False         2248771.03
          True            75848.42
    B     False          132873.65
          True            21827.90
    C     False           91331.14
          True            58463.15
    Name: weekly_sales, dtype: float64



#### Multiple grouped summaries


```python
df.groupby('type')['weekly_sales'].agg([np.min,np.max])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>amin</th>
      <th>amax</th>
    </tr>
    <tr>
      <th>type</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>1376.15</td>
      <td>57258.43</td>
    </tr>
    <tr>
      <th>B</th>
      <td>2876.19</td>
      <td>39773.71</td>
    </tr>
    <tr>
      <th>C</th>
      <td>7857.88</td>
      <td>50605.27</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby('type')[['weekly_sales','frac_sales']].agg([np.min,np.max])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">weekly_sales</th>
      <th colspan="2" halign="left">frac_sales</th>
    </tr>
    <tr>
      <th></th>
      <th>amin</th>
      <th>amax</th>
      <th>amin</th>
      <th>amax</th>
    </tr>
    <tr>
      <th>type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>1376.15</td>
      <td>57258.43</td>
      <td>1141.613223</td>
      <td>47499.895208</td>
    </tr>
    <tr>
      <th>B</th>
      <td>2876.19</td>
      <td>39773.71</td>
      <td>2386.001914</td>
      <td>32995.090104</td>
    </tr>
    <tr>
      <th>C</th>
      <td>7857.88</td>
      <td>50605.27</td>
      <td>6518.664179</td>
      <td>41980.631009</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
