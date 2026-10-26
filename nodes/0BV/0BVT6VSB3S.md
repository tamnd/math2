---
tag: 0BVT6VSB3S
kind: definition
name: Trajectory
msc: [37C10, 34C05]
defines: 07TZ2Q4C1M
uses: [07BNRFQ0PJ, 02903SSA48]
sources:
  - url: https://en.wikipedia.org/wiki/Orbit_(dynamics)
    locator: Definition
---

## Definition

Let $U$ be an open subset of $\mathbb{R}^n$ and let $f : U \to \mathbb{R}^n$ be locally Lipschitz. Let $\varphi$ be the [[flow|02903SSA48]] of the [[autonomous system|07BNRFQ0PJ]] $x' = f(x)$.
Let $x_0 \in U$, and let $I(x_0)$ be the maximal interval of existence of the solution with $x(0) = x_0$.
The trajectory, or orbit, of $x_0$ is the set
$$\mathcal{O}(x_0) = \{\varphi_t(x_0) : t \in I(x_0)\} \subseteq U.$$
The positive half-trajectory is $\mathcal{O}^+(x_0) = \{\varphi_t(x_0) : t \in I(x_0),\ t \ge 0\}$, and the negative half-trajectory uses $t \le 0$.

## Remarks

Two trajectories are either equal or disjoint. So the trajectories form a partition of $U$.
A trajectory is a single point exactly when $x_0$ is an [[equilibrium point|0G4X36AE0X]]. It is a closed curve when the solution is [[periodic|01DSNP0B4R]] and not constant.
Some books use the word trajectory for the solution curve $t \mapsto \varphi_t(x_0)$ itself, and the word orbit for its image.

## Explanations

### L1 human

The trajectory is the path that the state follows in the phase space.
It forgets the time: it records where the state goes, not when.
