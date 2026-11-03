---
tag: DECWPTFMJ6
kind: statement
role: theorem
name: Folk theorem
msc: [91A20, 91A10]
uses: [XHE1BSE7BF, 5MZTZRC3CZ, P01KKHB155, 745WYP9YJ0, 0FQSDC2EQ2, 1YER21VF5Q, JEMK4V2PCW]
about: [XHE1BSE7BF]
sources:
  - url: https://en.wikipedia.org/wiki/Folk_theorem_(game_theory)
same_as:
  wikidata: Q650738
  wikipedia: Folk theorem (game theory)
---

## Statement

Let $G$ be a finite [[normal-form game|5MZTZRC3CZ]] with players $i = 1, \dots, n$, action sets $A_i$ and payoff functions $u_i$, and let $A = A_1 \times \cdots \times A_n$.
For player $i$, let
$$\underline{v}_i = \min_{\alpha_{-i}} \max_{a_i \in A_i} u_i(a_i, \alpha_{-i})$$
be her minmax value, where $\alpha_{-i}$ ranges over the profiles of independent [[mixed strategies|P01KKHB155]] of the other players.
Let $V$ be the [[convex hull|0FQSDC2EQ2]] of the set $\set{u(a) : a \in A}$ of payoff vectors of $G$.
Let $v \in V$ satisfy $v_i > \underline{v}_i$ for every player $i$.
Then there is $\underline{\delta} < 1$ with the following property.
For every $\delta \in (\underline{\delta}, 1)$, the infinitely [[repeated game|XHE1BSE7BF]] $G^\infty(\delta)$ has a [[Nash equilibrium|745WYP9YJ0]] with payoff vector $v$.

## Remarks

The proof uses trigger strategies.
The players follow a fixed sequence of action profiles whose normalized discounted payoff is $v$.
If some player $i$ deviates, the others switch forever to a profile $\alpha_{-i}$ that holds her to $\underline{v}_i$.
A deviation gains a bounded amount once and then loses $v_i - \underline{v}_i > 0$ in every later period, so for $\delta$ close to $1$ it does not pay.
When $v$ is not itself a payoff vector $u(a)$, one can let the players use a public random signal in each period.
Alternatively, one chooses a deterministic sequence of action profiles whose discounted average is $v$, which works for $\delta$ close to $1$.

Example: in the prisoner's dilemma with $u(C, C) = (2, 2)$, $u(D, D) = (1, 1)$, $u(D, C) = (3, 0)$ and $u(C, D) = (0, 3)$, each minmax value is $1$.
So every vector in the quadrilateral with corners $(1,1), (2,2), (3,0), (0,3)$ with both coordinates above $1$, such as $(2, 2)$, is an equilibrium payoff for $\delta$ close to $1$.

Payoffs below the minmax values cannot occur: in every Nash equilibrium of the repeated game, each player gets at least $\underline{v}_i$, because she can best respond in every period.
Stronger versions give subgame perfect equilibria instead of Nash equilibria.
Fudenberg and Maskin proved such a version in 1986, with a full-dimensionality condition on $V$ when there are three or more players.

## Explanations

### L1 human

When a game is repeated forever and players care enough about the future, almost any outcome can be held together by threats.
The only limit is that each player must get more than the least she can guarantee herself when everyone else gangs up on her.
So repetition can turn a world of mutual defection into one of stable cooperation.
The name comes from the fact that the result was widely known among game theorists before anyone published it.

### L2 human

The theorem explains why cooperation in the repeated [[prisoner's dilemma|1YER21VF5Q]] is possible, but it also says that repeated games have a huge number of equilibria.
So it is as much a negative result about prediction as a positive result about cooperation.
In finitely repeated games the picture is different.
If the stage game has a unique Nash equilibrium, [[backward induction|JEMK4V2PCW]] shows that the only subgame perfect equilibrium plays it in every period.
Folk theorems with imperfect monitoring, where players see only noisy signals of the actions, are an active area of research.
