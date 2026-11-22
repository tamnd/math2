---
tag: GS8WE1ZYV9
kind: statement
role: theorem
name: Sylvester's rank inequality and the Frobenius inequality
aliases: [sylvester-rank-inequality, frobenius-rank-inequality]
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug2
about: [0ZC9YTXZRY]
uses: [0EWQEYRVA8, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Properties
---

## Statement

A product of matrices cannot lose more rank than the null space of the left factor allows.
Let $F$ be a field, and let $A$ be an $m \times n$ matrix, $B$ an $n \times p$ matrix and $C$ a $p \times q$ matrix over $F$.
Let $\rank$ be the [[rank of a matrix|0ZC9YTXZRY]].

1. (Frobenius inequality) $\rank(AB) + \rank(BC) \le \rank B + \rank(ABC)$.
2. (Sylvester's rank inequality) $\rank A + \rank B - n \le \rank(AB)$.

## Remarks

### A first check

Take
$$A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad AB = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}.$$
Here $n = 3$, $\rank A = 2$ and $\rank B = 2$, so Sylvester's inequality says $\rank(AB) \ge 2 + 2 - 3 = 1$.
The product has rank exactly $1$, so the bound is reached.
The null space of $A$ is the third axis, and the image of $B$ is the plane of the second and third axes, so $A$ kills one direction of that image.

### Why the inner size is needed

In part 2, $n$ is the inner size: the number of columns of $A$ and of rows of $B$.
The bound fails with an outer size in its place.
For the $1 \times 2$ matrix $A = \begin{pmatrix} 1 & 0 \end{pmatrix}$ and the $2 \times 1$ matrix $B = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$, the product is $AB = (0)$.
With the outer size $1$ we would get $1 + 1 - 1 = 1 > 0$, which is false.
With the inner size $n = 2$, the bound is $1 + 1 - 2 = 0 \le 0$, which is true.

### What it gives you

If $AB = 0$, then $\rank A + \rank B \le n$.
In particular, an $n \times n$ matrix $N$ with $N^2 = 0$ has $2 \rank N \le n$, so $\rank N \le n/2$; for $n = 2$, the matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ reaches this bound.
For $n \times n$ matrices, part 2 written with nullities reads
$$\dim \operatorname{Null}(AB) \le \dim \operatorname{Null}(A) + \dim \operatorname{Null}(B),$$
by [[rank-nullity for matrices|TR48YQGCCA]], so the null spaces of a product grow at most additively.
Together with the [[rank of a product|02FDWY55AS]], Sylvester's inequality pins $\rank(AB)$ between $\rank A + \rank B - n$ and $\min(\rank A, \rank B)$.

### Sharp and strict cases

Part 2 can be an equality.
For $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$, we get $1 + 1 - 2 = 0 = \rank(AB)$.
It can also be strict: for $A = B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, the bound is $0$, but $AB = A$ has rank $1$.

### Generalizations

For linear maps $U \xrightarrow{C} V \xrightarrow{B} W \xrightarrow{A} X$ between finite-dimensional spaces, both inequalities hold with $\rank$ the dimension of the image and $n = \dim W$.
Part 2 is the case of part 1 in which the middle factor is the identity $I_n$, as the [[proof|Z65SFWJKJ1]] shows.

## History

The lower bound of part 2 carries the name of Sylvester, and part 1 carries the name of Frobenius.

## Explanations

### L1 human

Sylvester's inequality says that a product cannot lose too much rank.
The left factor $A$ can only destroy the directions that it sends to zero.
There are $n - \rank A$ of those, so the product loses at most that many directions from the rank of $B$.

### L2 human

Here is the argument in a worked form.
The map $x \mapsto Ax$, restricted to the column space of $B$, has image $\operatorname{Col}(AB)$ and kernel $\operatorname{Col}(B) \cap \operatorname{Null}(A)$.
Rank-nullity for this restricted map gives
$$\rank B - \rank(AB) = \dim\bigl(\operatorname{Col}(B) \cap \operatorname{Null}(A)\bigr) \le \dim \operatorname{Null}(A) = n - \rank A.$$
Rearranging gives $\rank(AB) \ge \rank A + \rank B - n$.
In the first check, the intersection is the third axis, of dimension $1$, and indeed $\rank B - \rank(AB) = 2 - 1 = 1$.
Watch out: the loss is the dimension of an intersection, and not the full nullity of $A$, unless $\operatorname{Null}(A)$ lies inside $\operatorname{Col}(B)$.

### L3 human

The Frobenius inequality compares the loss of rank under $A$ on the two nested subspaces $\operatorname{Col}(BC) \subseteq \operatorname{Col}(B)$.
The loss on the smaller subspace is the dimension of a smaller intersection with $\operatorname{Null}(A)$, so it is at most the loss on the larger one.
In the language of subspaces: for subspaces $W_2 \subseteq W_1$ of $F^n$, the drop $\dim W - \dim A(W)$ is at least as large for $W = W_1$ as for $W = W_2$.
Both inequalities are statements about finite-dimensional spaces and hold for linear maps without any choice of bases.
