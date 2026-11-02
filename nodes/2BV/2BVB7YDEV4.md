---
tag: 2BVB7YDEV4
kind: example
name: Herbrand universe
msc: [03B10, 08B20]
instance_of: [TTTEV3NWWM]
uses: [TTTEV3NWWM, 3YYKGWJJND, VZ21F10WRS]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand_structure
---

## Example

Let $L$ be a first-order language with at least one constant symbol; if it has none, one constant is added.
The *Herbrand universe* $H(L)$ is the set of ground terms of $L$, the terms that contain no variables.
It is the smallest set that contains every constant symbol of $L$ and contains $f(t_1, \ldots, t_n)$ whenever $f$ is an $n$-ary function symbol and $t_1, \ldots, t_n \in H(L)$.

With the function symbols acting by $f(t_1, \ldots, t_n) \mapsto$ the term $f(t_1, \ldots, t_n)$, the set $H(L)$ is the [[term algebra|3YYKGWJJND]] on the empty set of variables.
So it is the [[absolutely free algebra|TTTEV3NWWM]] on no generators.
Check: every map from the empty set extends uniquely.
Indeed, a homomorphism to any algebra $A$ must send each ground term to its value in $A$.

For $L$ with one constant $0$ and one unary symbol $s$, the universe is $\set{0, s(0), s(s(0)), \ldots}$, a copy of $\N$.
For $L$ with one constant $a$ and one binary symbol $g$, it contains $a$, $g(a, a)$, $g(a, g(a, a))$, $g(g(a, a), a)$, and so on.
There is one element for each binary tree.

## Explanations

### L1 human

The Herbrand universe is the list of all objects that a language can name without variables.
Start from the constants and apply the function symbols again and again.
[[Herbrand's theorem|VZ21F10WRS]] reduces the unsatisfiability of a universal sentence to that of finitely many instances built from ground terms in this universe.
This is why it is central in automated theorem proving.
