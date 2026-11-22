---
tag: C98TZ6ZAXC
kind: statement
role: theorem
name: Characteristic polynomial of an endomorphism
msc: ["15A04", "15A18"]
topics: [6R1D6QPY3S]
audience: ug2
about: [0J5EMJRRFM]
uses: [0BZ81AJNWF, 039HF58KQ5, 0YYMY95FWS, 0ACX5QT8TE, 0KN7EPH7Z0, 0XYYT5KNTX, 0ASDFEQS6P]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Properties
  - book: isbn:9780134860244
---

## Statement

The characteristic polynomial of a linear map does not depend on the basis, and it splits into factors along invariant subspaces.
Let $F$ be a field, let $V$ be a vector space over $F$ with $n = \dim V$ and $1 \le n < \infty$, and let $T \colon V \to V$ be an endomorphism.

1. (Basis independence.) For any two bases $B$ and $C$ of $V$, the [[matrices of T|0YYMY95FWS]] have the same characteristic polynomial, $p_{[T]_B} = p_{[T]_C}$. So $p_T$ is well defined, and it is monic of degree $n$.
2. (Block triangular matrices.) Let $K$ be a commutative ring, and let $M = \begin{pmatrix} A & B \\ 0 & D \end{pmatrix}$ be a [[block matrix|0ASDFEQS6P]] over $K$ with square blocks $A$ and $D$. Then $p_M = p_A \, p_D$.
3. (Invariant subspaces.) Let $U$ be a $T$-[[invariant subspace|0ACX5QT8TE]] with $0 \ne U \ne V$, and let $T|_U$ be the [[restriction|0KN7EPH7Z0]]. Then $p_{T|_U}$ divides $p_T$ in $F[t]$.
4. (Invariant direct sums.) If $V = U \oplus W$ is an [[internal direct sum|0XYYT5KNTX]] of nonzero $T$-invariant subspaces, then $p_T = p_{T|_U} \, p_{T|_W}$.

## Remarks

### A block triangular example

Take
$$M = \begin{pmatrix} 1 & 2 & 5 \\ 3 & 4 & 6 \\ 0 & 0 & 7 \end{pmatrix}, \qquad A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \qquad D = (7).$$
The block $A$ has trace $5$ and determinant $-2$, so $p_A(t) = t^2 - 5t - 2$, and $p_D(t) = t - 7$.
Part 2 gives
$$p_M(t) = (t^2 - 5t - 2)(t - 7) = t^3 - 12t^2 + 33t + 14.$$
Check with the [[coefficients of the characteristic polynomial|0FRYPZ6D0X]]: $\operatorname{tr} M = 12$, the three $2 \times 2$ principal minors are $-2$, $7$ and $28$ with sum $33$, and $\det M = 7 \cdot (-2) = -14$, so the constant term is $-(-14) = 14$.

### Why each hypothesis is needed

Part 1 needs the same basis for the input and the output of $T$.
With two different bases, the identity of $\mathbb{R}^2$ can have the matrix $\operatorname{diag}(2, 1)$, whose polynomial $(t - 2)(t - 1)$ is not $(t - 1)^2$.

Part 2 needs the zero block below the diagonal.
For $M = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ with $1 \times 1$ blocks $A = D = (0)$, the product $p_A \, p_D$ is $t^2$, but $p_M = t^2 - 1$.

Parts 3 and 4 need invariant subspaces, because otherwise $T|_U$ is not a map from $U$ to $U$ and has no characteristic polynomial.
The rotation of $\mathbb{R}^2$ by a right angle shows that nothing weaker would do: it has $p_T = t^2 + 1$, which has no factor of degree $1$ over $\mathbb{R}$, and in agreement with part 3 it has no invariant line.

### What it gives you

The trace and the determinant of $T$ are coefficients of $p_T$, so part 1 makes the [[trace of a linear map|0KZDNGA561]] and the determinant of a linear map independent of the basis.
The [[algebraic multiplicity|0FY42N02DV]] of each eigenvalue is an invariant of $T$ in the same way.
Part 3 is the main step in the proof that the [[geometric multiplicity is at most the algebraic multiplicity|FWY8A9M5HK]]: an eigenspace of dimension $g$ gives the factor $(t - \lambda)^g$.
For a [[block diagonal matrix|001T5FJDC1]], part 2 gives the product of the polynomials of the blocks.

### The converse

Equal characteristic polynomials do not make two matrices similar.
The matrices $I_2$ and $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ both have $p(t) = (t - 1)^2$, but only $I_2$ is similar to $I_2$.
Similarity is decided by finer data, the invariant factors, whose product is $p_T$; see the [[Jordan normal form|085HQ5G5TE]].

### Generalizations

Part 1 holds for an endomorphism of a finite free module over any commutative ring, with the same proof.
Part 2 holds for block upper triangular matrices with any number of square diagonal blocks, by induction on the number of blocks.

## Explanations

### L1 human

To get the characteristic polynomial of a map, you write the map as a matrix and compute.
Different axes give different matrices, but they always give the same polynomial.
If the map keeps a smaller subspace in place, the polynomial splits into a part for that subspace and a part for the rest.
For the mirror of space in a plane, the plane gives $(t - 1)^2$ and the normal line gives $t + 1$.

### L2 human

Here is a typical use: find $p_T$ for $T(x, y, z) = (x + 2y, 3x + 4y, 5x + 6y + 7z)$ on $\mathbb{R}^3$.
The $z$-axis $U$ is invariant, since $T(0, 0, z) = (0, 0, 7z)$, so put $e_3$ first in the basis $B = (e_3, e_1, e_2)$.
Then $T(e_3) = 7 e_3$, $T(e_1) = 5 e_3 + e_1 + 3 e_2$ and $T(e_2) = 6 e_3 + 2 e_1 + 4 e_2$, and
$$[T]_B = \begin{pmatrix} 7 & 5 & 6 \\ 0 & 1 & 2 \\ 0 & 3 & 4 \end{pmatrix}.$$
Part 2 gives $p_T(t) = (t - 7)(t^2 - 5t - 2)$, the same polynomial as in the block triangular example above.
The lesson is to start the basis with a basis of an invariant subspace, so that the matrix becomes block triangular.
Watch out: a block matrix with a nonzero block below the diagonal does not split in this way.

### L3 human

The lower right block $D$ in part 3 is the matrix of the map $\bar T$ that $T$ induces on the quotient $V / U$, so $p_T = p_{T|_U} \, p_{\bar T}$.
In the language of modules over $F[t]$, the characteristic polynomial is multiplicative in short exact sequences.
So $p_T$ is the product of the characteristic polynomials of the factors of a composition series of the $F[t]$-module $V$.
When $p_T$ splits into linear factors, these factors are lines, and this gives [[triangularization|0363JMQ42Y]].
