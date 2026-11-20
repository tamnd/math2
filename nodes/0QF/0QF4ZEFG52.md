---
tag: 0QF4ZEFG52
kind: statement
role: theorem
name: Eigenvalues are the roots of the minimal polynomial
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
about: [03NDVCSHSB, 0BQAA2BK3Q]
uses: [0V58FPM3EQ, 0ZND7NQ970, 0BZ81AJNWF]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)
    locator: Properties
  - book: isbn:9783031410253
    locator: Chapter 5
  - book: isbn:9780135367971
---

## Statement

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $\lambda \in F$.
Let $T \colon V \to V$ be an endomorphism with [[minimal polynomial|03NDVCSHSB]] $m_T$.

1. $\lambda$ is an [[eigenvalue|0BQAA2BK3Q]] of $T$ if and only if $m_T(\lambda) = 0$.
2. So $m_T$ and the [[characteristic polynomial|0J5EMJRRFM]] $p_T$ have the same roots in $F$.

The same holds for an $n \times n$ matrix $A$ over $F$.

## Remarks

The proof is in [[the proof without the Cayley-Hamilton theorem|RJYK29EFS2]].
It uses only the definition of $m_T$, the factor theorem, and, for part 2, the theorem that the [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]].
The multiplicities of a common root in $m_T$ and in $p_T$ can differ.

### Why each hypothesis is needed

- $V$ must be finite-dimensional so that $m_T$ exists.
- The roots must lie in $F$. Over $\R$, the rotation by $90$ degrees has $m = x^2 + 1$, with no real root and no real eigenvalue. Over $\C$ both sides change together.

### Consequences

- The minimal polynomial is a second tool to find eigenvalues, often of smaller degree than $p_T$.
- If $T^k = 0$, then $m_T$ divides $x^k$, so $0$ is the only possible eigenvalue.
- If $T$ is diagonalisable with distinct eigenvalues $\lambda_1, \dots, \lambda_r$, then $m_T = (x - \lambda_1) \cdots (x - \lambda_r)$. The polynomial annihilates $T$ on an eigenbasis, and by part 1 each factor must occur.
- $T$ is invertible if and only if $m_T(0) \ne 0$.

### Converse

Part 1 is already an equivalence.
A polynomial with the same roots as $m_T$ need not annihilate $T$.
For the shear, $x - 1$ has the same root as $m = (x - 1)^2$, but it does not annihilate the shear.

### Generalizations

- Over any field, $m_T$ and $p_T$ have the same irreducible factors. This follows from the structure of $V$ as a module over $F[x]$.
- The [[eigenvalues of a polynomial in an endomorphism|F2S8WGVARA]] satisfy a similar rule: every annihilating polynomial vanishes on the eigenvalues.

## History

The fact appears in the standard treatments of the minimal polynomial, for example in Axler, where it is proved without determinants.

## Explanations

### L1 human

The minimal polynomial and the characteristic polynomial have the same roots: the eigenvalues.
Only the multiplicities of the roots can differ.
So the minimal polynomial is a second way to find the eigenvalues.

### L2 human

We check the theorem for $A = \begin{pmatrix} 4 & 1 & 1 \\ 1 & 4 & 1 \\ 1 & 1 & 4 \end{pmatrix}$, studied in the [[worked 3 by 3 example|7XFGVVTZ2X]].

1. $A - 3I$ has every entry equal to $1$, and $A - 6I$ has the rows $(-2, 1, 1)$, $(1, -2, 1)$ and $(1, 1, -2)$.
2. Each entry of $(A - 3I)(A - 6I)$ is a column sum of $A - 6I$, and each column sum is $0$. So $(A - 3I)(A - 6I) = 0$. So $m_A$ divides $(x - 3)(x - 6)$.
3. $A - 3I \ne 0$ and $A - 6I \ne 0$, so $m_A = (x - 3)(x - 6)$, with roots $3$ and $6$.
4. The eigenvalues are $3$ and $6$: $(1, -1, 0)^{\mathsf{T}} \mapsto (3, -3, 0)^{\mathsf{T}}$ and $(1, 1, 1)^{\mathsf{T}} \mapsto (6, 6, 6)^{\mathsf{T}}$.
5. $p_A = (x - 3)^2 (x - 6)$ has the same roots, with a different multiplicity of $3$.

The typical use is to find the eigenvalues from a known annihilating relation such as $A^2 = 9A - 18I$.
A trap: the exponent of $x - \lambda$ in $m_A$ is not the algebraic multiplicity of $\lambda$.

### L3 human

Under the module view, $m_T(\lambda) = 0$ means that $F[x]/(x - \lambda)$ is a quotient of $F[x]/(m_T)$.
The proof of the converse direction finds a submodule isomorphic to $F[x]/(x - \lambda)$ inside the image of $q(T)$.
