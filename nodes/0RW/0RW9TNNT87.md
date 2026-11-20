---
tag: 0RW9TNNT87
kind: concept
name: Orthonormal family
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
specializes: [01TXN7ETH2]
uses: [0Y2X7P2WB7, 0MFJJV97RJ]
sources:
  - url: https://en.wikipedia.org/wiki/Orthonormality
    locator: Definition
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-3.xml#L545
    locator: src/section6-3.xml:545
  - url: https://en.wikipedia.org/wiki/Gram–Schmidt_process
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 6
same_as:
  wikidata: Q1411166
  wikipedia: Orthonormality
---

## Summary

Let $V$ be an inner product space over $\mathbb{R}$ or $\mathbb{C}$.
A family $(e_i)_{i \in I}$ of vectors of $V$ is orthonormal when $\ip{e_i}{e_j} = 1$ for $i = j$ and $\ip{e_i}{e_j} = 0$ for $i \neq j$.
So the vectors are unit vectors for the [[induced norm|0MFJJV97RJ]], and any two of them are [[orthogonal|0Y2X7P2WB7]].
The [[formal definition|09VYHEF2VT]] states this with the Kronecker delta.
Orthonormal families matter because coefficients, lengths and inner products become simple formulas in them.

## Motivation

In $\mathbb{R}^n$ the standard basis vectors have length $1$ and meet at right angles.
For this reason, the coordinates of $x$ are the dot products $x \cdot e_j$, and the length of $x$ comes from its coordinates by Pythagoras.
We want the same simple formulas in every inner product space.
The property that makes them work is exactly $\ip{e_i}{e_j} = \delta_{ij}$, so we give it a name.

## Notation

- We write $(e_1, \dots, e_k)$ or $(e_i)_{i \in I}$, and $\delta_{ij}$ for the Kronecker delta.
- Some books say "orthonormal set" or "orthonormal list". A family can repeat a vector, but an orthonormal family never does, since $\ip{e_i}{e_j} = 0 \neq 1$ for $i \neq j$.
- An orthogonal family has $\ip{e_i}{e_j} = 0$ for $i \neq j$ but no condition on the lengths. Some books call an orthonormal family an orthogonal family of unit vectors.
- In Mathlib, `Orthonormal 𝕜 v` says that each `v i` has norm $1$ and that `v i` and `v j` are orthogonal for $i \neq j$.

## Remarks

### Examples

- The standard basis $e_1, \dots, e_n$ of $\mathbb{R}^n$ or $\mathbb{C}^n$ is orthonormal for the standard inner product, because $e_i \cdot e_j = \delta_{ij}$.
- In $\mathbb{R}^2$, $(\frac35, \frac45)$ and $(-\frac45, \frac35)$ are orthonormal: the norms are $\frac{9 + 16}{25} = 1$, and the dot product is $-\frac{12}{25} + \frac{12}{25} = 0$.
- In $\mathbb{C}^2$, $\frac{1}{\sqrt2}(1, i)$ and $\frac{1}{\sqrt2}(1, -i)$ are orthonormal. The [[orthonormal basis of $\mathbb{C}^2$|~22363b43]] checks this.
- For the [[trace inner product|~381c6461]] on $M_2(\mathbb{C})$, the four [[matrix units|A4HTT7JFD1]] $E_{jk}$ are orthonormal, because $\tr(E_{lm}^* E_{jk})$ is $1$ for $(j, k) = (l, m)$ and $0$ otherwise.
- On polynomials with $\ip{p}{q} = \int_{-1}^{1} p q$, the family $\frac{1}{\sqrt2}$, $\sqrt{\frac32}\,x$ is orthonormal: $\int_{-1}^1 \frac12 = 1$, $\int_{-1}^1 \frac32 x^2 = 1$ and $\int_{-1}^1 x = 0$. The [[Legendre polynomials|~8c407ecd]] continue it.
- The empty family is orthonormal, since there is nothing to check.

### Non-examples

- The vectors $(1, 1)$ and $(1, -1)$ of $\mathbb{R}^2$ are orthogonal, but their norm is $\sqrt2$, so the [[family is not orthonormal|~f4d12cdc]]. Dividing each by $\sqrt2$ repairs it.
- The unit vectors $(1, 0)$ and $\frac{1}{\sqrt2}(1, 1)$ of $\mathbb{R}^2$ are not orthonormal, because their dot product is $\frac{1}{\sqrt2} \neq 0$.
- The family $(1, 0)$, $(0, 1)$, $(1, 0)$ in $\mathbb{R}^2$ repeats a vector. The first and third vectors have inner product $1$, so the family is not orthonormal.
- Orthonormality depends on the inner product. For $\ip{x}{y} = 2x_1 y_1 + x_2 y_2$ on $\mathbb{R}^2$, the standard basis is not orthonormal, since $\ip{e_1}{e_1} = 2$.

