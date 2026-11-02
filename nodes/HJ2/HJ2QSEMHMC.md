---
tag: HJ2QSEMHMC
kind: definition
name: LF-space
msc: [46A13]
defines: 7THJSH9SFP
uses: [3GAA614673, B6GY2KJMWW, 02AS45T3H9, 2TDSHJJYS4, 0ZCY0Z80B6]
sources:
  - url: https://en.wikipedia.org/wiki/LF-space
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $E$ be a vector space over $\mathbb{K}$.
Suppose $E = \bigcup_{n \ge 1} E_n$, where $E_1 \subseteq E_2 \subseteq \cdots$ are linear subspaces.
Suppose each $E_n$ carries a topology making it a [[Fréchet space|3GAA614673]], and each inclusion $E_n \to E_{n+1}$ is continuous.
The *inductive limit topology* on $E$ is the locally convex topology defined as follows.
A set is a [[neighbourhood|0ZCY0Z80B6]] of $0$ if it contains a [[convex|02AS45T3H9]] [[balanced|2TDSHJJYS4]] set $U$ with the following property.
For every $n$, the set $U \cap E_n$ is a neighbourhood of $0$ in $E_n$.
A [[locally convex space|B6GY2KJMWW]] is an *LF-space* if it is Hausdorff and arises in this way.

## Remarks

The inductive limit topology is the finest locally convex topology on $E$ for which all inclusions $E_n \to E$ are continuous.
Many authors require the limit to be *strict*: each $E_n$ carries the topology induced by $E_{n+1}$.
Consider a strict limit with each $E_n$ closed in $E_{n+1}$.
Then $E$ is Hausdorff and complete, and it induces the given topology on each $E_n$.
A set is bounded in $E$ if and only if it lies in some $E_n$ and is bounded there.
Example: let $\Omega \subseteq \R^d$ be open, and let $K_1 \subseteq K_2 \subseteq \cdots$ be compact sets with union $\Omega$, each inside the interior of the next.
Let $\mathcal{D}_{K_n}$ be the Fréchet space of smooth functions supported in $K_n$.
Then $C_c^\infty(\Omega) = \bigcup_n \mathcal{D}_{K_n}$ is a strict LF-space.
Non-example: the space $c_{00}$ of finitely supported sequences with the sup norm is not an LF-space, since every LF-space is barrelled and this space is not.
