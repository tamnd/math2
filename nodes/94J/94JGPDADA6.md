---
tag: 94JGPDADA6
kind: statement
role: theorem
name: Myerson–Satterthwaite theorem
msc: [91B26, 91B03]
uses: [DTXJQKEHDP, T1GTBBMHCW, S7D82PQ62H, YWZHYJAW1P, 0ZY9DX8FBF]
about: [DTXJQKEHDP]
sources:
  - url: https://en.wikipedia.org/wiki/Myerson%E2%80%93Satterthwaite_theorem
same_as:
  wikidata: Q6947442
  wikipedia: Myerson–Satterthwaite theorem
---

## Statement

A seller owns one indivisible object and a buyer may buy it.
The seller's value $s$ and the buyer's value $b$ are independent random variables, private to each trader.
The value $s$ has a positive continuous [[density|0ZY9DX8FBF]] on $[\underline{s}, \overline{s}]$ and $b$ has a positive continuous density on $[\underline{b}, \overline{b}]$.
Assume the two intervals overlap: $\underline{s} < \overline{b}$ and $\underline{b} < \overline{s}$.
Then no trading mechanism has all four properties:

1. it is Bayesian [[incentive compatible|T1GTBBMHCW]];
2. it is interim individually rational: each trader of each value expects a payoff of at least $0$;
3. it is ex post efficient: trade happens exactly when $b > s$;
4. it is budget balanced: no outside party needs to pay money into the mechanism, on average.

## Remarks

By the payment identity of the [[revenue equivalence theorem|S7D82PQ62H]], all incentive compatible efficient mechanisms with the same payoffs for the worst types give the same expected transfers.
One computes these transfers for a mechanism of the [[Vickrey–Clarke–Groves|YWZHYJAW1P]] type, in which the buyer pays the seller's value and the seller receives the buyer's value.
That mechanism runs an expected deficit, and individual rationality prevents moving that deficit onto the traders.

Example: if $s$ and $b$ are both uniform on $[0, 1]$, every efficient, individually rational, incentive compatible mechanism needs a subsidy.
In the second-best mechanism found by Myerson and Satterthwaite for this case, trade happens only when $b \ge s + 1/4$.

When the intervals do not overlap, for example $\overline{s} \le \underline{b}$, the fixed price $p = \overline{s}$ achieves all four properties, so the overlap hypothesis is necessary.

## Explanations

### L1 human

A buyer and a seller each know their own value for a good, and each would like to bluff to get a better price.
The theorem says that no rule of bargaining can make them trade every time trade is worth it, unless someone from outside adds money.
Private information always costs some lost trades.

### L2 human

The theorem is the basic impossibility result for bilateral trade.
It shows that the Coase argument, that bargaining reaches efficient outcomes, can fail when values are private.
Its proof uses the envelope formula for payments, the same one that gives revenue equivalence and Myerson's optimal auction.
