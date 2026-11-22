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

Let $V$ be the space of polynomials of degree at most $2$ over $\mathbb{Q}$, and let $D \colon V \to V$ be the derivative, $Df = f'$.
We show that $x^2$ is a [[cyclic vector|42MMQBTP0M]] for $D$, and we find the matrix of $D$ in the basis that it generates.

1. Differentiate $x^2$ three times: $D(x^2) = 2x$, $D^2(x^2) = 2$ and $D^3(x^2) = 0$.
2. The polynomials $x^2$, $2x$ and $2$ are nonzero and have distinct degrees, so they are linearly independent. Three independent vectors in the $3$-dimensional space $V$ form a [[basis|0KCQ9Y3QKA]].
3. So $Z(x^2; D) = V$, and $D$ is cyclic.
4. By step 1 the polynomial $x^3$ kills $x^2$, and by step 2 no nonzero polynomial of degree less than $3$ does. So the annihilator is $m_{x^2} = x^3$.
5. Write $b_1 = x^2$, $b_2 = 2x$ and $b_3 = 2$. Then $D b_1 = b_2$, $D b_2 = b_3$ and $D b_3 = 0$.
6. So the matrix of $D$ in this basis is the [[companion matrix|0VH1TC1PWF]] $C(x^3) = \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$.
7. The [[minimal polynomial|03NDVCSHSB]] and the characteristic polynomial of $D$ are both $x^3$, since they equal those of $C(x^3)$.

## Remarks

Not every vector works.
For $x$ we get $Dx = 1$ and $D1 = 0$, so $Z(x; D)$ is only the plane of polynomials of degree at most $1$.

The pattern holds for every degree over $\mathbb{Q}$.
On the polynomials of degree at most $n$, the vector $x^n$ is cyclic and the minimal polynomial of $D$ is $x^{n+1}$.

The field matters.
Over a field of characteristic $p$ with $p \le n$, the derivative of $x^p$ is $p x^{p-1} = 0$, and the chain breaks.
For example, over $\mathbb{F}_2$ with $n = 2$ we get $D(x^2) = 2x = 0$, $D(x) = 1$ and $D(1) = 0$.
Then $D^2 = 0$ while $D \ne 0$, so $m_D = x^2$, which is not the characteristic polynomial $x^3$, and $D$ is not cyclic.

## Explanations

### L1 human

Take the polynomial $x^2$ and differentiate it again and again.
You get $2x$, then $2$, then $0$.
The three polynomials $x^2$, $2x$ and $2$ are enough to build every polynomial of degree at most two, for example $5x^2 + 4x + 6 = 5 \cdot x^2 + 2 \cdot 2x + 3 \cdot 2$.
So one polynomial generates the whole space under differentiation.

### L2 human

Here is a test of a second vector.
Take $f = x^2 + x$, so that $Df = 2x + 1$ and $D^2 f = 2$.
Write the three polynomials in coordinates for the basis $1, x, x^2$: they are $(0, 1, 1)$, $(1, 2, 0)$ and $(2, 0, 0)$.
Put them as columns and expand along the last row:
$$\det \begin{pmatrix} 0 & 1 & 2 \\ 1 & 2 & 0 \\ 1 & 0 & 0 \end{pmatrix} = 1 \cdot (1 \cdot 0 - 2 \cdot 2) = -4 \ne 0.$$
So $f$ is also a cyclic vector.
In the reversed basis $2, 2x, x^2$ the derivative sends each vector to the one before it, so its matrix is the Jordan block $J_3(0)$.
The derivative is thus a model of a nilpotent cyclic map, and the trap is to use it over a field of small characteristic, where the derivative of $x^p$ is $0$.
