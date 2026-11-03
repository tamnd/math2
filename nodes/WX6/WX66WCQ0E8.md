---
tag: WX66WCQ0E8
kind: definition
name: Lee–Yang zeros
msc: [82B20, 82B26, 30C15]
defines: BH3ZRF72H1
uses: [R0KGM32QN6, 00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Lee%E2%80%93Yang_theorem
---

## Definition

Let $G = (V, E)$ be a finite [[graph|00C0BR7D7H]] with $N = \abs{V}$ vertices, with real couplings $J_e$ for $e \in E$, and let $\beta > 0$.
The partition function of the [[Ising model|R0KGM32QN6]] on $G$ with field $h$ is
$$Z(h) = \sum_{\sigma \in \set{-1,+1}^V} \exp\Big( \beta \sum_{\set{u,v} \in E} J_{uv} \sigma_u \sigma_v + \beta h \sum_{v \in V} \sigma_v \Big).$$
Let $z = e^{-2\beta h}$, and let $k(\sigma)$ be the number of vertices $v$ with $\sigma_v = -1$.
Then $Z(h) = e^{\beta h N} P(z)$, where
$$P(z) = \sum_{\sigma} \exp\Big( \beta \sum_{\set{u,v} \in E} J_{uv} \sigma_u \sigma_v \Big) z^{k(\sigma)}$$
is a polynomial of degree $N$ in $z$.
The *Lee–Yang zeros* of the model are the zeros of $P$ in $\C$.

## Remarks

The identity holds since $\sum_v \sigma_v = N - 2k(\sigma)$.
The coefficients of $P$ are positive, so $P$ has no zero on $[0, \infty)$, which is the set of values of $z$ for real $h$.

Example: two vertices joined by one edge with coupling $J$.
Then $P(z) = e^{\beta J} (1 + 2 e^{-2\beta J} z + z^2)$, whose roots $z = -e^{-2\beta J} \pm i \sqrt{1 - e^{-4\beta J}}$ satisfy $\abs{z}^2 = e^{-4\beta J} + 1 - e^{-4\beta J} = 1$ when $J > 0$.
This agrees with the [[Lee–Yang theorem|NYTQ2BY74G]], which says that all zeros lie on $\abs{z} = 1$ when every $J_e \ge 0$.

Non-example: the zeros of $Z$ as a function of a complex inverse temperature $\beta$ at fixed $h$ are not Lee–Yang zeros.
They are called Fisher zeros and need not lie on a circle.
For $J < 0$ in the example above, the roots are real and negative with product $1$, so they are off the unit circle.
