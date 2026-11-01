---
tag: MZNFPJJMY9
kind: definition
name: Semimartingale
msc: [60G48, 60H05]
defines: 4EJB6E2AZK
uses: [HNK1Y62G7V, YRNFE016FF, ZWJ9G89W3T]
sources:
  - url: https://en.wikipedia.org/wiki/Semimartingale
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a probability space with a [[filtration|HNK1Y62G7V]] $(\mathcal{F}_t)_{t \ge 0}$ that is right-continuous and complete.
A function $a \colon [0, \infty) \to \R$ has finite variation if $\sup \sum_{k} \abs{a(t_k) - a(t_{k-1})} < \infty$ on each interval $[0, t]$, the supremum being over finite partitions $0 = t_0 < \dots < t_m = t$.
A real [[adapted|YRNFE016FF]] process $(X_t)_{t \ge 0}$ with càdlàg paths is a *semimartingale* if it can be written as
$$X_t = X_0 + M_t + A_t, \qquad t \ge 0,$$
where:

1. $(M_t)$ is a [[local martingale|ZWJ9G89W3T]] with $M_0 = 0$.
2. $(A_t)$ is an adapted càdlàg process with $A_0 = 0$ whose paths have finite variation almost surely.

## Remarks

Brownian motion with drift, $X_t = W_t + \mu t$ with $W$ a Wiener process and $\mu \in \R$, is a semimartingale: $M = W$ is a martingale and $A_t = \mu t$ has finite variation.
[[Fractional Brownian motion|VC6R7XSKRQ]] with Hurst index $H \ne 1/2$ is not a semimartingale for its own filtration, so it admits no such decomposition.
The decomposition is not unique in general; it is unique when $A$ is required to be predictable and such a decomposition exists, as for continuous semimartingales.
By the Bichteler–Dellacherie theorem, semimartingales are exactly the good integrators: the adapted càdlàg processes for which the stochastic integral of simple predictable processes extends continuously.
Every semimartingale has a [[quadratic variation|ZBYC3MFW89]], and [[Itô's lemma|2J1RVQB0CM]] holds for $C^2$ functions of semimartingales.
