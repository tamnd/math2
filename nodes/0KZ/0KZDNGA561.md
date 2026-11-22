---
tag: 0KZDNGA561
kind: concept
name: Trace of a linear map
msc: ["15A04", "15A15"]
topics: [S6559D61BP]
audience: ug1
uses: [0J7H0YBFDJ, 0XC1RDBY7A, 0YQSGNYE3K]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a linear operator
  - book: isbn:9783031410253
---

## Summary

The trace of a linear map is the diagonal sum of any of its matrices, and every basis gives the same number.
Let $V$ be a finite-dimensional vector space over a field $F$ and let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]].
The trace of $T$ is the [[trace|0XC1RDBY7A]] of its [[matrix|0YQSGNYE3K]] $[T]_B$ in a basis $B$ of $V$.
The value does not depend on $B$, because the matrices in two bases are similar and the trace has the cyclic property $\tr(XY) = \tr(YX)$.
So the trace is a linear function $\End(V) \to F$, and it satisfies $\tr(ST) = \tr(TS)$.
The trace of a projection is its rank, times $1$ in the field.

## Motivation

The trace of a matrix is easy to compute, but a matrix depends on the choice of a basis.
A quantity that belongs to the map should not depend on that choice.
Two bases give the matrices $M$ and $P^{-1}MP$, and the trace cannot tell them apart.
So the trace passes from matrices to linear maps.
Over an algebraically closed field, the trace of $T$ is also the sum of the eigenvalues of $T$, counted with multiplicity.

## Notation

The [[definition|0RPDTWY2JS]] writes $\tr T = \tr [T]_B$.
Other notations are $\operatorname{Tr} T$ and $\operatorname{trace} T$.
Here $[T]_B$ is the matrix of $T$ with the same basis $B$ for the domain and the codomain.
In Mathlib, the trace of a linear map is `LinearMap.trace R M`.

## Remarks

### A first computation

Let $T \colon \mathbb{R}^2 \to \mathbb{R}^2$ have the matrix $M = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ in the standard basis, so $\tr T = 1 + 4 = 5$.
In the basis $B' = ((1, 1), (1, -1))$ the change of basis matrix is $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, with $P^{-1} = \tfrac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.
We get $MP = \begin{pmatrix} 3 & -1 \\ 7 & -1 \end{pmatrix}$ and
$$[T]_{B'} = P^{-1}MP = \frac{1}{2}\begin{pmatrix} 10 & -2 \\ -4 & 0 \end{pmatrix} = \begin{pmatrix} 5 & -1 \\ -2 & 0 \end{pmatrix}.$$
The matrix is different, but its trace is $5 + 0 = 5$ again.

### More examples

- [[The derivative on polynomials of degree at most 2|SFGW76FSS3]]: two bases give two different matrices, both with trace $0$.
- [[Transposition of 2 x 2 matrices|RKJES8857B]]: the map $X \mapsto X^\top$ on $M_2(\mathbb{R})$ has trace $2$.
- [[A projection and the identity over F2|BJ3ZVHZ6VF]]: an oblique projection of rank $1$ has trace $1$, and the identity of $\mathbb{F}_2^2$ has trace $0$.
- The identity map of $V$ has trace $(\dim V) \cdot 1$, and the map $v \mapsto cv$ has trace $(\dim V) \cdot c$.
- On $M_2(F)$, the map $X \mapsto AX$ has trace $2 \tr A$, since in the basis $(E_{11}, E_{21}, E_{12}, E_{22})$ its matrix is block diagonal with two copies of $A$.

### What it is not

- [[A matrix with two bases|VND2T4RZK8]]: the diagonal sum of $[\mathrm{id}]_{C,B}$ with $C \ne B$ is not the trace of the identity.
- A linear map $T \colon V \to W$ with $V \ne W$ has no trace.
  Its matrices can be rectangular, and a change of bases in $V$ and $W$ separately can change the diagonal sum.

### The rules you can use

- $\tr T = \tr [T]_B$ for every basis $B$, by the [[theorem on the independence of the basis|0WCPH5Z7FA]].
- $\tr(S + T) = \tr S + \tr T$ and $\tr(cT) = c \tr T$.
- $\tr(ST) = \tr(TS)$ for endomorphisms $S$ and $T$ of $V$.
- If $P$ is a projection, then $\tr P = (\rank P) \cdot 1_F$, by the [[theorem on the trace of a projection|BJTJ41YW55]].
- $\tr T$ is minus the coefficient of $x^{n-1}$ in the characteristic polynomial $\det(x\,\mathrm{id} - T)$, where $n = \dim V$.

### Watch out

- The domain and the codomain must use the same basis, as the [[non-example|VND2T4RZK8]] shows.
- In positive characteristic, $\tr P = \rank P$ can fail for a projection.
  Over $\mathbb{F}_2$, the identity of $\mathbb{F}_2^2$ has rank $2$ but trace $1 + 1 = 0$.
- Only cyclic permutations of the factors keep the trace, so in general $\tr(STU) \ne \tr(SUT)$.

### History

In German the trace is called "Spur", and some books write $\operatorname{Sp} A$.

### Try it

1. Find the trace of the map $p(x) \mapsto p(x + 1)$ on the real polynomials of degree at most $2$.
2. Check that $A = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$ satisfies $A^2 = A$, and compare its trace with its rank.

Answers: in the basis $(1, x, x^2)$ the images are $1$, $1 + x$ and $1 + 2x + x^2$, so the diagonal is $1, 1, 1$ and the trace is $3$.
For the second, $A^2 = A$ by direct multiplication, and $\tr A = 1 = \rank A$.

## Explanations

### L1 human

To find the trace of a linear map, write its matrix in any basis and add the diagonal entries.
Every basis gives the same number.
So the trace belongs to the map itself.

### L2 human

Two bases $B$ and $B'$ give similar matrices $[T]_{B'} = P^{-1} [T]_B P$.
The trace of $P^{-1} M P$ equals the trace of $M P P^{-1} = M$, by the cyclic property.
So the trace of $T$ is well defined.
For a projection, a basis made of vectors of the image and of the kernel gives a diagonal matrix with entries $1$ and $0$, so the trace counts the rank.

### L3 human

There is a definition without bases.
The map $V^* \otimes V \to \End(V)$, $f \otimes v \mapsto (x \mapsto f(x) v)$, is an isomorphism for finite-dimensional $V$.
The trace is the linear map $\End(V) \to F$ that corresponds to the evaluation $f \otimes v \mapsto f(v)$.
In infinite dimensions the identity map has no trace, and only special classes of operators, such as trace-class operators, have one.
