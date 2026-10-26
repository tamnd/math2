---
tag: 0EERDDPSVT
kind: definition
name: Limit cycle
msc: [34C07, 37C27]
defines: 0AAQ73WRFB
uses: [01DSNP0B4R, 02903SSA48, 05VDGH129F]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_cycle
    locator: Definition
---

## Definition

Let $U$ be an open subset of $\mathbb{R}^2$, let $f : U \to \mathbb{R}^2$ be continuously differentiable, and let $\varphi$ be the [[flow|02903SSA48]] of $x' = f(x)$.
Let $y \in U$ be a point whose solution exists for all $t \ge 0$. Its $\omega$-limit set $\omega(y)$ is the set of points $z \in U$ such that $\varphi_{t_k}(y) \to z$ for some sequence $t_k \to \infty$.
For a point $y$ whose solution exists for all $t \le 0$, the $\alpha$-limit set $\alpha(y)$ is defined in the same way with $t_k \to -\infty$.
A limit cycle is a [[periodic orbit|01DSNP0B4R]] $\Gamma$ such that $\Gamma = \omega(y)$ or $\Gamma = \alpha(y)$ for some point $y \in U$ that is not on $\Gamma$.

## Remarks

A limit cycle is stable if all nearby trajectories approach it as $t \to \infty$, and unstable if they approach it as $t \to -\infty$. It can also be semi-stable.
A linear system has no limit cycles: its periodic orbits, if any, fill a region around the origin.
The van der Pol oscillator $x'' - \mu (1 - x^2) x' + x = 0$ with $\mu > 0$ has exactly one limit cycle, and it is stable.
The [[Poincaré–Bendixson theorem|0EW1X61ZT1]] is a main tool to prove that a limit cycle exists.

## Explanations

### L1 human

A limit cycle is an isolated loop in the phase plane that nearby motions spiral toward or away from.
It models a self-sustained oscillation, such as a heartbeat, whose size does not depend on the initial state.
