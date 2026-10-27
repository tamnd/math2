---
tag: 0DZPD2MG33
kind: definition
name: Nilpotent group
msc: [20F18]
defines: 0Q7MMQHC1P
uses: [0S7Y9Q990Q, 0W77CVBCHQ, 0YYWCNTPWR]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_group
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Central_series
    locator: Definition
inventory: [AN65SA9AHA]
---

## Definition

A [[group|G5S1M9]] $G$ is nilpotent when it has a central series. This is a finite sequence $\{e\} = N_0 \subseteq N_1 \subseteq \cdots \subseteq N_n = G$ of [[normal subgroups|0CB0DX5BVV]] of $G$ with $N_{i+1}/N_i \subseteq Z(G/N_i)$ for each $i < n$.
Here $Z(G/N_i)$ is the [[centre|0DZ93493VN]] of the [[quotient group|0KYX2N69J0]] $G/N_i$.

## Remarks

The condition $N_{i+1}/N_i \subseteq Z(G/N_i)$ means $[N_{i+1}, G] \subseteq N_i$.
Equivalently, the [[lower central series|0K98R7A4VC]] reaches $\{e\}$, or the [[upper central series|0XW54DH28V]] reaches $G$; the least such length is the nilpotency class.
The nilpotent groups of class at most $1$ are exactly the [[abelian groups|082GHNPJ53]].
The quaternion group $Q_8$ is nilpotent of class $2$, but $S_3$ is not nilpotent.

## Explanations

### L1 human

A nilpotent group is close to abelian in a strong sense.
Each layer of a central series commutes with the whole group, up to the lower layers.
Each nilpotent group is solvable, but the converse is false, for example for $S_3$.
