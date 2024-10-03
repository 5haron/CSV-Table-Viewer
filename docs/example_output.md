1. Display the table with default settings:
```bash
python3 showTable.py example.csv
```

```bash
╒══════════╤═══════════════╤═══════════════════════╤════════╤═════════════╤══════════════╤═══════════════════╤═══════════╤════════════╕
│   Number │ Name          │ Email                 │    Age │ Country     │ Phone        │ Occupation        │ Salary    │ Date       │
╞══════════╪═══════════════╪═══════════════════════╪════════╪═════════════╪══════════════╪═══════════════════╪═══════════╪════════════╡
│        1 │ Ddrraakkee    │ drraakkee@hello.com   │ 234324 │ USA         │ 123-456-7890 │ Software Engineer │           │ 1980       │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        2 │ Bad Bunnyy    │ badbunnybaby@ebay.com │     30 │ UK          │ 098-765-4321 │ Singer            │ -123      │ 2016-02-12 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        3 │ b33           │ beeee@yahoo.com       │      0 │ Spain       │ 345-678-9012 │ Designer          │ 1231      │ 2019-10-01 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        4 │ Bryson Tiller │ brybry@yas.com        │ -23423 │ Germany     │ 567-890-1234 │ Dancer            │ 22323     │ 2017-05-20 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        5 │ William Chen  │ wammo@word.com        │     32 │ France      │              │ Cashier           │ 88000     │ 2018-01-25 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        6 │ Sharon Li     │ sharonli@slay.com     │     27 │ Netherlands │ 789-012-3456 │                   │ 1         │ 2020-09-15 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        7 │ $$Ca$h        │                       │     40 │ Brazil      │ 901-234-5678 │ Accountant        │ 78000     │ 2015-03-30 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        8 │ Nikki Ng      │ nikki@yale.edu        │     33 │             │ 234-567-8901 │ Software Engineer │ 234234234 │ 2019-08-01 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        9 │ Jessica Chan  │ jessica@gmail.com     │      3 │ Russia      │ 345-678-9012 │ Unemployed        │ 0         │ 2021-02-01 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│       10 │ Bee eyonce    │ queen@newyork.com     │     31 │ Mexico      │ 456-789-0123 │ Professor         │ 12213242  │ 2017-11-01 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│       11 │ Jason Hoang   │ viet@gmail.com        │     26 │ Italy       │              │ President         │ 68000     │ 2020-04-05 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│       12 │ Dylan O'Brien │ dylan@bay.com         │     34 │ Ireland     │ 678-901-2345 │ Student           │ 75000     │ 2016-06-18 │
╘══════════╧═══════════════╧═══════════════════════╧════════╧═════════════╧══════════════╧═══════════════════╧═══════════╧════════════╛
```

2. Use a different column separator:
```bash
python3 showTable.py -s "|" example.csv
```

```bash
╒══════════════════════════════════════════════════════════════════════════════════════╕
│ Number,Name,Email,Age,Country,Phone,Occupation,Salary,Date                           │
╞══════════════════════════════════════════════════════════════════════════════════════╡
│ 1,Ddrraakkee,drraakkee@hello.com,234324,USA,123-456-7890,Software Engineer,,1980     │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ 2,Bad Bunnyy,badbunnybaby@ebay.com,30,UK,098-765-4321,Singer,-123,2016-02-12         │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ 3,b33,beeee@yahoo.com,0,Spain,345-678-9012,Designer,1231,2019-10-01                  │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ 4,Bryson Tiller,brybry@yas.com,-23423,Germany,567-890-1234,Dancer,22323,2017-05-20   │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ 5,William Chen,wammo@word.com,32,France,,Cashier,88000,2018-01-25                    │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ 6,Sharon Li,sharonli@slay.com,27,Netherlands,789-012-3456,,1,2020-09-15              │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ 7,$$Ca$h,,40,Brazil,901-234-5678,Accountant,78000,2015-03-30                         │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ 8,Nikki Ng,nikki@yale.edu,33,,234-567-8901,Software Engineer,234234234,2019-08-01    │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ 9,Jessica Chan,jessica@gmail.com,3,Russia,345-678-9012,Unemployed,0,2021-02-01       │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ 10,Bee eyonce,queen@newyork.com,31,Mexico,456-789-0123,Professor,12213242,2017-11-01 │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ 11,Jason Hoang,viet@gmail.com,26,Italy,,President,68000,2020-04-05                   │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ 12,Dylan O'Brien,dylan@bay.com,34,Ireland,678-901-2345,Student,75000,2016-06-18      │
╘══════════════════════════════════════════════════════════════════════════════════════╛
```

