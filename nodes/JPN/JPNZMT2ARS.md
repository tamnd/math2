---
tag: JPNZMT2ARS
kind: definition
name: Poincaré map
msc: [37C27, 34C25]
defines: 60TDCPY4Z4
uses: [07BNRFQ0PJ, 02903SSA48, 0AA97XA70K]
sources:
  - url: https://en.wikipedia.org/wiki/Poincaré_map
---

## Definition

Let $U$ be an open subset of $\R^n$ with $n \ge 2$ and let $f \colon U \to \R^n$ be continuously differentiable.
Let $\varphi$ be the [[flow|02903SSA48]] of the [[autonomous system|07BNRFQ0PJ]] $x' = f(x)$.
Let $\Gamma$ be a [[periodic orbit|0AA97XA70K]] of period $T > 0$ and let $x_0 \in \Gamma$.
Let $H$ be a hyperplane through $x_0$ that does not contain the direction $f(x_0)$.
A transversal section at $x_0$ is the intersection $\Sigma$ of $H$ with a small open ball around $x_0$.
Then there are an open neighbourhood $V$ of $x_0$ in $\Sigma$ and a continuously differentiable function $\tau \colon V \to (0, \infty)$ with $\tau(x_0) = T$.
For each $x \in V$, the time $\tau(x)$ is the first time near $T$ at which the solution through $x$ returns to $\Sigma$.
The Poincaré map of $\Gamma$ at $\Sigma$ is
$$P \colon V \to \Sigma, \qquad P(x) = \varphi_{\tau(x)}(x).$$

## Remarks

The existence of $\tau$ follows from the implicit function theorem, because $f(x_0)$ is not parallel to $\Sigma$.
The point $x_0$ is a fixed point of $P$, and fixed points of $P$ correspond to periodic orbits near $\Gamma$.
If the eigenvalues of the derivative $DP(x_0)$ all have absolute value less than $1$, the orbit $\Gamma$ attracts nearby solutions.
Example: in polar coordinates let $r' = r(1 - r^2)$ and $\theta' = 1$, with $\Gamma$ the unit circle and $\Sigma$ the positive $x$-axis near $(1, 0)$.
Every solution returns to $\Sigma$ after the time $2\pi$, and solving the equation for $r$ gives $P(r) = \left(1 + (r^{-2} - 1) e^{-4\pi}\right)^{-1/2}$.
Then $P(1) = 1$ and $P'(1) = e^{-4\pi} < 1$, so the circle is attracting.
Non-example: in the same system, the vertical line $x = 1$ near $(1, 0)$ does not give a transversal section at $(1, 0)$, since $f(1, 0) = (0, 1)$ points along that line.

## Explanations

### L1 human

The Poincaré map records where a solution crosses a fixed screen after one trip around a closed orbit.
It turns the study of the orbit into the study of a fixed point of one map.
