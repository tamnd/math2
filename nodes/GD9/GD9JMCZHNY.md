---
tag: GD9JMCZHNY
kind: definition
name: Exponential object
msc: [18D15]
defines: RHWD8DY41R
uses: [A2DE66937D, S5744QZV4N, EN4DD2FAJH]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_object
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] with binary [[products|S5744QZV4N]], and let $Y$ and $Z$ be objects of $\mathcal{C}$.
An *exponential object* of $Z$ by $Y$ is an object $Z^Y$ with a morphism $\mathrm{ev} \colon Z^Y \times Y \to Z$ with this [[universal property|EN4DD2FAJH]].
For every object $X$ and every morphism $g \colon X \times Y \to Z$, there is a unique morphism $\lambda g \colon X \to Z^Y$ with $\mathrm{ev} \circ (\lambda g \times \id_Y) = g$.

## Remarks

The morphism $\mathrm{ev}$ is the *evaluation*, and $\lambda g$ is the *transpose* or *curried form* of $g$.
An exponential object is unique up to a unique isomorphism compatible with $\mathrm{ev}$.
If $Z^Y$ exists for all $Z$, then $Z \mapsto Z^Y$ is a functor right adjoint to $- \times Y$.

Example: in the category of sets, let $Z^Y$ be the set of maps $Y \to Z$ and $\mathrm{ev}(h, y) = h(y)$.
For $g \colon X \times Y \to Z$, the map $\lambda g$ sends $x$ to $y \mapsto g(x, y)$.
It is the only map with $\lambda g(x)(y) = g(x, y)$ for all $x, y$.

Non-example: in the category of topological spaces, not every exponential exists.
For the space $\Q$ of rational numbers, the functor $- \times \Q$ has no right adjoint, so some $Z^{\Q}$ do not exist.
For $Y$ locally compact Hausdorff, $Z^Y$ exists and is the space of maps with the [[compact-open topology|RG15F0TWPW]].
