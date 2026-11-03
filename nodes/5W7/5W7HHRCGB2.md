---
tag: 5W7HHRCGB2
kind: statement
role: theorem
name: Myerson's optimal auction
msc: [91B26, 91B03]
uses: [86ZWXGHNGB, DTXJQKEHDP, T1GTBBMHCW, S7D82PQ62H, 75GR8RZSFP, 0H8H7ZTHW2, 0ZY9DX8FBF]
about: [86ZWXGHNGB, DTXJQKEHDP]
sources:
  - url: https://en.wikipedia.org/wiki/Auction_theory
---

## Statement

Let a seller who values it at $0$ sell one indivisible object to $n$ risk-neutral bidders.
Bidder $i$ has a private value $v_i$, the values are independent, and $v_i$ has [[distribution function|0H8H7ZTHW2]] $F_i$ with a [[density|0ZY9DX8FBF]] $f_i > 0$ on $[a_i, b_i]$.
The *virtual value* of bidder $i$ is
$$\varphi_i(v_i) = v_i - \frac{1 - F_i(v_i)}{f_i(v_i)}.$$
Assume each $\varphi_i$ is nondecreasing (the *regular* case).
Among all Bayesian [[incentive compatible|T1GTBBMHCW]] and individually rational direct mechanisms, the following one maximizes the seller's expected revenue:

1. if $\max_i \varphi_i(v_i) < 0$, the seller keeps the object;
2. otherwise the object goes to a bidder with the largest virtual value;
3. the winner pays the smallest value she could have reported and still won, and the others pay nothing.

Its expected revenue is $\mathbb{E}\left[\max\left(0, \max_i \varphi_i(v_i)\right)\right]$.

## Remarks

The payment formula behind the [[revenue equivalence theorem|S7D82PQ62H]] gives, after integration by parts, that the expected revenue of any such mechanism equals $\mathbb{E}\left[\sum_i \varphi_i(v_i)\, x_i(v)\right]$ minus the payoffs of the lowest types.
Here $x_i(v)$ is the probability that $i$ gets the object.
This is maximized pointwise by giving the object to the largest nonnegative virtual value.
Regularity makes this pointwise rule monotone, hence incentive compatible.

When the bidders are symmetric ($F_i = F$ for all $i$), the optimal auction is a [[second-price auction|75GR8RZSFP]] with reserve price $r$ such that $\varphi(r) = 0$.
For values uniform on $[0, 1]$, $\varphi(v) = 2v - 1$ and $r = 1/2$.
With two such bidders the optimal revenue is $5/12$, more than the revenue $1/3$ of the second-price auction without reserve.

Without regularity the pointwise rule may not be monotone.
Myerson then replaces $\varphi_i$ by an "ironed" nondecreasing version, and the same conclusion holds with the ironed virtual values.

## Explanations

### L1 human

A seller who knows only the odds of how much buyers will pay wants to design the auction that earns the most on average.
Myerson showed that the best auction ranks bidders by an adjusted value, which is their value minus a penalty for the information they hold.
In the simplest case this is an ordinary second-price auction with a minimum price.

### L2 human

The result is the founding example of optimal mechanism design.
It explains reserve prices: the seller sometimes refuses to sell, giving up some trades to raise the price paid by high bidders.
The virtual value is the marginal revenue of a monopolist facing the demand curve $1 - F_i$.
