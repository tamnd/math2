---
tag: EQ055QMACW
kind: definition
name: Submartingale
msc: [60G42, 60G44]
defines: 6M852B4RA8
uses: [0ZYBZ34RT2, HNK1Y62G7V, YRNFE016FF, 0YAMJRK04E, 0CDVK9RQBH, 0RWMRTPC87]
sources:
  - url: https://en.wikipedia.org/wiki/Martingale_(probability_theory)
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0ZYBZ34RT2]], let $T \subseteq [0, \infty)$ be an index set, and let $(\mathcal{F}_t)_{t \in T}$ be a [[filtration|HNK1Y62G7V]].
A *submartingale* with respect to $(\mathcal{F}_t)$ is a family $(X_t)_{t \in T}$ of real random variables such that:

1. $(X_t)$ is [[adapted|YRNFE016FF]]: $X_t$ is $\mathcal{F}_t$-measurable for each $t \in T$.
2. $E[\abs{X_t}] < \infty$ for each $t \in T$.
3. $E[X_t \mid \mathcal{F}_s] \ge X_s$ almost surely for all $s \le t$ in $T$, where $E[\cdot \mid \mathcal{F}_s]$ is the [[conditional expectation|0YAMJRK04E]].

## Remarks

Let $S_n = \xi_1 + \dots + \xi_n$, where the $\xi_i$ are independent with $P(\xi_i = 1) = P(\xi_i = -1) = 1/2$, and let $\mathcal{F}_n = \sigma(\xi_1, \dots, \xi_n)$.
Then $X_n = S_n^2$ is a submartingale: it is adapted, $\abs{X_n} \le n^2$, and $E[S_{n+1}^2 \mid \mathcal{F}_n] = S_n^2 + 2 S_n E[\xi_{n+1}] + E[\xi_{n+1}^2] = S_n^2 + 1 \ge S_n^2$.
The process $-S_n^2$ is adapted and integrable but fails clause 3, since $E[-S_{n+1}^2 \mid \mathcal{F}_n] = -S_n^2 - 1$.
In discrete time $T = \{0, 1, 2, \dots\}$, clause 3 is equivalent to $E[X_{n+1} \mid \mathcal{F}_n] \ge X_n$ for each $n$, by the tower property.
A process is a [[martingale|0CDVK9RQBH]] if and only if it is both a submartingale and a [[supermartingale|KYW1PV0SX5]].
If $(M_t)$ is a martingale and $\varphi$ is convex with $E[\abs{\varphi(M_t)}] < \infty$ for all $t$, then $(\varphi(M_t))$ is a submartingale by the conditional form of [[Jensen's inequality|0RWMRTPC87]].
Taking expectations in clause 3 shows that $t \mapsto E[X_t]$ is non-decreasing.
