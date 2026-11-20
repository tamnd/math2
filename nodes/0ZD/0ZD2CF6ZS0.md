---
tag: 0ZD2CF6ZS0
kind: concept
name: Dual basis
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug1
specializes: [0KCQ9Y3QKA]
uses: [07JBSZE0V4, 0KCQ9Y3QKA, 04CYQHN6MC, 0R8X9XA83A]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_basis
    locator: Finite-dimensional vector spaces
  - url: https://en.wikipedia.org/wiki/Dual_basis
    locator: Examples
  - book: isbn:9783031410253
    locator: Section 3F
  - book: isbn:9780134860244
    locator: Section 2.6
same_as:
  wikidata: Q2297777
  wikipedia: Dual basis
---

## Summary

Let $V$ be a finite-dimensional vector space over a field $F$ with a [[basis|0KCQ9Y3QKA]] $b_1, \dots, b_n$.
The dual basis is the family of [[linear forms|07YQ1C78G0]] $b_1^*, \dots, b_n^*$ in the [[dual space|07JBSZE0V4]] $V^*$ with $b_i^*(b_j) = 1$ if $i = j$ and $b_i^*(b_j) = 0$ if $i \ne j$.
The form $b_i^*$ reads off coordinate $i$ in the basis: $b_i^*(a_1 b_1 + \dots + a_n b_n) = a_i$.
It is a basis of $V^*$, so $\dim V^* = \dim V$.

## Motivation

The [[coordinates|04CYQHN6MC]] of a vector in a basis are numbers that depend linearly on the vector.
So each coordinate is a linear form, and these forms deserve a name.
They are the dual basis.
With them, each vector and each form can be expanded in the basis without solving equations: $v = \sum_i b_i^*(v)\, b_i$ and $f = \sum_i f(b_i)\, b_i^*$.

## Notation

The dual basis of $b_1, \dots, b_n$ is written $b_1^*, \dots, b_n^*$, or $b^1, \dots, b^n$ with upper indices in physics and differential geometry.
The defining condition is written with the Kronecker delta: $b_i^*(b_j) = \delta_{ij}$.
The notation $b_i^*$ is misleading: $b_i^*$ depends on the whole basis, not only on the vector $b_i$.
Mathlib writes `Module.Basis.dualBasis`.

## Remarks

### Examples

- For the standard basis $e_1, \dots, e_n$ of $F^n$, the dual basis is the family of coordinate forms $e_i^*(x) = x_i$; see the [[row vectors as linear forms|~455e6319]].
- [[The dual basis of a basis of R^2|~9ec3ae83]]: for $b_1 = (1, 1)$ and $b_2 = (1, 2)$, the dual basis is $b_1^* = 2x - y$ and $b_2^* = -x + y$.
- [[Evaluation at nodes and Lagrange polynomials|~fbd2f34b]]: on $P_2(\R)$, the evaluations at $0, 1, 2$ are the dual basis of the Lagrange basis for these nodes.

### Non-examples

- [[The coordinate forms of an infinite basis|~d17873c6]] are linearly independent in $V^*$, but they do not span $V^*$. So there is no dual basis in infinite dimension.
- For a basis $b_1, b_2$ of $V$, the forms $b_1^*, b_2^*$ of one basis are not the forms of another basis with the same $b_1$. For $b_1 = (1, 1)$, the dual form $b_1^*$ is $y$ when $b_2 = (1, 0)$, but $2x - y$ when $b_2 = (1, 2)$.

### Basic properties

- The dual basis is a basis of $V^*$. This is the main step in the proof of the [[dimension of the dual space|00889YD15K]].
- Expansions: $v = \sum_i b_i^*(v)\, b_i$ for $v \in V$, and $f = \sum_i f(b_i)\, b_i^*$ for $f \in V^*$. Both follow because linear maps that agree on a basis are equal, by the [[theorem on maps determined by a basis|0R8X9XA83A]].
- If a new basis is $c_j = \sum_i p_{ij} b_i$ with matrix $P$, then the new dual basis has matrix $(P^{-1})^{\mathsf{T}}$ in the old dual basis, by the [[change of dual basis lemma|~6d879f22]].
- The dual basis of the dual basis is the image of $b_1, \dots, b_n$ under the evaluation map $V \to V^{**}$ of the [[double dual theorem|0ZJM9D7NPS]].
- In $F^n$, if the basis vectors are the columns of an invertible matrix $P$, then the dual basis forms are the rows of $P^{-1}$, since $P^{-1} P = I$.

### History

The idea of a dual or reciprocal basis appears in the vector calculus of Gibbs, in the 1880s, as the reciprocal system of three vectors in space.
The covariant and contravariant components of tensor calculus, from Ricci and Levi-Civita (1900), are coordinates in a basis and in its dual basis.

### Common errors

- Thinking that $b_i^*$ depends only on $b_i$. Changing $b_2$ changes $b_1^*$, as the non-example above shows.
- Using $P^{\mathsf{T}}$ or $P$ in place of $(P^{-1})^{\mathsf{T}}$ when the basis changes. Forms change "contragrediently", with the inverse transpose.
- Using the map $b_i \mapsto b_i^*$ as if it were a preferred isomorphism $V \to V^*$. It depends on the whole basis. For $V = \R^2$, the standard basis sends $(1, 1)$ to $x + y$, but the basis $(1, 1), (1, 2)$ sends $(1, 1)$ to $2x - y$.

## Explanations

### L1 human

A basis lets us describe each vector by a list of coordinates.
The dual basis is the list of rules that compute these coordinates.
The first rule returns the first coordinate, the second rule returns the second coordinate, and so on.
Each rule gives $1$ on its own basis vector and $0$ on the others.

### L2 human

In $F^n$, the dual basis is found by one matrix inversion.

1. Put the basis vectors $b_1, \dots, b_n$ as the columns of a matrix $P$.
2. Compute $P^{-1}$.
3. Row $i$ of $P^{-1}$ is the dual form $b_i^*$, because $(P^{-1} P)_{ij} = \delta_{ij}$ says that row $i$ applied to $b_j$ gives $\delta_{ij}$.

For example, $b_1 = (1, 1)$, $b_2 = (1, 2)$ give $P^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$, so $b_1^* = 2x - y$.
The typical use is to find coordinates: the coordinates of $v$ in the basis are $P^{-1} v$, that is, the values $b_i^*(v)$.
A trap: the dual form $b_1^*$ is not "the same vector as $b_1$, written as a row".

### L3 human

A basis of $V$ is an isomorphism $F^n \to V$, and the dual basis is the inverse isomorphism $V \to F^n$, read off one coordinate at a time.
The change rule with $(P^{-1})^{\mathsf{T}}$ is the reason why lower-index and upper-index quantities transform differently in tensor calculus.
With an inner product, the dual basis can be pulled back to $V$ as the reciprocal basis $b^1, \dots, b^n$ with $\langle b^i, b_j \rangle = \delta_{ij}$, as in crystallography.
In infinite dimension, a basis $B$ gives an injective map $V \to V^*$ by $b \mapsto b^*$, but its image is only the forms that vanish on all but finitely many elements of $B$.
