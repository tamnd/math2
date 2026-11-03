---
tag: JC6T2ZAH2X
kind: definition
name: Online algorithm and competitive analysis
msc: [68W27, 68W40, 68Q25]
defines: 6KWDEYZ88A
uses: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Competitive_analysis_(online_algorithm)
---

## Definition

Consider a minimization problem whose inputs are finite request sequences $\sigma = (\sigma_1, \dots, \sigma_T)$.
An *online algorithm* is an [[algorithm|9DMSG5HAQX]] $A$ that serves $\sigma_1, \sigma_2, \dots$ in order, choosing its action for $\sigma_t$ from $\sigma_1, \dots, \sigma_t$ only.
Let $A(\sigma)$ be its total cost, and let $\mathrm{OPT}(\sigma)$ be the least total cost of serving $\sigma$ with full knowledge of $\sigma$.
For a real number $c \ge 1$, the algorithm $A$ is *$c$-competitive* if there is a constant $\alpha$ with $A(\sigma) \le c \cdot \mathrm{OPT}(\sigma) + \alpha$ for every $\sigma$.
It is *strictly $c$-competitive* if this holds with $\alpha = 0$.
The *competitive ratio* of $A$ is the infimum of all $c$ for which $A$ is $c$-competitive.

## Remarks

Example: in ski rental with an integer buying price $B \ge 1$, the request $\sigma_t$ says that the skier goes skiing on day $t$, and renting costs $1$ per day.
For $d$ days of skiing, $\mathrm{OPT} = \min(d, B)$.
The algorithm that rents on days $1, \dots, B - 1$ and buys on day $B$ pays $d$ if $d < B$ and $2B - 1$ if $d \ge B$.
So it is strictly $(2 - 1/B)$-competitive.

Non-example: the algorithm that always rents pays $d$, while $\mathrm{OPT} = B$ for $d \ge B$.
For any $c$ and $\alpha$, the inequality $d \le cB + \alpha$ fails for large $d$, so this algorithm is not $c$-competitive for any $c$.

For a randomized online algorithm, $A(\sigma)$ is replaced by its expected cost, and the adversary is usually assumed not to see the random choices.
