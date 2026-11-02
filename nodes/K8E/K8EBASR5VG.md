---
tag: K8EBASR5VG
kind: problem
name: Optimal transport and the Monge problem
msc: [49Q22, 35J96, 60A10]
uses: [059TJN0NZ1, 3N66TM3TSQ, B91V9BKZMR, 14AKAC0S0T, VEY29CS26X]
about: [059TJN0NZ1, 3N66TM3TSQ]
sources:
  - url: https://en.wikipedia.org/wiki/Transportation_theory_(mathematics)
same_as:
  wikidata: Q1929885
  wikipedia: Transportation theory (mathematics)
history:
  posed_by: "Gaspard Monge"
  first_stated: "1781"
---

## Problem

Let $X$ and $Y$ be complete separable metric spaces.
Let $\mu$ be a [[Borel|B91V9BKZMR]] [[probability measure|059TJN0NZ1]] on $X$ and $\nu$ a Borel probability measure on $Y$.
Let $c \colon X \times Y \to [0, \infty]$ be a lower semicontinuous cost function.

1. Monge problem: minimize $\int_X c(x, T(x)) \, d\mu(x)$ over all Borel maps $T \colon X \to Y$ with $T_\# \mu = \nu$, where $T_\# \mu$ is the [[pushforward measure|3N66TM3TSQ]] $T_\#\mu(B) = \mu(T^{-1}(B))$.
2. Kantorovich problem: minimize $\int_{X \times Y} c \, d\pi$ over all transport plans, the Borel probability measures $\pi$ on $X \times Y$ with marginals $\mu$ and $\nu$.

Decide when minimizers exist, when they are unique, and when an optimal plan is given by a map.

## Remarks

Monge posed the problem in 1781, in his memoir on cuttings and fillings, for the cost $c(x, y) = \abs{x - y}$ in $\R^3$.
His aim was to move a pile of soil into a hole of the same volume with least total work.
The Monge problem may have no admissible map at all: if $\mu$ is a Dirac mass and $\nu$ is not, no $T$ satisfies $T_\#\mu = \nu$.
Kantorovich introduced the relaxed problem in 1942; under the hypotheses above it always has a minimizer, by weak compactness of the set of plans and lower semicontinuity of the cost.
For $X = Y = \R^n$, $c(x, y) = \abs{x - y}^2$, $\mu$ absolutely continuous and both measures with finite second moments, Brenier's theorem gives a unique optimal plan, induced by the map $T = \nabla \varphi$ for a convex function $\varphi$.
Then $\varphi$ solves a [[Monge–Ampère equation|14AKAC0S0T]] in a weak sense, and the optimal cost defines the squared [[Wasserstein distance|VEY29CS26X]] $W_2(\mu, \nu)^2$.
For Monge's original cost $\abs{x - y}$ in $\R^n$ with $\mu$ absolutely continuous and both measures with finite first moments, optimal maps exist but are in general not unique.
Evans and Gangbo proved existence under extra hypotheses in 1999, and later work removed them.

## Explanations

### L1 human

You have a pile of sand and a hole of the same volume, and you want to fill the hole while moving the sand as little as possible in total.
Monge asked for the best way to decide where each grain goes.
Kantorovich allowed each grain to be split among several destinations, which makes the problem much easier to solve.
Today optimal transport gives a way to measure distances between probability distributions, with uses in geometry, PDE, economics and machine learning.
