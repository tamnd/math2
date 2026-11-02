---
tag: G3TZAZ3XDR
kind: definition
name: Sketch
msc: [18C30]
defines: K8P15XTH1M
uses: [A2DE66937D, 7TPBQPPN97, CHS5AFJGWE, BJS1CGTKQ5, 28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/Sketch_(mathematics)
---

## Definition

A *sketch* is a triple $\mathcal{S} = (\mathcal{A}, L, C)$ with these parts.

1. $\mathcal{A}$ is a small [[category|A2DE66937D]].
2. $L$ is a set of [[cones|7TPBQPPN97]] in $\mathcal{A}$, each over a small diagram in $\mathcal{A}$.
3. $C$ is a set of cocones in $\mathcal{A}$, each under a small diagram in $\mathcal{A}$.

Let $\mathcal{K}$ be a category.
A *model* of $\mathcal{S}$ in $\mathcal{K}$ is a [[functor|28NQ0KRHD3]] $M \colon \mathcal{A} \to \mathcal{K}$ with two properties.
$M$ sends each cone in $L$ to a [[limit|CHS5AFJGWE]] cone.
$M$ sends each cocone in $C$ to a [[colimit|BJS1CGTKQ5]] cocone.
A morphism of models is a natural transformation.

## Remarks

The sketch is a *limit sketch* when $C$ is empty.
Some authors use a directed graph with chosen diagrams instead of the category $\mathcal{A}$; this gives the same models.

Example: let $\mathcal{A}$ be the free category on the graph with two objects $X, P$ and three arrows $p_1, p_2, m \colon P \to X$.
Let $L$ contain the single cone $(P; p_1, p_2)$ over the discrete diagram $(X, X)$, and let $C$ be empty.
A model in sets is a functor $M$ with $M(P) \cong M(X) \times M(X)$ through $M(p_1), M(p_2)$.
Then $M(m)$ is a binary operation on $M(X)$, so models are sets with a binary operation.

Non-example: let $M(X) = M(P) = \set{0, 1}$ with $M(p_1) = M(p_2) = M(m) = \id$.
This functor is not a model, since $\set{0, 1}$ with two identity maps is not a product of $\set{0, 1}$ with itself.
Indeed, the pair of maps $(\id, \text{constant } 0)$ does not factor through it.
