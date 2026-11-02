---
tag: C5MA8PA2Q5
kind: definition
name: Projective determinacy
msc: ["03E60", "03E15", "03E55"]
defines: 2GY3131ZPS
uses: [QXECDPAYTN, 8DZTNVTGY2, P2WS16HKD7]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_determinacy
---

## Definition

*Projective determinacy* (PD) is the following statement in the language of set theory.
For every projective set $X \subseteq \N^{\N}$, that is, every set in some level $\boldsymbol{\Sigma}^1_n$ of the [[projective hierarchy|8DZTNVTGY2]], the game $G(\N, X)$ is [[determined|QXECDPAYTN]].

## Remarks

Example: every Borel set $X$ of the [[Baire space|P2WS16HKD7]] is projective, and its game is determined in ZFC by the Borel determinacy theorem.
So the Borel instances of PD are theorems of ZFC.

Non-example: the axiom of choice gives a set $X \subseteq \N^{\N}$ whose game is not determined.
PD does not cover this set, and under PD such a set is not projective.

For each $n$, the statement that all $\boldsymbol{\Sigma}^1_n$ games are determined is a separate hypothesis, and PD is the conjunction of all of them.
The statement that all analytic games, the case $n = 1$, are determined follows from the existence of a measurable cardinal.
