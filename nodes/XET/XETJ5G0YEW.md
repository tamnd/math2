---
tag: XETJ5G0YEW
kind: definition
name: F-sigma set
msc: [54H05, "54E52"]
defines: 8MGC7M64GW
uses: [0CQHFPGJ45, 0ZCK8DQYN1, 01TQB88H4C]
sources:
  - url: https://en.wikipedia.org/wiki/Fσ_set
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
A subset $A \subseteq X$ is an *$F_\sigma$ set* if there are [[closed sets|0ZCK8DQYN1]] $F_1, F_2, F_3, \dots$ of $X$ with
$$A = \bigcup_{n=1}^{\infty} F_n.$$

## Remarks

A set is $F_\sigma$ if and only if its complement is a [[G-delta set|V1TBNP8R3S]], by De Morgan's laws.

Example: $\Q = \bigcup_{q \in \Q} \set{q}$ in $\R$.
Each $\set{q}$ is closed and $\Q$ is [[countable|01TQB88H4C]], so $\Q$ is $F_\sigma$.

Example: $(0, 1) = \bigcup_{n \ge 3} [1/n, 1 - 1/n]$, so this open interval is $F_\sigma$.
In a [[metric space|0VKD1TP7F3]], every open set is $F_\sigma$.

Non-example: the set $\R \setminus \Q$ of irrational numbers is not $F_\sigma$ in $\R$.
Otherwise its complement $\Q$ would be a $G_\delta$ set, and it is not.
