---
tag: VQPN24VDH1
kind: statement
role: theorem
name: Chow–Rashevskii theorem
msc: [93B05, 53C17, 93B27]
uses: [F45VQ47GPV, 0299VCW1TH, 68FGQEBD6J, A9WFM77Z4P, 06738GGWWK, 97NYHNBZ2D]
about: [A9WFM77Z4P, 68FGQEBD6J]
sources:
  - url: https://en.wikipedia.org/wiki/Chow–Rashevsky_theorem
same_as:
  wikidata: Q5105585
  wikipedia: Chow–Rashevsky theorem
---

## Statement

Let $M$ be a connected [[smooth manifold|F45VQ47GPV]] and let $X_1, \ldots, X_k$ be smooth [[vector fields|0299VCW1TH]] on $M$.
Assume the bracket-generating condition.
For every $p \in M$, the values at $p$ of the $X_i$ and of their iterated [[Lie brackets|68FGQEBD6J]] $[X_i, X_j]$, $[X_i, [X_j, X_l]]$, and so on, span $T_p M$.
Consider the driftless control system
$$x' = \sum_{i=1}^{k} u_i X_i(x), \qquad u = (u_1, \ldots, u_k) \in \R^k.$$
This system is [[controllable|A9WFM77Z4P]]: any two points of $M$ are joined by a trajectory of the system for a piecewise constant control.
Equivalently, any two points of $M$ are joined by a piecewise smooth curve whose velocity lies at each point in the span of $X_1, \ldots, X_k$.

## Remarks

The set of points reachable from $p$ is the set of endpoints of finite compositions of [[flows|06738GGWWK]] of the fields $\pm X_i$.
Since the system is symmetric under $u \mapsto -u$, reachability is an equivalence relation, and the equivalence classes partition $M$.
Flowing back and forth along two fields moves a point, to second order, in the direction of their bracket.
With the bracket condition, this shows that for suitable $Y_j$ among the $\pm X_i$, the map $(t_1, \ldots, t_N) \mapsto e^{t_N Y_N} \circ \cdots \circ e^{t_1 Y_1}(p)$ has an image with nonempty interior.
So each class is open, and connectedness of $M$ leaves only one class.
Example: on $\R^3$, the fields $X_1 = \partial_x - \frac{y}{2} \partial_z$ and $X_2 = \partial_y + \frac{x}{2} \partial_z$ satisfy $[X_1, X_2] = \partial_z$, so $X_1, X_2, [X_1, X_2]$ span $\R^3$ at each point and every point is reachable, although only two directions are controlled.
The bracket condition cannot be dropped: for $X_1 = \partial_x$ and $X_2 = \partial_y$ on $\R^3$ all brackets vanish, and the trajectories from $p$ stay in the plane through $p$ where $z$ is constant.

## Explanations

### L1 human

A car can move forward, backward and turn, but it cannot slide sideways.
Still, by a sequence of small forward and turning motions, it can park in a gap beside it.
The theorem explains why: alternating two allowed motions produces a motion in a new direction, given by their Lie bracket.
If the allowed motions and their brackets point in all directions, then every position can be reached.

### L2 human

The theorem is the basic controllability result of geometric control theory for systems without drift.
In [[sub-Riemannian geometry|97NYHNBZ2D]] it shows that the distance defined by curves tangent to a bracket-generating distribution is finite, and it is the starting point of that theory.
For systems with drift $x' = X_0(x) + \sum u_i X_i(x)$ the bracket condition only gives that the reachable sets have nonempty interior, not controllability.
