---
tag: RR5JH5K74X
kind: definition
name: Baire property
msc: ["54E52", "03E15"]
defines: FZ7237VY65
uses: [0CQHFPGJ45, 02BH3MCBQB, 0XGCZ4GDZ6, 0ME21QN125, 0VQYCCQVJ5, 0RZH6W98HK]
sources:
  - url: https://en.wikipedia.org/wiki/Property_of_Baire
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] and let $A \subseteq X$.
The set $A$ has the *Baire property* if there is an [[open set|02BH3MCBQB]] $U \subseteq X$ such that the [[symmetric difference|0ME21QN125]] $A \mathbin{\triangle} U$ is [[meagre|0XGCZ4GDZ6]] in $X$.

## Remarks

Example: every closed set $F \subseteq X$ has the Baire property.
Take $U$ to be the [[interior|0RZH6W98HK]] of $F$.
Then $F \mathbin{\triangle} U = F \setminus U$ is closed and has empty interior, so it is [[nowhere dense|0VQYCCQVJ5]] and hence meagre.

Non-example: a Vitali set $V \subseteq \R$ contains exactly one point of each coset of $\Q$ in $\R$.
Such a set does not have the Baire property; its construction uses the axiom of choice.

The sets with the Baire property form a sigma-algebra that contains the open sets, so every Borel set has the Baire property.
Equivalently, $A$ has the Baire property if $A = G \cup M$ for a $G_\delta$ set $G$ and a meagre set $M$.
