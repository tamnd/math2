---
tag: TCA8AZBXRC
kind: example
name: Topological closure on the real line is not a cylindrification
msc: ["03G15", "54A05"]
topics: [QYA4H5Y7VR]
audience: research
not_instance_of:
  - target: 1MDT9BF81H
    note: the closure of an open interval meets the closure of an adjacent interval, which fails clause 3
uses: [RKCSWWVYTC]
sources:
  - url: https://en.wikipedia.org/wiki/Cylindric_algebra
---

## Example

Let $A = \mathcal{P}(\mathbb{R})$ with the set operations, and let $c X = \overline{X}$, the topological closure.
Take dimension $\alpha = 1$, so $d_{00} = 1$ and clauses 6 and 7 of [[the definition|RKCSWWVYTC]] are empty.

1. Clause 1: $\overline{\emptyset} = \emptyset$.
2. Clause 2: $X \subseteq \overline{X}$.
3. Clause 3 fails. Take $x = (0, 1)$ and $y = (1, 2)$. Then $c y = [1, 2]$ and $x \cap c y = \emptyset$, so $c(x \cap c y) = \emptyset$.
4. But $c x \cap c y = [0, 1] \cap [1, 2] = \set{1}$.

So $A$ with closure is not a [[cylindric algebra|1MDT9BF81H]].

## Remarks

1. Clause 3 implies that $c$ maps complements of closed sets to closed sets: $c(-c y) = -c y$. For closure, this says that open sets are closed, which fails in $\mathbb{R}$.
2. On a discrete space, closure is the identity, and clauses 1 to 4 hold.
3. Topological closure is a modal $\Diamond$ of S4, not of S5. The cylindric algebras of dimension $1$ are the S5 algebras.

## Explanations

### L1 human

Closure adds the boundary points to a set.
An existential quantifier must behave like a projection: once applied, applying it to the complement gives nothing new.
Closure does not: the complement of a closed interval is open, and its closure is larger.

### L2 human

1. Let $y = [1, 2]$, which is closed.
2. Its complement $-y = (-\infty, 1) \cup (2, \infty)$ has closure $(-\infty, 1] \cup [2, \infty)$.
3. So $c(-c y) \ne -c y$, which a cylindrification must satisfy.

The typical use: the example separates S4 closure operators from the S5 quantifiers of cylindric algebras.
The trap: clauses 1 and 2 hold, and closure is idempotent, but this is not enough.
