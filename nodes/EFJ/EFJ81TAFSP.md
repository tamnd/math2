---
tag: EFJ81TAFSP
kind: counterexample
name: St. Petersburg paradox
msc: [91B16, 91B06]
uses: [0WQNRCNY3M, 8C2N37XPJ8, FZNYZWR7MY]
sources:
  - url: https://en.wikipedia.org/wiki/St._Petersburg_paradox
same_as:
  wikidata: Q874375
  wikipedia: St. Petersburg paradox
---

## Counterexample

A fair coin is tossed until it first shows heads.
If the first heads comes on toss $k$, which has probability $2^{-k}$, the player receives $2^k$ euros.
Let $W$ be the payment.
Its [[expected value|0WQNRCNY3M]] is
$$\mathbb{E}[W] = \sum_{k=1}^{\infty} 2^{-k} \cdot 2^k = \sum_{k=1}^{\infty} 1 = \infty.$$
So a player who values a gamble by its expected payment would pay any finite price to play.
Yet people are willing to pay only a small amount.
So the expected payment is not a good model of how gambles are valued.

## Remarks

Daniel Bernoulli proposed to value the game by an [[expected utility|8C2N37XPJ8]] with the utility $u(w) = \ln w$.
Then $\mathbb{E}[\ln W] = \sum_{k \ge 1} 2^{-k} k \ln 2 = 2 \ln 2$, so the [[certainty equivalent|FZNYZWR7MY]] of the game is $e^{2 \ln 2} = 4$ euros, ignoring the initial wealth of the player.
An unbounded utility does not fully solve the problem.
If $u$ is unbounded above, choose payments $x_k$ with $u(x_k) \ge 2^k$; the game paying $x_k$ on toss $k$ again has infinite expected utility.
A bounded utility, or a cap on the payments, such as the finite wealth of the casino, removes the paradox.

## Explanations

### L1 human

The game promises a payment that doubles each time the coin lands tails before the first heads.
On average it pays an infinite amount, because each possible round adds one euro to the average.
Still, almost nobody would pay more than a small fixed amount to play.
The paradox shows that people do not value gambles by their average payment, and it led to the idea of utility.
