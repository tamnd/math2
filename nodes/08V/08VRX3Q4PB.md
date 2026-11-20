---
tag: 08VRX3Q4PB
kind: concept
name: Semisimple endomorphism
msc: ["15A04", "15A20"]
topics: [Z6S6PWMJPH]
audience: grad
specializes: [0J7H0YBFDJ]
uses: [0J7H0YBFDJ, 0ACX5QT8TE, 03NDVCSHSB]
sources:
  - url: https://en.wikipedia.org/wiki/Semisimple_operator
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Jordan%E2%80%93Chevalley_decomposition
    locator: Decomposition of a linear operator
  - book: isbn:9780135367971
    locator: Section 6.8
same_as:
  wikidata: Q3299281
  wikipedia: Semisimple operator
---

## Summary

An [[endomorphism|0J7H0YBFDJ]] $T$ of a finite-dimensional vector space is [[semisimple|0QS8P74F2Z]] when every $T$-[[invariant subspace|0ACX5QT8TE]] has a $T$-invariant complement.
Equivalently, its [[minimal polynomial|03NDVCSHSB]] is a product of distinct monic irreducible polynomials.
When the characteristic polynomial splits, semisimple means [[diagonalizable|07SQCNV233]].
Over a [[perfect field|VWBVKT794W]], for example in characteristic $0$, semisimple means diagonalizable over the algebraic closure; over an imperfect field this can fail.

## Motivation

Diagonalizability depends on the field: the rotation by a right angle is not diagonalizable over $\R$, but it has no nilpotent behaviour.
Semisimplicity captures "no nilpotent part" without leaving the field.
It is the right notion for the semisimple part $S$ of the [[Jordan-Chevalley decomposition|011K11VPJN]] $T = S + N$ over fields that are not algebraically closed.

## Notation

In Mathlib, `Module.End.IsSemisimple T` means that $V$ is a semisimple module over $F[t]$, with $t$ acting as $T$.
This is the same as the condition on invariant complements, since the $F[t]$-submodules of $V$ are the $T$-invariant subspaces.
Some authors call a map semisimple only when it is diagonalizable over the algebraic closure; others call this absolutely semisimple.

## Remarks

### Examples

- Every [[diagonalizable matrix|~36eb7d45]] is semisimple. An invariant $W$ is the sum of the $W \cap E_\lambda$, and complements of these inside the eigenspaces $E_\lambda$ add up to an invariant complement.
- The [[rotation by a right angle|~43d2ecd4]] over $\R$ is semisimple, since its only invariant subspaces are $0$ and $\R^2$.
- The [[companion matrix of x² + s over F₂(s)|~d837395a]] is semisimple, but it is not diagonalizable over the algebraic closure.
- The matrix $B$ of the [[primary decomposition example|~81757fe9]] has minimal polynomial $(t^2 + 1)(t - 2)$, which is squarefree, so $B$ is semisimple over $\R$.

### Non-examples

- The [[shear|~58e14c85]] is not semisimple: the invariant line $F e_1$ has no invariant complement.
- A nonzero [[nilpotent|063D5Z2C70]] map $N$ is not semisimple, since its minimal polynomial $t^k$ with $k \ge 2$ has a repeated factor.
- The [[Jordan block of size 3|~6530bcca]] is not semisimple, since its minimal polynomial is $(t - 2)^3$.

### Basic properties

- $T$ is semisimple exactly when $m_T = p_1 \cdots p_k$ with distinct monic irreducible $p_i$. This follows from the [[primary decomposition theorem|~81757fe9]].
- If $p_T$ splits, then $T$ is semisimple exactly when it is diagonalizable, by the [[minimal polynomial criterion|0MPAJRB23T]].
- Over a perfect field, irreducible polynomials have distinct roots in the algebraic closure. So $T$ is semisimple exactly when it is diagonalizable over the [[algebraic closure|0X6AB5P3G1]].
- The restriction of a semisimple map to an invariant subspace is semisimple, since its minimal polynomial divides $m_T$.
- A map that is both semisimple and nilpotent is $0$, since its minimal polynomial is squarefree and a power of $t$.

### History

The name comes from module theory: $T$ is semisimple when $V$ is a semisimple module over $F[t]$, that is, a direct sum of simple modules.
Chevalley used semisimple and nilpotent parts in his work on algebraic groups and Lie algebras, which gave the Jordan-Chevalley decomposition its name.

### Common errors

- Identifying "semisimple" with "diagonalizable". This holds only when the characteristic polynomial splits, and the rotation over $\R$ is a counterexample.
- Identifying "semisimple" with "diagonalizable over the algebraic closure" in characteristic $p$. This needs a perfect field, as the [[imperfect field example|~d837395a]] shows.
- Thinking that $n$ eigenvalues counted with multiplicity make $T$ semisimple. The shear has the eigenvalue $1$ twice and is not semisimple.

## Explanations

### L1 human

A semisimple map is a map with no hidden "shearing" part.
Whenever it keeps a subspace in place, it also keeps a complementary subspace in place.
Over the complex numbers, this simply means that the map is diagonal in a suitable basis.
Over the real numbers, it also allows rotations, which have no real eigenvectors.

### L2 human

Decide whether $A = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$ is semisimple over $\R$.

1. The trace is $2$ and the determinant is $2$, so $p_A = t^2 - 2t + 2$.
2. The discriminant is $4 - 8 = -4 < 0$, so $p_A$ is irreducible over $\R$.
3. The minimal polynomial divides $p_A$ and is not constant, so $m_A = p_A$, which is squarefree.
4. So $A$ is semisimple over $\R$. Over $\C$ it has the distinct eigenvalues $1 \pm i$, so it is diagonalizable over $\C$.

The typical use is to test semisimplicity by checking that $m_T$ has no repeated irreducible factor.
The trap is to conclude from step 2 that $A$ is not semisimple because it has no real eigenvalue.

### L3 human

For a finite-dimensional algebra $A$ over a field, an element is semisimple when it acts semisimply in the regular representation.
In a linear algebraic group over a perfect field, every element $g$ has a multiplicative Jordan decomposition $g = g_s g_u$, with $g_s$ semisimple and $g_u$ unipotent.
In a semisimple Lie algebra, the abstract Jordan decomposition uses the semisimple and nilpotent parts of the adjoint map; this belongs to Lie theory.
