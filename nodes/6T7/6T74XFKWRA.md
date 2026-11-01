---
tag: 6T74XFKWRA
kind: definition
name: Projective dimension
msc: [13D05, 18G20]
defines: MR9QCH1PNA
uses: [0B1261B5ED, 0NZ8JA25WK, HK2AA1YSQ2, BFFA03GE3V, 4P7GBWJ4RR]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_module
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] and let $M$ be a nonzero [[$R$-module|0NZ8JA25WK]].
The *projective dimension* $\operatorname{pd}_R M$ is the least integer $n \ge 0$ such that $M$ has a [[projective resolution|HK2AA1YSQ2]]
$$0 \to P_n \to P_{n-1} \to \cdots \to P_0 \to M \to 0$$
of length $n$.
If no such finite resolution exists, then $\operatorname{pd}_R M = \infty$.

## Remarks

One has $\operatorname{pd}_R M = 0$ if and only if $M$ is a [[projective module|BFFA03GE3V]].
Equivalently, $\operatorname{pd}_R M \le n$ if and only if $\operatorname{Ext}^{n+1}_R(M, N) = 0$ for every $R$-module $N$, where $\operatorname{Ext}$ is the [[Ext functor|4P7GBWJ4RR]].
Example: $\operatorname{pd}_\Z \Z/n\Z = 1$ for $n \ge 2$; the resolution $0 \to \Z \xrightarrow{\cdot n} \Z \to \Z/n\Z \to 0$ has length $1$, and $\Z/n\Z$ is not projective, because projective $\Z$-modules are free and hence have no nonzero torsion.
Non-example of finiteness: over $R = \Z/4\Z$, the module $\Z/2\Z$ has $\operatorname{pd}_R \Z/2\Z = \infty$.
Some authors set $\operatorname{pd}_R 0 = -\infty$.
