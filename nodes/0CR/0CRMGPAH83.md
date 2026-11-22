---
tag: 0CRMGPAH83
kind: concept
name: Linear independence
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
uses: [0V8F3E48E6, 0JB3DP1BMF]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_independence
    locator: Definition
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section2-4.xml#L510
    locator: src/section2-4.xml:510
  - book: isbn:9783031410253
    locator: Section 2A
  - book: isbn:9780134860244
    locator: Section 1.5
same_as:
  wikidata: Q27670
  wikipedia: Linear independence
---

## Summary

Vectors are linearly independent when none of them is wasted: no vector can be built from the others, so each one adds a new direction.
Independence is what makes coordinates unique, and together with spanning it gives the idea of a [[basis|0KCQ9Y3QKA]].
A family $(v_1, \dots, v_k)$ in a vector space over a field $F$ is *linearly independent* when the only [[linear combination|0V8F3E48E6]] of it with value $0$ is the trivial one:
$$a_1 v_1 + \dots + a_k v_k = 0 \implies a_1 = \dots = a_k = 0.$$
An infinite family is independent when each finite subfamily is, as the [[formal definition|0EVHJFTG9Z]] states.
Equivalently, by the [[linear dependence lemma|H75GS7QVPB]], no vector of the family is a linear combination of the others.

## Motivation

A spanning set lets you write every vector as a combination, but sometimes in several ways.
With $(1, 0)$, $(0, 1)$ and $(1, 1)$, the vector $(1, 1)$ is both $1(1, 1)$ and $1(1, 0) + 1(0, 1)$.
The two expressions differ by the combination $(1, 0) + (0, 1) - (1, 1) = 0$.
So the question "are coefficients unique?" is the question "is the zero vector written in only one way?", and that is exactly independence.

Independence appears wherever one asks whether some quantities are really different.
In differential equations, two solutions of a second order linear equation give all solutions only when they are independent.
In data analysis, a column of a table that is a combination of other columns carries no new information.
Within linear algebra, independence leads to [[bases|0KCQ9Y3QKA]], to [[coordinates|04CYQHN6MC]] and, through the [[Steinitz exchange lemma|08ZDRN6H41]], to [[dimension|03GSZ8RTZJ]].

## Notation

We say "$v_1, \dots, v_k$ are independent" for the family $(v_1, \dots, v_k)$.
A family that is not independent is *linearly dependent*, and a relation $\sum a_i v_i = 0$ with some $a_i \ne 0$ is a *dependence relation*.
Some books define independence for sets and others for lists or families, and the difference matters when a vector repeats.
Mathlib uses families: `LinearIndependent F v` for `v : ι → V`.

## Remarks

### A first test

Are $(1, 0)$ and $(1, 1)$ independent in $\mathbb{R}^2$?
Start from a combination with value $0$ and solve for the coefficients:
$$a(1, 0) + b(1, 1) = (a + b, b) = (0, 0).$$
The second entry gives $b = 0$, and then the first gives $a = 0$.
Only the trivial combination is zero, so the vectors are independent.

The same method works far from $F^n$.
For $1, x, x^2$ in the polynomials, $a + bx + cx^2$ is the zero polynomial only when $a = b = c = 0$, since a polynomial is zero exactly when all its coefficients are.
For the functions $\sin$ and $\cos$ on $\mathbb{R}$, suppose $a \sin t + b \cos t = 0$ for every $t$.
Putting $t = 0$ gives $b = 0$, and putting $t = \pi/2$ gives $a = 0$.

### Dependent families

The vectors $(1, 2)$ and $(2, 4)$ are dependent, because
$$2(1, 2) + (-1)(2, 4) = (0, 0)$$
is a combination with nonzero coefficients.
Every family that contains the zero vector is dependent, by the relation $1 \cdot 0 = 0$.
Three vectors in $\mathbb{R}^2$ are always dependent, by the [[column test|76GG9B25A1]], since a $2 \times 3$ matrix has at most two pivots.

### Families and sets

The family $(v, v)$ with $v \ne 0$ is dependent, by the relation $1v + (-1)v = 0$.
The set $\{v, v\}$ is the set $\{v\}$, which is independent.
So a list with a repeated vector is dependent, while the set of its entries may be independent.
Mathlib states independence for families, so in Lean repeated vectors make a family dependent; for a set `s` one uses the family of its elements.

### Tests in coordinates

