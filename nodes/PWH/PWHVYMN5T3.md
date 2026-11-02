---
tag: PWHVYMN5T3
kind: definition
name: Grothendieck universe
msc: ["03E55", "18A15"]
defines: SMMK9E0MTM
uses: [00E0YZCERH]
sources:
  - url: https://en.wikipedia.org/wiki/Grothendieck_universe
---

## Definition

A *Grothendieck universe* is a set $U$ such that:

1. If $x \in U$ and $y \in x$, then $y \in U$.
2. If $x, y \in U$, then $\set{x, y} \in U$.
3. If $x \in U$, then the [[power set|00E0YZCERH]] $\mathcal{P}(x)$ is in $U$.
4. If $I \in U$ and $(x_i)_{i \in I}$ is a family with $x_i \in U$ for each $i \in I$, then $\bigcup_{i \in I} x_i \in U$.

## Remarks

The set $V_\omega$ of hereditarily finite sets is a Grothendieck universe.
Each clause holds because elements, pairs, power sets and finite unions of hereditarily finite sets are again hereditarily finite, and an index set $I \in V_\omega$ is finite.
The set $V_{\omega + \omega}$ is a non-example: it contains $\omega$ and each ordinal $\omega + n$.
The union of the family $(\omega + n)_{n \in \omega}$ is $\omega + \omega$, which is not in $V_{\omega + \omega}$, so clause 4 fails.
In ZFC the Grothendieck universes are exactly the empty set, $V_\omega$, and the sets $V_\kappa$ for [[inaccessible cardinals|NW4DREQ5DQ]] $\kappa$.
Many authors add the clause $\omega \in U$, which leaves only the universes $V_\kappa$ with $\kappa$ inaccessible.
The axiom of universes states that every set is an element of some Grothendieck universe; it is equivalent to the existence of arbitrarily large inaccessible cardinals.
