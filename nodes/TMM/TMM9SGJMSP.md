---
tag: TMM9SGJMSP
kind: definition
name: Bifurcation in a family of maps
msc: [39A28, 37G15, "37E05"]
defines: EE9X3NZW81
uses: [5AA9AJEARJ, HNXXAPQKG3, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Bifurcation_theory
---

## Definition

Let $X \subseteq \R^k$, let $I \subseteq \R$ be an open interval, and let $f_\mu \colon X \to X$, $\mu \in I$, be a family of maps such that $(\mu, x) \mapsto f_\mu(x)$ is [[continuous|0X3WGX95FE]].
A parameter $\mu_0 \in I$ is a *bifurcation value* of the family if the following holds.
Every open interval $J \ni \mu_0$ contains some $\mu$ such that $f_\mu$ is not [[topologically conjugate|HNXXAPQKG3]] to $f_{\mu_0}$.
One then says that the family, or the difference equation $x_{n+1} = f_\mu(x_n)$, undergoes a *bifurcation* at $\mu_0$.

## Remarks

Example: for $f_\mu(x) = \mu x$ on $\R$ with $\mu \in (0, \infty)$, the value $\mu_0 = 1$ is a bifurcation value.
The map $f_1$ is the identity, so every point is fixed, while for $\mu \ne 1$ the only fixed point is $0$.
A conjugacy maps fixed points bijectively to fixed points, so $f_\mu$ is not conjugate to $f_1$.

Non-example: in the same family, $\mu_0 = 1/2$ is not a bifurcation value.
For $0 < a, b < 1$ the homeomorphism $h(x) = \sgn(x) \abs{x}^{\ln b / \ln a}$ satisfies $h(a x) = b\, h(x)$, so all $f_\mu$ with $\mu \in (0, 1)$ are conjugate to each other.

Many texts use a local version, in which only the behaviour near a fixed point or a periodic orbit is compared.
A local bifurcation of a fixed point $x^*$ of a smooth family can only occur when an eigenvalue of $D f_{\mu_0}(x^*)$ lies on the unit circle.
For one-dimensional maps this means $f_{\mu_0}'(x^*) = 1$ or $f_{\mu_0}'(x^*) = -1$.