3. Display only column headers:
```bash
python3 showTable.py -l example.csv
```

```bash
╒════════╤══════╤═══════╤═════╤═════════╤═══════╤════════════╤════════╤══════╕
│ Number │ Name │ Email │ Age │ Country │ Phone │ Occupation │ Salary │ Date │
╘════════╧══════╧═══════╧═════╧═════════╧═══════╧════════════╧════════╧══════╛
```

4. Display the two following columns:
```bash
python3 showTable.py example.csv -o Phone Name 
```

```bash
╒══════════════╤═══════════════╕
│ Phone        │ Name          │
╞══════════════╪═══════════════╡
│ 123-456-7890 │ Ddrraakkee    │
├──────────────┼───────────────┤
│ 098-765-4321 │ Bad Bunnyy    │
├──────────────┼───────────────┤
│ 345-678-9012 │ b33           │
├──────────────┼───────────────┤
│ 567-890-1234 │ Bryson Tiller │
├──────────────┼───────────────┤
│              │ William Chen  │
├──────────────┼───────────────┤
│ 789-012-3456 │ Sharon Li     │
├──────────────┼───────────────┤
│ 901-234-5678 │ $$Ca$h        │
├──────────────┼───────────────┤
│ 234-567-8901 │ Nikki Ng      │
├──────────────┼───────────────┤
│ 345-678-9012 │ Jessica Chan  │
├──────────────┼───────────────┤
│ 456-789-0123 │ Bee eyonce    │
├──────────────┼───────────────┤
│              │ Jason Hoang   │
├──────────────┼───────────────┤
│ 678-901-2345 │ Dylan O'Brien │
╘══════════════╧═══════════════╛
```

5. Sort rows by the Name column in ascending order:
```bash
python3 showTable.py -u Name example.csv
```

```bash
╒══════════╤═══════════════╤═══════════════════════╤════════╤═════════════╤══════════════╤═══════════════════╤═══════════╤════════════╕
│   Number │ Name          │ Email                 │    Age │ Country     │ Phone        │ Occupation        │ Salary    │ Date       │
╞══════════╪═══════════════╪═══════════════════════╪════════╪═════════════╪══════════════╪═══════════════════╪═══════════╪════════════╡
│        7 │ $$Ca$h        │                       │     40 │ Brazil      │ 901-234-5678 │ Accountant        │ 78000     │ 2015-03-30 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        3 │ b33           │ beeee@yahoo.com       │      0 │ Spain       │ 345-678-9012 │ Designer          │ 1231      │ 2019-10-01 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        2 │ Bad Bunnyy    │ badbunnybaby@ebay.com │     30 │ UK          │ 098-765-4321 │ Singer            │ -123      │ 2016-02-12 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│       10 │ Bee eyonce    │ queen@newyork.com     │     31 │ Mexico      │ 456-789-0123 │ Professor         │ 12213242  │ 2017-11-01 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        4 │ Bryson Tiller │ brybry@yas.com        │ -23423 │ Germany     │ 567-890-1234 │ Dancer            │ 22323     │ 2017-05-20 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        1 │ Ddrraakkee    │ drraakkee@hello.com   │ 234324 │ USA         │ 123-456-7890 │ Software Engineer │           │ 1980       │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│       12 │ Dylan O'Brien │ dylan@bay.com         │     34 │ Ireland     │ 678-901-2345 │ Student           │ 75000     │ 2016-06-18 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│       11 │ Jason Hoang   │ viet@gmail.com        │     26 │ Italy       │              │ President         │ 68000     │ 2020-04-05 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        9 │ Jessica Chan  │ jessica@gmail.com     │      3 │ Russia      │ 345-678-9012 │ Unemployed        │ 0         │ 2021-02-01 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        8 │ Nikki Ng      │ nikki@yale.edu        │     33 │             │ 234-567-8901 │ Software Engineer │ 234234234 │ 2019-08-01 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        6 │ Sharon Li     │ sharonli@slay.com     │     27 │ Netherlands │ 789-012-3456 │                   │ 1         │ 2020-09-15 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        5 │ William Chen  │ wammo@word.com        │     32 │ France      │              │ Cashier           │ 88000     │ 2018-01-25 │
╘══════════╧═══════════════╧═══════════════════════╧════════╧═════════════╧══════════════╧═══════════════════╧═══════════╧════════════╛
```

