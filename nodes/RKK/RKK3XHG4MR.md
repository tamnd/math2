---
tag: RKK3XHG4MR
kind: statement
role: theorem
name: Dirichlet's principle
msc: [31B20, 35J25, 35A15]
uses: [YG3W8CBB3E, 0DEB0JMN0W, 02BH3MCBQB, 05D5EGMFYV, 0X3WGX95FE]
about: [YG3W8CBB3E, 8D56GQ4AG8]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet%27s_principle
same_as:
  wikidata: Q975727
  wikipedia: Dirichlet's principle
---

## Statement

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be a bounded [[open set|02BH3MCBQB]] with $C^1$ [[boundary|05D5EGMFYV]], and let $g$ be a [[continuous function|0X3WGX95FE]] on $\partial\Omega$.
Let $\mathcal{A}$ be the set of functions $w$ that are twice continuously differentiable on $\overline{\Omega}$ with $w = g$ on $\partial\Omega$.
Let $E[w] = \frac12 \int_\Omega \abs{\nabla w}^2 \, dx$ be the [[Dirichlet energy|YG3W8CBB3E]].
For $u \in \mathcal{A}$, the following are equivalent:

1. $u$ is [[harmonic|0DEB0JMN0W]] on $\Omega$.
2. $E[u] \le E[w]$ for every $w \in \mathcal{A}$.

## Remarks

Proof idea: for $w \in \mathcal{A}$ put $v = w - u$, which vanishes on $\partial\Omega$.
Then $E[w] = E[u] + \int_\Omega \nabla u \cdot \nabla v \, dx + E[v]$, and integration by parts gives $\int_\Omega \nabla u \cdot \nabla v \, dx = -\int_\Omega v \, \Delta u \, dx$.
If $u$ is harmonic, the middle term is $0$, so $E[w] \ge E[u]$.
If $u$ minimizes, the derivative of $t \mapsto E[u + tv]$ at $t = 0$ is $0$ for all such $v$, which forces $\Delta u = 0$.
The theorem does not say that a minimizer exists in $\mathcal{A}$; Weierstrass pointed out that this needs proof, and it was later justified by Hilbert.
Existence can fail even for continuous $g$: on the unit disc, $g(\theta) = \sum_{k \ge 1} k^{-2} \cos(2^k \theta)$ is continuous, but its harmonic extension $\sum_k k^{-2} r^{2^k} \cos(2^k\theta)$ has energy $\frac{\pi}{2}\sum_k 2^k k^{-4} = \infty$.

## Explanations

### L1 human

Among all ways to fill in a function with given boundary values, the harmonic one is the least wiggly.
It has the smallest Dirichlet energy.
This is why a soap film or a stretched membrane with a fixed rim takes the shape of a harmonic function, for small slopes.

### L2 human

Dirichlet's principle turns the [[Dirichlet problem|8D56GQ4AG8]] into a minimization problem.
In modern form, one minimizes the energy over the Sobolev space $H^1$ with given trace.
The minimizer exists by the Hilbert space projection theorem, and it is a weak solution of Laplace's equation.
Elliptic regularity then shows that the weak solution is a classical harmonic function.
The same variational idea gives existence for many other elliptic equations.
