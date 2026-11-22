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

The invariant factors of a square matrix are a short list of polynomials that decides, all by itself, whether two matrices are similar.
The elementary divisors carry the same information, cut into prime powers.

Let $F$ be a field and $A \in M_n(F)$, or let $T$ be an endomorphism of an $n$-dimensional space $V$ over $F$.
The *invariant factors* of $A$ are the nonconstant [[monic polynomials|0C3QBCR46M]] $d_1 \mid d_2 \mid \cdots \mid d_r$ for which there is a decomposition
$$F^n = Z(v_1) \oplus \cdots \oplus Z(v_r)$$
into cyclic subspaces with [[$A$-annihilators|42MMQBTP0M]] $m_{v_i} = d_i$.
They exist and are unique by the [[cyclic decomposition theorem|R3Z20J19BR]].
In the language of [[modules|KGVTFBZX59]], $F^n_A \cong F[x]/(d_1) \oplus \cdots \oplus F[x]/(d_r)$.
Write each $d_i$ as a product of powers of distinct monic [[irreducible polynomials|03FKX7Z5DC]].
The list of all the prime powers $p^e$ that occur, with repetitions, is the list of *elementary divisors* of $A$.
Two matrices in $M_n(F)$ are similar if and only if they have the same invariant factors, and if and only if they have the same elementary divisors.

## Motivation

Trace, determinant, rank, and the characteristic and minimal polynomials are all unchanged by similarity, but even together they do not decide it.
The [[pair $J_2(1) \oplus J_2(1)$ and $J_2(1) \oplus I_2$|J4Q3B9ZNHF]] agrees on all of them, and the two matrices are not similar.
The invariant factors close this gap.
They refine the characteristic polynomial $\chi_A = d_1 \cdots d_r$ and the minimal polynomial $m_A = d_r$ into a full list, and the list is a complete invariant.

The list is also computable.
Row and column operations on the polynomial matrix $xI - A$ produce it without finding a single root, as the [[theorem on the characteristic matrix|92VZF0QRM8]] shows.
The invariant factors are the blocks of the [[rational canonical form|042JWAR3Q0]], and the elementary divisors $(x - \lambda)^k$ are the blocks of the [[Jordan normal form|085HQ5G5TE]].

## Notation

Many books follow the Smith normal form and list $n$ invariant factors $1, \dots, 1, d_1, \dots, d_r$, with $n - r$ entries equal to $1$.
The nonconstant entries are the same in both conventions.
Hoffman and Kunze list the nonconstant ones in the opposite order, $p_1 = m_A$ with $p_k \mid p_{k-1}$.
Over an algebraically closed field every irreducible polynomial is linear, so the elementary divisors there are all of the form $(x - \lambda)^k$.
The same words are used for [[finitely generated abelian groups|0WHCA4SVP2]], with integers in place of polynomials.

## Remarks

### From blocks to invariant factors

Take the block diagonal matrix $A = J_2(1) \oplus J_1(1) \oplus J_1(2)$ of size $4$.
Its elementary divisors are the polynomials of the Jordan blocks: $(x - 1)^2$, $x - 1$ and $x - 2$.
To build the invariant factors, sort the powers of each prime from the largest down.
The last invariant factor takes the largest power of every prime, the one before it takes the second largest, and so on:
$$d_2 = (x - 1)^2 (x - 2), \qquad d_1 = x - 1.$$
Check: $d_1 \mid d_2$, and $d_1 d_2 = (x - 1)^3 (x - 2) = \chi_A$.
The [[worked example of this matrix|4415DMWRP1]] also finds the cyclic vectors.

Two quick cases show the extremes.
A cyclic matrix has one invariant factor, $d_1 = \chi_A$.
The scalar matrix $c I_n$ has $n$ invariant factors, all equal to $x - c$, because every nonzero vector spans a cyclic subspace of dimension one.

### The list depends on the field only through factoring

The companion matrix $C(x^2 + 1)$ over $\mathbb{R}$ has the single invariant factor $x^2 + 1$.
Over $\mathbb{R}$ it is irreducible, so it is also the single elementary divisor.
Over $\mathbb{C}$ the invariant factor is still $x^2 + 1$, but it factors as $(x - i)(x + i)$, so the elementary divisors become $x - i$ and $x + i$.
The invariant factors never change under an extension of the field, and that is why [[similarity does not depend on the field|5PVFX89NM7]].

### Telling two matrices apart

Let $A = J_2(1) \oplus J_2(1)$ and $B = J_2(1) \oplus I_2$.
Both have $\chi = (x - 1)^4$ and $m = (x - 1)^2$.
The invariant factors are $(x - 1)^2, (x - 1)^2$ for $A$ and $x - 1, x - 1, (x - 1)^2$ for $B$.
The lists differ, even in length, so $A$ and $B$ are not similar, as the [[example on this pair|1K0AP4D1S2]] works out.

