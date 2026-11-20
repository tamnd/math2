---
tag: 0PBN8VEKY8
kind: concept
name: Annihilating polynomial
aliases: [annihilating-polynomials, annihilator-of-an-endomorphism]
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
uses: [0E3MV6E6MG]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)
    locator: Formal definition
  - book: isbn:9780135367971
---

## Summary

Let $T$ be an endomorphism of a vector space $V$ over a field $F$.
An annihilating polynomial of $T$ is a polynomial $p \in F[x]$ with $p(T) = 0$, where $p(T)$ is the [[value of p at T|0E3MV6E6MG]].
The annihilating polynomials form an ideal $I_T$ of $F[x]$.
If $V$ is finite-dimensional, then $I_T \ne 0$, and its monic generator is the [[minimal polynomial|03NDVCSHSB]].

## Motivation

A polynomial relation such as $T^2 = T$ or $T^3 = 0$ controls the whole behaviour of $T$.
Every eigenvalue of $T$ is a root of every annihilating polynomial.
Annihilating polynomials also turn high powers of $T$ and the inverse $T^{-1}$ into polynomials in $T$ of low degree.

## Notation

The formal definition is the [[definition of an annihilating polynomial|052M4SX57M]].
The ideal is written $I_T$, $\operatorname{Ann}(T)$ or $\ker(\operatorname{ev}_T)$, the kernel of evaluation at $T$.

## Remarks

### Examples

- [[Polynomials in a projection|F5TTF31NR5]]: a projection $P$ is annihilated by $x^2 - x$ and by every multiple of it, such as $x^3 - x$.
- [[Minimal polynomials of a diagonal and a nilpotent matrix|APPAHXTJ6C]]: $(x - 1)(x - 2)$ annihilates $\operatorname{diag}(1, 1, 2)$, and $x^3$ annihilates the $3 \times 3$ shift.
- A reflection $R$ with $R^2 = I$ is annihilated by $x^2 - 1$.
- By the [[Cayley-Hamilton theorem|0F765KFC2J]], the characteristic polynomial annihilates $T$.

### Non-examples

- [[A polynomial that kills one vector but not the map|BF2G985KRZ]]: for the shear $A$, $x - 1$ kills $e_1$, but $A - I \ne 0$.
- For the derivative $D$ on $C^\infty(\R)$, no nonzero polynomial annihilates $D$, because every real number is an eigenvalue of $D$.

### Basic properties

- $I_T$ is an ideal of $F[x]$, by the theorem on [[annihilating polynomials|AH34SFJ8SF]].
- If $\dim V = n$ is finite, then $I_T$ contains a nonzero polynomial of degree at most $n^2$, by the same theorem, and of degree $n$, by the Cayley-Hamilton theorem.
- If $p(T) = 0$ and $Tv = \lambda v$ with $v \ne 0$, then $p(\lambda)v = p(T)v = 0$, so $p(\lambda) = 0$.
- Similar matrices have the same annihilating polynomials.

### History

Hoffman and Kunze organise their account of the minimal polynomial around the ideal of annihilating polynomials.

### Common errors

- Confusing $p(T) = 0$, an equation between maps, with $p(T)v = 0$ for one vector $v$.
- Forgetting the identity in the constant term: $T^2 - T - 2$ means $T^2 - T - 2I$.

## Explanations

### L1 human

An annihilating polynomial is a polynomial that becomes the zero map when we put $T$ into it.
For example, a reflection $R$ satisfies $R^2 = I$, so $x^2 - 1$ annihilates it.
Each such relation limits the possible eigenvalues to the roots of the polynomial.

### L2 human

We check that $p(x) = x^2 - 5x + 6$ annihilates $A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$.

1. $A^2 = \begin{pmatrix} 4 & 5 \\ 0 & 9 \end{pmatrix}$, because the $(1, 2)$ entry is $2 \cdot 1 + 1 \cdot 3 = 5$.
2. $A^2 - 5A + 6I = \begin{pmatrix} 4 - 10 + 6 & 5 - 5 \\ 0 & 9 - 15 + 6 \end{pmatrix} = 0$.
3. So the eigenvalues of $A$ lie among the roots $2$ and $3$ of $p$. They are $2$ and $3$, the diagonal entries.

The typical use is to bound the eigenvalues or to simplify powers of $A$.
A trap: an annihilating polynomial can have roots that are not eigenvalues.
Here $(x - 2)(x - 3)(x - 7)$ also annihilates $A$, but $7$ is not an eigenvalue.

### L3 human

$I_T$ is the kernel of the evaluation homomorphism $F[x] \to \End_F(V)$, and the annihilator of $V$ as an $F[x]$-module.
For an element of a finite-dimensional algebra, the same ideal gives the minimal polynomial of that element.
