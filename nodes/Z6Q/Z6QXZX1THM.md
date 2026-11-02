---
tag: Z6QXZX1THM
kind: definition
name: Current
msc: [49Q15, 58A25]
defines: 360H7MD9RD
uses: [0E3G0GRPZ6, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Current_(mathematics)
---

## Definition

Let $U \subseteq \R^n$ be an [[open set|02BH3MCBQB]] and let $0 \le m \le n$.
Let $\mathcal{D}^m(U)$ be the real vector space of smooth [[differential $m$-forms|0E3G0GRPZ6]] on $U$ with compact support in $U$.
A sequence $(\omega_k)$ in $\mathcal{D}^m(U)$ *converges to $0$* if two conditions hold.

1. There is a compact set $K \subseteq U$ that contains the support of every $\omega_k$.
2. Every partial derivative of every coefficient of $\omega_k$ converges to $0$ uniformly on $K$.

An *$m$-dimensional current* on $U$ is a linear map $T \colon \mathcal{D}^m(U) \to \R$ such that $T(\omega_k) \to 0$ whenever $\omega_k \to 0$ in this sense.
The *boundary* of an $m$-current $T$ with $m \ge 1$ is the $(m-1)$-current $\partial T$ given by $\partial T(\omega) = T(d\omega)$.

## Remarks

Example: let $S \subseteq U$ be a compact oriented $m$-dimensional $C^1$ submanifold, possibly with boundary.
Then $[\![S]\!](\omega) = \int_S \omega$ is linear in $\omega$.
It is continuous, since $\abs{\int_S \omega} \le \operatorname{area}(S) \cdot \sup_S \abs{\omega}$.
So $[\![S]\!]$ is an $m$-current, and Stokes' theorem gives $\partial [\![S]\!] = [\![\partial S]\!]$.
Non-example: the map $\omega \mapsto \abs{\int_S \omega}$ is continuous but not linear, so it is not a current.
The $0$-currents on $U$ are the distributions on $U$.
The *mass* of $T$ is the supremum of $T(\omega)$ over the forms $\omega$ with $\abs{\omega(x)} \le 1$ for all $x$, for a suitable norm on $m$-covectors.
