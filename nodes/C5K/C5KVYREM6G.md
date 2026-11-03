---
tag: C5KVYREM6G
kind: statement
role: theorem
name: Hotelling's rule
msc: [91B76]
uses: [Q626SC54P7]
about: [Q626SC54P7]
sources:
  - url: https://en.wikipedia.org/wiki/Hotelling%27s_rule
same_as:
  wikidata: Q443972
  wikipedia: Hotelling's rule
---

## Statement

Consider a competitive market for a non-renewable resource with a fixed total stock, over continuous time $t \ge 0$.
Assume that the interest rate $r > 0$ is constant and that owners have perfect foresight of the price path $p(t)$.
Assume that the marginal cost of extraction is a constant $c \ge 0$.
If the resource is extracted at a positive rate at every time in an interval $[t_0, t_1]$, then for all $t$ in that interval
$$p(t) - c = (p(t_0) - c) \, e^{r (t - t_0)}.$$
In words, the net price of the resource rises at the rate of interest.

## Remarks

The idea is a no-[[arbitrage|Q626SC54P7]] argument.
An owner can extract a unit at time $s$ and invest the net price $p(s) - c$ at rate $r$.
Or the owner can keep the unit in the ground and extract it at a later time $t$.
If both are done in equilibrium, neither can be strictly better, so $e^{r(t - s)}(p(s) - c) = p(t) - c$.
If the net price grew faster than $r$, all owners would delay extraction; if slower, all would extract at once.

Example: with $c = 0$, $r = 0.05$ and $p(0) = 10$, the price after $10$ years is $10 e^{0.5} \approx 16.5$.

The net price $p - c$ is the scarcity rent of the resource.
The rule changes when extraction costs depend on the rate of extraction or on the remaining stock.
Then it is the marginal rent, not the price net of a constant cost, that grows at rate $r$.
The rule comes from Harold Hotelling's 1931 paper on the economics of exhaustible resources.

## Explanations

### L1 human

Oil in the ground is an asset, just like money in a bank.
An owner will leave oil in the ground only if its value is expected to grow as fast as money in the bank.
So in a market where people extract over time, the profit per barrel must rise at the rate of interest.
The rising price slows consumption as the resource runs out.

### L2 human

Hotelling's rule is the starting point of the economics of exhaustible resources.
It is the Euler equation of the planner's problem of extracting a finite stock to maximise discounted surplus.
Together with the demand curve and the condition that the stock is used up exactly, it fixes the whole price path.
It is also an example of the general principle that, without [[arbitrage|Q626SC54P7]], every asset held in equilibrium earns the same return.
