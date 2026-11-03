---
tag: K7VVYFE9YJ
kind: statement
role: theorem
name: Cartan decomposition
msc: ["17B20", "22E46"]
uses: [EY9DN7QAX1, TWVQT18JXE, 59DHW3BZTW, 6QQF55DQ6K, 0G0RFPG8HR]
about: [EY9DN7QAX1]
sources:
  - url: https://en.wikipedia.org/wiki/Cartan_decomposition
---

## Statement

Let $\mathfrak{g}_0$ be a finite-dimensional [[semisimple Lie algebra|EY9DN7QAX1]] over $\R$ with [[Killing form|TWVQT18JXE]] $B$.
A *Cartan involution* of $\mathfrak{g}_0$ is an automorphism $\theta$ with $\theta^2 = \id$ such that $B_\theta(X, Y) = -B(X, \theta Y)$ is positive definite.
Then:

1. $\mathfrak{g}_0$ has a Cartan involution;
2. any two Cartan involutions of $\mathfrak{g}_0$ are conjugate by an inner automorphism of $\mathfrak{g}_0$;
3. for a Cartan involution $\theta$, let $\mathfrak{k}$ and $\mathfrak{p}$ be its [[eigenspaces|0G0RFPG8HR]] for $1$ and $-1$; then $\mathfrak{g}_0 = \mathfrak{k} \oplus \mathfrak{p}$;
4. $[\mathfrak{k}, \mathfrak{k}] \subseteq \mathfrak{k}$, $[\mathfrak{k}, \mathfrak{p}] \subseteq \mathfrak{p}$ and $[\mathfrak{p}, \mathfrak{p}] \subseteq \mathfrak{k}$;
5. $\mathfrak{k}$ and $\mathfrak{p}$ are orthogonal for $B$, and $B$ is negative definite on $\mathfrak{k}$ and positive definite on $\mathfrak{p}$.

The decomposition $\mathfrak{g}_0 = \mathfrak{k} \oplus \mathfrak{p}$ is the *Cartan decomposition* of $\mathfrak{g}_0$.

## Remarks

For existence, let $\mathfrak{g}$ be the complexification of $\mathfrak{g}_0$, a [[real form|59DHW3BZTW]] of which is $\mathfrak{g}_0$, with conjugation $\sigma$.
One finds a [[compact real form|6QQF55DQ6K]] $\mathfrak{u}$ of $\mathfrak{g}$ that is stable under $\sigma$.
Then the conjugation of $\mathfrak{g}$ with respect to $\mathfrak{u}$ restricts to a Cartan involution, with $\mathfrak{k} = \mathfrak{g}_0 \cap \mathfrak{u}$ and $\mathfrak{p} = \mathfrak{g}_0 \cap i\mathfrak{u}$.
Items 3 to 5 follow at once from $\theta^2 = \id$, from $\theta$ being an automorphism, and from the invariance of $B$ under $\theta$.
Example: for $\mathfrak{g}_0 = \mathfrak{sl}_n(\R)$, the map $\theta(X) = -X^T$ is a Cartan involution, $\mathfrak{k} = \mathfrak{so}(n)$ is the skew-symmetric matrices, and $\mathfrak{p}$ is the symmetric matrices of trace $0$.
This is the Lie algebra form of the polar decomposition of a matrix; the group form is the [[Cartan decomposition of a Lie group|A5JB9JQKR0]].

## Explanations

### L1 human

Every real semisimple Lie algebra splits into a part $\mathfrak{k}$ that behaves like rotations and a part $\mathfrak{p}$ that behaves like stretchings.
For real matrices of trace $0$, these parts are the skew-symmetric and the symmetric matrices.
The splitting is unique up to a symmetry of the algebra.

### L2 human

The subalgebra $\mathfrak{k}$ is the Lie algebra of a maximal compact subgroup of the corresponding Lie group, and $\mathfrak{p}$ models the tangent space of the symmetric space $G/K$.
The Cartan decomposition is the first step toward the Iwasawa decomposition and toward the classification of real simple Lie algebras by Satake diagrams.