### Basic properties

- An orthonormal family is [[linearly independent|0JWM6GJNQW]]. So in a space of dimension $n$ it has at most $n$ vectors.
- If $v = \sum_j a_j e_j$ is a finite combination, then $a_j = \ip{v}{e_j}$ and $\norm{v}^2 = \sum_j |a_j|^2$, by the [[Pythagorean theorem|0BVTDM872V]].
- An orthonormal family of $n$ vectors in a space of dimension $n$ is an [[orthonormal basis|0S9GGTR0EX]].
- The columns $q_1, \dots, q_k$ of an $n \times k$ matrix $Q$ are orthonormal in $\mathbb{K}^n$ if and only if $Q^* Q = I_k$, by the [[criterion for orthonormal columns|~f79cc316]].
- For each $v \in V$, [[Bessel's inequality|0RBT5PB74K]] gives $\sum_j |\ip{v}{e_j}|^2 \leq \norm{v}^2$.
- The [[Gram-Schmidt process|0VT6P0GNQR]] turns each finite independent family into an orthonormal family with the same initial spans.

### History

The [[Gram-Schmidt process|0VT6P0GNQR]], which produces orthonormal families, is named after Gram and Schmidt.
According to the Wikipedia article on the process, Laplace knew the method before Gram and Schmidt.

### Common errors

- Students call a family orthonormal when it is only orthogonal. The test $\ip{e_j}{e_j} = 1$ must be checked too.
- Students check only consecutive pairs, $\ip{e_1}{e_2}$, $\ip{e_2}{e_3}$, and so on. Every pair $i \neq j$ must be checked.
- Students compute in $\mathbb{C}^n$ without conjugates. Then $(1, i)/\sqrt2$ seems to have $\ip{e}{e} = \frac{1 + i^2}{2} = 0$, but the correct value is $1$.

## Explanations

### L1 human

An orthonormal family is a set of arrows of length $1$ that meet at right angles, two by two.
The arrows $(1, 0)$ and $(0, 1)$ in the plane are the first example.
The arrows $(0.6, 0.8)$ and $(-0.8, 0.6)$ are another: we turn the first pair by one angle.
With such arrows, the amount of a vector in each direction is one inner product.

### L2 human

Worked example: we test a family in $\mathbb{R}^3$.

1. Let $e_1 = \frac13(1, 2, 2)$, $e_2 = \frac13(2, 1, -2)$ and $e_3 = \frac13(2, -2, 1)$.
2. Norms: $\norm{e_1}^2 = \frac{1 + 4 + 4}{9} = 1$, and the same sum $9$ appears for $e_2$ and $e_3$.
3. Pairs: $e_1 \cdot e_2 = \frac{2 + 2 - 4}{9} = 0$, $e_1 \cdot e_3 = \frac{2 - 4 + 2}{9} = 0$ and $e_2 \cdot e_3 = \frac{4 - 2 - 2}{9} = 0$.
4. So the family is orthonormal, and the matrix with columns $e_1, e_2, e_3$ satisfies $Q^\top Q = I_3$.
5. For $v = (3, 3, 0)$, the coefficients are $v \cdot e_1 = 3$, $v \cdot e_2 = 3$ and $v \cdot e_3 = 0$, so $v = 3e_1 + 3e_2$.

The typical use is to compute coefficients without solving a linear system.
A trap: a family can pass the norm test and fail the pair test, or the other way round, so do both tests.

### L3 human

An orthonormal family is an isometric copy of the standard basis: the map $\mathbb{K}^k \to V$, $a \mapsto \sum_j a_j e_j$, preserves inner products.
In matrix language, the columns of $Q$ are orthonormal exactly when $Q^* Q = I$, so $Q$ is an isometry from $\mathbb{K}^k$ into $\mathbb{K}^n$.
For square $Q$ this gives the [[orthogonal matrices|0W02QESPJQ]] and the [[unitary matrices|0AR68JTMDT]].
In a [[Hilbert space|HM2HHE3J51]], infinite orthonormal families such as $e^{2\pi i k t}$ on $[0, 1]$ lead to [[Fourier series|G12KXDHPPS]].
The concept specializes the [[orthogonal family for a bilinear form|01TXN7ETH2]] to a positive definite form, with the extra condition of unit length.
