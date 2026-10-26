---
tag: 0GNG2KVPZJ
kind: statement
role: proposition
name: Nilpotent groups are solvable
msc: [20F18, 20F16]
uses: [0DZPD2MG33, 0P3KZK0FTV]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_group
    locator: Properties
---

## Statement

Let $G$ be a [[nilpotent group|0Q7MMQHC1P]].
Then $G$ is [[solvable|0FXJ7YFMMX]].

## Remarks

A central series $\{e\} = N_0 \subseteq \cdots \subseteq N_n = G$ is a subnormal series, and each factor $N_{i+1}/N_i$ is central in $G/N_i$, so it is abelian.
The converse is false: $S_3$ is solvable, but it is not nilpotent.
So there are strict inclusions: abelian groups, then nilpotent groups, then solvable groups.

## Explanations

### L1 human

A central series has layers that commute with the whole group.
In particular, each layer is abelian.
So a nilpotent group is solvable.
