---
tag: VCMGZGT39B
kind: definition
name: Mechanism design
msc: [91B03, 91A80]
defines: DTXJQKEHDP
uses: [2XQ7VWT8KJ, 745WYP9YJ0, 9BF72YM075]
sources:
  - url: https://en.wikipedia.org/wiki/Mechanism_design
---

## Definition

A *mechanism design environment* consists of:

1. a finite set $N = \set{1, \dots, n}$ of agents;
2. for each agent $i$ a set $\Theta_i$ of types, private information known only to $i$, with $\Theta = \Theta_1 \times \cdots \times \Theta_n$;
3. a set $X$ of outcomes;
4. for each agent $i$ a utility function $u_i \colon X \times \Theta_i \to \R$.

A *social choice function* is a map $f \colon \Theta \to X$.
A *mechanism* is a tuple $(S_1, \dots, S_n, g)$ of strategy sets $S_i$ and an outcome function $g \colon S_1 \times \cdots \times S_n \to X$.
A *strategy* of agent $i$ is a map $s_i \colon \Theta_i \to S_i$.
The mechanism *implements* $f$ in dominant strategies if there are strategies $s_1, \dots, s_n$ with two properties for every type profile $\theta$.
First, each $s_i(\theta_i)$ is a [[dominant strategy|9BF72YM075]] for $i$ in the game with payoffs $u_i(g(\cdot), \theta_i)$.
Second, $g(s_1(\theta_1), \dots, s_n(\theta_n)) = f(\theta)$.
Suppose the types are drawn from a common prior on $\Theta$.
The mechanism *implements* $f$ in Bayes–Nash equilibrium if the second property holds for a Bayes–Nash equilibrium $(s_1, \dots, s_n)$ of the induced [[Bayesian game|2XQ7VWT8KJ]].
A mechanism is *direct* if $S_i = \Theta_i$ for every $i$.

## Remarks

Example: a single object and $n$ bidders with values $\theta_i \in [0, \infty)$; outcomes say who gets the object and what everyone pays, and $u_i$ is value received minus payment.
The second-price auction is a direct mechanism, and truthful bidding $s_i(\theta_i) = \theta_i$ is dominant in it.
So it implements in dominant strategies the rule "give the object to a bidder with the highest value and charge her the second-highest value".
Non-example: the first-price auction with $s_i(\theta_i) = \theta_i$ does not implement this function in dominant strategies, since bidding one's value is not a dominant strategy there.
The designer's problem is to find, for a given goal $f$, a mechanism that implements it, or to show that none exists.
Bayes–Nash equilibrium is the analogue of [[Nash equilibrium|745WYP9YJ0]] for games with private types.

## Explanations

### L1 human

The environment records who the agents are, what each privately knows, and what outcomes are possible.
A mechanism is a game: each agent sends a message, and a rule turns the messages into an outcome.
It implements a goal if, when everyone plays strategically, the outcome is the one the goal prescribes.
