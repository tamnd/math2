---
tag: A3DP43YC3Z
kind: definition
name: Linear topology
msc: [13J99, 16W80]
defines: 6RF8CB69KQ
uses: [0310REJJY8, 096Z9MP2ME, 0CQHFPGJ45, 0NZ8JA25WK, 05WDSN597C]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_topology
---

## Definition

Let $A$ be a [[commutative ring|0310REJJY8]].
A [[topology|0CQHFPGJ45]] on $A$ is *linear* if it satisfies both conditions:

1. With this topology, $A$ is a topological ring.
2. The open [[ideals|096Z9MP2ME]] of $A$ form a fundamental system of neighbourhoods of $0$: every neighbourhood of $0$ contains an open ideal.

More generally, let $M$ be an [[$A$-module|0NZ8JA25WK]] and give $A$ a linear topology.
A topology on $M$ is *linear* if $M$ is a topological group under addition and the scalar multiplication $A \times M \to M$ is continuous.
In addition, the open [[submodules|05WDSN597C]] of $M$ must form a fundamental system of neighbourhoods of $0$.

## Remarks

Equivalently, a linear topology on $A$ is given by a family $\mathcal{F}$ of ideals such that each intersection $I \cap J$ of two members contains a member.
A set $U$ is then open when for each $x \in U$ there is $I \in \mathcal{F}$ with $x + I \subseteq U$.

Example: for an ideal $I$ of $A$, the [[I-adic topology|2VF2TSJ3PY]] has the powers $I^n$ as a fundamental system of neighbourhoods of $0$.
Each $I^n$ is an open ideal, so clause 2 holds; addition and multiplication are continuous because $(x + I^n) + (y + I^n) = x + y + I^n$ and $(x + I^n)(y + I^n) \subseteq xy + I^n$.
The discrete topology is linear, with the zero ideal open.

Non-example: the usual topology on $\R$ makes $\R$ a topological ring, so clause 1 holds.
But the only ideals of the field $\R$ are $0$ and $\R$.
The set $\set{0}$ is not open, and the interval $(-1, 1)$ does not contain $\R$; so clause 2 fails.
