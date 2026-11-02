---
tag: 10WTA1QZXD
kind: definition
name: Fractional factorial design
msc: [62K15]
defines: PBK2XY4M0A
uses: [EHJ3R589ZX, 0ZXZ82FTX2, 0X1JXT47GA]
sources:
  - url: https://en.wikipedia.org/wiki/Fractional_factorial_design
---

## Definition

Let $k > p \ge 1$, and code the levels of $k$ two-level factors as $\pm 1$.
Then the runs of the full $2^k$ [[factorial experiment|EHJ3R589ZX]] are the points of $\set{-1, 1}^k$.
For a subset $w \subseteq \set{1, \dots, k}$, called a *word*, write $x^w = \prod_{j \in w} x_j$ for $x \in \set{-1, 1}^k$.
Identify words with vectors of $\F_2^k$, with the symmetric difference as addition.
A *regular $2^{k-p}$ fractional factorial design* is a set of runs
$$F = \set{x \in \set{-1, 1}^k : x^{w} = \epsilon_w \text{ for all } w \in H},$$
where:

1. $H$ is a [[subgroup|0X1JXT47GA]] of $\F_2^k$ of order $2^p$, the *defining relation*, with no word of size $1$;
2. the signs $\epsilon_w \in \set{-1, 1}$ satisfy $\epsilon_{\emptyset} = 1$ and $\epsilon_{w \triangle w'} = \epsilon_w \epsilon_{w'}$, so that $F$ is not empty.

Then $F$ has $2^{k-p}$ runs.
Two effects with words $u$ and $v$ are *aliased* if $u \triangle v \in H$.
The *resolution* of the design is the smallest size of a nonempty word of $H$.

## Remarks

On $F$, the contrast columns $x^u$ and $x^v$ of aliased effects agree up to the sign $\epsilon_{u \triangle v}$, so their effects cannot be separated.
Here $\F_2$ is the [[field with two elements|0ZXZ82FTX2]].

Example: $k = 3$, $p = 1$, $H = \set{\emptyset, \set{1,2,3}}$ with $\epsilon = +1$, that is, the generator $C = AB$ and the defining relation $I = ABC$.
The runs are $(-1,-1,+1)$, $(+1,-1,-1)$, $(-1,+1,-1)$, $(+1,+1,+1)$, four of the eight.
The main effect $A$, with word $\set{1}$, is aliased with $BC$, since $\set{1} \triangle \set{1,2,3} = \set{2,3}$.
The design has resolution III.

Non-example: the four runs with $x_1 = -1$ form the set $\set{x : x^{\set{1}} = -1}$, which uses the word $\set{1}$ of size $1$, so clause 1 fails.
In these runs factor $A$ never changes, so its main effect cannot be estimated at all.
