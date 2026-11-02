---
tag: WC5JZVG82R
kind: definition
name: Axiom of determinacy
msc: ["03E60", "03E25"]
defines: PEXTM3MJ5Z
uses: [QXECDPAYTN, P2WS16HKD7, 0HE5WDQ9FJ, 0HTGB13FE2]
sources:
  - url: https://en.wikipedia.org/wiki/Axiom_of_determinacy
---

## Definition

The *axiom of determinacy* (AD) is the following statement in the language of set theory.
For every set $X \subseteq \N^{\N}$ of sequences of natural numbers, the game $G(\N, X)$ is [[determined|QXECDPAYTN]].
Here, in $G(\N, X)$, players I and II alternately choose natural numbers $a_0, a_1, a_2, \dots$, and player I wins if $(a_0, a_1, a_2, \dots) \in X$.

## Remarks

Example: for each Borel set $X$ of the [[Baire space|P2WS16HKD7]] $\N^{\N}$, the instance of AD for $X$ holds.
It is even a theorem of ZFC, by the Borel determinacy theorem.

Non-example: AD is false in [[ZFC|0HE5WDQ9FJ]].
The [[axiom of choice|0HTGB13FE2]] gives a well-ordering of all strategies.
A diagonal argument along it builds a set $X$ that defeats every strategy of each player.

AD is therefore studied over ZF without choice.
It still implies the axiom of countable choice for sets of reals.
