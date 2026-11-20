---
tag: 0J7H0YBFDJ
kind: concept
name: Endomorphism
aliases: [linear-operator]
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
specializes: [0NRYHJPQG2]
uses: [0NRYHJPQG2]
sources:
  - url: https://en.wikipedia.org/wiki/Endomorphism
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Endomorphisms and automorphisms
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: History
  - book: isbn:9783031410253
    locator: Chapter 3
  - book: isbn:9780135367971
    locator: Section 3.2
---

## Summary

An endomorphism of a vector space $V$ is a [[linear map|0NRYHJPQG2]] $T \colon V \to V$ from the space to itself.
Endomorphisms can be composed with each other, so powers $T^k$ and polynomials $p(T)$ make sense.
An invertible endomorphism is an automorphism.

## Motivation

Many linear maps send a space into itself: rotations of the plane, the derivative on polynomials, a change of state in a dynamical system.
For such a map, the image $T(v)$ lies in the same space as $v$.
So one can compare $T(v)$ with $v$, ask whether $T(v) = \lambda v$, and iterate $T$.
Eigenvalues, the trace and the determinant are defined for endomorphisms for this reason.

## Notation

The set of endomorphisms of $V$ is written $\End_F(V)$, $\End(V)$ or $L(V)$.
An endomorphism is also called a linear operator on $V$, or a linear transformation of $V$.
Powers are $T^0 = \id_V$ and $T^{k+1} = T \circ T^k$.
The invertible endomorphisms form the [[general linear group|0FCHE902D7]] $GL(V)$.

## Remarks

### Examples

- [[The rotation by a quarter turn|~197ae80d]] of $\R^2$, an automorphism with $R^4 = \id$.
- [[The derivative on quadratic polynomials|~1197ce29]], an endomorphism $D$ of $P_2$ with $D^3 = 0$.
- For a square matrix $A \in M_n(F)$, the map $x \mapsto Ax$ of $F^n$.
- The identity $\id_V$ and the zero map $0$ of each space $V$.

### Non-examples

- [[The projection of $\R^3$ onto $\R^2$|~696fc91b]], $(x, y, z) \mapsto (x, y)$, is linear but not an endomorphism, since its codomain differs from its domain.
- The map $x \mapsto x + 1$ of $\R$ sends $\R$ to itself, but it is not linear.

### Basic properties

- The composite of two endomorphisms of $V$ is an endomorphism of $V$, by the [[theorem on composites|~ed2e194c]].
- $\End(V)$ is a vector space, as the case $W = V$ of the [[space of linear maps|0X9MBPP2Z3]]. With composition, it is the [[algebra of endomorphisms|~42300f41]].
- In finite dimension, an endomorphism is injective if and only if it is surjective, by the [[theorem on endomorphisms|0912EEEVCT]].
- In a basis of an $n$-dimensional space, an endomorphism has an $n \times n$ [[matrix|0YQSGNYE3K]]. A change of basis replaces the matrix $A$ by $P^{-1} A P$.
- The invertible endomorphisms are the units of the ring $\End(V)$, so $GL(V)$ is the [[group of units|07C6ECNJET]] of $\End(V)$.

### History

Peano gave the modern definition of vector spaces and linear maps in 1888.
Endomorphisms are the linear maps whose domain and codomain are the same space.
In abstract algebra, the word means more generally a homomorphism from any object to itself.

### Common errors

- Calling every square-matrix-like map an endomorphism. A map $\R^3 \to \R^2$ is not one, and neither is an isomorphism $P_2 \to \R^3$.
- Writing $T^2$ for a map $T \colon V \to W$ with $W \ne V$. The composite $T \circ T$ is not defined.
- Assuming that an injective endomorphism is invertible in infinite dimension. The [[right shift|~834be223]] is a counterexample.

## Explanations

### L1 human

An endomorphism is a linear map that sends a space into the same space.
Because the output lives where the input lives, the map can be applied again and again.
Rotating the plane by a quarter turn four times gives back each vector.

### L2 human

For an endomorphism $T$ of $V$, ask what $T$, $T^2$ and $T^3$ do.
For the derivative $D$ on polynomials of degree at most $2$, $D^3 = 0$, since three derivatives kill each quadratic.
In a basis, an endomorphism of $F^n$ is a square matrix, and powers of $T$ are powers of the matrix.
The trap is to compose maps whose domain and codomain differ.

### L3 human

In category theory, an endomorphism is an arrow from an object to itself, and the endomorphisms of an object form a monoid.
For a vector space, this monoid is the multiplicative part of the ring $\End(V)$.
Spectral theory, Jordan normal form and the theory of [[nilpotent endomorphisms|063D5Z2C70]] all study the structure of single endomorphisms.
