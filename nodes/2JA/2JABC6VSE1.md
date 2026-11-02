---
tag: 2JABC6VSE1
kind: definition
name: Pro-p group
msc: ["20E18", 22C05]
defines: C13D6W3MM9
uses: [KA0YDB6QXE, 06QYRTX9KQ, QYCFH68RD1, 0CB0DX5BVV, V6TJAFZ4MD]
sources:
  - url: https://en.wikipedia.org/wiki/Pro-p_group
---

## Definition

Let $p$ be a prime number.
A *pro-$p$ group* is a [[profinite group|KA0YDB6QXE]] $G$ such that for every [[open|QYCFH68RD1]] [[normal subgroup|0CB0DX5BVV]] $N$ of $G$ the finite quotient $G/N$ is a [[p-group|06QYRTX9KQ]].

## Remarks

Equivalently, $G$ is isomorphic as a topological group to an inverse limit of finite $p$-groups.
Example: the [[p-adic integers|V6TJAFZ4MD]] $\Z_p = \varprojlim \Z/p^n\Z$.
Its open subgroups are the subgroups $p^n \Z_p$, and each quotient $\Z_p / p^n \Z_p \cong \Z/p^n\Z$ has order $p^n$.
Non-example: the profinite completion $\hat\Z$ of $\Z$ is profinite, but it has the open normal subgroup $6\hat\Z$ with quotient $\Z/6\Z$, which is not a $p$-group for any prime $p$.
Every finite $p$-group with the discrete topology is a pro-$p$ group.
