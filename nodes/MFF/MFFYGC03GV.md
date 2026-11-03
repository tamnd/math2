---
tag: MFFYGC03GV
kind: conjecture
name: Global attractor conjecture
msc: ["92E20", 37N25, 34D23]
uses: [KCGE92DJ1W, 0N8NGKDZDZ, 5JP25MVJ8Y]
about: [KCGE92DJ1W]
sources:
  - url: https://en.wikipedia.org/wiki/Chemical_reaction_network_theory
history:
  posed_by: "Fritz Horn"
  first_stated: "1974"
---

## Statement

Let a mass-action system on a [[chemical reaction network|KCGE92DJ1W]] with $m$ species be complex balanced.
This means that it has a positive [[equilibrium|0N8NGKDZDZ]] with the following property.
For each complex, the total rate of the reactions out of it equals the total rate of the reactions into it.
Let $P$ be a positive stoichiometric compatibility class, and let $\bar x$ be the unique equilibrium in $P$.
Then every solution $x(t)$ with $x(0) \in P$ satisfies $x(t) \to \bar x$ as $t \to \infty$.

## Remarks

Horn and Jackson showed that a complex balanced system has exactly one positive equilibrium in each positive class, and that it is locally asymptotically stable relative to the class.
The difficulty is to exclude solutions that approach the boundary of the positive orthant, where some concentration tends to $0$.
By the [[deficiency zero theorem|5JP25MVJ8Y]], every weakly reversible network of deficiency zero is complex balanced for all rate constants, so the conjecture covers these systems.
Anderson proved the conjecture for networks with a single linkage class.
It is also known when the stoichiometric subspace has dimension at most $3$.
Craciun has proposed a proof of the general case, using toric differential inclusions.

## Explanations

### L1 human

For many reaction networks, there is exactly one balanced state for each total amount of material, and states nearby are pulled towards it.
The conjecture says that every starting state with all species present is pulled towards it, not only the nearby ones.
The worry is that some species could die out along the way and trap the system on the edge.
