---
tag: 435FYS7FBK
kind: definition
name: First-price sealed-bid auction
msc: [91B26]
defines: 298P32KHRW
uses: [86ZWXGHNGB, 2XQ7VWT8KJ, 75GR8RZSFP]
sources:
  - url: https://en.wikipedia.org/wiki/First-price_sealed-bid_auction
---

## Definition

Let $n \ge 2$ bidders submit sealed bids $b_1, \dots, b_n \ge 0$ for a single object.
The *first-price sealed-bid [[auction|86ZWXGHNGB]]* is the auction in which:

1. the object goes to a bidder $i$ with the highest bid, $b_i = \max_j b_j$, ties being broken by a fixed rule;
2. the winner pays her own bid $b_i$;
3. the other bidders pay nothing.

## Remarks

Example: bids $10, 7, 4$ give the object to bidder $1$ at price $10$.
Non-example: the [[Vickrey auction|75GR8RZSFP]] fails clause 2, since there the winner pays the second-highest bid, $7$ in this example.
Suppose the $n$ bidders have private values that are independent and uniform on $[0, 1]$.
Then the bid function $\beta(v) = \frac{n - 1}{n} v$ is a symmetric Bayes–Nash equilibrium of the induced [[Bayesian game|2XQ7VWT8KJ]].
The expected revenue of this equilibrium is $\frac{n - 1}{n + 1}$, the expected second-highest value, which is also the expected revenue of the Vickrey auction with truthful bids.
The Dutch descending auction, where the price falls until a bidder accepts it, is strategically equivalent to the first-price sealed-bid auction.

## Explanations

### L1 human

The highest bid wins and the winner pays what she bid.
Because of this, bidders shade their bids below their values, and the equilibrium amount of shading depends on how many rivals there are.
