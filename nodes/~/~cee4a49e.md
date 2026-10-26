---
tag: ~cee4a49e
kind: definition
name: Torsion subgroup
msc: [20K10]
defines: ~9dce9986
uses: [~914d79a4, ~74c6b403, ~47dae8e0, ~7fdf454c]
sources:
  - url: https://en.wikipedia.org/wiki/Torsion_subgroup
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Torsion_subgroup
    locator: Examples and further results
---

## Definition

Let $A$ be an [[abelian group|~b6df27fe]].
The torsion subgroup of $A$ is $A_T = \{a \in A : a \text{ has finite order}\}$.
The group $A$ is a torsion group when $A_T = A$, and it is torsion-free when $A_T = \{e\}$.

## Remarks

The set $A_T$ is a [[subgroup|~b600248b]] because $A$ is commutative: if $a^m = e$ and $b^n = e$, then $(a b)^{m n} = e$.
In a nonabelian group, the elements of finite order need not form a subgroup. In $\langle x, y \mid x^2, y^2 \rangle$, the product $x y$ has infinite order.
The [[quotient group|~592bfb26]] $A / A_T$ is torsion-free, and $A_T$ is a characteristic subgroup of $A$.
For $A = \mathbb{Q}/\mathbb{Z}$, each element has finite order, so $A_T = A$, but the orders have no upper bound.

## Explanations

### L1 human

The torsion subgroup collects the elements that return to the identity after finitely many steps.
In an abelian group, these elements form a subgroup.
Removing them leaves a group in which only the identity has finite order.
