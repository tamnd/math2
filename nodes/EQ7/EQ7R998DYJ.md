---
tag: EQ7R998DYJ
kind: definition
name: Congruence subgroup
msc: [11F06, 20H05]
defines: 1H6R856P3C
uses: [VEKV1EM77B, 0X1JXT47GA, 0W88CEGQP1, 0DTXBQPA2S]
sources:
  - url: https://en.wikipedia.org/wiki/Congruence_subgroup
---

## Definition

Let $N \ge 1$ be an integer.
The *principal congruence subgroup of level $N$* is the [[kernel|0W88CEGQP1]] of the reduction map $\mathrm{SL}_2(\Z) \to \mathrm{SL}_2(\Z / N\Z)$:
$$\Gamma(N) = \set{\gamma \in \mathrm{SL}_2(\Z) : \gamma \equiv I \pmod N}.$$
A *congruence subgroup* is a [[subgroup|0X1JXT47GA]] $\Gamma$ of the [[modular group|VEKV1EM77B]] $\mathrm{SL}_2(\Z)$ such that $\Gamma(N) \subseteq \Gamma$ for some $N \ge 1$.

## Remarks

Example: $\Gamma_0(N) = \set{\begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \mathrm{SL}_2(\Z) : c \equiv 0 \pmod N}$ is a congruence subgroup, since each matrix of $\Gamma(N)$ has $c \equiv 0 \pmod N$.
Another example is $\Gamma_1(N)$, defined by $c \equiv 0$ and $a \equiv d \equiv 1 \pmod N$.
Since $\mathrm{SL}_2(\Z / N\Z)$ is finite, $\Gamma(N)$ has finite [[index|0DTXBQPA2S]], and so does every congruence subgroup.
Non-example: the subgroup $\set{\begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix} : n \in \Z}$ has infinite index, so it contains no $\Gamma(N)$.
For a prime $p$, the index of $\Gamma_0(p)$ in $\mathrm{SL}_2(\Z)$ is $p + 1$.
Not every subgroup of finite index in $\mathrm{SL}_2(\Z)$ is a congruence subgroup.
