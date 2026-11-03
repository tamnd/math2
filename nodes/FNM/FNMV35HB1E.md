---
tag: FNMV35HB1E
kind: statement
role: theorem
name: Existence of competitive equilibrium
msc: [91B50, 47H10]
uses: [YTBPB52K27, HGMHZSM0XQ, JGP0Q56FRY, 02AS45T3H9]
about: [YTBPB52K27]
sources:
  - url: https://en.wikipedia.org/wiki/Arrow%E2%80%93Debreu_model
---

## Statement

Let an [[exchange economy|HGMHZSM0XQ]] have $L$ goods and $I$ consumers, where consumer $i$ has consumption set $\R^L_+$, a [[preference relation|JGP0Q56FRY]] $\succsim_i$ and an endowment $\omega_i$.
Assume that for every $i$:

1. $\succsim_i$ is continuous: its upper and lower contour sets are closed;
2. $\succsim_i$ is convex: each upper contour set $\set{y : y \succsim_i x}$ is a [[convex set|02AS45T3H9]];
3. $\succsim_i$ is strongly monotone: if $y \ge x$ componentwise and $y \ne x$, then $y \succ_i x$;
4. $\omega_i$ has all entries positive.

Then the economy has a [[competitive equilibrium|YTBPB52K27]] $(p, x)$, and every equilibrium price vector has all entries positive.

## Remarks

The proof works on the price simplex $\Delta = \set{p \in \R^L_+ : \sum_\ell p_\ell = 1}$.
The demand of each consumer is a set-valued map with nonempty convex values, and [[Berge's maximum theorem|NDABCTQQFK]] gives it a closed graph away from the boundary.
A map that raises the prices of goods in excess demand is then shown to satisfy the hypotheses of the [[Kakutani fixed-point theorem|7V3HWGR32Z]].
A fixed point of this map is an equilibrium price.
Strong monotonicity handles prices near the boundary of $\Delta$.
With strictly convex preferences, demand is single-valued and the [[Brouwer fixed-point theorem|N7AAJ2MW5T]] is enough.

Arrow and Debreu proved in 1954 a version for the economy with production, the [[Arrow–Debreu model|SVGN7R3RDY]].
It assumes convex production sets and further conditions on the consumption sets and endowments.

Convexity is needed.
Without it, a consumer's demand can jump from one corner of the budget set to another as prices move.
Then the aggregate excess demand can skip over $0$, and there are small economies with no equilibrium.
Some condition like positive endowments is needed too.
If a consumer can have zero wealth at relevant prices, demand can fail to be continuous there, and there are examples without equilibrium.

## Explanations

### L1 human

The theorem says that a market of price-taking traders always has prices at which everything balances, as long as tastes are reasonable.
Reasonable means: more is better, mixtures are not worse than extremes, small changes in bundles give small changes in preference, and everyone owns some of every good.
It turns Adam Smith's idea of an invisible hand into a precise and checkable claim about existence.

### L2 human

The result is the foundation of [[general equilibrium theory|HGMHZSM0XQ]]: without it, the [[fundamental theorems of welfare economics|J6KA8R1H5Z]] could be about an empty set.
Its proof is the standard application of fixed-point theorems in economics, in the same way as [[Nash's existence theorem|85RY1ZGSTC]] in game theory.
Existence does not give uniqueness or stability; the [[Sonnenschein–Mantel–Debreu theorem|H8J1J00JXX]] shows that the excess demand can be almost arbitrary, so there can be several equilibria.
