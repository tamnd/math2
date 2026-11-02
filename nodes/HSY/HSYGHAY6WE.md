---
tag: HSYGHAY6WE
kind: definition
name: Scott domain
msc: [06B35, 68Q55]
defines: 1SAAZG46DG
uses: [7TSXP95QN6, 9F7TYES4KE, D9RY4667K6, 0S60DVMVPN, 0R3H5PANRQ]
sources:
  - url: https://en.wikipedia.org/wiki/Scott_domain
---

## Definition

Let $D$ be a [[directed-complete partial order|7TSXP95QN6]].
It is a *Scott domain* if:

1. $D$ is algebraic: for every $x \in D$, the set of [[compact elements|9F7TYES4KE]] $c \le x$ is [[directed|D9RY4667K6]] and has [[supremum|0R3H5PANRQ]] $x$;
2. $D$ is bounded complete: every subset of $D$ that has an [[upper bound|0S60DVMVPN]] in $D$ has a supremum in $D$.

## Remarks

Taking the empty subset in clause 2 gives a least element when $D$ is nonempty; some authors require $D$ nonempty, and some also require countably many compact elements.
Example: the partial functions from $\N$ to $\N$, ordered by extension.
The compact elements are the finite partial functions, and every partial function is the union of its finite restrictions.
A family with a common extension consists of compatible functions, and their union is its supremum.
Non-example: take the poset with elements $\bot, a, b, c, d$, where $\bot$ is below all, and $a, b$ are each below both $c$ and $d$.
It is a finite dcpo, but $\set{a, b}$ has the upper bounds $c$ and $d$ and no least one.
So it is not bounded complete.
Every algebraic lattice is a Scott domain.
