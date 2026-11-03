---
tag: SPRBTRTD36
kind: statement
role: theorem
name: Bondareva–Shapley theorem
msc: [91A12, 90C05]
uses: [39HGM44CFZ, CBP13S0ETD, VNMXB0J2KA]
about: [CBP13S0ETD]
sources:
  - url: https://en.wikipedia.org/wiki/Bondareva%E2%80%93Shapley_theorem
same_as:
  wikidata: Q4941364
  wikipedia: Bondareva–Shapley theorem
---

## Statement

Let $(N, v)$ be a [[cooperative game with transferable utility|39HGM44CFZ]].
A family of weights $(\lambda_S)$, indexed by the nonempty coalitions $S \subseteq N$, is *balanced* if $\lambda_S \ge 0$ for all $S$ and $\sum_{S \ni i} \lambda_S = 1$ for every player $i \in N$.
The game is *balanced* if $\sum_{S} \lambda_S v(S) \le v(N)$ for every balanced family of weights.
Then the [[core|CBP13S0ETD]] of $(N, v)$ is nonempty if and only if $(N, v)$ is balanced.

## Remarks

The core is nonempty exactly when the [[linear program|VNMXB0J2KA]] "minimise $x(N)$ subject to $x(S) \ge v(S)$ for all nonempty $S$" has optimal value at most $v(N)$.
The dual program is "maximise $\sum_S \lambda_S v(S)$ over balanced families $(\lambda_S)$", and the duality theorem of linear programming gives equal optimal values.
So the core is nonempty if and only if every balanced family satisfies $\sum_S \lambda_S v(S) \le v(N)$.
Example: in the three-player majority game, with $v(S) = 1$ for $\abs{S} \ge 2$ and $v(S) = 0$ otherwise, take $\lambda_S = 1/2$ for the three pairs and $\lambda_S = 0$ otherwise.
This family is balanced, and $\sum_S \lambda_S v(S) = 3/2 > 1 = v(N)$, so the core is empty.
The theorem was found independently by Olga Bondareva and Lloyd Shapley.

## Explanations

### L1 human

The core is the set of stable ways to share the total, and it can be empty.
The theorem gives a test: think of each player as splitting one unit of time among coalitions.
If some such part-time arrangement earns more than the grand coalition does, there is no stable split, and otherwise there is one.

### L2 human

The theorem is a direct application of linear programming duality, and the balanced families are the dual feasible points.
A game whose subgames all have nonempty cores is called totally balanced.
Shapley and Shubik showed that the totally balanced games are exactly the games that arise from exchange markets.
Convex games, where $v(S \cup T) + v(S \cap T) \ge v(S) + v(T)$, are balanced, so their cores are nonempty.
