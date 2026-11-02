---
tag: 7V3HWGR32Z
kind: statement
role: theorem
name: Kakutani fixed-point theorem
msc: [47H10, 47H04, 54H25]
uses: [02AS45T3H9, 0R6EWFKRCF, 0ZCK8DQYN1]
about: [02AS45T3H9]
sources:
  - url: https://en.wikipedia.org/wiki/Kakutani_fixed-point_theorem
same_as:
  wikidata: Q518524
  wikipedia: Kakutani fixed-point theorem
---

## Statement

Let $n \ge 1$ and let $S \subseteq \R^n$ be a nonempty [[compact|0R6EWFKRCF]] [[convex set|02AS45T3H9]].
Let $\varphi$ be a set-valued map that assigns to each $x \in S$ a subset $\varphi(x) \subseteq S$, such that:

1. $\varphi(x)$ is nonempty and convex for every $x \in S$;
2. the graph $\set{(x, y) \in S \times S : y \in \varphi(x)}$ is a [[closed set|0ZCK8DQYN1]].

Then $\varphi$ has a fixed point: there is $x \in S$ with $x \in \varphi(x)$.

## Remarks

When each $\varphi(x)$ is a single point $f(x)$, the graph is closed exactly when $f$ is continuous, and the theorem becomes the Brouwer fixed-point theorem.
The usual proof approximates $\varphi$ by continuous maps on finer and finer triangulations of a simplex containing $S$.
It applies Brouwer's theorem to these maps and passes to a limit using the closed graph and the convex values.

Convex values are needed.
On $S = [0, 1]$, let $\varphi(x) = \set{1}$ for $x < 1/2$, $\varphi(1/2) = \set{0, 1}$ and $\varphi(x) = \set{0}$ for $x > 1/2$.
The graph is $[0, 1/2] \times \set{1} \cup [1/2, 1] \times \set{0}$, which is closed, but no $x$ lies in $\varphi(x)$; the value $\varphi(1/2)$ is not convex.

Example: consider a two-player game with mixed strategy sets $S_1$ and $S_2$, which are simplices.
Let $B_1(x_2) \subseteq S_1$ be the set of best replies of player 1 to the strategy $x_2$ of player 2, and define $B_2(x_1) \subseteq S_2$ in the same way.
On $S = S_1 \times S_2$, let $\varphi(x_1, x_2) = B_1(x_2) \times B_2(x_1)$.
Its values are nonempty and convex and its graph is closed, so it has a fixed point, which is a Nash equilibrium.

## Explanations

### L1 human

Brouwer's theorem is about a map that sends each point to one point.
Kakutani's theorem allows each point to be sent to a whole convex set of points, and still finds a point that lies in its own image.
This is what one needs when a choice is not unique, such as the best reply to an opponent's move in a game.

### L2 human

Nash used the theorem in his proof of the existence of equilibria in finite games, and it is basic in general equilibrium theory in economics.
The closed graph condition is a form of upper hemicontinuity, which is equivalent to it when the values are closed in a compact $S$.
The Kakutani–Glicksberg–Fan theorem extends the result to compact convex subsets of locally convex spaces, just as Schauder and Tychonoff extend Brouwer's theorem.