6. Sort rows by the Name column in descending order:
```bash
python3 showTable.py -d Name example.csv
```

```bash
╒══════════╤═══════════════╤═══════════════════════╤════════╤═════════════╤══════════════╤═══════════════════╤═══════════╤════════════╕
│   Number │ Name          │ Email                 │    Age │ Country     │ Phone        │ Occupation        │ Salary    │ Date       │
╞══════════╪═══════════════╪═══════════════════════╪════════╪═════════════╪══════════════╪═══════════════════╪═══════════╪════════════╡
│        5 │ William Chen  │ wammo@word.com        │     32 │ France      │              │ Cashier           │ 88000     │ 2018-01-25 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        6 │ Sharon Li     │ sharonli@slay.com     │     27 │ Netherlands │ 789-012-3456 │                   │ 1         │ 2020-09-15 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        8 │ Nikki Ng      │ nikki@yale.edu        │     33 │             │ 234-567-8901 │ Software Engineer │ 234234234 │ 2019-08-01 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        9 │ Jessica Chan  │ jessica@gmail.com     │      3 │ Russia      │ 345-678-9012 │ Unemployed        │ 0         │ 2021-02-01 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│       11 │ Jason Hoang   │ viet@gmail.com        │     26 │ Italy       │              │ President         │ 68000     │ 2020-04-05 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│       12 │ Dylan O'Brien │ dylan@bay.com         │     34 │ Ireland     │ 678-901-2345 │ Student           │ 75000     │ 2016-06-18 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        1 │ Ddrraakkee    │ drraakkee@hello.com   │ 234324 │ USA         │ 123-456-7890 │ Software Engineer │           │ 1980       │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        4 │ Bryson Tiller │ brybry@yas.com        │ -23423 │ Germany     │ 567-890-1234 │ Dancer            │ 22323     │ 2017-05-20 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│       10 │ Bee eyonce    │ queen@newyork.com     │     31 │ Mexico      │ 456-789-0123 │ Professor         │ 12213242  │ 2017-11-01 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        2 │ Bad Bunnyy    │ badbunnybaby@ebay.com │     30 │ UK          │ 098-765-4321 │ Singer            │ -123      │ 2016-02-12 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        3 │ b33           │ beeee@yahoo.com       │      0 │ Spain       │ 345-678-9012 │ Designer          │ 1231      │ 2019-10-01 │
├──────────┼───────────────┼───────────────────────┼────────┼─────────────┼──────────────┼───────────────────┼───────────┼────────────┤
│        7 │ $$Ca$h        │                       │     40 │ Brazil      │ 901-234-5678 │ Accountant        │ 78000     │ 2015-03-30 │
╘══════════╧═══════════════╧═══════════════════════╧════════╧═════════════╧══════════════╧═══════════════════╧═══════════╧════════════╛
```

7. Filter rows based on the string "on":
```bash
python3 showTable.py -m "on" example.csv
```

