---
tag: D08SKTH2T2
kind: example
name: Almost Mathieu operator
msc: [47B36, 81Q10, 47A10]
instance_of: [0NEGN5CRSC]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_Mathieu_operator
same_as:
  wikidata: Q4733975
  wikipedia: Almost Mathieu operator
---

## Example

Let $\lambda, \alpha, \theta$ be real numbers.
The *almost Mathieu operator* $H_{\lambda,\alpha,\theta}$ acts on the Hilbert space $\ell^2(\Z)$ of square-summable sequences $u = (u(n))_{n \in \Z}$ by
$$(H_{\lambda,\alpha,\theta}u)(n) = u(n + 1) + u(n - 1) + 2\lambda\cos\big(2\pi(n\alpha + \theta)\big)u(n).$$
It is a bounded [[self-adjoint operator|0NEGN5CRSC]].
Check: each of the three terms has norm at most $1$, $1$ and $2\abs{\lambda}$, so $\norm{H_{\lambda,\alpha,\theta}} \le 2 + 2\abs{\lambda}$.
The shifts $u(n) \mapsto u(n + 1)$ and $u(n) \mapsto u(n - 1)$ are adjoint to each other, so their sum is self-adjoint, and multiplication by a real sequence is self-adjoint.

## Remarks

The operator is a discrete [[Schrödinger operator|89AA6XJY5K]] with a quasi-periodic potential when $\alpha$ is irrational.
For irrational $\alpha$, its [[spectrum|BMKATJ802A]] does not depend on $\theta$.
Aubry duality relates the operators with coupling $\lambda$ and $1/\lambda$, and $\lambda = 1$ is the critical coupling.
For irrational $\alpha$, the Lebesgue measure of the spectrum is $\abs{4 - 4\abs{\lambda}}$; in particular it is zero at $\lambda = 1$.
The [[ten martini problem|3X4ZQ41PXG]] asked whether the spectrum is a Cantor set for all irrational $\alpha$ and all $\lambda \ne 0$; Avila and Jitomirskaya proved that it is.
Plotting the spectrum against $\alpha$ for $\lambda = 1$ gives Hofstadter's butterfly.

## Explanations

### L1 human

The operator models an electron hopping along a chain of atoms, one site to the next, with an energy at each site that varies like a cosine.
When $\alpha$ is irrational, the pattern of site energies never repeats exactly, but it comes close to repeating again and again.
This in-between situation, neither periodic nor random, gives a spectrum of remarkable fractal structure.
The operator is a test case for the spectral theory of quasi-periodic systems and also models electrons in a crystal under a magnetic field.
