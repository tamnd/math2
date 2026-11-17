---
tag: 0YB2NRP0T5
kind: concept
name: Cayley table
aliases: [multiplication-table]
msc: [20A05]
topics: [BAZT8JJ70S]
audience: school
uses: [0M418FE7BB]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley_table
    locator: Structure and layout
  - url: https://en.wikipedia.org/wiki/Cayley_table
    locator: Properties and uses
  - book: isbn:9780471433347
    locator: Section 1.1
same_as:
  wikidata: Q1546924
  wikipedia: Cayley table
inventory: [S5VMKP5TYZ]
---

## Summary

Let $S = \{a_1, \ldots, a_n\}$ be a finite set with a [[binary operation|0M418FE7BB]] $\ast$.
The Cayley table of $(S, \ast)$ is the $n \times n$ table with the entry $a_i \ast a_j$ in row $i$ and column $j$.
The table contains the full information about the operation.
For a finite [[group|G5S1M9]], each element occurs exactly one time in each row and in each column, so the table is a [[Latin square|CDVRMVED2V]].
The group is [[abelian|082GHNPJ53]] exactly when its table is symmetric about the main diagonal.
Cayley tables let us write down small groups completely and compare them.

## Motivation

A finite group has only finitely many products, so we can list all of them.
The list is clearest as a table, in the same way as the multiplication table of school arithmetic.
With the table, we can compute in the group without a formula for the operation.
We can also read properties of the group from the table, such as the identity, the inverses and commutativity.
Two groups with the same table, after a renaming of the elements, have the same structure.

## Notation

The row label is the left factor and the column label is the right factor: the entry in row $a$ and column $b$ is $ab$.
Most books list the identity first, so the first row and the first column repeat the labels.
Some books put the right factor in the rows.
For an abelian group the two conventions give the same table, but for other groups they give transposed tables.

## Remarks

### Examples

We write the identity first in each table.

1. The trivial group $\{e\}$ has the table with the single entry $ee = e$.
2. The group $\mathbb{Z}/2\mathbb{Z} = \{0, 1\}$ under addition modulo $2$ has the rows $0, 1$ and $1, 0$.
3. The group [[$\mathbb{Z}/3\mathbb{Z}$|03VFZ2WETT]] $= \{0, 1, 2\}$ under addition modulo $3$ has the rows $0, 1, 2$ and $1, 2, 0$ and $2, 0, 1$.
4. The group $\mathbb{Z}/4\mathbb{Z} = \{0, 1, 2, 3\}$ under addition modulo $4$ has the rows $0, 1, 2, 3$ and $1, 2, 3, 0$ and $2, 3, 0, 1$ and $3, 0, 1, 2$. Its main diagonal is $0, 2, 0, 2$.
5. The [[Cayley table of the Klein four-group|7XQ1G27N7H]] $\{e, a, b, c\}$ has the rows $e, a, b, c$ and $a, e, c, b$ and $b, c, e, a$ and $c, b, a, e$. Its main diagonal is $e, e, e, e$.
6. The [[Cayley table of the symmetric group S3|N8JZF84SZ3]] is a $6 \times 6$ table that is not symmetric, because $S_3$ is not abelian.

### Non-examples

1. [[A Latin square that is not the Cayley table of a group|TJ3CZ91FJ9]]: the table of subtraction modulo $3$ has each element one time in each row and column, but the operation has no identity and is not associative.
2. The table of multiplication modulo $4$ on $\{0, 1, 2, 3\}$ is the Cayley table of a monoid, not of a group. The row of $0$ is $0, 0, 0, 0$, so it repeats an element, and $0$ has no inverse.
3. The addition table of the integers $0$ and $1$ is not a Cayley table of an operation on $\{0, 1\}$, because the entry $1 + 1 = 2$ is not in the set.

### Basic properties

1. In the table of a group, each row and each column contains each element exactly one time. Reason: the [[cancellation laws|0VSNX4P2Q0]] show that $x \mapsto ax$ and $x \mapsto xa$ are bijections.
2. The row of the identity repeats the column labels, and the column of the identity repeats the row labels.
3. The inverse of $a$ is the label of the column in which $e$ occurs in row $a$. By [[uniqueness of identity and inverses|0D9NDGE9KP]], $e$ then also occurs in row $a^{-1}$, column $a$.
4. A group is abelian if and only if its table is symmetric about the main diagonal, because the entry in row $a$, column $b$ is $ab$ and the entry in row $b$, column $a$ is $ba$.
5. Associativity is not visible in the table in a simple way. A direct check of a table with $n$ elements needs $n^3$ triples.
6. After a renaming of the elements, there is exactly one group of each order $1$, $2$ and $3$, and there are exactly two groups of order $4$: $\mathbb{Z}/4\mathbb{Z}$ and the [[Klein four-group|0PMRQJVTME]]. The explanation L2 below proves this.

