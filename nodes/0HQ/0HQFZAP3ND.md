---
tag: 0HQFZAP3ND
kind: concept
name: Coefficient matrix
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
specializes: [0VD9ZSWWJG]
uses: [0GT4WWGWH2, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Coefficient_matrix
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 1.1
same_as:
  wikidata: Q5140577
  wikipedia: Coefficient matrix
---

## Summary

The coefficient matrix of a [[system of linear equations|0GT4WWGWH2]] with $m$ equations in $n$ unknowns is the $m \times n$ [[matrix|0VD9ZSWWJG]] $A = (a_{ij})$, where $a_{ij}$ is the coefficient of $x_j$ in equation $i$.
The system is then the matrix equation $Ax = b$.
The main page, with examples and the exact definition, is [[the definition node|0P7A2MJD24]].
The coefficient matrix matters because it carries all the information about uniqueness of solutions and about the homogeneous system.

## Motivation

Writing every unknown in every row is slow, and the names of the unknowns do not change during elimination.
Only the numbers change, so we keep only the numbers in a table.

## Remarks

### Examples

1. The system $2x + y = 5$, $x - 3y = 0$ has the coefficient matrix $\begin{bmatrix} 2 & 1 \\ 1 & -3 \end{bmatrix}$.
2. The system in [[the example with missing unknowns|2E4TZ2ZV57]] needs zero entries for the missing unknowns.
3. A homogeneous system $Ax = 0$ is given by its coefficient matrix alone.

### Non-examples

1. The [[augmented matrix|0T6MWGZSXA]] $[A \mid b]$ has one more column than the coefficient matrix.
2. The array read off before all unknowns are moved to the left side is not the coefficient matrix, see [[the example with unknowns on both sides|PE7H79RRY9]].

### Basic properties

1. $Ax$ is a [[linear combination|0V8F3E48E6]] of the columns of $A$, see [[linear systems as vector equations|E7SAHXQEVC]].
2. A consistent system $Ax = b$ has a unique solution exactly when every column of $A$ has a pivot, see [[the existence and uniqueness theorem|BKA191KD1S]].

### History

Arrays of coefficients on a counting board were used in the *Nine Chapters on the Mathematical Art*.
Sylvester introduced the word "matrix" in 1850.

### Common errors

1. Forgetting zero entries for unknowns that do not appear in an equation.

## Explanations

### L1 human

The coefficient matrix is the table of numbers in front of the unknowns.
Each row is one equation and each column is one unknown.
For $2x + y = 5$, $x - 3y = 0$, the table has rows $2, 1$ and $1, -3$.

### L2 human

See [[the definition node|0P7A2MJD24]] for a worked example.
A trap: put all unknowns in the same order in every row before you read the table.

### L3 human

The coefficient matrix is the matrix of the linear map $x \mapsto Ax$ in the standard bases, see [[the definition node|0P7A2MJD24]].
