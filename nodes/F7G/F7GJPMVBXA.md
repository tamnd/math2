---
tag: F7GJPMVBXA
kind: concept
name: Invariant factors and elementary divisors of a matrix
aliases: [invariant-factors-of-a-matrix, elementary-divisors-of-a-matrix]
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: grad
uses: [KGVTFBZX59, 42MMQBTP0M, 0C3QBCR46M, 0PG2H7WKGG, 03FKX7Z5DC, 0WHCA4SVP2]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_normal_form
    locator: General case and theory
  - url: https://en.wikipedia.org/wiki/Invariant_factor
    locator: lead section
  - book: isbn:9780471433347
    locator: Section 12.2
---

## Summary

Let $F$ be a field and $A \in M_n(F)$, or let $T$ be an endomorphism of an $n$-dimensional space $V$.
The *invariant factors* of $A$ are the nonconstant [[monic polynomials|0C3QBCR46M]] $d_1 \mid d_2 \mid \cdots \mid d_r$ such that $F^n = Z(v_1) \oplus \cdots \oplus Z(v_r)$ with [[$A$-annihilators|42MMQBTP0M]] $m_{v_i} = d_i$; they exist and are unique by the [[cyclic decomposition theorem|R3Z20J19BR]].
Equivalently, the [[module|KGVTFBZX59]] $F^n_A$ is isomorphic to $F[x]/(d_1) \oplus \cdots \oplus F[x]/(d_r)$.
Write each $d_i$ as a product of powers of distinct monic [[irreducible polynomials|03FKX7Z5DC]].
The list of all these prime powers $p^e$, with repetitions, is the list of *elementary divisors* of $A$.
Both lists are complete invariants of similarity.
Two matrices are similar if and only if they have the same invariant factors, and if and only if they have the same elementary divisors.

## Motivation

Trace, determinant, rank, and the characteristic and minimal polynomials are similarity invariants, but even together they do not decide similarity.
The [[pair $J_2(1) \oplus J_2(1)$ and $J_2(1) \oplus I_2$|J4Q3B9ZNHF]] shares all of them and is not similar.
The invariant factors refine the characteristic polynomial $\chi_A = d_1 \cdots d_r$ and the minimal polynomial $m_A = d_r$ into a full list.
This list decides similarity, and it can be computed by row and column operations over $F[x]$.

## Notation

Many books, following the Smith normal form, list $n$ invariant factors $1, \dots, 1, d_1, \dots, d_r$, with $n - r$ entries equal to $1$.
Hoffman and Kunze list the nonconstant ones in the opposite order, $p_1 = m_A$ with $p_{k} \mid p_{k-1}$.
The elementary divisors are sometimes written $(x - \lambda)^k$ only, for algebraically closed $F$, where every irreducible polynomial is linear.
The same words are used for [[finitely generated abelian groups|0WHCA4SVP2]], with integers in place of polynomials.

## Remarks

### Examples

- For $A = J_2(1) \oplus J_1(1) \oplus J_1(2)$, the [[invariant factors are $x - 1$ and $(x - 1)^2 (x - 2)$|4415DMWRP1]], and the elementary divisors are $(x - 1)^2$, $x - 1$, $x - 2$.
- The two matrices of the [[pair $J_2(1) \oplus J_2(1)$ and $J_2(1) \oplus I_2$|1K0AP4D1S2]] have different invariant factors.
- A cyclic matrix has one invariant factor, $d_1 = \chi_A$.
- The scalar matrix $c I_n$ has $n$ invariant factors, all equal to $x - c$.
- $C(x^2 + 1)$ over $\mathbb{R}$ has the single invariant factor $x^2 + 1$ and the single elementary divisor $x^2 + 1$; over $\mathbb{C}$ the elementary divisors are $x - i$ and $x + i$.

### Non-examples

