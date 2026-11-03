---
tag: NY83V7S6VP
kind: problem
name: Lambert's problem
msc: [70F05, 70M20]
uses: [BXFSBB8Q46, TYXD1T6FRX]
about: [BXFSBB8Q46]
sources:
  - url: https://en.wikipedia.org/wiki/Lambert%27s_problem
same_as:
  wikidata: Q6481210
  wikipedia: Lambert's problem
history:
  posed_by: "Johann Heinrich Lambert"
  first_stated: "1761"
---

## Problem

Let $\mu > 0$, let $r_1, r_2 \in \R^3 \setminus \set{0}$ be two positions that are not on a common line through $0$, and let $\Delta t > 0$.
Find the [[Kepler orbits|BXFSBB8Q46]] with gravitational parameter $\mu$ that go from $r_1$ to $r_2$ in time $\Delta t$.
That is, find the velocities $v_1$ such that the solution of the [[Kepler problem|TYXD1T6FRX]] $r'' = -\mu\, r / \norm{r}^3$ with $r(0) = r_1$ and $r'(0) = v_1$ satisfies $r(\Delta t) = r_2$.

## Remarks

Lambert's theorem states that the time of flight depends only on the semi-major axis $a$ of the orbit, on the sum $\norm{r_1} + \norm{r_2}$ and on the chord $\norm{r_2 - r_1}$.
This reduces the problem to one scalar equation for $a$, or for a related variable.
For a fixed direction of motion and a transfer of less than one revolution, the problem has exactly one solution.
For longer times of flight there are also solutions that make one or more full revolutions first.
The problem is the core of the planning of interplanetary trajectories and of rendezvous, and of the determination of an orbit from two positions.
Practical solvers use universal variables and Newton-type iterations.

## Explanations

### L1 human

Lambert's problem asks: to get from here to there in exactly this much time, coasting under gravity, how fast and in which direction must one start?
It is a boundary value problem, because the start and the end are fixed, not the start and the initial velocity.
Mission planners solve it many times to draw charts of launch dates and arrival dates.
