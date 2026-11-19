---
tag: 0YCDZ7N8VD
kind: definition
name: Augmented matrix
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
defines: 0T6MWGZSXA
uses: [0P7A2MJD24]
sources:
  - url: https://en.wikipedia.org/wiki/Augmented_matrix
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 1.1
inventory: [7FF7WWJRZD]
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]].
Take a [[system of linear equations|0GT4WWGWH2]] $Ax = b$ over $F$, with [[coefficient matrix|0HQFZAP3ND]] $A$ of size $m \times n$ and constant vector $b \in F^m$.
The *augmented matrix* of the system is the $m \times (n+1)$ matrix $[A \mid b]$.
Its first $n$ columns are the columns of $A$, and its last column is $b$.
More generally, for an $m \times k$ matrix $B$, the matrix $[A \mid B]$ is the $m \times (n + k)$ matrix whose first $n$ columns are those of $A$ and whose last $k$ columns are those of $B$.

## Notation

1. The bar in $[A \mid b]$ only marks where the equals signs were; some books write $[A \; b]$ or $(A, b)$ without a bar.
2. Row $i$ of $[A \mid b]$ is written $(a_{i1}, \dots, a_{in} \mid b_i)$.

## Remarks

### Examples

1. The system $2x + y = 5$, $x - 3y = 0$ has the augmented matrix $\left[\begin{array}{cc|c} 2 & 1 & 5 \\ 1 & -3 & 0 \end{array}\right]$.
2. Conversely, the augmented matrix $\left[\begin{array}{ccc|c} 1 & 0 & 2 & 3 \\ 0 & 1 & -1 & 1 \end{array}\right]$ in the unknowns $x, y, z$ is the system $x + 2z = 3$, $y - z = 1$.
3. Two systems $Ax = b$ and $Ax = c$ with the same $A$ are solved together by reducing $[A \mid b \; c]$, see [[the example with two right-hand sides|~697909d5]].
4. The inverse of an invertible $A$ is found by reducing $[A \mid I]$ to $[I \mid A^{-1}]$, see [[the inverse example|~3f9cc605]].

### Non-examples

1. The coefficient matrix $\begin{bmatrix} 2 & 1 \\ 1 & -3 \end{bmatrix}$ of example 1 is not the augmented matrix: it lacks the column $b$.
2. The table $\left[\begin{array}{cc|c} 1 & 1 & 3 \\ 1 & -1 & 1 \end{array}\right]$ obtained from $x^2 + y = 3$, $x - y = 1$ by treating $x^2$ as $x$ is not an augmented matrix of that system, see [[the nonlinear array|~81e627f4]].

### Basic properties

1. The system is determined by $[A \mid b]$ once the order of the unknowns is fixed, and conversely.
2. [[Elementary row operations|04XWH28452]] on $[A \mid b]$ do not change the solution set of the system, see [[the theorem on row operations|~6410ee51]].
3. A row operation on $[A \mid B]$ acts on $A$ and $B$ together: $E[A \mid B] = [EA \mid EB]$ for every matrix $E$ with $m$ columns.
4. The system is inconsistent exactly when an echelon form of $[A \mid b]$ has a pivot in the last column, see [[the existence and uniqueness theorem|BKA191KD1S]].
5. The rank of $[A \mid b]$ is $\rank A$ or $\rank A + 1$; it is $\rank A$ exactly when the system is consistent, by the [[Rouché-Capelli theorem|0HV1SKWPMS]].

### Common errors

1. Reducing $A$ alone and then trying to read off the solution of $Ax = b$; the operations must also act on $b$, see [[the trap example|~7ea020f3]].
2. Treating the last column as an unknown, so that a pivot there is read as a value of a variable instead of the equation $0 = 1$.

## Explanations

### L1 human

The augmented matrix is the full system written as a table of numbers.
Each row is one equation, and the last column holds the numbers on the right of the equals signs.
The vertical bar reminds us where the equals signs were.
We do row reduction on this table instead of rewriting the equations each time.

### L2 human

We solve $x + 2y = 5$, $3x + 4y = 6$ with its augmented matrix.

1. Write $\left[\begin{array}{cc|c} 1 & 2 & 5 \\ 3 & 4 & 6 \end{array}\right]$.
2. $R_2 \leftarrow R_2 - 3R_1$ gives $(0, -2 \mid -9)$.
3. $R_2 \leftarrow -\tfrac12 R_2$ gives $(0, 1 \mid \tfrac92)$.
4. $R_1 \leftarrow R_1 - 2R_2$ gives $(1, 0 \mid -4)$.
5. So $x = -4$ and $y = \tfrac92$.
6. Check: $-4 + 9 = 5$ and $-12 + 18 = 6$.

The typical use is to keep the bookkeeping of elimination short and safe.
A trap: the [[reduced row echelon form|0WF5AQYTW6]] of $[A \mid b]$ and that of $A$ are different matrices, and they can have different ranks.

### L3 human

The augmented matrix $[A \mid b]$ is the coefficient matrix of the homogeneous system $Ax - b t = 0$ in the $n + 1$ unknowns $(x, t)$.
The solutions of $Ax = b$ correspond to the solutions of this homogeneous system with $t = 1$.
This is the projective view of an affine system, and it explains why consistency is a statement about the last column.
The augmentation principle says that the RREF of $[A \mid B]$ begins with the RREF of $A$, see [[the augmentation principle|BE3NZP35HY]].
