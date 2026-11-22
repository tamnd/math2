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

An endomorphism is a linear map that sends a space into itself, so it can be applied again and again.
Precisely, an endomorphism of a vector space $V$ is a [[linear map|0NRYHJPQG2]] $T \colon V \to V$, as in the [[formal definition|0PTF1PTJK0]].
Endomorphisms can be composed with each other, so powers $T^k$ and polynomials $p(T)$ make sense.
An invertible endomorphism is an automorphism.

## Motivation

Many linear maps send a space into itself: rotations of the plane, the derivative on polynomials, a change of state in a dynamical system.
For such a map, the output $T(v)$ lies in the same space as the input $v$.
So one can compare $T(v)$ with $v$, ask whether $T(v) = \lambda v$, and iterate $T$.
Eigenvalues, the trace and the determinant are defined for endomorphisms for this reason.

## Notation

The set of endomorphisms of $V$ is written $\End_F(V)$, $\End(V)$ or $L(V)$.
An endomorphism is also called a linear operator on $V$, or a linear transformation of $V$.
Powers are defined by $T^0 = \id_V$ and $T^{k+1} = T \circ T^k$.
The invertible endomorphisms form the [[general linear group|0FCHE902D7]] $GL(V)$.

## Remarks

### Examples

[[The rotation by a quarter turn|HGGYPYA9XB]] of $\R^2$ is an automorphism with $R^4 = \id$.
[[The derivative on quadratic polynomials|29A5DCNMHJ]] is an endomorphism $D$ of $P_2$ with $D^3 = 0$.
For a square matrix $A \in M_n(F)$, the map $x \mapsto Ax$ is an endomorphism of $F^n$.
The identity $\id_V$ and the zero map are endomorphisms of every space $V$.

### What it is not

[[The projection of R³ onto R²|VPN91Y1K18]], $(x, y, z) \mapsto (x, y)$, is linear but not an endomorphism, since its target differs from its source.
The map $x \mapsto x + 1$ of $\R$ sends $\R$ to itself, but it is not linear, so it is not an endomorphism in the sense of linear algebra.

### Properties

The composite of two endomorphisms of $V$ is an endomorphism of $V$, by the [[theorem on composites|FSXBBV9C76]].
The set $\End(V)$ is a vector space, as the case $W = V$ of the [[space of linear maps|0X9MBPP2Z3]], and with composition it is the [[algebra of endomorphisms|5JA4CYT1TB]].
In finite dimension, an endomorphism is injective exactly when it is surjective, by the [[theorem on endomorphisms|0912EEEVCT]].
The invertible endomorphisms are the units of the ring $\End(V)$, so $GL(V)$ is the [[group of units|07C6ECNJET]] of $\End(V)$.

### Endomorphisms and square matrices

In a basis of an $n$-dimensional space, an endomorphism has an $n \times n$ [[matrix|0YQSGNYE3K]], and powers of the map become powers of the matrix.
A change of basis with matrix $P$ replaces the matrix $A$ by $P^{-1} A P$.
So quantities that do not change under $A \mapsto P^{-1} A P$, such as the trace and the determinant, belong to the endomorphism itself.

### History

Peano gave the modern definition of vector spaces and linear maps in 1888.
In abstract algebra, the word endomorphism means more generally a homomorphism from any object to itself.

### Watch out

A map between two spaces of the same dimension is not an endomorphism unless the spaces are the same: an isomorphism $P_2 \to \R^3$ is not one.
For a map $T \colon V \to W$ with $W \ne V$, the expression $T^2$ has no meaning, since $T \circ T$ is not defined.
In infinite dimension, an injective endomorphism need not be invertible, and the [[right shift|N1G1WQW59J]] is a counterexample.

### Try it

First, for the swap $T(x, y) = (y, x)$ of $\R^2$, find $T^2$.
We get $T^2(x, y) = T(y, x) = (x, y)$, so $T^2 = \id$.

Second, is $(x, y) \mapsto (x, \; y, \; x + y)$ an endomorphism?
No: it is linear, but its source is $\R^2$ and its target is $\R^3$.

## Explanations

### L1 human

An endomorphism is a linear map that sends a space into the same space.
Because the output lives where the input lives, the map can be applied again and again.
Rotating the plane by a quarter turn four times gives back each vector.

### L2 human

For an endomorphism $T$ of $V$, ask what $T$, $T^2$ and $T^3$ do.
For the derivative $D$ on polynomials of degree at most $2$, we get $D^3 = 0$, since three derivatives kill each quadratic.
In a basis, an endomorphism of $F^n$ is a square matrix, and powers of $T$ are powers of the matrix.
Watch out: maps whose source and target differ cannot be composed with themselves.

### L3 human

In category theory, an endomorphism is an arrow from an object to itself, and the endomorphisms of an object form a monoid.
For a vector space, this monoid is the multiplicative part of the ring $\End(V)$.
Spectral theory, the Jordan normal form and the theory of [[nilpotent endomorphisms|063D5Z2C70]] all study the structure of single endomorphisms.