- The [[list $x, x - 1$ is not a list of invariant factors|JRYD5VTG8Z]], since $x$ does not divide $x - 1$; the matrix $\operatorname{diag}(0, 1)$ has the single invariant factor $x(x - 1)$.
- The list of eigenvalues with multiplicities is not a complete invariant: $I_2$ and $J_2(1)$ share it.
- The polynomial $(x - 1)^2 (x - 2)$ is not an elementary divisor, since it is not a power of one irreducible polynomial.

### Basic properties

- $d_r = m_A$ and $d_1 \cdots d_r = \chi_A$, so $\sum \deg d_i = n$.
- The invariant factors are the nonconstant diagonal entries of the [[Smith normal form of $xI - A$|92VZF0QRM8]], and $d_1 \cdots d_k$ is a quotient of gcds of minors of $xI - A$.
- From the invariant factors to the elementary divisors: factor each $d_i$ into prime powers.
- From the elementary divisors back: for each irreducible $p$, sort its powers $p^{e_1} \ge p^{e_2} \ge \cdots$. The product of the largest powers of all $p$ is $d_r$, the product of the second largest is $d_{r-1}$, and so on.
- They give the [[rational canonical form|042JWAR3Q0]] $C(d_1) \oplus \cdots \oplus C(d_r)$, and, when $\chi_A$ splits, the elementary divisors $(x - \lambda)^k$ give the Jordan blocks $J_k(\lambda)$.
- They do not change under field extension, so [[similarity does not depend on the field|5PVFX89NM7]].

### History

The invariant factors of a matrix are the invariant factors of the module $F^n_A$ in the structure theorem over the principal ideal domain $F[x]$.
They are also the diagonal entries of the Smith normal form of $xI - A$, which is named after Henry John Stephen Smith.

### Common errors

- Reading the invariant factors as the factors of $\chi_A$: for $\chi_A = (x - 1)^2$ the invariant factors are either $(x - 1)^2$ or $x - 1, x - 1$.
- Forgetting the repetitions in the list of elementary divisors.
- Forgetting the convention: with $n$ entries the list starts with ones, and the nonconstant entries are the same.

## Explanations

### L1 human

Two matrices can share many numbers, such as the trace and the determinant, and still not be the same map in different coordinates.
The invariant factors are a short list of polynomials that tells exactly when two matrices are the same map in different coordinates.
Each polynomial in the list divides the next one.
The last one is the minimal polynomial, and their product is the characteristic polynomial.

### L2 human

Find the invariant factors and elementary divisors of $A = \operatorname{diag}(1, 1, 2, 2, 2)$ over $\mathbb{Q}$.

1. The elementary divisors are the polynomials of the diagonal entries: $x - 1, x - 1, x - 2, x - 2, x - 2$.
2. Sort by prime: for $x - 1$ the powers are $1, 1$; for $x - 2$ they are $1, 1, 1$.
3. $d_3$ takes the largest power of each prime: $(x - 1)(x - 2)$.
4. $d_2$ takes the next ones: $(x - 1)(x - 2)$.
5. $d_1$ takes what is left: $x - 2$.
6. Check: $d_1 \mid d_2 \mid d_3$, and $d_1 d_2 d_3 = (x - 1)^2 (x - 2)^3 = \chi_A$.

The typical use is to decide whether two matrices are similar, by comparing their invariant factors.
The trap is to think that the number of invariant factors equals the number of distinct eigenvalues: here there are $3$ invariant factors and $2$ eigenvalues.

### L3 human

The invariant factors are the invariant factor decomposition of the torsion $F[x]$-module $F^n_A$, and the elementary divisors are its primary decomposition.
The same two forms exist for finite abelian groups.
Over the principal ideal domain $F[x]$ they can be computed by the Smith normal form of the presentation matrix $xI - A$.
For pairs of matrices up to simultaneous similarity there is no such finite list of invariants, which is the content of the [[wild problem|H3E52HTEZ2]].
