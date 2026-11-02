---
tag: QREYWGEH41
kind: definition
name: Lyapunov exponent
msc: [34D08, 34A30]
defines: NJ1FJSNK6A
uses: [037ZNY7NAG, 07VX34QXAV, 0T3RZQXDYD, 0V2WP9B1MF]
sources:
  - url: https://en.wikipedia.org/wiki/Lyapunov_exponent
---

## Definition

Let $I = [t_0, \infty)$ and let $A \colon I \to \R^{n \times n}$ be continuous.
Consider the [[linear system|037ZNY7NAG]] $x' = A(t) x$, and fix a [[norm|0V2WP9B1MF]] $\norm{\cdot}$ on $\R^n$.
Let $x$ be a nonzero [[solution|07VX34QXAV]] of this system on $I$.
The *Lyapunov exponent* (or characteristic exponent) of $x$ is
$$\lambda(x) = \limsup_{t \to \infty} \frac{1}{t} \ln \norm{x(t)} \in [-\infty, \infty],$$
where $\limsup$ is the [[limit superior|0T3RZQXDYD]].

## Remarks

The value does not depend on the choice of norm, because any two norms on $\R^n$ are within constant factors of each other.
A nonzero solution never vanishes, by uniqueness of solutions, so the logarithm is defined for all $t$.
If $A$ is bounded on $I$, then every exponent is finite.

Example: for constant $A$ with an eigenvalue $\mu$ and eigenvector $v$, the solution $x(t) = e^{\mu t} v$ satisfies $\norm{x(t)} = e^{(\operatorname{Re} \mu) t} \norm{v}$.
So $\frac{1}{t} \ln \norm{x(t)} = \operatorname{Re} \mu + \frac{1}{t} \ln \norm{v} \to \operatorname{Re} \mu$, and $\lambda(x) = \operatorname{Re} \mu$.

Non-example: the zero solution has no Lyapunov exponent in this sense, since $\ln \norm{0}$ is undefined; some authors set it to $-\infty$.

For a nonlinear system $x' = f(x)$ with $f$ of class $C^1$, the exponents along a trajectory are those of the variational equation $y' = Df(x(t))\, y$.
The largest of them measures the rate of separation of nearby trajectories.
