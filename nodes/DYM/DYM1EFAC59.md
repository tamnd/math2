---
tag: DYM1EFAC59
kind: definition
name: Priestley space
msc: [06D50, 54F05, "06E15"]
defines: ZGBV8V3823
uses: [0CQHFPGJ45, 0TVJZYB6SH, 0QV2JS9RJ3, ETCE287E2R]
sources:
  - url: https://en.wikipedia.org/wiki/Priestley_space
---

## Definition

Let $X$ be a set with a [[topology|0CQHFPGJ45]] $\tau$ and a [[partial order|0QV2JS9RJ3]] $\le$.
The triple $(X, \tau, \le)$ is a *Priestley space* if:

1. $(X, \tau)$ is [[compact|0TVJZYB6SH]];
2. for all $x, y \in X$ with $x \not\le y$, some $U \subseteq X$ has $x \in U$ and $y \notin U$, is open and closed in $\tau$, and is an [[upper set|ETCE287E2R]].

Clause 2 is called the Priestley separation axiom.

## Remarks

A Priestley space is Hausdorff and totally disconnected, so its underlying space is a [[Stone space|ZV38HA5PAQ]].
Indeed, for $x \ne y$, say $x \not\le y$, the sets $U$ and $X \setminus U$ from clause 2 separate $x$ and $y$.

Example: a finite poset with the discrete topology.
Every subset is clopen, and for $x \not\le y$ the upper set ${\uparrow} x = \set{z : x \le z}$ contains $x$ but not $y$.

Non-example: the interval $[0, 1]$ with its usual topology and usual order.
It is compact, but its only clopen sets are $\emptyset$ and $[0, 1]$, so no clopen set separates $1 \not\le 0$, and clause 2 fails.

The morphisms of Priestley spaces are the continuous order-preserving maps.
