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

Let $F$ be a field, let $V$ be a vector space over $F$ with $n = \dim V \ge 1$, and let $T \colon V \to V$ be an endomorphism.

1. (Basis independence.) For any two bases $B$ and $C$ of $V$, the [[matrices of $T$|0YYMY95FWS]] have the same characteristic polynomial: $p_{[T]_B} = p_{[T]_C}$. So $p_T$ is well defined, and it is monic of degree $n$.
2. (Block triangular matrices.) Let $K$ be a commutative ring, and let $M = \begin{pmatrix} A & B \\ 0 & D \end{pmatrix}$ be a [[block matrix|0ASDFEQS6P]] over $K$ with square blocks $A$ and $D$. Then $p_M = p_A \cdot p_D$.
3. (Invariant subspaces.) Let $U$ be a $T$-[[invariant subspace|0ACX5QT8TE]] with $0 \ne U \ne V$, and let $T|_U$ be the [[restriction|0KN7EPH7Z0]]. Then $p_{T|_U}$ divides $p_T$ in $F[t]$.
4. (Invariant direct sums.) If $V = U \oplus W$ is an [[internal direct sum|0XYYT5KNTX]] of nonzero $T$-invariant subspaces, then $p_T = p_{T|_U} \cdot p_{T|_W}$.

## Remarks

### Why each hypothesis is needed

- Part 1 needs the same basis $B$ for the source and the target of $T$. With two different bases, the matrix of $\id_V$ can be any invertible matrix, and its characteristic polynomial changes.
- Part 2 needs $M$ block triangular. For $M = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ with $1 \times 1$ blocks, $p_A p_D = t^2$, but $p_M = t^2 - 1$.
- Parts 3 and 4 need invariant subspaces. For the rotation by $90$ degrees and the line $U = \R e_1$, which is not invariant, $p_T = t^2 + 1$ has no factor of degree $1$ over $\R$.

### Consequences

- The [[trace of a linear map|0KZDNGA561]] and the determinant of a linear map are coefficients of $p_T$, so they do not depend on a basis.
- The [[algebraic multiplicity|0FY42N02DV]] of an eigenvalue is an invariant of $T$.
- Part 3 is the main step in the proof that the [[geometric multiplicity is at most the algebraic multiplicity|FWY8A9M5HK]].
- For a [[block diagonal matrix|001T5FJDC1]], $p_M$ is the product of the characteristic polynomials of the blocks.

### Converse

Equal characteristic polynomials do not imply similar matrices: $I_2$ and $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ both have $p(t) = (t - 1)^2$.
A matrix is determined up to similarity by its invariant factors, of which $p_T$ is the product; see the [[Jordan normal form|085HQ5G5TE]].

### Generalizations

Part 1 holds for an endomorphism of a finite free module over any commutative ring, with the same proof.
Part 2 holds for block upper triangular matrices with any number of square diagonal blocks, by induction on the number of blocks.

## History

Part 1 makes the characteristic polynomial an invariant of the endomorphism, and not only of one matrix.
So it is a first invariant in the study of matrices up to similarity.

## Explanations

### L1 human

The characteristic polynomial of a map is computed from a matrix of the map.
Different bases give different matrices, but always the same polynomial.
If the map keeps a smaller subspace in place, then the polynomial splits into a part for the subspace and a part for the rest.

### L2 human

We compute $p_M$ for $M = \begin{pmatrix} 1 & 2 & 5 \\ 3 & 4 & 6 \\ 0 & 0 & 7 \end{pmatrix}$, with blocks $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $D = (7)$.

1. $p_A(t) = t^2 - 5t - 2$, from the trace $5$ and the determinant $-2$.
2. $p_D(t) = t - 7$.
3. By part 2, $p_M(t) = (t^2 - 5t - 2)(t - 7) = t^3 - 12t^2 + 33t + 14$.
4. Check by the principal minors: $\operatorname{tr} M = 12$, the $2 \times 2$ principal minors are $-2$, $7$ and $28$ with sum $33$, and $\det M = 7 \cdot (-2) = -14$.
5. So $p_M(t) = t^3 - 12t^2 + 33t - (-14)$, as in step 3.

The typical use is to choose a basis that starts with a basis of an invariant subspace, and to split $p_T$ into two smaller factors.
A trap: a block matrix with a nonzero block below the diagonal does not split in this way.

### L3 human

Part 3 says that $p_T = p_{T|_U} \cdot p_{\bar T}$, where $\bar T$ is the map induced on the quotient $V / U$, because $D$ is the matrix of $\bar T$.
So the characteristic polynomial is multiplicative in short exact sequences of $F[t]$-modules.
This is the reason that $p_T$ is the product of the characteristic polynomials of the factors in a composition series, the basis of [[triangularisation|0363JMQ42Y]].
