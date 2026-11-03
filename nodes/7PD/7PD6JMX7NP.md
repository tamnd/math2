---
tag: 7PD6JMX7NP
kind: definition
name: Parametric programming
msc: [90C31]
defines: 2WBKEY0778
uses: [NS0Q42Y3FX, 1TTKMRW8PD, VNMXB0J2KA]
sources:
  - url: https://en.wikipedia.org/wiki/Parametric_programming
---

## Definition

Let $\Theta \subseteq \R^k$ be a set of parameters.
For each $\theta \in \Theta$ let $X(\theta) \subseteq \R^n$ be a [[feasible region|1TTKMRW8PD]] and let $f(\cdot, \theta) \colon \R^n \to \R$ be an objective function.
A *parametric program* is the family of [[optimization problems|NS0Q42Y3FX]]
$$z(\theta) = \inf \set{f(x, \theta) : x \in X(\theta)}, \qquad \theta \in \Theta.$$
The function $z$ is the *optimal value function*, and the set-valued map $\theta \mapsto \set{x \in X(\theta) : f(x, \theta) = z(\theta)}$ is the *optimal solution map*.
*Parametric programming* is the task of computing $z$ and the optimal solution map, or one optimal solution for each $\theta$, as explicit functions of $\theta$.

## Remarks

Example: a multiparametric [[linear program|VNMXB0J2KA]] has the form
$$z(\theta) = \min \set{c^T x : A x \le b + F \theta}$$
with a matrix $F$.
The set of $\theta$ for which this program is feasible is a convex polyhedron.
On the part of it where $z(\theta)$ is finite, $z$ is convex and piecewise affine.
For instance $z(\theta) = \min \set{x : -x \le 0, \ -x \le -\theta}$ equals $\max(0, \theta)$.

Non-example: solving the program $\min \set{c^T x : A x \le b}$ for one fixed vector $b$ is ordinary linear programming, not parametric programming, since no parameter varies.

When the parameter is a single real number, one speaks of *one-parameter* or *uniparametric* programming; with several, of *multiparametric* programming.
