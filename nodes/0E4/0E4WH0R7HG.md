---
tag: 0E4WH0R7HG
kind: definition
name: Cayley table
msc: [20A05]
topics: [BAZT8JJ70S]
audience: school
defines: 0YB2NRP0T5
uses: [0M418FE7BB]
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

## Notation

The row label is the left factor and the column label is the right factor.
For a [[group|G5S1M9]], the identity is usually listed first.
Some books use the opposite convention, with the right factor in the rows.

## Remarks

The operation is [[commutative|099E72KTF8]] exactly when the table is symmetric about its main diagonal.
In the Cayley table of a finite group, each element occurs exactly one time in each row and one time in each column.
Thus the Cayley table of a finite group is a [[Latin square|CDVRMVED2V]].
A different order of the elements gives a table with the rows and the columns permuted in the same way.
The concept page [[Cayley table|0YB2NRP0T5]] gives the tables of all groups with at most $4$ elements.

## Explanations

### L1 human

A Cayley table is like the multiplication table from school, but for any finite set with an operation.
For the integers modulo $2$ under addition, the table has the rows $0, 1$ and $1, 0$.
You can read many properties from the table, for example if the operation is commutative.

### L2 human

To write a Cayley table, we follow three steps.

1. Choose an order of the elements, with the identity first when there is one.
2. Write the elements in this order as row labels and as column labels.
3. In row $a$ and column $b$, write $a \ast b$.

For the set $\{1, -1\}$ with multiplication, the rows are $1, -1$ and $-1, 1$.
A trap is to write $b \ast a$ in row $a$ and column $b$; for a commutative operation this gives the same table, but in general it does not.
