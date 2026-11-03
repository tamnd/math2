---
tag: FYXH5YQYG2
kind: definition
name: Sequential equilibrium
msc: [91A11, 91A18]
defines: T4Y6J21Q04
uses: [4Y8AF9H9HA, 0DVDCMA2DK, 0990W5PN13, 0WQNRCNY3M, 05M5SWSZZD]
sources:
  - url: https://en.wikipedia.org/wiki/Sequential_equilibrium
---

## Definition

Let $\Gamma$ be a finite [[extensive-form game|4Y8AF9H9HA]] with perfect recall.
A *behaviour strategy* of a player assigns to each of her information sets a [[probability distribution|0DVDCMA2DK]] over the actions available there.
A *belief system* $\mu$ assigns to each information set $h$ a probability distribution $\mu(\cdot \mid h)$ over the nodes of $h$.
An *assessment* is a pair $(\sigma, \mu)$ of a profile $\sigma$ of behaviour strategies and a belief system $\mu$.
The assessment $(\sigma, \mu)$ is a *sequential equilibrium* if:

1. (Sequential rationality) At every information set $h$, the mover's strategy maximizes her [[expected payoff|0WQNRCNY3M]] from $h$ onward, given $\mu(\cdot \mid h)$ and $\sigma$.
2. (Consistency) There is a sequence $(\sigma^k, \mu^k)$ converging to $(\sigma, \mu)$ with two properties. Each $\sigma^k$ gives positive probability to every action at every information set. Each $\mu^k$ is computed from $\sigma^k$ by Bayes' rule, that is, by [[conditional probability|0990W5PN13]].

## Remarks

Under $\sigma^k$ every node is reached with positive probability, so Bayes' rule defines $\mu^k$ everywhere.
Kreps and Wilson proved that every finite extensive-form game with perfect recall has a sequential equilibrium.
The strategy part of a sequential equilibrium is a subgame perfect equilibrium.

Example: an entrant chooses Out, with payoffs $(0, 2)$, or In; after In the incumbent chooses Fight, with payoffs $(-1, -1)$, or Accommodate, with payoffs $(1, 1)$.
Every information set is a single node, so beliefs are trivial and consistency holds.
In (In, Accommodate), the incumbent gets $1 > -1$ by accommodating, and the entrant gets $1 > 0$ by entering, so clause 1 holds.

Non-example: (Out, Fight) is a Nash equilibrium of this game, but it fails clause 1.
At the incumbent's node, Fight gives $-1$ while Accommodate gives $1$.
