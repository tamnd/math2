---
tag: R9NBEJNQY3
kind: definition
name: Vickrey–Clarke–Groves mechanism
msc: [91B03, 91B26]
defines: YWZHYJAW1P
uses: [DTXJQKEHDP, T1GTBBMHCW, 75GR8RZSFP]
sources:
  - url: https://en.wikipedia.org/wiki/Vickrey%E2%80%93Clarke%E2%80%93Groves_mechanism
---

## Definition

Let $N = \set{1, \dots, n}$ be a set of agents and $A$ a finite set of alternatives.
Each agent $i$ has a valuation $v_i \colon A \to \R$ and receives utility $v_i(a) - p_i$ when alternative $a$ is chosen and she pays $p_i$.
The *Vickrey–Clarke–Groves mechanism* is the direct [[mechanism|DTXJQKEHDP]] in which each agent reports a valuation $\hat v_i$ and:

1. the chosen alternative is some $a^* \in A$ that maximises $\sum_{j \in N} \hat v_j(a)$, ties being broken by a fixed rule;
2. agent $i$ pays
$$p_i = \max_{a \in A} \sum_{j \ne i} \hat v_j(a) - \sum_{j \ne i} \hat v_j(a^*).$$

## Remarks

Truthful reporting is a dominant strategy.
Up to a term that agent $i$ cannot influence, her utility equals $v_i(a^*) + \sum_{j \ne i} \hat v_j(a^*)$.
When she reports $\hat v_i = v_i$, the mechanism chooses $a^*$ to maximise exactly this sum.
So the mechanism is dominant-strategy [[incentive compatible|T1GTBBMHCW]].
The payment of clause 2 is the *Clarke pivot* payment, and $p_i \ge 0$.
If all valuations are nonnegative, truthful agents also get nonnegative utility.
Example: sell one object, with alternatives "bidder $k$ gets it" for $k = 1, \dots, n$.
Let $v_i$ be $i$'s value if she gets the object and $0$ otherwise.
Then the highest bidder wins and pays the second-highest value, which is the [[Vickrey auction|75GR8RZSFP]].
Non-example: charging nothing, $p_i = 0$, keeps clause 1 but fails clause 2, and then agents gain by exaggerating their values.
More generally, a *Groves mechanism* replaces the first term of $p_i$ by any function $h_i$ of the reports of the others, and it is still dominant-strategy incentive compatible.

## Explanations

### L1 human

The mechanism picks the outcome that is best for the group as a whole, according to the reports.
Each agent pays for the loss her presence imposes on the others, so she has every reason to report honestly.
