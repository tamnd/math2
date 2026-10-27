---
tag: 0E4WH0R7HG
kind: definition
name: Cayley table
msc: [20A05]
defines: 0YB2NRP0T5
uses: [0580ZJSA3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley_table
    locator: Structure and layout
  - url: https://en.wikipedia.org/wiki/Cayley_table
    locator: Properties and uses
inventory: [S5VMKP5TYZ]
---

## Definition

Let $S = \{a_1, \ldots, a_n\}$ be a finite set with $n$ elements, listed in a fixed order, and let $\ast$ be a [[binary operation|0M418FE7BB]] on $S$.
The Cayley table of $(S, \ast)$ is the $n \times n$ table whose rows and columns are labelled $a_1, \ldots, a_n$.
The entry in row $i$ and column $j$ is $a_i \ast a_j$.

## Remarks

The operation is [[commutative|099E72KTF8]] exactly when the table is symmetric about its main diagonal.
In the Cayley table of a finite [[group|G5S1M9]], each element occurs exactly one time in each row and one time in each column.
Thus the Cayley table of a finite group is a Latin square.

## Explanations

### L1 human

A Cayley table is like the multiplication table from school, but for any finite set with an operation.
For the integers modulo $2$ under addition, the table has the rows $0, 1$ and $1, 0$.
You can read many properties from the table, for example if the operation is commutative.
