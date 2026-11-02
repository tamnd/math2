---
tag: MBF660WMYJ
kind: statement
role: theorem
name: Duality of Lp spaces
msc: ["46E30", 46B10]
uses: [SASP14MA1Z, P15VQS5DJ9, WEBBT18D4X, 4A82S5FVRT, 07SJXTWVQW, JQ9WXC729D]
about: [SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Lp_space
  - url: https://en.wikipedia.org/wiki/Riesz_representation_theorem
---

## Statement

Let $(\Omega, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]] and let $1 \le p < \infty$.
Let $L^p(\mu)$ be the [[Lp space|SASP14MA1Z]] of real or complex functions.
Let $q$ be the conjugate exponent, with $1/p + 1/q = 1$ and $q = \infty$ when $p = 1$.
For $g \in L^q(\mu)$, let $\Phi(g)$ be the functional $f \mapsto \int_\Omega f g \, d\mu$ on $L^p(\mu)$.

1. If $1 < p < \infty$, then $\Phi$ is a [[linear isometry|07SJXTWVQW]] of $L^q(\mu)$ onto the [[continuous dual|4A82S5FVRT]] of $L^p(\mu)$.
2. If $p = 1$ and $\mu$ is [[σ-finite|WEBBT18D4X]], then $\Phi$ is a linear isometry of $L^\infty(\mu)$ onto the continuous dual of $L^1(\mu)$.

## Remarks

By [[Hölder's inequality|JQ9WXC729D]], $\abs{\Phi(g)(f)} \le \norm{f}_p \norm{g}_q$, so $\Phi(g)$ is bounded with norm at most $\norm{g}_q$.
The test function $f = \abs{g}^{q-1} \overline{\sgn g}$ gives equality when $1 < p < \infty$.
Surjectivity is the hard part: for σ-finite $\mu$ it follows from the Radon–Nikodym theorem, and for $1 < p < \infty$ uniform convexity of $L^p$ removes the σ-finiteness.

For counting measure on $\N$, the theorem says that the dual of $\ell^p$ is $\ell^q$, and the dual of $\ell^1$ is $\ell^\infty$.
The case $p = \infty$ is excluded: the dual of $\ell^\infty$ is strictly larger than $\ell^1$.
For example, a Banach limit is a bounded functional on $\ell^\infty$ that is not given by any sequence in $\ell^1$.
For $p = 1$, the σ-finite hypothesis cannot be dropped in general.

## Explanations

### L1 human

Every continuous linear way to turn an $L^p$ function into a number is integration against a fixed function from $L^q$.
That function is unique, and its size is exactly the size of the functional.
This turns abstract functionals into concrete functions.

### L2 human

The theorem shows that $L^p$ is reflexive for $1 < p < \infty$, since the dual of $L^q$ is again $L^p$.
In the case $p = 2$ it is a special case of the Riesz representation theorem for Hilbert spaces.
It is used to identify weak limits, to define weak solutions of equations and to prove inequalities by duality, where one computes $\norm{f}_p$ as a supremum of $\abs{\int f g}$ over $\norm{g}_q \le 1$.
