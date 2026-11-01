---
tag: Z3KPTM2YWX
kind: definition
name: Henselian field
msc: [12J10, 13J15]
defines: 3ACEE4N6NE
uses: [B85T5VKR3M, QSX12D8RQM, 09J6KGT65G, 0AD4VS02H3]
sources:
  - url: https://en.wikipedia.org/wiki/Henselian_ring
---

## Definition

Let $K$ be a field with a [[valuation|B85T5VKR3M]] $v$.
Let $\mathcal{O} = \set{x \in K : v(x) \ge 0}$ be its [[valuation ring|QSX12D8RQM]] and $\mathfrak{m} = \set{x \in K : v(x) > 0}$ its [[maximal ideal|09J6KGT65G]].
The valued field $(K, v)$ is *Henselian* if the following holds.
For every monic $f \in \mathcal{O}[X]$ and every $a \in \mathcal{O}$ with $f(a) \in \mathfrak{m}$ and $f'(a) \notin \mathfrak{m}$, there is $b \in \mathcal{O}$ with $f(b) = 0$ and $b - a \in \mathfrak{m}$.

Here $f'$ is the formal [[derivative|0AD4VS02H3]] of $f$.

## Remarks

Example: for a prime $p$, the field $\Q_p$ with the $p$-adic valuation is Henselian; this is [[Hensel's lemma|010QVB71T2]] in its $p$-adic form.
More generally, a field that is complete for a valuation with values in $\R$ is Henselian.
Non-example: $\Q$ with the $7$-adic valuation $v_7$ is not Henselian.
Take $f = X^2 - 2$ and $a = 3$: $f(3) = 7 \in \mathfrak{m}$ and $f'(3) = 6 \notin \mathfrak{m}$, but $f$ has no root in $\Q$.
Equivalent forms: $(K, v)$ is Henselian if and only if $\mathcal{O}$ is a [[Henselian ring|RNXPV3KC5J]].
It is Henselian if and only if $v$ extends to a unique valuation on each algebraic extension of $K$.
The element $b$ is then unique.
Every field with the trivial valuation is Henselian.
