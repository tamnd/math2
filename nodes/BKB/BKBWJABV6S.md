---
tag: BKBWJABV6S
kind: statement
role: theorem
name: Revelation principle
msc: [91B03, 91A35]
uses: [DTXJQKEHDP, T1GTBBMHCW, 9BF72YM075, 2XQ7VWT8KJ]
about: [DTXJQKEHDP, T1GTBBMHCW]
sources:
  - url: https://en.wikipedia.org/wiki/Revelation_principle
same_as:
  wikidata: Q7317833
  wikipedia: Revelation principle
---

## Statement

Let $N = \set{1, \dots, n}$ be a set of agents with type sets $\Theta_i$, let $X$ be a set of outcomes, and let $u_i \colon X \times \Theta_i \to \R$ be the utilities.
Let $f \colon \Theta_1 \times \cdots \times \Theta_n \to X$ be a social choice function.

Call *direct mechanism $f$* the mechanism in which each agent reports a type and the outcome is $f$ of the reports.

1. If some [[mechanism|DTXJQKEHDP]] $(S_1, \dots, S_n, g)$ implements $f$ in [[dominant strategies|9BF72YM075]], then the direct mechanism $f$ is dominant-strategy [[incentive compatible|T1GTBBMHCW]].
2. With a common prior on types, if some mechanism implements $f$ in Bayes–Nash equilibrium, then the direct mechanism $f$ is Bayesian incentive compatible.

## Remarks

Let $s_1, \dots, s_n$ be the equilibrium strategies of the given mechanism, so that $g(s_1(\theta_1), \dots, s_n(\theta_n)) = f(\theta)$.
The direct mechanism simulates the original one: on reports $\theta'$ it outputs $g(s_1(\theta_1'), \dots, s_n(\theta_n'))$, which equals $f(\theta')$.
Suppose agent $i$ of type $\theta_i$ gained by reporting $\theta_i'$ in the direct mechanism.
Then she would gain by playing $s_i(\theta_i')$ instead of $s_i(\theta_i)$ in the original mechanism, which contradicts the equilibrium property.
Example: let bidders in a first-price auction play a Bayes–Nash equilibrium bid function $b$.
The direct mechanism that asks for values $v_i$ and charges the winner $b(v_i)$ makes truthful reporting a Bayes–Nash equilibrium.
In part 2, the agents play the [[Bayesian game|2XQ7VWT8KJ]] induced by the mechanism and the prior.
The principle says nothing about other equilibria: the direct mechanism may have untruthful equilibria that the original mechanism did not have.

## Explanations

### L1 human

Any outcome that a clever set of rules achieves through strategic play can also be achieved by simply asking people for their private information.
The asking can be done so that honesty is their best choice.
The designer can promise to "play the game for them" with the strategies they would have used.
This reduces the search for good mechanisms to the search for incentive compatible ones.

### L2 human

The principle is the first step in most results of mechanism design.
To find the best auction or prove that a goal cannot be reached, one only needs to study direct incentive compatible mechanisms, which turn into explicit inequalities.
Impossibility results such as the Gibbard–Satterthwaite theorem and the Myerson–Satterthwaite theorem, and the derivation of the optimal auction, rely on it.
