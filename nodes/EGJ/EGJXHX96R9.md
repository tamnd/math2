---
tag: EGJXHX96R9
kind: example
name: Row vectors as linear forms on column vectors
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug1
instance_of: [07YQ1C78G0, 07JBSZE0V4]
uses: [0RT96J4D3H, 0M856Q1AMZ, 713F6AM1X1, 0PDVQEP0ZC, C5QA672NPH, 0B8T10CE7N]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_form
    locator: Linear functionals in Rn
  - book: isbn:9780134860244
    locator: Section 2.6
---

## Example

Let $F$ be a field, and let $F^n$ be the [[coordinate space|713F6AM1X1]] of columns $x = (x_1, \dots, x_n)^{\mathsf{T}}$.
For a row vector $c = (c_1, \dots, c_n)$, define $f_c \colon F^n \to F$ by the [[matrix product|0PDVQEP0ZC]]
$$f_c(x) = cx = c_1 x_1 + \dots + c_n x_n.$$
We show that each $f_c$ is a [[linear form|0RT96J4D3H]], and that every linear form on $F^n$ equals $f_c$ for exactly one row $c$.
So the rows of length $n$ are the linear forms on $F^n$, under a linear isomorphism.

1. Each $f_c$ is linear.
The matrix product is distributive, so $c(x + y) = cx + cy$.
Since $F$ is commutative, $c(ax) = a(cx)$ for every scalar $a$.
2. The row is read off from the standard basis.
Let $e_1, \dots, e_n$ be the [[standard basis|C5QA672NPH]]; then $f_c(e_i) = c_i$, because $e_i$ has entry $1$ in place $i$ and $0$ elsewhere.
3. Every form is some $f_c$.
Let $f$ be any linear form on $F^n$ and put $c_i = f(e_i)$.
Write $x = x_1 e_1 + \dots + x_n e_n$.
Then linearity gives $f(x) = x_1 f(e_1) + \dots + x_n f(e_n) = c_1 x_1 + \dots + c_n x_n = f_c(x)$.
4. The row is unique.
If $f_c = f_d$, then step 2 gives $c_i = f_c(e_i) = f_d(e_i) = d_i$ for each $i$, so $c = d$.
5. The correspondence is linear.
For rows $c, d$ and a scalar $a$, we have $f_{c + d}(x) = (c + d)x = cx + dx$ and $f_{ac}(x) = (ac)x = a(cx)$.
6. Steps 3 to 5 show that $c \mapsto f_c$ is a bijective linear map from the rows $F^{1 \times n}$ onto the [[dual space|0M856Q1AMZ]] $(F^n)^*$.
So it is a [[linear isomorphism|0B8T10CE7N]].

Here is a check with numbers in $\mathbb{R}^3$.
For $c = (2, -3, 1)$ and $x = (1, 4, 2)^{\mathsf{T}}$, multiply matching entries and add:
$$f_c(x) = 2 \cdot 1 + (-3) \cdot 4 + 1 \cdot 2 = -8.$$

## Remarks

The standard rows play a special role.
The row with $1$ in place $i$ and $0$ elsewhere is the coordinate form $x \mapsto x_i$, and these $n$ rows are the [[dual basis|0ZD2CF6ZS0]] of $e_1, \dots, e_n$.

The same method works on any space with a chosen basis: a form is the row of its values on the basis.
For the [[trace|0XC1RDBY7A]] on $M_2(F)$, with the basis $E_{11}, E_{12}, E_{21}, E_{22}$, the values are $1, 0, 0, 1$, so the row is $(1, 0, 0, 1)$.
On an abstract space there is no standard basis, so there is no preferred isomorphism $V \cong V^*$; the [[dimension of the dual space|00889YD15K]] discusses this.

A matrix is a stack of forms.
An $m \times n$ matrix $A$ has $m$ rows, so it is a list of $m$ linear forms on $F^n$, and $Ax = 0$ says that all $m$ forms vanish at $x$.
For example, the rows of $\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & -1 \end{pmatrix}$ both vanish at $(1, -1, -1)^{\mathsf{T}}$, since $1 - 1 + 0 = 0$ and $0 - 1 + 1 = 0$.

## Explanations

### L1 human

A row of numbers can "eat" a column of numbers and return one number.
You multiply matching entries and add.
The row $(2, -3, 1)$ and the column $(1, 4, 2)$ give $2 - 12 + 2 = -8$.
This rule is a linear form, and every linear form on columns of length $3$ comes from exactly one row in this way.

### L2 human

Suppose you are given $f(x, y, z) = 5x - z$ on $\mathbb{R}^3$ and you want its row.
Evaluate $f$ on the standard basis:
$$f(e_1) = 5, \qquad f(e_2) = 0, \qquad f(e_3) = -1.$$
So the row of $f$ is $(5, 0, -1)$, and $f(x) = (5, 0, -1) \, x$.
Check with $x = (1, 2, 3)^{\mathsf{T}}$: the formula gives $5 - 3 = 2$, and the row gives $5 + 0 - 3 = 2$.
The typical use runs the other way too: the solution set of $Ax = 0$ is the set of columns where every row of $A$, read as a form, is zero.
Watch out: if you write a form as a column, you can mix it up with a vector, and the two change by different rules when the basis changes.
