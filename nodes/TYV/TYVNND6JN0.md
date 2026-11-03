---
tag: TYVNND6JN0
kind: statement
role: theorem
name: Fundamental theorem of asset pricing
msc: [91G20, 60G42]
uses: [Q626SC54P7, 858BHBY2BD, A1V152H2CA, 0D0GBNDKDH, 6GWMGFGFJJ]
about: [Q626SC54P7, 858BHBY2BD]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_asset_pricing
same_as:
  wikidata: Q5508973
  wikipedia: Fundamental theorem of asset pricing
---

## Statement

Let $\Omega$ be a finite set with a probability $P$ such that $P(\set{\omega}) > 0$ for every $\omega \in \Omega$.
Consider a market in discrete time $t = 0, \dots, T$ with a filtration $(\mathcal{F}_t)$ and discounted prices $S_t \in \R^d$ of the risky assets.

1. The market is free of [[arbitrage|Q626SC54P7]] if and only if a [[risk-neutral measure|858BHBY2BD]] exists.
2. Suppose the market is free of arbitrage.
   Then it is [[complete|A1V152H2CA]] if and only if the risk-neutral measure is unique.

## Remarks

The easy direction of part 1: if $Q$ is a risk-neutral measure, the gain $G_T$ of any strategy is a [[martingale|0D0GBNDKDH]] transform with $\mathbb{E}_Q[G_T] = 0$.
So $G_T \ge 0$ almost surely forces $G_T = 0$ almost surely, and there is no arbitrage.
The hard direction separates the cone of non-negative payoffs from the subspace of attainable gains by a hyperplane, as in the [[separation theorem|6GWMGFGFJJ]].
The normal vector of the hyperplane, suitably normalised, is the density of the risk-neutral measure.

Example: one period with $S_0 = 100$ and $S_1 \in \set{120, 90}$ and interest rate $0$.
The unique risk-neutral measure gives the up state probability $1/3$, so the market is free of arbitrage and complete.
With $S_1 \in \set{120, 110}$, a martingale measure would need $100 = 120q + 110(1 - q)$, which has no solution in $(0, 1)$, and indeed buying the stock is an arbitrage.

Part 1 holds in discrete time on any probability space; this is the Dalang–Morton–Willinger theorem.
In continuous time, "no arbitrage" must be strengthened to "no free lunch with vanishing risk", and martingales to local martingales or σ-martingales, by the work of Delbaen and Schachermayer.

## Explanations

### L1 human

The theorem turns an economic condition into a mathematical object.
"No free lunch" in a market is the same as the existence of probabilities under which every asset is a fair game.
And the market can replicate every payoff exactly when these probabilities are unique.
This is why derivative prices are computed as expected discounted payoffs.

### L2 human

Part 1 is the reason that pricing by a risk-neutral measure never creates arbitrage.
If a claim $H$ is priced at $\mathbb{E}_Q[H]$, adding it to the market keeps $Q$ a martingale measure.
In an incomplete market there are many risk-neutral measures, and they give an interval of arbitrage-free prices for a claim that cannot be replicated.
The binomial model is the simplest complete market, and the Black–Scholes model is its continuous-time limit.
The proof of part 1 is a finite-dimensional duality argument, close to Farkas' lemma in linear programming.
