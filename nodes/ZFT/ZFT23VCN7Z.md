---
tag: ZFT23VCN7Z
kind: definition
name: Functor category
msc: [18A25, 18A23]
defines: 1X0WKFQX8K
uses: [A2DE66937D, 28NQ0KRHD3, KYCPCC57FT, 0WCY42EV9V, G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Functor_category
---

## Definition

Let $\mathcal{C}$ be a small [[category|A2DE66937D]] and let $\mathcal{D}$ be a category.
The *functor category* $[\mathcal{C}, \mathcal{D}]$ is defined as follows:

1. its objects are the [[functors|28NQ0KRHD3]] $\mathcal{C} \to \mathcal{D}$;
2. its morphisms $F \to G$ are the [[natural transformations|KYCPCC57FT]] $\alpha \colon F \Rightarrow G$;
3. the composite of $\alpha \colon F \Rightarrow G$ and $\beta \colon G \Rightarrow H$ is $\beta \circ \alpha$ with components $(\beta \circ \alpha)_A = \beta_A \circ \alpha_A$, and the identity of $F$ has components $1_{F(A)}$.

## Remarks

The composite $\beta \circ \alpha$ is natural, because both of its naturality squares can be pasted together.
It is also written $\mathcal{D}^{\mathcal{C}}$ or $\mathrm{Fun}(\mathcal{C}, \mathcal{D})$.
Smallness of $\mathcal{C}$ ensures that, when $\mathcal{D}$ is locally small, the natural transformations between two functors form a set.
Example: let $G$ be a [[group|G5S1M9]], seen as a category with one object $\ast$ and with the elements of $G$ as morphisms.
A functor $G \to \mathbf{Set}$ is a set $X = F(\ast)$ with a [[group action|0WCY42EV9V]] $g \cdot x = F(g)(x)$, and a natural transformation is a map $h$ with $h(g \cdot x) = g \cdot h(x)$.
So $[G, \mathbf{Set}]$ is the category of $G$-sets.
Non-example: a family of morphisms $\alpha_A \colon F(A) \to G(A)$ that fails one naturality square is not a morphism of $[\mathcal{C}, \mathcal{D}]$.
A morphism of $[\mathcal{C}, \mathcal{D}]$ is an isomorphism exactly when all its components are isomorphisms.