### What is not a list of invariant factors

The list $x, x - 1$ fails the divisibility condition, since $x \nmid x - 1$.
For $\operatorname{diag}(0, 1)$ the axes are cyclic subspaces with these annihilators, but the [[correct list is the single polynomial $x(x - 1)$|JRYD5VTG8Z]].
The polynomial $(x - 1)^2 (x - 2)$ is not an elementary divisor, because it is not a power of one irreducible polynomial.
The list of eigenvalues with multiplicities is not a complete invariant either: $I_2$ and $J_2(1)$ both have the eigenvalue $1$ twice and are not similar.

### The rules you can use

Since $d_r = m_A$ and $d_1 \cdots d_r = \chi_A$, the degrees add up to $n$.
The invariant factors are the nonconstant diagonal entries of the [[Smith normal form of $xI - A$|92VZF0QRM8]].
Each diagonal entry of that form is a quotient $D_k / D_{k-1}$, where $D_k$ is the monic gcd of the $k \times k$ minors of $xI - A$.
Passing from invariant factors to elementary divisors means factoring each $d_i$.
Passing back means the sorting rule of the first example.
The number $r$ of invariant factors is the largest dimension of an eigenspace, taken over the eigenvalues in an algebraic closure.

### Watch out

The invariant factors are not the factors of $\chi_A$.
For $\chi_A = (x - 1)^2$ there are two possible lists: the single factor $(x - 1)^2$ for $J_2(1)$, and $x - 1, x - 1$ for $I_2$.
A second trap is to drop repetitions from the elementary divisors.
For $I_2$ the list is $x - 1, x - 1$, and the single entry $x - 1$ would describe a matrix of size $1$.

### History

The invariant factors of a matrix are the invariant factors of the module $F^n_A$ in the structure theorem over the principal ideal domain $F[x]$.
They are also the diagonal entries of the Smith normal form of $xI - A$, which is named after Henry John Stephen Smith.

### Try it

First, find the invariant factors of a matrix with elementary divisors $x^2$, $x$ and $x - 1$.
The largest powers give $d_2 = x^2 (x - 1)$, and what is left gives $d_1 = x$.

Second, a $3 \times 3$ matrix has $\chi_A = (x - 1)^2 (x + 1)$ and $m_A = (x - 1)(x + 1)$; find its invariant factors.
The last one is $d_2 = m_A$, and the rest of $\chi_A$ is $\chi_A / m_A = x - 1$, so the list is $x - 1, (x - 1)(x + 1)$.

## Explanations

### L1 human

Two matrices can share many numbers, such as the trace and the determinant, and still not be the same map seen in different coordinates.
The invariant factors are a short list of polynomials that settles the question exactly.
Each polynomial in the list divides the next one.
The last one is the smallest polynomial that the matrix satisfies, and the product of all of them is the characteristic polynomial.
For example, the identity matrix of size two has the list $x - 1$, $x - 1$.

### L2 human

Here is a typical problem: find the invariant factors and the elementary divisors of $A = \operatorname{diag}(1, 1, 2, 2, 2)$ over $\mathbb{Q}$.
Each diagonal entry spans an eigenline, so the elementary divisors are $x - 1, x - 1, x - 2, x - 2, x - 2$.

Sort them by prime.
The prime $x - 1$ occurs with the powers $1, 1$, and the prime $x - 2$ with the powers $1, 1, 1$.
The longest column has length $3$, so there are three invariant factors.
Building from the top gives
$$d_3 = (x - 1)(x - 2), \qquad d_2 = (x - 1)(x - 2), \qquad d_1 = x - 2.$$
Check: $d_1 \mid d_2 \mid d_3$, and $d_1 d_2 d_3 = (x - 1)^2 (x - 2)^3 = \chi_A$.

The typical use is to decide whether two matrices are similar by comparing their invariant factors.
The trap is to expect one invariant factor for each eigenvalue: here there are $3$ invariant factors and only $2$ eigenvalues.

### L3 human

The invariant factors give the invariant factor decomposition of the torsion $F[x]$-module $F^n_A$, and the elementary divisors give its primary decomposition.
The same two forms exist for finite abelian groups, where the [[structure theorem|0RY0B72XAS]] plays the same role.
Over the principal ideal domain $F[x]$ both lists come from the Smith normal form of the presentation matrix $xI - A$.
For pairs of matrices up to simultaneous similarity there is no comparable finite list of invariants, and the [[classification essay|H3E52HTEZ2]] explains why that problem is called wild.
The invariant factors return in the count of [[conjugacy classes of $GL_n(\mathbb{F}_q)$|4FV9TDGWWH]].
