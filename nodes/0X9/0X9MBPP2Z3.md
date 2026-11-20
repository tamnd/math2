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

The space of linear maps $\Hom_F(V, W)$ is the set of all [[linear maps|0NRYHJPQG2]] from $V$ to $W$.
Maps are added and scaled value by value.
With these operations, $\Hom_F(V, W)$ is again a [[vector space|000AYPA9AJ]] over $F$.

## Motivation

Linear maps are often added and scaled.
For example, $T - \lambda \id$ appears in the study of eigenvalues, and $aD + b\id$ appears in differential equations.
These operations stay inside the linear maps, so the linear maps form a vector space.
Then linear algebra applies to the maps themselves.
In coordinates, the maps from $F^n$ to $F^m$ correspond to the $m \times n$ matrices, with their usual sum and scalar multiple.

## Notation

The space is written $\Hom_F(V, W)$, $\Hom(V, W)$, $L(V, W)$ or $\mathcal L(V, W)$.
For $W = V$, it is written $\End(V)$ or $L(V)$.
For $W = F$, it is the [[dual space|07JBSZE0V4]], written $V^*$.
Mathlib writes `V →ₗ[F] W` for the type of linear maps, with its vector space structure built in.

## Remarks

### Examples

- [[The linear forms on $F^2$|~ca677c2c]]: $\Hom(F^2, F)$ is the set of maps $(x, y) \mapsto ax + by$, a space of dimension $2$.
- [[Sums and multiples of two plane maps|~91f1668e]]: a rotation plus a scaling of $\R^2$ is again a linear map.
- $\Hom(F^n, F^m)$, identified with the matrices $M_{m \times n}(F)$ through $A \mapsto (x \mapsto Ax)$.

### Non-examples

- [[The invertible maps of a space|~82757841]] do not form a subspace of $\End(V)$: $\id$ and $-\id$ are invertible, but their sum $0$ is not.
- The set of all maps $\R \to \R$ is a vector space, but its elements are not all linear. The linear ones form the subspace $\Hom(\R, \R)$.

### Basic properties

- The zero vector of $\Hom(V, W)$ is the zero map, and the negative of $T$ is $v \mapsto -T(v)$.
- In finite dimension, $\dim \Hom(V, W) = \dim V \cdot \dim W$, by the [[dimension theorem|0Z9N1ER0W0]].
- After a choice of bases, the [[matrix of a linear map|0YQSGNYE3K]] gives an isomorphism $\Hom(V, W) \cong M_{m \times n}(F)$, where $n = \dim V$ and $m = \dim W$.
- Composition $\Hom(U, V) \times \Hom(V, W) \to \Hom(U, W)$ is linear in each argument, by the [[theorem on composites|~ed2e194c]].
- The space $\End(V) = \Hom(V, V)$ is also a ring under composition, the [[algebra of endomorphisms|~42300f41]].

### History

Cayley introduced matrix notation in 1857.
Peano gave the modern definition of vector spaces and linear maps in 1888.
The space $\Hom(V, W)$ is the basis-free form of the space of matrices of a fixed size.

### Common errors

- Thinking that the product of two linear maps in $\Hom(V, W)$ is defined. Composition needs the codomain of one map to equal the domain of the other.
- Confusing the pointwise product $(ST)(v) = S(v) \cdot T(v)$ with composition. The [[pointwise product|~8cc2e580]] is not linear.
- Writing $\dim \Hom(V, W) = \dim V + \dim W$. The dimensions multiply.

## Explanations

### L1 human

Two linear maps from $V$ to $W$ can be added: send each vector to the sum of its two images.
A linear map can also be scaled.
The results are again linear maps, so the linear maps form a vector space.

### L2 human

To compute with $\Hom(V, W)$, choose bases and use matrices.
For $S(x, y) = (y, x)$ and $T(x, y) = (x, 0)$ on $\R^2$, the sum is $(S + T)(x, y) = (x + y,\ x)$.
Its matrix $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ is the sum of the matrices of $S$ and $T$.
The trap is to confuse the sum of maps with their composite.

### L3 human

$\Hom(-, -)$ is a functor, contravariant in the first argument and covariant in the second.
For each $v \in V$, the evaluation map $\Hom(V, W) \to W$, $T \mapsto T(v)$, is linear.
In infinite dimension, $\Hom(V, W)$ can be much larger than the formula $\dim V \cdot \dim W$ suggests; for example, $\dim V^* > \dim V$ when $\dim V$ is infinite.
