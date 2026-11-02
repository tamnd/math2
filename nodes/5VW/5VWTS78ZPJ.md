---
tag: 5VWTS78ZPJ
kind: definition
name: Flat norm
msc: [49Q15, 28A75]
defines: Y7P66D41Z8
uses: [360H7MD9RD, EG4AJVEFT2]
sources:
  - url: https://en.wikipedia.org/wiki/Current_(mathematics)
---

## Definition

Let $0 \le m \le n$, and for a [[current|360H7MD9RD]] $R$ on $\R^n$ let $\mathbf{M}(R) \in [0, \infty]$ be its mass.
The *flat norm* of an $m$-current $T$ on $\R^n$ is
$$\mathbf{F}(T) = \inf \set{ \mathbf{M}(R) + \mathbf{M}(S) : R \text{ an } m\text{-current}, \ S \text{ an } (m+1)\text{-current}, \ T = R + \partial S },$$
with $\inf \emptyset = \infty$.
The *flat distance* between $m$-currents $T_1$ and $T_2$ is $\mathbf{F}(T_1 - T_2)$.
For [[integral currents|EG4AJVEFT2]], the *integral flat norm* is defined in the same way with $R$ and $S$ required to be integral currents.

## Remarks

Taking $S = 0$ shows $\mathbf{F}(T) \le \mathbf{M}(T)$.
If $\mathbf{F}(T_j - T) \to 0$, then $T_j(\omega) \to T(\omega)$ for every smooth compactly supported $m$-form $\omega$, so flat convergence implies weak convergence.
When $\mathbf{F}(T) < \infty$, there is a dual description of $\mathbf{F}(T)$ as the supremum of $T(\omega)$ over the forms $\omega$ such that $\omega$ and $d\omega$ have comass at most $1$ everywhere.

Example: in $\R$, let $a < b$ and $T = \delta_b - \delta_a$, a $0$-current.
Then $T = \partial [\![a, b]\!]$, so $\mathbf{F}(T) \le b - a$, and $\mathbf{F}(T) \le \mathbf{M}(T) = 2$.
Testing $T$ on a function $\varphi$ with $\abs{\varphi} \le 1$ and $\abs{\varphi'} \le 1$, chosen with $\varphi(b) - \varphi(a) = \min(b - a, 2)$, shows that $\mathbf{F}(T) = \min(b - a, 2)$.
So $\delta_b - \delta_a \to 0$ in the flat norm as $b \to a$, while its mass stays $2$.

Non-example: the mass $\mathbf{M}$ is a norm on currents of finite mass, but it is not the flat norm, as the example shows.

## Explanations

### L1 human

The flat norm of a current is the cheapest way to write it as a piece plus a boundary, where each part costs its mass.
