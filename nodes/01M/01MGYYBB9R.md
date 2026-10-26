---
tag: 01MGYYBB9R
kind: definition
name: Antisymmetric relation
msc: ["03E20"]
defines: 0M0H1ZH8TT
uses: [08EJC6Q25H]
sources:
  - url: https://en.wikipedia.org/wiki/Antisymmetric_relation
    locator: lead section
---

## Definition

Let $R$ be a [[binary relation|08EJC6Q25H]] on a set $A$.
The relation $R$ is antisymmetric when, for all $a, b \in A$, $a \mathrel{R} b$ and $b \mathrel{R} a$ imply $a = b$.

## Remarks

The relation $\le$ on $\mathbb{R}$ and the relation $\subseteq$ on sets are antisymmetric.
Divisibility is antisymmetric on $\mathbb{N}$ but not on $\mathbb{Z}$, because $1 \mid -1$ and $-1 \mid 1$.
Antisymmetric is not the opposite of symmetric: equality is both symmetric and antisymmetric.

## Explanations

### L1 human

If $a \le b$ and $b \le a$, then $a = b$.
So for $\le$, a two-way relation between two elements forces them to be the same.
