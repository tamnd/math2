---
tag: HVT4QVHRTF
kind: statement
role: theorem
name: Kronecker's approximation theorem
msc: [11J13, 11J71]
uses: [080T2TXVQV, 0EVHJFTG9Z, 0D198GPMTJ, 08GR54CKEA, 04JAY9DGB7, NCCGNTBEYV]
about: [0BSJSX7ME2]
sources:
  - url: https://en.wikipedia.org/wiki/Kronecker%27s_theorem
---

## Statement

For a real number $x$, let $\{x\} = x - \floor{x}$ be its fractional part, where $\floor{x}$ is the [[floor|08GR54CKEA]] of $x$.
Let $k \ge 1$ and let $\theta_1, \ldots, \theta_k$ be real numbers such that $1, \theta_1, \ldots, \theta_k$ are [[linearly independent|0EVHJFTG9Z]] over $\Q$.
Then the set
$$\set{(\{n\theta_1\}, \ldots, \{n\theta_k\}) : n \ge 1 \text{ an integer}}$$
is [[dense|0D198GPMTJ]] in $[0, 1]^k$.
For $k = 1$: if $\theta$ is an [[irrational number|080T2TXVQV]], then the fractional parts $\{n\theta\}$, $n \ge 1$, are dense in $[0, 1]$.

## Remarks

For $k = 1$, fix $\varepsilon > 0$.
The pigeonhole principle, as in [[Dirichlet's approximation theorem|04JAY9DGB7]], gives an $m \ge 1$ with $0 < \{m\theta\} < \varepsilon$ or $1 - \varepsilon < \{m\theta\} < 1$.
The value $\{m\theta\}$ is never $0$, since $\theta$ is irrational.
The multiples of $m$ then move around the circle in steps shorter than $\varepsilon$, so they come within $\varepsilon$ of every point.
In general dimension, the theorem follows from the $k$-dimensional form of Weyl's criterion, which gives even equidistribution in $[0,1]^k$.
The independence hypothesis is necessary.
Suppose $a_0 + a_1 \theta_1 + \cdots + a_k \theta_k = 0$ with integers $a_i$ not all $0$; then some $a_i$ with $i \ge 1$ is nonzero.
All points then satisfy $a_1 \{n\theta_1\} + \cdots + a_k \{n\theta_k\} \in \Z$, so they lie on finitely many hyperplanes and are not dense.
Example: $1, \sqrt{2}, \sqrt{3}$ are linearly independent over $\Q$, so the points $(\{n\sqrt{2}\}, \{n\sqrt{3}\})$ are dense in the unit square.

## Explanations

### L1 human

Walk around a circle of length $1$ in steps of an irrational length $\theta$.
You never come back to the start, and in the long run you pass as close as you like to every point of the circle.
Kronecker's theorem says the same for several walks at once, as long as the step lengths have no rational relation between them.

### L2 human

The theorem is the qualitative form of the [[equidistribution theorem|NCCGNTBEYV]] and its higher-dimensional versions.
It is a statement about the orbit of a rotation of the torus $\R^k / \Z^k$: under the independence condition, the orbit of $0$ is dense.
Its higher-dimensional form is used in dynamics and in the theory of almost periodic functions.
