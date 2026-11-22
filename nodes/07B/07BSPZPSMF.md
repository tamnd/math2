---
tag: 07BSPZPSMF
kind: concept
name: Nilpotent matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
specializes: [0JXZKX526R]
uses: [0JXZKX526R, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: Characterization
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: Examples
same_as:
  wikidata: Q650670
  wikipedia: Nilpotent matrix
inventory: [HSZH6NG7SR]
---

## Summary

A nilpotent matrix is a matrix that becomes the zero matrix when we multiply it by itself enough times.
Nonzero matrices of this kind have no counterpart among the numbers, where $x^k = 0$ forces $x = 0$, and no change of basis can make them diagonal.
Exactly, a [[square matrix|0JXZKX526R]] $N$ is *nilpotent* when
$$N^k = 0 \quad \text{for some integer } k \ge 1,$$
and the least such $k$ is the *index* of $N$.
The [[formal definition|0419GJC84P]] states this over any ring.
Over a field, an $n \times n$ matrix is nilpotent exactly when its characteristic polynomial is $x^n$, and then already $N^n = 0$.

## Motivation

For numbers, $x^2 = 0$ means $x = 0$.
Matrices break this rule, and the nilpotent matrices are the cleanest way in which they break it.
The matrix $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ moves the second basis vector to the first and the first to zero, so two steps send everything to zero.
Every nilpotent map works like this: it pushes each vector down a chain that ends at $0$.

Nilpotent matrices are useful because their power series stop.
The inverse of $I - N$ is the finite sum $I + N + \dots + N^{k-1}$, and the exponential $e^{tN}$ is the polynomial $I + tN + \dots + t^{k-1} N^{k-1}/(k-1)!$.
So systems of linear differential equations $x' = Nx$ can be solved by hand.
Later, the [[Jordan-Chevalley decomposition|011K11VPJN]] writes every complex matrix as $D + N$ with $D$ diagonalizable, $N$ nilpotent and $DN = ND$.
The sub-area on canonical forms studies the nilpotent part in detail.

## Notation

Books write the index as the *index of nilpotency*, the *degree* or the *order*; all three mean the least $k$ with $N^k = 0$.
In Mathlib the predicate is `IsNilpotent N`, which says that some power of `N` is `0`; it is defined in any monoid with zero, so it applies to matrices over any ring.
Watch the difference between "nilpotent" and "nilpotent of index $k$": the first only says that some power vanishes.

## Remarks

### Three first examples

The smallest example is the matrix above.
Its square is
$$\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}^2 = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 0 & 0 \cdot 1 + 1 \cdot 0 \\ 0 & 0 \end{pmatrix} = 0,$$
so it is [[a nonzero matrix with square zero|DXX58EAKG3]], nilpotent of index $2$.

A nilpotent matrix need not have any zero entry.
For $N = \begin{pmatrix} 2 & 4 \\ -1 & -2 \end{pmatrix}$ we get
$$N^2 = \begin{pmatrix} 4 - 4 & 8 - 8 \\ -2 + 2 & -4 + 4 \end{pmatrix} = 0,$$
which is [[a nilpotent 2 × 2 matrix with no zero entries|YHCD6MTSV8]].

Every strictly upper triangular matrix is nilpotent, by [[the theorem on strictly triangular matrices|AW5RBMW7RK]].
Take $N = \begin{pmatrix} 0 & 1 & 2 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{pmatrix}$.
Each multiplication pushes the nonzero entries one diagonal further up:
$$N^2 = \begin{pmatrix} 0 & 0 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \qquad N^3 = 0.$$
So the index is $3$, the same as the size; [[a strictly upper triangular 3 × 3 matrix|NRNV4AJJ0E]] works out another case.

### What it is not

A triangular shape is not enough.
The matrix $U = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has powers $U^k = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$, and none of them is $0$, because the diagonal stays $1, 1$.
An [[invertible matrix|0EB9N0S33C]] is never nilpotent, since $N^k = 0$ would give $I = (N^{-1})^k N^k = 0$.
Both cases appear in [[two matrices that look nilpotent but are not|EA0YN4H604]].

### The rules you can use

Let $N$ be nilpotent with $N^k = 0$.
Then $N^m = 0$ for every $m \ge k$, since $N^m = N^{m-k} N^k$.
Every multiple $cN$ is nilpotent, because $(cN)^k = c^k N^k = 0$, and every similar matrix $P^{-1} N P$ is nilpotent, because $(P^{-1} N P)^k = P^{-1} N^k P$.
The matrix $I - N$ is invertible with inverse $I + N + \dots + N^{k-1}$, by the [[geometric series for a nilpotent matrix|N40XPYS89W]].

