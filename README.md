# DSP301x_asm2_vyntFX11699-funix.edu.vn
This program allows user to enter file name, then analyze each line in the input file whether valid or not and notify user the invalid lines with specific causes. 
Then calculate the total grades and some basic statistic calculations for each valid line and finally export the results to ".txt" files.

## Description
1. First, ask user to enter the name of input file, then open and read it if this file exists, notify and ask the user to retry if it doesn't. 
The below sample is an example of expected result:

```bash
Enter a class file to grade (i.e. class1 for class1.txt): foobar
File cannot be found.
Enter a class file to grade (i.e. class1 for class1.txt): class1
Successfully opened class1.txt
```

2. Next, analyse data lines in the input file to ensure it follows the format and count total of valid and invalid lines. Each file contains lines of students' ID and their answers in the following format:

```python
N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D
```
or 

```python
N12345678,B,,D,,C,B,,A,C,C,,B,A,B,A,,,,A,C,A,A,B,D,
```
- The first element is student's ID which startedy N and followedy 8 digits, the 25 remaining letters are students' exam answers. Every element is splitted by a comma, if there is no character between two commas, it means that student passed this question without giving answer.

**Note that** there are some invalid lines. For instance, the line below doesn't have enough answers:

```python
N12345678,B,A,D,D,C,B
```
Or the below example has too much answers:

```python
N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D,A,B,C,D,E
```
- Notify the user about the invalid line and its cause. The expected output as below:

```python
Successfully opened class2.txt
**** ANALYZING ****
Invalid line of data: does not contain exactly 26 values:
N00000023,,A,D,D,C,B,D,A,C,C,,C,,B,A,C,B,D,A,C,A,A
Invalid line of data: N# is invalid
N0000002,B,A,D,D,C,B,D,A,C,D,D,D,A,,A,C,D,,A,C,A,A,B,D,D
Invalid line of data: N# is invalid
NA0000027,B,A,D,D,,B,,A,C,B,D,B,A,,A,C,B,D,A,,A,A,B,D,D
Invalid line of data: does not contain exactly 26 values:
N00000035,B,A,D,D,B,B,,A,C,,D,B,A,B,A,A,B,D,A,C,A,C,B,D,D,A,A
**** REPORT ****
Total valid lines of data: 21
Total invalid lines of data: 4
```

3. After that, grading the students' exam (grade scale 100) and make some basic statistics calculations: max, min, mean, median and range of scores. Each correct answer will gain 4 points, 0 for passed answer and minus 1 point for every wrong one.
And display the result of basic statistics

```python
Mean (average) score: 78.00
Highest score: 100
Lowest score: 66
Range of scores: 34
Median score: 76
```

4. Finally, export the result to a text file according to the class in the origin input file with file name as: "classX_grades.txt". Each line in result file follows the format as: student's ID, student's grade.
A sample from the result file:

```python
# this is what class2_grades.txt should look like
N00000021,68
N00000022,76
....
N00000045,67
```
