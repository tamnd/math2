---
tag: 6QHFMX4ZHV
kind: statement
role: proposition
name: Put–call parity
msc: [91G20]
uses: [Q626SC54P7]
about: [Q626SC54P7]
sources:
  - url: https://en.wikipedia.org/wiki/Put%E2%80%93call_parity
same_as:
  wikidata: Q1183706
  wikipedia: Put–call parity
---

## Statement

Consider a stock that pays no dividends, with price $S_t$ at time $t$.
Let $C_t$ and $P_t$ be the prices of a European call and a European put on the stock.
Both have the same strike $K > 0$ and the same maturity $T > t$.
Let $B(t, T)$ be the price at time $t$ of a zero-coupon bond paying $1$ at time $T$.
If the market is free of [[arbitrage|Q626SC54P7]], then
$$C_t - P_t = S_t - K \, B(t, T).$$
With a constant interest rate $r$ and continuous compounding, $B(t, T) = e^{-r(T - t)}$.

## Remarks

At maturity the call pays $\max(S_T - K, 0)$ and the put pays $\max(K - S_T, 0)$.
Their difference is $S_T - K$ in every state.
So a long call with a short put has the same payoff as one share minus $K$ bonds.
Two portfolios with the same payoff must have the same price at time $t$; otherwise buying the cheaper and selling the dearer is an arbitrage.
The argument uses no model for the stock price.

Example: with $S_t = 100$, $K = 100$, $r = 0.05$ and $T - t = 1$, parity gives $C_t - P_t = 100 - 100 e^{-0.05} \approx 4.88$.

The hypotheses matter.
For American options, early exercise breaks the equality, and with a non-negative interest rate only the bounds $S_t - K \le C_t - P_t \le S_t - K B(t, T)$ hold.
If the stock pays dividends before $T$, their present value must be subtracted from $S_t$.

## Explanations

### L1 human

A call lets you buy at $K$, and a put lets you sell at $K$.
Owning a call and owing a put is the same as agreeing now to buy the stock at $K$ later.
So the price gap between the call and the put must equal the price of the stock minus the present value of $K$.
If it did not, traders could lock in a riskless profit.

### L2 human

Put–call parity is the simplest example of pricing by static replication.
It means that a model only needs to price calls; puts then follow.
It also shows that calls and puts with the same strike and maturity have the same implied volatility in the Black–Scholes model.