### History

Arthur Cayley introduced such tables in 1854, in his paper on abstract groups.
He used them to describe the groups of order $4$ and $6$.
In 1896 Ferdinand Georg Frobenius studied the determinant of a Cayley table with variables as entries, and this work started the theory of group characters.

### Common errors

1. The rows and columns are exchanged. For a group that is not abelian, this gives the table of $ba$ in place of $ab$.
2. A Latin square is taken to be the table of a group. Each group table is a Latin square, but the converse is false.
3. The table is read as symmetric without a check. Only abelian groups have symmetric tables.

## Explanations

### L1 human

A Cayley table is like the multiplication table from school, but for any small set with an operation.
Each row is for the first element and each column is for the second element.
The box where they meet holds the result.
For a clock with $4$ hours, numbered $0, 1, 2, 3$, adding hours gives the table with the rows $0, 1, 2, 3$ and $1, 2, 3, 0$ and $2, 3, 0, 1$ and $3, 0, 1, 2$.
In this table each row contains each number one time, just like a Sudoku row.

### L2 human

We find all group tables with $3$ or $4$ elements, and we use only the rule that each row and each column contains each element one time.
First let $G = \{e, a, b\}$ be a group with $3$ elements.

1. The row and column of $e$ are fixed by property 2.
2. In row $a$, the entry $aa$ is not $a$, because column $a$ already has $a$ in row $e$.
3. If $aa = e$, then row $a$ is $a, e, b$, so $ab = b$, but column $b$ already has $b$ in row $e$. So $aa = b$, and row $a$ is $a, b, e$.
4. Column $a$ is now $a, b$, so $ba = e$, and the last entry of row $b$ is $bb = a$.

So there is only one possible table, and it is the table of $\mathbb{Z}/3\mathbb{Z}$ with $a = 1$ and $b = 2$.
The same rule gives only one table for $1$ and $2$ elements.

Now let $G = \{e, a, b, c\}$ be a group with $4$ elements.

5. Suppose that $xx = e$ for each $x \in G$. The entry $ab$ is not $e$, because $aa = e$ and $e$ occurs one time in row $a$. It is not $a$ or $b$, because column $b$ has $b$ in row $e$ and row $a$ has $a$ in column $e$. So $ab = c$. In the same way, each product of two different elements of $a, b, c$ is the third one. This is the table of the Klein four-group.
6. Otherwise, rename the elements so that $aa \neq e$. Then $aa \neq a$, by the Latin square rule, so we may call $aa = b$.
7. The entry $ab$ is not $a$ or $b$, because column $b$ and row $a$ already contain these elements in the first row and column. If $ab = e$, then $ac$ is not $e$, $a$ or $c$, and $ac = b = aa$ gives $c = a$ by cancellation. This is impossible, so $ab = c$.
8. The entry $ac$ is not $a$ or $c$, and $ac = b = aa$ would give $c = a$. So $ac = e$. Then the powers $a, a^2 = b, a^3 = c, a^4 = e$ give the table of $\mathbb{Z}/4\mathbb{Z}$ with $a = 1$, $b = 2$ and $c = 3$.

So there are at most two group tables with $4$ elements, up to renaming.
Both tables occur, because $\mathbb{Z}/4\mathbb{Z}$ and the Klein four-group are groups.
They are different, because the main diagonal of $\mathbb{Z}/4\mathbb{Z}$ contains $2$ and the main diagonal of the Klein four-group contains only $e$.

### L3 human

A finite set with a binary operation whose table is a Latin square is a finite [[quasigroup|ZJD31SPPFP]].
So the groups are the associative quasigroups, and a Latin square is a group table only when the associated operation is associative.
Two groups are [[isomorphic|08MG7H8JW5]] exactly when one table becomes the other after a renaming of the elements and a reordering of the rows and columns.
The number of groups of order $n$ grows fast with $n$, so tables are useful only for small groups.
For larger groups we use generators and relations, permutations or matrices instead.
The [[Cayley graph|0GYQK9NDJF]] is a different picture of a group, built from a set of generators.
