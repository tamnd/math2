---
tag: XFZ12FWK4F
kind: example
name: The derivative on polynomials of degree at most two is cyclic
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
instance_of: [42MMQBTP0M]
illustrates: [RK1QVMYW7H]
uses: [42MMQBTP0M, 0KCQ9Y3QKA, 0VH1TC1PWF, 03NDVCSHSB]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_subspace
    locator: Examples
---

## Example

Let $V$ be the space of polynomials of degree at most $2$ over $\mathbb{Q}$, and let $D \colon V \to V$ be the derivative, $D f = f'$.
We show that $x^2$ is a [[cyclic vector|42MMQBTP0M]] for $D$.

1. $D(x^2) = 2x$ and $D^2(x^2) = 2$, and $D^3(x^2) = 0$.
2. The polynomials $x^2$, $2x$, $2$ have distinct degrees and are nonzero, so they are linearly independent. Three independent vectors in the $3$-dimensional space $V$ form a [[basis|0KCQ9Y3QKA]].
3. So $Z(x^2; D) = V$, and $D$ is cyclic.
4. By step 1, $D^3$ kills $x^2$, and by step 2 no polynomial of degree less than $3$ does. So $m_{x^2} = x^3$.
5. In the basis $b_1 = x^2$, $b_2 = 2x$, $b_3 = 2$, we have $D b_1 = b_2$, $D b_2 = b_3$ and $D b_3 = 0$.
6. So the matrix of $D$ is the [[companion matrix|0VH1TC1PWF]] $C(x^3) = \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$.
7. The [[minimal polynomial|03NDVCSHSB]] and the characteristic polynomial of $D$ are both $x^3$.

## Remarks

The vector $x$ is not cyclic: $D x = 1$ and $D 1 = 0$, so $Z(x; D)$ is the space of polynomials of degree at most $1$.
The same works for polynomials of degree at most $n$: $x^n$ is cyclic and $m_D = x^{n+1}$.
Over a field of characteristic $p$ with $p \le n$, the example fails: $D(x^p) = p x^{p-1} = 0$.
For example, over $\mathbb{F}_2$ and $n = 2$, $D(x^2) = 0$, and $D$ has rank $1$, so $m_D = x^2 \ne x^3$, and $D$ is not cyclic.

## Explanations

### L1 human

Take the polynomial $x$ squared and differentiate it again and again.
You get $2x$, then $2$, then $0$.
The three polynomials $x$ squared, $2x$ and $2$ are enough to build every polynomial of degree at most two.
So one polynomial generates the whole space under differentiation.

### L2 human

1. Take $f = x^2 + x$. Then $Df = 2x + 1$ and $D^2 f = 2$.
2. The matrix of coefficients in the basis $1, x, x^2$ has columns $(0, 1, 1)$, $(1, 2, 0)$, $(2, 0, 0)$.
3. Its determinant is $-4 \ne 0$, so $f$ is also a cyclic vector.

The typical use is a model of a nilpotent cyclic map: the derivative is a single Jordan block $J_3(0)$ in the basis $2, 2x, x^2$.
The trap is to work over a field of small characteristic, where the derivative of $x^p$ is $0$.
