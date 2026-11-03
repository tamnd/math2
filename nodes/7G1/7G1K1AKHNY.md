---
tag: 7G1K1AKHNY
kind: definition
name: Perfect Bayesian equilibrium
msc: [91A27, 91A18, 91A11]
defines: RG94E9CBQJ
uses: [4Y8AF9H9HA, 0DVDCMA2DK, 0990W5PN13, 0WQNRCNY3M, 745WYP9YJ0, DNVNS5HNYR]
sources:
  - url: https://en.wikipedia.org/wiki/Perfect_Bayesian_equilibrium
---

## Definition

Let $\Gamma$ be a finite [[extensive-form game|4Y8AF9H9HA]] with perfect recall, possibly with moves of chance.
Let $\sigma$ be a profile of behaviour strategies, which give at each information set a [[probability distribution|0DVDCMA2DK]] over the available actions.
Let $\mu$ be a belief system, which gives at each information set $h$ a probability distribution $\mu(\cdot \mid h)$ over the nodes of $h$.
The pair $(\sigma, \mu)$ is a *perfect Bayesian equilibrium* if:

1. (Sequential rationality) At every information set $h$, the mover's strategy maximizes her [[expected payoff|0WQNRCNY3M]] from $h$ onward, given $\mu(\cdot \mid h)$ and $\sigma$.
2. (Bayes' rule on the path) Let $h$ be reached with positive probability under $\sigma$ and the chance moves. Then $\mu(\cdot \mid h)$ is the [[conditional probability|0990W5PN13]] of the nodes of $h$ given that $h$ is reached.

## Remarks

Beliefs at information sets reached with probability zero are not restricted by clause 2.
This version is often called a *weak* perfect Bayesian equilibrium.
Stronger versions also require Bayes' rule wherever possible off the path of play, or within every subgame, and the strongest common requirement leads to sequential equilibrium.
Every weak perfect Bayesian equilibrium is a [[Nash equilibrium|745WYP9YJ0]], but it need not be subgame perfect.

Example: the entrant chooses Out, with payoffs $(0, 2)$, or In; after In the incumbent chooses Fight, with payoffs $(-1, -1)$, or Accommodate, with payoffs $(1, 1)$.
With the trivial beliefs at single-node information sets, (In, Accommodate) satisfies clause 1: Accommodate gives $1 > -1$ and In gives $1 > 0$.
Clause 2 holds because every belief is concentrated on the only node.

Non-example: in the same game (Out, Fight) fails clause 1, because at the incumbent's node Fight gives $-1 < 1$, even though the node is off the path.

In a [[signaling game|DNVNS5HNYR]], clause 2 says that after a message sent with positive probability, the receiver's belief about the sender's type is the posterior given by Bayes' rule.
