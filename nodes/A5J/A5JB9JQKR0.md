---
tag: A5JB9JQKR0
kind: statement
role: theorem
name: Cartan decomposition of a Lie group
msc: ["22E46", "22E15"]
uses: [XJS07AJ50Y, H3QX1ZFC8K, T2EB8R9HEV]
about: [XJS07AJ50Y, T2EB8R9HEV]
sources:
  - url: https://en.wikipedia.org/wiki/Cartan_decomposition
---

## Statement

Let $G$ be a connected [[semisimple Lie group|XJS07AJ50Y]] with finite center, with Lie algebra $\mathfrak{g}$ and [[Killing form|TWVQT18JXE]] $B$.
Let $\theta$ be a Cartan involution of $\mathfrak{g}$: an automorphism with $\theta^2 = \id$ such that $(X, Y) \mapsto -B(X, \theta Y)$ is positive definite.
Let $\mathfrak{k}$ and $\mathfrak{p}$ be the eigenspaces of $\theta$ for the eigenvalues $1$ and $-1$, so that $\mathfrak{g} = \mathfrak{k} \oplus \mathfrak{p}$.
Let $K$ be the connected Lie subgroup of $G$ with Lie algebra $\mathfrak{k}$.
Then:

1. $K$ is a compact subgroup of $G$, and it is a [[maximal compact subgroup|T2EB8R9HEV]];
2. the map $K \times \mathfrak{p} \to G$, $(k, X) \mapsto k \exp X$, is a diffeomorphism, where $\exp$ is the [[exponential map|H3QX1ZFC8K]].

In particular $G = K \exp(\mathfrak{p})$.

## Remarks

A Cartan involution exists and is unique up to inner automorphisms; this is the [[Cartan decomposition of the Lie algebra|K7VVYFE9YJ]].
The proof of 2 lets $G$ act on the symmetric space $G/K$, which has nonpositive curvature.
Then the map $X \mapsto \exp(X) K$ is a diffeomorphism from $\mathfrak{p}$ onto $G/K$.

Example: $G = \mathrm{SL}_n(\R)$ with $\theta(X) = -X^{T}$.
Then $\mathfrak{k} = \mathfrak{so}(n)$, $\mathfrak{p}$ is the space of symmetric matrices of trace $0$, and $K = \mathrm{SO}(n)$.
The theorem is the polar decomposition: each $g \in \mathrm{SL}_n(\R)$ is uniquely $g = k e^{X}$ with $k$ orthogonal and $e^X$ symmetric positive definite.

Without a finite center, part 2 still holds with $K$ closed, but $K$ is no longer compact.
For the universal cover of $\mathrm{SL}_2(\R)$, the subgroup $K$ is isomorphic to $\R$.

## Explanations

### L1 human

Every element of a semisimple Lie group splits as a rotation part times a stretching part.
The rotation part lies in a compact subgroup $K$.
The stretching part is the exponential of an element of a vector space $\mathfrak{p}$.
For invertible matrices this is the familiar fact that a matrix is a rotation times a positive symmetric matrix.

### L2 human

The theorem shows that $G$ is diffeomorphic to $K \times \R^{d}$ with $d = \dim \mathfrak{p}$.
So the topology of $G$, for example its fundamental group, is the topology of the compact group $K$.
The quotient $G/K$ is a Riemannian symmetric space of noncompact type, diffeomorphic to $\mathfrak{p}$.
The Iwasawa decomposition $G = KAN$ and the decomposition $G = KAK$ refine this splitting.
