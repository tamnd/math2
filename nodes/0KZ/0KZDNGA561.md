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

The trace of an [[endomorphism|0J7H0YBFDJ]] $T$ of a finite-dimensional vector space $V$ is the [[trace|0XC1RDBY7A]] of its [[matrix|0YQSGNYE3K]] $[T]_B$ in a basis $B$ of $V$.
The value does not depend on the basis, so the trace is a property of the map.
It is a linear function $\End(V) \to F$ with $\tr(ST) = \tr(TS)$.
The trace of a projection is its rank, times $1$ in the field.

## Motivation

The trace of a matrix is easy to compute, but a matrix depends on the choice of a basis.
Similar matrices have the same trace, so the trace passes from matrices to linear maps.
The trace of $T$ is also the sum of the eigenvalues of $T$, counted with multiplicity, over an algebraically closed field.

## Notation

The [[definition|0RPDTWY2JS]] writes $\tr T = \tr [T]_B$.
Other notations are $\operatorname{Tr} T$ and $\operatorname{trace} T$.
Here $[T]_B$ is the matrix of $T$ with the same basis $B$ for the domain and the codomain.
In Mathlib, the trace of a linear map is `LinearMap.trace R M`.

## Remarks

### Examples

- [[The derivative on polynomials of degree at most 2|SFGW76FSS3]]: two bases give two different matrices, both with trace $0$.
- [[Transposition of 2 x 2 matrices|RKJES8857B]]: the map $X \mapsto X^\top$ on $M_2(\R)$ has trace $2$.
- [[A projection and the identity over F2|BJ3ZVHZ6VF]]: an oblique projection of rank $1$ has trace $1$, and the identity of $\mathbb{F}_2^2$ has trace $0$.
- The identity map of $V$ has trace $(\dim V) \cdot 1$.
- The map $v \mapsto cv$ has trace $(\dim V) \cdot c$.

### Non-examples

- [[A matrix with two bases|VND2T4RZK8]]: the diagonal sum of $[\id]_{C,B}$ with $C \ne B$ is not the trace of the identity.
- A linear map $T \colon V \to W$ with $V \ne W$ has no trace. Its matrices can be rectangular, and a change of bases in $V$ and $W$ can change the diagonal sum.

### Basic properties

- $\tr T = \tr [T]_B$ for every basis $B$, by the [[theorem on the independence of the basis|0WCPH5Z7FA]].
- $\tr(S + T) = \tr S + \tr T$ and $\tr(cT) = c \tr T$.
- $\tr(ST) = \tr(TS)$ for endomorphisms $S$ and $T$ of $V$.
- If $P$ is a projection, then $\tr P = (\rank P) \cdot 1_F$, by the [[theorem on the trace of a projection|BJTJ41YW55]].
- $\tr T$ is minus the coefficient of $x^{n-1}$ in the characteristic polynomial $\det(x \id - T)$, where $n = \dim V$.

### History

In German, the trace is called "Spur", and some books write $\operatorname{Sp} A$.

### Common errors

- Using two different bases for the domain and the codomain, as in the [[non-example|VND2T4RZK8]].
- Writing $\tr P = \rank P$ in positive characteristic. Over $\mathbb{F}_2$, the identity of $\mathbb{F}_2^2$ has rank $2$ but trace $0$.
- Assuming $\tr(STU) = \tr(SUT)$. Only cyclic permutations of the factors keep the trace.

## Explanations

### L1 human

To find the trace of a linear map, write its matrix in any basis and add the diagonal entries.
Every basis gives the same number.
So the trace belongs to the map itself.

### L2 human

Two bases $B$ and $B'$ give similar matrices $[T]_{B'} = P^{-1} [T]_B P$.
The trace of $P^{-1} M P$ equals the trace of $M P P^{-1} = M$, by the cyclic property.
So the trace of $T$ is well defined.

### L3 human

There is a definition without bases.
The map $V^* \otimes V \to \End(V)$, $f \otimes v \mapsto (x \mapsto f(x) v)$, is an isomorphism for finite-dimensional $V$.
The trace is the linear map $\End(V) \to F$ that corresponds to the evaluation $f \otimes v \mapsto f(v)$.
In infinite dimensions, the identity map has no trace, and only special classes of operators, such as trace-class operators, have one.
