---
tag: 0X9MBPP2Z3
kind: concept
name: Space of linear maps
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
specializes: [000AYPA9AJ]
uses: [0NRYHJPQG2, 000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Vector space of linear maps
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: History
  - book: isbn:9783031410253
    locator: Chapter 3
  - book: isbn:9780135367971
    locator: Section 3.2
  - book: isbn:9780134860244
    locator: Section 2.2
---

## Summary

Linear maps can themselves be added and scaled, so the linear maps from one space to another form a vector space.
The space of linear maps $\Hom_F(V, W)$ is the set of all [[linear maps|0NRYHJPQG2]] from $V$ to $W$, as in the [[formal definition|0VPCJWGMP9]].
Maps are added and scaled value by value, and with these operations $\Hom_F(V, W)$ is again a [[vector space|000AYPA9AJ]] over $F$.

## Motivation

Expressions that combine linear maps appear everywhere.
The map $T - \lambda \id$ appears in the study of eigenvalues, and $aD + b\,\id$ appears in differential equations.
These operations stay inside the linear maps, so linear algebra applies to the maps themselves.

In coordinates, the maps from $F^n$ to $F^m$ correspond to the $m \times n$ matrices, and the sum and scalar multiple of maps correspond to the usual sum and scalar multiple of matrices.
So $\Hom_F(V, W)$ is the basis-free form of the space of matrices of a fixed size.

## Notation

The space is written $\Hom_F(V, W)$, $\Hom(V, W)$, $L(V, W)$ or $\mathcal L(V, W)$.
For $W = V$ it is written $\End(V)$ or $L(V)$, and for $W = F$ it is the [[dual space|07JBSZE0V4]] $V^*$.
Mathlib writes `V →ₗ[F] W` for the type of linear maps, with its vector space structure built in.

## Remarks

### Examples

The space [[Hom(F², F) of linear forms on F²|TZXEB00DW7]] consists of the maps $(x, y) \mapsto ax + by$, and it has dimension $2$.
[[A rotation plus a scaling of the plane|KC7XFCE6T1]] is again a linear map, and its matrix is the sum of the two matrices.
The space $\Hom(F^n, F^m)$ is identified with the matrices $M_{m \times n}(F)$ through $A \mapsto (x \mapsto Ax)$.

### What it is not

[[The invertible maps of a space|T1FZVSM1FN]] do not form a subspace of $\End(V)$, since $\id$ and $-\id$ are invertible while their sum $0$ is not.
The set of all maps $\R \to \R$ is a vector space, but most of its elements are not linear.
The linear ones form the subspace $\Hom(\R, \R)$, the maps $x \mapsto ax$.

### Properties

The zero vector of $\Hom(V, W)$ is the zero map, and the negative of $T$ is $v \mapsto -T(v)$.
In finite dimension, $\dim \Hom(V, W) = \dim V \cdot \dim W$, by the [[dimension theorem|0Z9N1ER0W0]].
After a choice of bases, the [[matrix of a linear map|0YQSGNYE3K]] gives an isomorphism $\Hom(V, W) \cong M_{m \times n}(F)$, where $n = \dim V$ and $m = \dim W$.
Composition $\Hom(U, V) \times \Hom(V, W) \to \Hom(U, W)$ is linear in each argument, by the [[theorem on composites|FSXBBV9C76]].
The space $\End(V)$ is also a ring under composition, the [[algebra of endomorphisms|5JA4CYT1TB]].

### History

Peano gave the modern definition of vector spaces and linear maps in 1888.
The space $\Hom(V, W)$ is the basis-free form of the space of matrices of a fixed size, which was studied first.

### Watch out

Two maps in $\Hom(V, W)$ have no product in general, since composition needs the target of one map to be the source of the other.
The pointwise product $v \mapsto S(v) \cdot T(v)$ is a different operation, and the [[pointwise product|ZVW35WJ3YZ]] of linear maps is not linear.
The dimensions multiply: $\dim \Hom(V, W)$ is $\dim V \cdot \dim W$, not $\dim V + \dim W$.

### Try it

First, for $S(x, y) = (x + y, \; 0)$ and $T(x, y) = (0, \; x - y)$ on $\R^2$, find $S + T$ and $2S$.
The sum is $(x + y, \; x - y)$, and $2S$ is $(2x + 2y, \; 0)$.

Second, what is $\dim \Hom(\R^3, \R^2)$?
It is $3 \cdot 2 = 6$, the number of entries of a $2 \times 3$ matrix.

## Explanations

### L1 human

Two linear maps from $V$ to $W$ can be added: send each vector to the sum of its two images.
A linear map can also be scaled.
The results are again linear maps, so the linear maps form a vector space.

### L2 human

To compute with $\Hom(V, W)$, choose bases and use matrices.
For $S(x, y) = (y, x)$ and $T(x, y) = (x, 0)$ on $\R^2$, the sum is $(S + T)(x, y) = (x + y, \; x)$.
Its matrix $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ is the sum of the matrices $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ of $S$ and $T$.
Watch out: the sum of two maps is not their composite.

### L3 human

The construction $\Hom(-, -)$ is a functor, contravariant in the first argument and covariant in the second.
For each $v \in V$, the evaluation map $\Hom(V, W) \to W$, $T \mapsto T(v)$, is linear.
In infinite dimension, $\Hom(V, W)$ can be much larger than the formula $\dim V \cdot \dim W$ suggests; for example, $\dim V^* > \dim V$ when $\dim V$ is infinite.
