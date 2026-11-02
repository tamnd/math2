---
tag: X32V6Y5PYW
kind: definition
name: Ordered vector space
msc: ["46A40", "06F20"]
defines: HHMS3WH9T7
uses: [05EGHEQZAW, 011C29Q1S1, WG6BY4SWTV]
sources:
  - url: https://en.wikipedia.org/wiki/Ordered_vector_space
---

## Definition

Let $V$ be a real [[vector space|05EGHEQZAW]] and let $\le$ be a [[partial order|011C29Q1S1]] on $V$.
The pair $(V, \le)$ is an *ordered vector space* if for all $x, y, z \in V$ and all real $\lambda \ge 0$:

1. if $x \le y$, then $x + z \le y + z$;
2. if $x \le y$, then $\lambda x \le \lambda y$.

## Remarks

Example: $\R^n$ with the componentwise order is an ordered vector space.
If $x_i \le y_i$ for all $i$, then $x_i + z_i \le y_i + z_i$ and $\lambda x_i \le \lambda y_i$ for $\lambda \ge 0$.
Non-example: on $\R$, let $x \preceq y$ when $x = y$ or $(x, y) = (0, 1)$.
This is a partial order, but $0 \preceq 1$ while $1 \not\preceq 2$, so clause 1 fails.
The set $\set{x \in V : 0 \le x}$ is a [[positive cone|WG6BY4SWTV]], and the order is recovered from it by $x \le y \iff y - x \ge 0$.
So giving an ordered vector space is the same as giving a real vector space with a positive cone.
