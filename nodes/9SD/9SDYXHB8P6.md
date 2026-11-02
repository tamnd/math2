---
tag: 9SDYXHB8P6
kind: definition
name: Brelot space
msc: [31D05]
defines: A51SQRPM5T
uses: [DWN0XEQHHK, 0FE2SB8WVJ, TB6TM6R4MD, 0X3WGX95FE, P15K8RKHDV, VP2HN86VAG, KD404MF042]
sources:
  - url: https://en.wikipedia.org/wiki/Potential_theory
---

## Definition

Let $X$ be a connected, locally connected, [[locally compact|0FE2SB8WVJ]] Hausdorff space.
Let $\mathcal{H}$ assign to each open $U \subseteq X$ a linear subspace $\mathcal{H}(U)$ of the real [[continuous functions|0X3WGX95FE]] on $U$.
Call an open set *regular* as in a [[harmonic space|DWN0XEQHHK]].
The pair $(X, \mathcal{H})$ is a *Brelot space* if:

1. $\mathcal{H}$ is a [[sheaf|TB6TM6R4MD]] of functions.
2. The regular domains, that is, the connected regular open sets, form a base of the topology of $X$.
3. Let $U \subseteq X$ be a domain and $(h_n)$ an increasing sequence in $\mathcal{H}(U)$. Then $\lim_n h_n$ either lies in $\mathcal{H}(U)$ or is $+\infty$ at every point of $U$.

## Remarks

Clause 3 implies the convergence axiom of a harmonic space: a locally bounded limit cannot be identically $+\infty$ on any component.
Example: $\R^n$ with the classical harmonic functions is a Brelot space.
Balls are regular domains, by the Poisson integral, and clause 3 is [[Harnack's principle|P15K8RKHDV]].
Non-example: $\R \times \R$ with the solutions of the [[heat equation|VP2HN86VAG]] $\partial_t u = \partial_x^2 u$ fails clause 3.
Let $\Phi(x, t) = (4\pi t)^{-1/2} e^{-x^2/(4t)}$ for $t > 0$ and $\Phi(x, t) = 0$ for $t \le 0$, the [[heat kernel|KD404MF042]] extended by $0$.
It solves the heat equation on the domain $U = \R^2 \setminus \set{(0, 0)}$, and $h_n = n \Phi$ increases to $+\infty$ where $t > 0$ and to $0$ where $t \le 0$.
The limit is neither a solution on $U$ nor identically $+\infty$.
