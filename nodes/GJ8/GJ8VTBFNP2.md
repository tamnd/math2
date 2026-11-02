---
tag: GJ8VTBFNP2
kind: statement
role: theorem
name: von Neumann's minimax theorem
msc: [91A05, 49J35, 90C47]
uses: [YX1DJK2QAG]
sources:
  - url: https://en.wikipedia.org/wiki/Minimax_theorem
    locator: Bilinear functions and zero-sum games
---

## Statement

Let $A$ be a real $m \times n$ matrix.
For $k \ge 1$ let $\Delta_k = \set{p \in \R^k : p_i \ge 0 \text{ for all } i, \ p_1 + \cdots + p_k = 1}$ be the standard [[simplex|YX1DJK2QAG]] of probability vectors.
Then
$$\max_{x \in \Delta_m} \min_{y \in \Delta_n} x^T A y = \min_{y \in \Delta_n} \max_{x \in \Delta_m} x^T A y.$$

## Remarks

The inequality $\max_x \min_y \le \min_y \max_x$ holds for every function on a product.
The reverse inequality is the content of the theorem.
One proof writes both sides as linear programs that are dual to each other, and uses the strong duality theorem of linear programming.
Another proof separates a convex set from a point with a hyperplane.
The common value is the *value* of the game, and the theorem says that $x^T A y$ has a saddle point on $\Delta_m \times \Delta_n$.

Example: matching pennies, with $A = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$.
For $x = y = (\tfrac12, \tfrac12)$ one gets $x^T A y' = 0$ for every $y'$ and $x'^T A y = 0$ for every $x'$, so the value is $0$.
Mixing is necessary: over pure strategies, that is vertices of the simplices, the row player can only guarantee $\max_i \min_j a_{ij} = -1$, while $\min_j \max_i a_{ij} = 1$.

The theorem extends to a continuous function $f(x, y)$ on $X \times Y$ with $X, Y$ compact convex sets in $\R^m$ and $\R^n$, concave in $x$ and convex in $y$.
Sion's minimax theorem weakens these hypotheses further.

## Explanations

### L1 human

In a two-player zero-sum game, one player's gain is the other's loss.
If the players may randomize, it does not matter who has to announce a strategy first.
The best guaranteed payoff of the first player equals the smallest loss the second player can guarantee.
This common number is the value of the game.

### L2 human

The theorem is the founding result of game theory, proved by John von Neumann in 1928.
It is equivalent to the duality theorem of linear programming, and the value and optimal mixed strategies of a matrix game can be computed by the simplex algorithm.
The general minimax theorems for convex-concave functions, and Sion's version for quasiconvex-quasiconcave functions, all rest on the same convexity.
They are the model for saddle point formulations of duality in convex optimization, such as saddle points of a Lagrangian.
