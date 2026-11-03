---
tag: TRJ4535TZT
kind: definition
name: Vickrey auction
msc: [91B26, 91B03]
defines: 75GR8RZSFP
uses: [86ZWXGHNGB, T1GTBBMHCW, 9BF72YM075]
sources:
  - url: https://en.wikipedia.org/wiki/Vickrey_auction
---

## Definition

Let $n \ge 2$ bidders submit sealed bids $b_1, \dots, b_n \ge 0$ for a single object.
The *Vickrey auction*, or second-price sealed-bid [[auction|86ZWXGHNGB]], is the auction in which:

1. the object goes to a bidder $i$ with the highest bid, $b_i = \max_j b_j$, ties being broken by a fixed rule;
2. the winner pays the highest bid among the other bidders, $\max_{j \ne i} b_j$;
3. the other bidders pay nothing.

## Remarks

If bidder $i$ values the object at $v_i$, then the bid $b_i = v_i$ is a weakly [[dominant strategy|9BF72YM075]].
Indeed, her bid affects only whether she wins, at the price $p = \max_{j \ne i} b_j$.
Bidding $v_i$ makes her win when $v_i > p$, where winning gives the gain $v_i - p > 0$.
It makes her lose when $v_i < p$, where winning would give a loss.
So the Vickrey auction is dominant-strategy [[incentive compatible|T1GTBBMHCW]].
Example: bids $10, 7, 4$ give the object to bidder $1$ at price $7$.
Non-example: the rule in which the winner pays her own bid fails clause 2; in it, bidding one's value always yields utility $0$, and shading the bid is profitable.

## Explanations

### L1 human

The highest bidder wins and pays the second-highest bid.
Because the price does not depend on the winner's own bid, overbidding and underbidding can only hurt.
