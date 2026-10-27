---
tag: 0RH1TPDGCQ
kind: definition
name: Torsion subgroup
msc: [20K10]
defines: 0DBWXQRXQJ
uses: [071DDFVG4J, 0N0PXCTYA7, 0JPYSD5E0B, 0YYWCNTPWR]
sources:
  - url: https://en.wikipedia.org/wiki/Torsion_subgroup
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Torsion_subgroup
    locator: Examples and further results
inventory: [YJVK0QTM6V]
---

## Definition

Let $A$ be an [[abelian group|082GHNPJ53]].
The torsion subgroup of $A$ is $A_T = \{a \in A : a \text{ has finite order}\}$.
The group $A$ is a torsion group when $A_T = A$, and it is torsion-free when $A_T = \{e\}$.

## Remarks

The set $A_T$ is a [[subgroup|0X1JXT47GA]] because $A$ is commutative: if $a^m = e$ and $b^n = e$, then $(a b)^{m n} = e$.
In a nonabelian group, the elements of finite order need not form a subgroup. In $\langle x, y \mid x^2, y^2 \rangle$, the product $x y$ has infinite order.
The [[quotient group|0KYX2N69J0]] $A / A_T$ is torsion-free, and $A_T$ is a characteristic subgroup of $A$.
For $A = \mathbb{Q}/\mathbb{Z}$, each element has finite order, so $A_T = A$, but the orders have no upper bound.

## Explanations

### L1 human

The torsion subgroup collects the elements that return to the identity after finitely many steps.
In an abelian group, these elements form a subgroup.
Removing them leaves a group in which only the identity has finite order.
