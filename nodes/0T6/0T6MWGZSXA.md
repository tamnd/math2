---
tag: 0T6MWGZSXA
kind: concept
name: Augmented matrix
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
specializes: [0VD9ZSWWJG]
uses: [0HQFZAP3ND, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Augmented_matrix
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 1.1
same_as:
  wikidata: Q2750301
  wikipedia: Augmented matrix
inventory: [7FF7WWJRZD]
---

## Summary

The augmented matrix of a system $Ax = b$ with $m$ equations in $n$ unknowns is the $m \times (n + 1)$ matrix $[A \mid b]$: the [[coefficient matrix|0HQFZAP3ND]] with the column of constant terms added on the right.
The main page, with examples and the exact definition, is [[the definition node|0YCDZ7N8VD]].
The augmented matrix matters because row reduction of $[A \mid b]$ solves the system and shows whether it is consistent.

## Motivation

During elimination, each equation changes as a whole, right side included.
Keeping the right sides in an extra column of the table lets us apply each row operation to the full equation at once.

## Remarks

### Examples

1. The system $2x + y = 5$, $x - 3y = 0$ has the augmented matrix $\left[\begin{array}{cc|c} 2 & 1 & 5 \\ 1 & -3 & 0 \end{array}\right]$.
2. Several right sides are handled at once with $[A \mid b \; c]$, see [[the example with two right-hand sides|KZ1G2TB2Q3]].
3. The reduced forms of $A$ and of $[A \mid b]$ can differ in rank, see [[the trap example|HCYVBVXBF4]].

### Non-examples

1. The coefficient matrix $A$ alone is not the augmented matrix.
2. An array built from a nonlinear system is not an augmented matrix, see [[the nonlinear array|VDC3D0JADY]].

### Basic properties

1. Row operations on $[A \mid b]$ keep the solution set, see [[the theorem on row operations|K41GT10YM6]].
2. The system is consistent exactly when $\rank [A \mid b] = \rank A$, see the [[Rouché-Capelli theorem|0HV1SKWPMS]].

### History

The vertical bar notation is common in modern textbooks such as Lay.
The counting-board arrays of the *Nine Chapters* already held the constants in the same array as the coefficients.

### Common errors

1. Row reducing $A$ and forgetting to apply the same operations to $b$.

## Explanations

### L1 human

The augmented matrix is the whole system written as a table of numbers.
The last column holds the numbers on the right of the equals signs, and a bar separates it.
For $2x + y = 5$, $x - 3y = 0$ the rows are $2, 1 \mid 5$ and $1, -3 \mid 0$.

### L2 human

See [[the definition node|0YCDZ7N8VD]] for a worked example.
A trap: a pivot in the last column means the equation $0 = 1$, not a value of an unknown.

### L3 human

$[A \mid b]$ is the coefficient matrix of the homogeneous system $Ax - bt = 0$ in $n + 1$ unknowns, see [[the definition node|0YCDZ7N8VD]].
