---
tag: NJEPVG39EZ
kind: definition
name: Itô calculus
msc: [60H05]
defines: JA95NH206E
uses: [22735FGJV6, HNK1Y62G7V, YRNFE016FF, 5MDK7HSYRM, 2J1RVQB0CM]
sources:
  - url: https://en.wikipedia.org/wiki/It%C3%B4_calculus
---

## Definition

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, P)$ be a filtered probability space with a [[filtration|HNK1Y62G7V]] that satisfies the usual conditions.
Let $(B_t)_{t \ge 0}$ be a [[Brownian motion|22735FGJV6]] for this filtration and let $T > 0$.

1. A *simple process* is a process $H_t = \sum_{i=0}^{n-1} \xi_i \mathbf{1}_{(t_i, t_{i+1}]}(t)$, where $0 = t_0 < t_1 < \cdots < t_n = T$ and each $\xi_i$ is a bounded $\mathcal{F}_{t_i}$-measurable random variable.
Its Itô integral is $\int_0^T H_t \, dB_t = \sum_{i=0}^{n-1} \xi_i (B_{t_{i+1}} - B_{t_i})$.
2. Let $H$ be a progressively measurable process with $E\left[\int_0^T H_t^2 \, dt\right] < \infty$.
There are simple processes $H^{(n)}$ with $E\left[\int_0^T (H^{(n)}_t - H_t)^2 \, dt\right] \to 0$.
The *Itô integral* $\int_0^T H_t \, dB_t$ is the limit in $L^2(P)$ of $\int_0^T H^{(n)}_t \, dB_t$.
The limit exists and does not depend on the choice of the $H^{(n)}$.

*Itô calculus* is the study of these integrals, of their extensions to integrators that are semimartingales, and of the processes they define.

## Remarks

Example: for $H = \mathbf{1}_{(0, T]}$, the integral is $B_T - B_0$.
For $H_t = B_t$, the left-point sums converge to $\int_0^T B_t \, dB_t = \tfrac12 (B_T^2 - T)$ when $B_0 = 0$.
Non-example: the process $H_t = B_T$ for all $t < T$ is not [[adapted|YRNFE016FF]], so clause 2 does not apply to it.
The limit in clause 2 exists because of the [[Itô isometry|5MDK7HSYRM]], which makes the map $H \mapsto \int H \, dB$ an isometry on simple processes.
The process $t \mapsto \int_0^t H_s \, dB_s$ has a continuous version that is a square-integrable martingale.
The chain rule of Itô calculus is [[Itô's lemma|2J1RVQB0CM]].
