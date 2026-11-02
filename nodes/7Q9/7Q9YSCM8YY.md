---
tag: 7Q9YSCM8YY
kind: definition
name: Weak lower semicontinuity
msc: [49J45, "58E30"]
defines: H6GTJRG26G
uses: [06GZ956657, P6KHVSTPZV, RN4G8SGP6P, 1EQM0DJ4NC]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_method_in_the_calculus_of_variations
---

## Definition

Let $X$ be a real [[Banach space|06GZ956657]] and let $J \colon X \to (-\infty, +\infty]$ be a [[functional|1EQM0DJ4NC]].
A sequence $(u_k)$ in $X$ converges *weakly* to $u$ if $\ell(u_k) \to \ell(u)$ for every continuous linear functional $\ell$ on $X$.
The functional $J$ is *sequentially weakly lower semicontinuous* if
$$J(u) \le \liminf_{k \to \infty} J(u_k)$$
for every $u \in X$ and every sequence $(u_k)$ that converges weakly to $u$.

## Remarks

Replacing sequences by the [[weak topology|P6KHVSTPZV]] itself gives weak lower [[semicontinuity|RN4G8SGP6P]] in the topological sense, which implies the sequential form.
In the calculus of variations the sequential form is the one that is used.

Example: the norm $J(u) = \norm{u}$ is weakly lower semicontinuous.
By the Hahn–Banach theorem $\norm{u} = \sup \abs{\ell(u)}$ over continuous linear $\ell$ with $\norm{\ell} \le 1$.
For each such $\ell$, $\abs{\ell(u)} = \lim_k \abs{\ell(u_k)} \le \liminf_k \norm{u_k}$.

Non-example: on $X = L^2(0, 2\pi)$ let $J(u) = -\norm{u}^2$ and $u_k(x) = \sin(kx)$.
Then $u_k \to 0$ weakly, by the Riemann–Lebesgue lemma, and $J(u_k) = -\pi$ for all $k$.
But $J(0) = 0 > -\pi$, so $J$ is not weakly lower semicontinuous, although it is continuous for the norm.

By Mazur's lemma, a convex functional that is lower semicontinuous for the norm is weakly lower semicontinuous.
