---
tag: 2JSA5DSGJE
kind: statement
role: theorem
name: Edgeworth's limit theorem
msc: [91B50, 91A12]
uses: [YTBPB52K27, HGMHZSM0XQ, CBP13S0ETD, JGP0Q56FRY]
about: [YTBPB52K27]
sources:
  - url: https://en.wikipedia.org/wiki/Edgeworth%27s_limit_theorem
same_as:
  wikidata: Q5337931
  wikipedia: Edgeworth's limit theorem
---

## Statement

Let an [[exchange economy|HGMHZSM0XQ]] have $L$ goods and $I$ consumer types.
Type $i$ has a [[preference relation|JGP0Q56FRY]] $\succsim_i$ on $\R^L_+$ that is continuous, strictly convex and strongly monotone.
Type $i$ has an endowment $\omega_i$ with all entries positive.
For $N \ge 1$, the $N$-fold replica economy has $N$ consumers of each type, each with the preferences and endowment of its type.
A coalition $S$ of consumers blocks an allocation $x$ if it can split its own endowments among its members in a better way.
Better means: each member is at least as well off as under $x$, and one member is strictly better off.
The core of an economy is the set of feasible allocations that no coalition blocks.

Let $x^* = (x^*_1, \dots, x^*_I)$ give bundle $x^*_i$ to type $i$.
For $N \ge 1$, let $x^{*N}$ be the allocation of the $N$-fold replica that gives $x^*_i$ to each consumer of type $i$.
If $x^{*N}$ lies in the core of the $N$-fold replica for every $N \ge 1$, then $x^*$ is a [[competitive equilibrium|YTBPB52K27]] allocation of the original economy.

## Remarks

The converse is easier: a competitive equilibrium allocation lies in the core of every replica, by the same argument as the first welfare theorem.
For the main direction, suppose that $x^*$ is not a competitive allocation.
Then one finds a small trade that improves on $x^*$ and that some coalition can carry out.
Using rational weights, a coalition with suitable numbers of consumers of each type implements it, and such coalitions exist once $N$ is large.
Strict convexity is used to show that in the core of a replica, all consumers of one type receive the same bundle.

Example: take two goods, one consumer of each of two types with utility $\sqrt{x y}$, and endowments $(3/4, 1/4)$ and $(1/4, 3/4)$.
The Pareto efficient allocations give $(t, t)$ to type $1$ and $(1 - t, 1 - t)$ to type $2$, and both start with utility $\sqrt{3}/4$.
So the core of the original economy is the set of these allocations with $\sqrt{3}/4 \le t \le 1 - \sqrt{3}/4$.
At prices $(1, 1)$ both consumers have wealth $1$ and demand $(1/2, 1/2)$, so $t = 1/2$ is the competitive allocation.
It is the only one that stays in the core of every replica.

## Explanations

### L1 human

With few traders, bargaining can end in many ways, and the core, the set of deals that no group can improve on by itself, is large.
Edgeworth argued that as the market grows, more and more groups can form, and they cut away every deal except those reached at market prices.
The theorem makes this precise: an outcome that survives in arbitrarily large copies of the market is a competitive equilibrium.

### L2 human

The core used here is the [[core|CBP13S0ETD]] of the cooperative game in which each coalition may trade only among its members.
Edgeworth proposed the idea in 1881; Debreu and Scarf proved this replica form in 1963.
Aumann later showed that in an economy with a continuum of traders the core equals the set of competitive allocations exactly.
The theorem supports price-taking behaviour: in large markets, no group gains by doing anything other than trading at equilibrium prices.
