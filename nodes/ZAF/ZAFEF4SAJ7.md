---
tag: ZAFEF4SAJ7
kind: definition
name: Singular perturbation
msc: ["34E15", 34D15]
defines: G6J21TGRMM
uses: [0NT64JV96A, TM8VQJWGHZ]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_perturbation
---

## Definition

Let $D$ be a set and let $\varepsilon_0 > 0$.
For each $\varepsilon \in (0, \varepsilon_0)$, let $P_\varepsilon$ be a problem on $D$, such as a [[boundary value problem|TM8VQJWGHZ]] for an [[ordinary differential equation|0NT64JV96A]].
Assume that the data of $P_\varepsilon$ have a limit $P_0$ as $\varepsilon \to 0$.
The problem $P_0$ is the *reduced problem*.
Let $u_\varepsilon \colon D \to \R^n$ be a solution of $P_\varepsilon$.
The family is a *regular perturbation* of $P_0$ if $P_0$ has a solution $u_0$ and $u_\varepsilon \to u_0$ uniformly on $D$ as $\varepsilon \to 0$.
The family is a *singular perturbation* if it is not a regular perturbation.
This means that $P_0$ has no solution, or that $u_\varepsilon$ does not converge uniformly on $D$ to a solution of $P_0$.

## Remarks

Example: $P_\varepsilon$ is $\varepsilon y'' + y' = 0$ on $D = [0, 1]$ with $y(0) = 0$ and $y(1) = 1$.
The solution is $y_\varepsilon(x) = (1 - e^{-x/\varepsilon}) / (1 - e^{-1/\varepsilon})$.
The reduced problem $y' = 0$, $y(0) = 0$, $y(1) = 1$ has no solution.
Indeed $y_\varepsilon(x) \to 1$ for each $x \in (0, 1]$ while $y_\varepsilon(0) = 0$, so the convergence is not uniform.

Non-example: $y' = -y + \varepsilon$ on $[0, 1]$ with $y(0) = 1$.
The solution $y_\varepsilon(x) = \varepsilon + (1 - \varepsilon) e^{-x}$ converges uniformly to $e^{-x}$, the solution of the reduced problem, so the perturbation is regular.

A small parameter multiplying the highest derivative usually makes the problem singular.
Singular problems are treated by the method of matched asymptotic expansions and the method of multiple scales.

## Explanations

### L1 human

A perturbation is regular when the solution at $\varepsilon = 0$ is a good approximation everywhere.
It is singular when this fails somewhere, often near the boundary.
