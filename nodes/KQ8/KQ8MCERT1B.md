---
tag: KQ8MCERT1B
kind: statement
role: proposition
name: Hotelling's law
msc: [91B72, 91A10, 91B54]
uses: [745WYP9YJ0, 5MZTZRC3CZ]
about: [745WYP9YJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Hotelling%27s_law
same_as:
  wikidata: Q1631149
  wikipedia: Hotelling's law
---

## Statement

Consider the following [[normal-form game|5MZTZRC3CZ]].
Consumers are spread uniformly over the interval $[0, 1]$, with total mass $1$, and each consumer buys one unit from the nearest firm.
Two firms, which sell at the same fixed price, choose locations $x_1, x_2 \in [0, 1]$ at the same time.
The payoff of each firm is its market share.
If $x_1 < x_2$, firm $1$ gets $(x_1 + x_2)/2$ and firm $2$ gets $1 - (x_1 + x_2)/2$.
If $x_1 = x_2$, each gets $1/2$, and the case $x_1 > x_2$ is symmetric.
Then the game has exactly one [[Nash equilibrium|745WYP9YJ0]], and in it both firms locate at the centre: $x_1 = x_2 = 1/2$.

## Remarks

At $(1/2, 1/2)$ each firm gets $1/2$.
A firm that moves to any $x \ne 1/2$ gets less than $1/2$, because the other firm keeps its side of the centre plus half the gap.
At any other profile, some firm can do better.
If $x_1 < x_2$, firm $1$ gains by moving right towards $x_2$, since its share $(x_1 + x_2)/2$ grows with $x_1$.
If $x_1 = x_2 = x \ne 1/2$, either firm gains by moving slightly towards the centre and taking the larger side, worth more than $1/2$.

Example: the firms at $0.3$ and $0.6$ share the market as $0.45$ and $0.55$; firm $1$ can raise its share to nearly $0.6$ by moving to just left of $0.6$.

The fixed equal price is needed.
When the firms also compete in prices after choosing locations, the conclusion can fail.
In some versions of that model, firms prefer to locate far apart to soften price competition.

## Explanations

### L1 human

Two ice-cream sellers on a beach of evenly spread sunbathers each want as many customers as possible.
Wherever one stands, the other does best by standing right next to it, on the longer side.
This pushes both sellers to the middle of the beach, side by side, even though spreading out would serve the sunbathers better.
It explains why competing products or shops often end up very similar.

### L2 human

Harold Hotelling introduced this spatial model in 1929.
The same argument with voters in place of consumers and policy positions in place of locations gives the [[median voter theorem|4J3G7Y0VYC]], where two parties converge to the median voter's position.
The outcome is not socially optimal: total travel distance is smallest with the firms at $1/4$ and $3/4$.
With three or more firms, or with price competition, the equilibrium structure changes, which makes the model a starting point for the study of product differentiation.
