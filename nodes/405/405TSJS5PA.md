---
tag: 405TSJS5PA
kind: definition
name: Bloch space
msc: [30H30]
defines: F6M8ME0DQR
uses: [0NAHXR1FRH, 06GZ956657, 8G5ABXRK85]
sources:
  - url: https://en.wikipedia.org/wiki/Bloch_space
---

## Definition

Let $\mathbb{D} = \set{z \in \C : \abs{z} < 1}$ be the [[unit disc|8G5ABXRK85]].
The *Bloch space* $\mathcal{B}$ is the set of [[holomorphic functions|0NAHXR1FRH]] $f \colon \mathbb{D} \to \C$ such that
$$\sup_{z \in \mathbb{D}} (1 - \abs{z}^2) \abs{f'(z)} < \infty.$$
Its norm is $\norm{f}_{\mathcal{B}} = \abs{f(0)} + \sup_{z \in \mathbb{D}} (1 - \abs{z}^2) \abs{f'(z)}$.

## Remarks

With this norm, $\mathcal{B}$ is a [[Banach space|06GZ956657]].
Example: let $f(z) = \log(1 - z)$ with the principal branch, so $f'(z) = -1/(1 - z)$.
Since $\abs{1 - z} \ge 1 - \abs{z}$, one has $(1 - \abs{z}^2)\abs{f'(z)} \le (1 - \abs{z})(1 + \abs{z})/(1 - \abs{z}) < 2$, so $f \in \mathcal{B}$, although $f$ is unbounded.
Non-example: $g(z) = 1/(1 - z)$ has $g'(z) = 1/(1 - z)^2$, and for real $z = r \in (0, 1)$ one gets $(1 - r^2)/(1 - r)^2 = (1 + r)/(1 - r) \to \infty$, so $g \notin \mathcal{B}$.
Every bounded holomorphic function is in $\mathcal{B}$: if $\abs{f} \le 1$, the [[Schwarz–Pick theorem|V1QYA9RW73]] gives $(1 - \abs{z}^2)\abs{f'(z)} \le 1$.
The closure of the polynomials in $\mathcal{B}$ is the little Bloch space $\mathcal{B}_0$, the set of $f$ with $(1 - \abs{z}^2)\abs{f'(z)} \to 0$ as $\abs{z} \to 1$.
