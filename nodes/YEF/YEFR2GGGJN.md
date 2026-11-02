---
tag: YEFR2GGGJN
kind: definition
name: Random dynamical system
msc: [37H05, 37H10]
defines: DMTFJY6CS0
uses: [0NFPJVJJHX, 556WBDAHNP, BBZP1R872N]
sources:
  - url: https://en.wikipedia.org/wiki/Random_dynamical_system
---

## Definition

Let $\mathbb{T}$ be $\Z$, $\N$, $\R$ or $[0, \infty)$, and let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0NFPJVJJHX]].
Let $(\theta_t)_{t \in \mathbb{T}}$ be a family of [[measure-preserving maps|556WBDAHNP]] $\theta_t \colon \Omega \to \Omega$ such that $(t, \omega) \mapsto \theta_t \omega$ is measurable, $\theta_0 = \id$ and $\theta_{s + t} = \theta_s \circ \theta_t$ for all $s, t \in \mathbb{T}$.
Let $X$ be a measurable space.
A *random dynamical system* on $X$ over $\theta$ is a measurable map $\varphi \colon \mathbb{T} \times \Omega \times X \to X$, written $\varphi(t, \omega) = \varphi(t, \omega, \cdot)$, such that for all $\omega \in \Omega$:

1. $\varphi(0, \omega) = \id_X$;
2. $\varphi(s + t, \omega) = \varphi(t, \theta_s \omega) \circ \varphi(s, \omega)$ for all $s, t \in \mathbb{T}$.

## Remarks

Clause 2 is the cocycle property.
When $\Omega$ has one point, $\varphi$ is an ordinary [[dynamical system|BBZP1R872N]].
Often $X$ is a topological space and each $\varphi(t, \omega)$ is required to be continuous.

Example: let $f_0, f_1 \colon X \to X$ be measurable maps.
Let $\Omega = \set{0, 1}^{\Z}$ with the product of the measures giving weight $\frac{1}{2}$ to $0$ and to $1$, and let $\theta_t$ be the $t$-th power of the left shift, for $t \in \N$.
Put $\varphi(0, \omega) = \id_X$ and $\varphi(n, \omega) = f_{\omega_{n-1}} \circ \cdots \circ f_{\omega_1} \circ f_{\omega_0}$ for $n \ge 1$.
Then $\varphi(m + n, \omega)$ applies $f_{\omega_0}, \ldots, f_{\omega_{m-1}}$ and then $f_{\omega_m}, \ldots, f_{\omega_{m+n-1}}$, and the second block is $\varphi(n, \theta_m \omega)$, so clause 2 holds.

Non-example: with the same data, $\psi(n, \omega) = f_{\omega_0}^{\,n}$ fails clause 2 when $f_0^{\,2} \ne f_1 \circ f_0$.
Indeed, for $\omega_0 = 0$ and $\omega_1 = 1$, $\psi(2, \omega) = f_0 \circ f_0$, while $\psi(1, \theta_1 \omega) \circ \psi(1, \omega) = f_1 \circ f_0$.

Stochastic differential equations with suitable coefficients generate random dynamical systems with $\Omega$ the space of Brownian paths and $\theta_t$ the shift of paths.
