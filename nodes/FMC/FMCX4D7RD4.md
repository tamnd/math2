---
tag: FMCX4D7RD4
kind: statement
role: lemma
name: Uniqueness of the inverse matrix
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: ug1
about: [0EB9N0S33C]
uses: [0TWTS88TWN, 073E4XC016, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Properties
  - book: isbn:9780321982384
    locator: Section 2.2
  - book: isbn:9780135367971
    locator: Section 1.6
---

## Statement

A left inverse and a right inverse of the same matrix are equal, so a matrix has at most one inverse.
Let $R$ be a commutative ring and let $A$, $B$ and $C$ be $n \times n$ matrices over $R$, with $I_n$ the [[identity matrix|06DW9BAWB1]].

1. If $CA = I_n$ and $AB = I_n$, then $B = C$.
2. In particular, if $B$ and $C$ are both [[inverses|0TWTS88TWN]] of $A$, then $B = C$.

## Remarks

### Why both sides are needed

Part 1 pairs a left inverse with a right inverse, and that pairing is what forces equality.
Two right inverses of one matrix can differ.
For the $1 \times 2$ matrix $A = (1 \;\; 0)$, both columns $B = (1, 0)^{\mathsf{T}}$ and $B' = (1, 5)^{\mathsf{T}}$ give
$$AB = 1 \cdot 1 + 0 \cdot 0 = 1, \qquad AB' = 1 \cdot 1 + 0 \cdot 5 = 1.$$
So a matrix can have many right inverses, but once it also has a left inverse, all of them collapse to one.

The square shape and the commutativity of $R$ are not needed for part 1.
The proof uses only the [[associativity of matrix multiplication|073E4XC016]] and the identity matrices.
For an $m \times n$ matrix $A$, two $n \times m$ matrices $C$ and $B$ with $CA = I_n$ and $AB = I_m$ are equal by the same argument.

### What it gives you

The notation $A^{-1}$ is well defined, because there is only one matrix it can name.
To prove that a matrix $X$ is the inverse of $A$, it is enough to check $AX = XA = I_n$, and no search for other candidates is needed.
The [[rules for inverses|2ZH4X4Q99D]] and the [[inverse of a product|0S4WTRE9GG]] work exactly this way.
A matrix with both a left and a right inverse is invertible, and both one-sided inverses equal $A^{-1}$.

For a worked use, take $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ and $C = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}$.
Then
$$CA = \begin{pmatrix} 1 & 2 - 2 \\ 0 & 1 \end{pmatrix} = I_2,$$
so if $A$ has any inverse $B$, the lemma gives $B = C$.

### The converse

The converse asks whether a one-sided inverse alone makes a matrix invertible.
For square matrices over a field the answer is yes, by [[one-sided inverses of square matrices|0753Y2X5K6]].
For non-square matrices the answer is no, as the [[right inverse of a 2 × 3 matrix|540E86V3N9]] shows.

### Generalizations

The same argument works in any [[monoid|0N6R902FG1]]: if $ca = 1$ and $ab = 1$, then $c = b$.
So an [[inverse element|0ZNZH0EXFX]] of a monoid is unique when it exists.
In infinite dimensions a linear map can have a left inverse and no right inverse, as the [[shift operators|MRJ5JPW9HN]] show, and then the left inverse need not be unique.

## Explanations

### L1 human

A matrix cannot have two different inverses.
If two matrices both undo $A$, they must be the same matrix.
The proof is a short chain of equalities that inserts the identity and moves the brackets.

### L2 human

The typical use is in proofs of formulas such as $(AB)^{-1} = B^{-1} A^{-1}$.
We guess a candidate, check that its products with the matrix are $I_n$, and uniqueness does the rest.
Watch out: the lemma says nothing about existence.
It tells you that there is at most one inverse, and you still have to find one, or show that none exists.

### L3 human

The lemma is the monoid computation $c = c(ab) = (ca)b = b$.
It holds in every associative structure with an identity, for example for linear maps of any vector space and for functions from a set to itself.
In a group the lemma is built in, and the [[general linear group|0FCHE902D7]] is the group in which it lives for matrices.