```bash
╒═════╤═════════════════╤═══════════════════╤══════════╤═════════════╤════════════════╤═══════════╤══════════╤══════════════╕
│   4 │ Bryson Tiller   │ brybry@yas.com    │   -23423 │ Germany     │ 567-890-1234   │ Dancer    │    22323 │ 2017-05-20   │
╞═════╪═════════════════╪═══════════════════╪══════════╪═════════════╪════════════════╪═══════════╪══════════╪══════════════╡
│   6 │ Sharon Li       │ sharonli@slay.com │       27 │ Netherlands │ 789-012-3456   │           │        1 │ 2020-09-15   │
├─────┼─────────────────┼───────────────────┼──────────┼─────────────┼────────────────┼───────────┼──────────┼──────────────┤
│  10 │ Bee eyonce      │ queen@newyork.com │       31 │ Mexico      │ 456-789-0123   │ Professor │ 12213242 │ 2017-11-01   │
├─────┼─────────────────┼───────────────────┼──────────┼─────────────┼────────────────┼───────────┼──────────┼──────────────┤
│  11 │ Jason Hoang     │ viet@gmail.com    │       26 │ Italy       │                │ President │    68000 │ 2020-04-05   │
╘═════╧═════════════════╧═══════════════════╧══════════╧═════════════╧════════════════╧═══════════╧══════════╧══════════════╛
```

8. Display the first 10 rows of the table:
```bash
python3 showTable.py -n 10 example.csv
```

```bash
╒═════╤═══════════════╤═══════════════════════╤══════════╤═════════════╤════════════════╤═════════════════════╤═══════════╤════════════╕
│   1 │ Ddrraakkee    │ drraakkee@hello.com   │   234324 │ USA         │ 123-456-7890   │ Software Engineer   │           │ 1980       │
╞═════╪═══════════════╪═══════════════════════╪══════════╪═════════════╪════════════════╪═════════════════════╪═══════════╪════════════╡
│   2 │ Bad Bunnyy    │ badbunnybaby@ebay.com │       30 │ UK          │ 098-765-4321   │ Singer              │      -123 │ 2016-02-12 │
├─────┼───────────────┼───────────────────────┼──────────┼─────────────┼────────────────┼─────────────────────┼───────────┼────────────┤
│   3 │ b33           │ beeee@yahoo.com       │        0 │ Spain       │ 345-678-9012   │ Designer            │      1231 │ 2019-10-01 │
├─────┼───────────────┼───────────────────────┼──────────┼─────────────┼────────────────┼─────────────────────┼───────────┼────────────┤
│   4 │ Bryson Tiller │ brybry@yas.com        │   -23423 │ Germany     │ 567-890-1234   │ Dancer              │     22323 │ 2017-05-20 │
├─────┼───────────────┼───────────────────────┼──────────┼─────────────┼────────────────┼─────────────────────┼───────────┼────────────┤
│   5 │ William Chen  │ wammo@word.com        │       32 │ France      │                │ Cashier             │     88000 │ 2018-01-25 │
├─────┼───────────────┼───────────────────────┼──────────┼─────────────┼────────────────┼─────────────────────┼───────────┼────────────┤
│   6 │ Sharon Li     │ sharonli@slay.com     │       27 │ Netherlands │ 789-012-3456   │                     │         1 │ 2020-09-15 │
├─────┼───────────────┼───────────────────────┼──────────┼─────────────┼────────────────┼─────────────────────┼───────────┼────────────┤
│   7 │ $$Ca$h        │                       │       40 │ Brazil      │ 901-234-5678   │ Accountant          │     78000 │ 2015-03-30 │
├─────┼───────────────┼───────────────────────┼──────────┼─────────────┼────────────────┼─────────────────────┼───────────┼────────────┤
│   8 │ Nikki Ng      │ nikki@yale.edu        │       33 │             │ 234-567-8901   │ Software Engineer   │ 234234234 │ 2019-08-01 │
├─────┼───────────────┼───────────────────────┼──────────┼─────────────┼────────────────┼─────────────────────┼───────────┼────────────┤
│   9 │ Jessica Chan  │ jessica@gmail.com     │        3 │ Russia      │ 345-678-9012   │ Unemployed          │         0 │ 2021-02-01 │
├─────┼───────────────┼───────────────────────┼──────────┼─────────────┼────────────────┼─────────────────────┼───────────┼────────────┤
│  10 │ Bee eyonce    │ queen@newyork.com     │       31 │ Mexico      │ 456-789-0123   │ Professor           │  12213242 │ 2017-11-01 │
╘═════╧═══════════════╧═══════════════════════╧══════════╧═════════════╧════════════════╧═════════════════════╧═══════════╧════════════╛
```