---
tag: 9P83YFRWDJ
kind: definition
name: Profunctor
msc: [18D60]
defines: EAPHAQVVD5
uses: [A2DE66937D, 28NQ0KRHD3, DAMK8XE1FR, AFNE9C4NH6, VJXS8AK67E, W9QTFV0Z8D]
sources:
  - url: https://en.wikipedia.org/wiki/Profunctor
---

## Definition

Let $\mathcal{C}$ and $\mathcal{D}$ be [[categories|A2DE66937D]], and let $\mathcal{D}^{\mathrm{op}}$ be the [[opposite category|DAMK8XE1FR]] of $\mathcal{D}$.
A *profunctor* $P$ from $\mathcal{C}$ to $\mathcal{D}$, written $P \colon \mathcal{C} \nrightarrow \mathcal{D}$, is a [[functor|28NQ0KRHD3]]
$$P \colon \mathcal{D}^{\mathrm{op}} \times \mathcal{C} \to \mathbf{Set}$$
on the [[product category|AFNE9C4NH6]].
A morphism of profunctors is a natural transformation between such functors.

## Remarks

Conventions differ: some authors call the same functor a profunctor from $\mathcal{D}$ to $\mathcal{C}$.
For small $\mathcal{D}$ it is the same as a functor $\mathcal{C} \to [\mathcal{D}^{\mathrm{op}}, \mathbf{Set}]$, from $\mathcal{C}$ to presheaves on $\mathcal{D}$.
Example: the [[hom functor|VJXS8AK67E]] $\Hom_{\mathcal{C}} \colon \mathcal{C}^{\mathrm{op}} \times \mathcal{C} \to \mathbf{Set}$ is a profunctor from $\mathcal{C}$ to $\mathcal{C}$, the identity profunctor.
Example: a functor $F \colon \mathcal{C} \to \mathcal{D}$ gives the profunctor $(d, c) \mapsto \Hom_{\mathcal{D}}(d, F(c))$ from $\mathcal{C}$ to $\mathcal{D}$.
Non-example: for the same $F$, the functor $(d, c) \mapsto \Hom_{\mathcal{D}}(F(c), d)$ is covariant in $d$ and contravariant in $c$.
So it is not a profunctor from $\mathcal{C}$ to $\mathcal{D}$; it is a profunctor from $\mathcal{D}$ to $\mathcal{C}$.
For $P \colon \mathcal{C} \nrightarrow \mathcal{D}$ and $Q \colon \mathcal{D} \nrightarrow \mathcal{E}$ with $\mathcal{D}$ small, the composite is given by the [[coend|W9QTFV0Z8D]] $(Q \circ P)(e, c) = \int^{d \in \mathcal{D}} Q(e, d) \times P(d, c)$.
Composition is associative and unital only up to natural isomorphism.
