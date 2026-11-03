---
tag: H8J1J00JXX
kind: statement
role: theorem
name: Sonnenschein–Mantel–Debreu theorem
msc: [91B50, 91B42]
uses: [HGMHZSM0XQ, JGP0Q56FRY, 0X3WGX95FE]
about: [HGMHZSM0XQ]
sources:
  - url: https://en.wikipedia.org/wiki/Sonnenschein%E2%80%93Mantel%E2%80%93Debreu_theorem
same_as:
  wikidata: Q925224
  wikipedia: Sonnenschein–Mantel–Debreu theorem
---

## Statement

Let $L \ge 2$ and $\varepsilon > 0$, and let
$$P_\varepsilon = \set{p \in \R^L : p_\ell > 0 \text{ for all } \ell, \ p_\ell / p_k \ge \varepsilon \text{ for all } \ell, k}.$$
Let $z \colon P_\varepsilon \to \R^L$ be a [[continuous function|0X3WGX95FE]] such that:

1. $z$ is homogeneous of degree zero: $z(t p) = z(p)$ for all $t > 0$;
2. $z$ satisfies Walras's law: $p \cdot z(p) = 0$ for all $p \in P_\varepsilon$.

Then there is an [[exchange economy|HGMHZSM0XQ]] with $L$ consumers whose aggregate excess demand function equals $z(p)$ for every $p \in P_\varepsilon$.
In it, each consumer has continuous, strictly convex and monotone [[preferences|JGP0Q56FRY]] on $\R^L_+$ and an endowment in $\R^L_+$.

## Remarks

Homogeneity, continuity and [[Walras's law|M6A75DMQJT]] hold for the excess demand of any economy of this kind.
So the theorem says that, away from the boundary of the price simplex, they are the only restrictions.
Sonnenschein raised the question and gave first results in 1972; Mantel and Debreu completed the answer in 1974, Debreu with the bound of $L$ consumers.
The proof constructs, for a decomposition of $z$ into $L$ pieces, one consumer whose individual excess demand is each piece.

Example of use: for $L = 2$, normalize $p_1 + p_2 = 1$; a continuous $z$ with these properties is fixed by $z_1(p)$, since $z_2 = - p_1 z_1 / p_2$.
Choosing $z_1$ with five sign changes on $P_\varepsilon$ gives, by the theorem, an economy with five equilibrium prices there.
So theory alone does not rule out many equilibria, and price adjustment in the direction of excess demand can move away from some of them.

The restriction to $P_\varepsilon$ matters.
In an economy with strongly monotone preferences and positive total endowment, excess demand becomes unbounded as some price tends to $0$, which a general continuous $z$ need not do.

## Explanations

### L1 human

Each consumer's demand obeys strong rules, such as the symmetry of the substitution effects.
The theorem says that these rules almost all wash out when demands are added up over a whole economy.
Total excess demand can have any shape that respects a few basic accounting rules.
So theory alone does not predict that equilibrium is unique or stable.

### L2 human

The result shows the limits of [[general equilibrium theory|HGMHZSM0XQ]]: existence of [[competitive equilibrium|YTBPB52K27]] holds broadly, but uniqueness, stability and comparative statics need extra assumptions.
Such assumptions include gross substitutability or restrictions on the distribution of preferences and endowments.
It also undercuts representative-agent models, since aggregate demand need not behave like the demand of a single consumer.
