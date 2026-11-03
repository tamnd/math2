---
tag: S96K5EDPPG
kind: definition
name: Mean free path
msc: [82C40, 76P05]
defines: M0J697D782
uses: [0WQNRCNY3M, 0MTNR28K60, 0E99F51GVB]
sources:
  - url: https://en.wikipedia.org/wiki/Mean_free_path
---

## Definition

Consider a particle that moves along straight lines between collisions.
The *free path* of the particle is the distance it travels from a given time to its next collision.
Its *mean free path* is the [[expected value|0WQNRCNY3M]] of the free path.
In the standard model, the particle starts at the origin and moves in a fixed direction among fixed obstacles.
The centres of the obstacles form a [[Poisson point process|0MTNR28K60]] in $\R^3$ of intensity $n > 0$.
A collision occurs when the centre of an obstacle comes within distance $d > 0$ of the particle, so that the *collision cross-section* is $\sigma = \pi d^2$.
The process is conditioned to have no centre at distance less than $d$ from the origin.
In this model the mean free path is
$$\lambda = \frac{1}{n \sigma}.$$

## Remarks

Derivation: the particle travels a distance greater than $\ell$ without collision exactly when no obstacle centre lies within distance $d$ of the first $\ell$ units of its path.
The set of these points, minus the ball of radius $d$ around the origin, has volume $\pi d^2 \ell = \sigma \ell$.
For a Poisson point process, conditioned on the ball being empty, this has probability $e^{-n \sigma \ell}$.
So the free path has the [[exponential distribution|0E99F51GVB]] with rate $n\sigma$, and its mean is $1/(n\sigma)$.

Example: for hard-sphere molecules of diameter $d$, two molecules collide when their centres are at distance $d$, so $\sigma = \pi d^2$ and $\lambda = 1/(\pi n d^2)$ for a particle moving among fixed molecules.

Non-example: if the obstacles are not fixed but move with the Maxwell distribution of a gas in equilibrium, the formula $1/(n\sigma)$ is not exact.
The relative speeds change the collision rate, and the standard result is $\lambda = 1/(\sqrt 2 \, n \sigma)$.

In the Boltzmann–Grad limit of $N$ hard spheres of diameter $\varepsilon$, the condition $N \varepsilon^2 = 1$ keeps the mean free path of order $1$.
