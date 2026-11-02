---
tag: SM2KFBGJTH
kind: definition
name: Hom functor
msc: [18A25, 18A05]
defines: VJXS8AK67E
uses: [A2DE66937D, 859F0TFVA3, 28NQ0KRHD3, DAMK8XE1FR, AFNE9C4NH6, 0BSJ7RQ9BW]
sources:
  - url: https://en.wikipedia.org/wiki/Hom_functor
---

## Definition

Let $\mathcal{C}$ be a locally small [[category|A2DE66937D]], so that for all objects $X, Y$ the [[morphisms|859F0TFVA3]] $X \to Y$ form a [[set|0BSJ7RQ9BW]] $\Hom(X, Y)$.
Let $\mathbf{Set}$ be the category of sets and functions, and let $A$ be an object of $\mathcal{C}$.

1. The *covariant hom functor* $\Hom(A, -) \colon \mathcal{C} \to \mathbf{Set}$ sends an object $X$ to $\Hom(A, X)$ and a morphism $f \colon X \to Y$ to the function $\Hom(A, f) \colon \Hom(A, X) \to \Hom(A, Y)$, $g \mapsto f \circ g$.
2. The *contravariant hom functor* $\Hom(-, A) \colon \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}$ sends an object $X$ to $\Hom(X, A)$ and a morphism $f \colon X \to Y$ to the function $\Hom(f, A) \colon \Hom(Y, A) \to \Hom(X, A)$, $h \mapsto h \circ f$.

## Remarks

Associativity of composition gives $\Hom(A, f' \circ f) = \Hom(A, f') \circ \Hom(A, f)$, and $\Hom(A, \id_X)$ is the identity, so clause 1 defines a [[functor|28NQ0KRHD3]].
Clause 2 defines a contravariant functor, that is, a functor on the [[opposite category|DAMK8XE1FR]] $\mathcal{C}^{\mathrm{op}}$.
The two together form the bifunctor $\Hom(-, -) \colon \mathcal{C}^{\mathrm{op}} \times \mathcal{C} \to \mathbf{Set}$ on the [[product category|AFNE9C4NH6]].
Other notations are $\mathcal{C}(A, X)$, $h^A = \Hom(A, -)$ and $h_A = \Hom(-, A)$.

Example: in the category of real vector spaces, take $A = \R$.
A linear map $\R \to V$ is determined by the image of $1$, so $\Hom(\R, V)$ is in bijection with $V$, and $\Hom(\R, f)$ corresponds to $f$ itself.

Non-example: the assignment $X \mapsto \Hom(A, X)$ with $f \mapsto (g \mapsto g \circ f)$ is not a covariant hom functor.
For $f \colon X \to Y$ and $g \colon A \to X$, the composite $g \circ f$ is in general not defined.
So it does not give a function $\Hom(A, X) \to \Hom(A, Y)$.