Over a field, the index is at most $n$.
The kernels $\ker N \subseteq \ker N^2 \subseteq \cdots$ grow strictly until they reach the whole space, and each strict step adds at least one dimension, so at most $n$ steps are possible.
Over a field the only eigenvalue of $N$ is $0$: from $Nv = \lambda v$ with $v \ne 0$ we get $0 = N^k v = \lambda^k v$, so $\lambda = 0$.
Hence the [[trace|0XC1RDBY7A]] is $0$, since the [[trace is the sum of the eigenvalues|0NMXDCNNKR]], and the determinant is $0$.

### Sums and products

If $M$ and $N$ are nilpotent and $MN = NM$, then $MN$ is nilpotent, since $(MN)^k = M^k N^k$.
The sum $M + N$ is nilpotent too, by the [[binomial theorem for commuting matrices|DS9TS6AFMW]]: in $(M + N)^{2k}$ each term contains $M^i N^j$ with $i \ge k$ or $j \ge k$.
Without commuting, both facts fail.
The matrices $E_{12}$ and $E_{21}$ are nilpotent, but
$$E_{12} + E_{21} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad (E_{12} + E_{21})^2 = I.$$

### Watch out

A zero diagonal does not make a matrix nilpotent: the matrix $E_{12} + E_{21}$ above has zero diagonal and square $I$.
A zero determinant is not enough either: $\operatorname{diag}(1, 0)$ has determinant $0$, but every power of it is itself.
Over $\mathbb{R}$, "no nonzero real eigenvalue" is not enough, since the quarter turn $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has no real eigenvalue and its fourth power is $I$.
The correct test over a field is that the characteristic polynomial is $x^n$, or directly that $N^n = 0$.

### History

The words *nilpotent* and *idempotent* come from Benjamin Peirce, who used them in his work on linear associative algebras around 1870.

### Try it

First, is $\begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix}$ nilpotent?
Its square has entries $1 - 1 = 0$ and $-1 + 1 = 0$ in each row, so yes, with index $2$.

Second, find $(I - N)^{-1}$ for the $3 \times 3$ matrix $N$ of the first examples.
It is $I + N + N^2 = \begin{pmatrix} 1 & 1 & 5 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{pmatrix}$, and multiplying by $I - N$ gives $I$.

Third, can a nilpotent real $3 \times 3$ matrix have trace $1$?
No, because its only eigenvalue is $0$, so its trace is $0$.

## Explanations

### L1 human

Think of a row of three boxes, and a machine that moves the content of each box one place to the left and throws away what falls off the end.
After three turns of the machine, every box is empty, whatever was in it at the start.
The matrix of this machine is nilpotent: three products of it with itself give the zero matrix.
A nilpotent matrix is any matrix that empties everything after a fixed number of turns.

### L2 human

Solve $x' = Nx$ with $N = \begin{pmatrix} 2 & 4 \\ -1 & -2 \end{pmatrix}$ and $x(0) = (1, 0)$.
Since $N^2 = 0$, the exponential series stops after two terms:
$$e^{tN} = I + tN = \begin{pmatrix} 1 + 2t & 4t \\ -t & 1 - 2t \end{pmatrix}.$$
So $x(t) = e^{tN} x(0) = (1 + 2t, -t)$.
Check: $x'(t) = (2, -1)$, and $N x(t) = (2 + 4t - 4t, -1 - 2t + 2t) = (2, -1)$.
For a nilpotent matrix, the solution is a polynomial in $t$, with no exponentials at all.
That is the typical use: nilpotency turns infinite series into finite sums.

### L3 human

In a commutative ring the nilpotent elements form an ideal, the nilradical.
In $M_n(F)$ with $n \ge 2$ they do not even form a subgroup, since $E_{12} + E_{21}$ is not nilpotent.
Over a field, every nilpotent matrix is similar to a strictly upper triangular one.
The Jordan form refines this to blocks with $1$ just above the diagonal, and the number and sizes of the blocks are read from the ranks of $N, N^2, \dots$.
The nilpotent $n \times n$ matrices form the nilpotent cone, the set cut out by the vanishing of the non-leading coefficients of the characteristic polynomial, which is a central object in the theory of Lie algebras.