In $F^m$, put the vectors as the columns of a matrix $A$.
They are independent exactly when $Ax = 0$ has only the solution $x = 0$, which holds exactly when every column of an echelon form of $A$ has a pivot, by the [[column test|76GG9B25A1]].
For $n$ vectors in $F^n$ the matrix is square, and independence holds exactly when its [[determinant|0C3CFHDN6R]] is nonzero, by the [[determinant test|FBSAPTP1PR]].
For example, the determinant of the matrix with columns $(1, 0)$ and $(1, 1)$ is $1 \cdot 1 - 1 \cdot 0 = 1 \ne 0$.

### The rules you can use

A family with at least one vector is dependent exactly when one of its vectors is a combination of the others, by the [[linear dependence lemma|H75GS7QVPB]].
The same lemma says that an independent family stays independent when you add a vector outside its span.
A subfamily of an independent family is independent, because a relation in the subfamily is a relation in the whole family, with zeros for the missing vectors.
By the [[Steinitz exchange lemma|08ZDRN6H41]], an independent family is never longer than a spanning family.

### Watch out

Pairwise independence is not enough.
The vectors $(1, 0)$, $(0, 1)$ and $(1, 1)$ are independent two at a time, but the three together satisfy $(1, 0) + (0, 1) - (1, 1) = 0$.

Independence depends on the field.
The family $(1, 0, 1)$, $(0, 1, 1)$, $(1, 1, 0)$ is independent over $\mathbb{R}$ but [[dependent over the field with two elements|KFJ7M9FRXV]].

The direction of the argument matters.
To prove independence, start from an arbitrary relation $\sum a_i v_i = 0$ and show that every $a_i$ is $0$.
Showing that $0v_1 + \dots + 0v_k = 0$ proves nothing, because that is true for every family.

### History

Grassmann used the notion of linear dependence of his quantities in the *Ausdehnungslehre* of 1844.

### Try it

First, are $(1, 2, 0)$, $(0, 1, 1)$ and $(1, 3, 1)$ independent?
No: the third is the sum of the first two, so $(1, 2, 0) + (0, 1, 1) - (1, 3, 1) = 0$.

Second, for which $t$ are $(1, t)$ and $(t, 4)$ dependent?
The determinant $1 \cdot 4 - t \cdot t = 4 - t^2$ is zero exactly for $t = 2$ and $t = -2$.

## Explanations

### L1 human

Vectors are independent when none of them is redundant.
Think of directions you can walk in.
If you have "east" and "north", neither one can be made from the other, so they are independent.
If you add "northeast", it can be made by walking east and then north, so the three together are dependent.
Two arrows in the plane are independent exactly when they do not lie on one line.

### L2 human

Here is the standard test: are $(1, 2, 3)$, $(4, 5, 6)$ and $(7, 8, 9)$ independent in $\mathbb{R}^3$?
Put them as columns and row reduce.
Subtract twice row 1 from row 2 and three times row 1 from row 3, then subtract twice the new row 2 from the new row 3:
$$\begin{pmatrix} 1 & 4 & 7 \\ 2 & 5 & 8 \\ 3 & 6 & 9 \end{pmatrix} \to \begin{pmatrix} 1 & 4 & 7 \\ 0 & -3 & -6 \\ 0 & -6 & -12 \end{pmatrix} \to \begin{pmatrix} 1 & 4 & 7 \\ 0 & -3 & -6 \\ 0 & 0 & 0 \end{pmatrix}.$$
The third column has no pivot, so the vectors are dependent.
The free variable gives the relation: $x_3 = 1$ forces $x_2 = -2$ and $x_1 = 1$, and indeed
$$(1, 2, 3) - 2(4, 5, 6) + (7, 8, 9) = (0, 0, 0).$$
The typical use is exactly this: the test either proves independence or hands you a dependence relation.

### L3 human

A family $v \colon I \to V$ is independent exactly when the linear map from the finitely supported functions $F^{(I)}$ to $V$, sending $a$ to $\sum_i a_i v_i$, is injective.
The independent subsets of $V$ are the independent sets of a [[matroid|PX31ZNYS3Z]], and the exchange property of that matroid gives the [[dimension theorem|0WK0Y8RH1M]].
Over a ring, independence is weaker than "no vector is a combination of the others".
In $\mathbb{Z}$, the family $(2, 3)$ is dependent, by $3 \cdot 2 - 2 \cdot 3 = 0$, but neither entry is an integer multiple of the other.
