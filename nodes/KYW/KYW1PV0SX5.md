---
tag: KYW1PV0SX5
kind: definition
name: Supermartingale
msc: [60G42, 60G44]
defines: NSK7247MKX
uses: [0ZYBZ34RT2, HNK1Y62G7V, YRNFE016FF, 0YAMJRK04E, 0CDVK9RQBH]
sources:
  - url: https://en.wikipedia.org/wiki/Martingale_(probability_theory)
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0ZYBZ34RT2]], let $T \subseteq [0, \infty)$ be an index set, and let $(\mathcal{F}_t)_{t \in T}$ be a [[filtration|HNK1Y62G7V]].
A *supermartingale* with respect to $(\mathcal{F}_t)$ is a family $(X_t)_{t \in T}$ of real random variables such that:

1. $(X_t)$ is [[adapted|YRNFE016FF]]: $X_t$ is $\mathcal{F}_t$-measurable for each $t \in T$.
2. $E[\abs{X_t}] < \infty$ for each $t \in T$.
3. $E[X_t \mid \mathcal{F}_s] \le X_s$ almost surely for all $s \le t$ in $T$, where $E[\cdot \mid \mathcal{F}_s]$ is the [[conditional expectation|0YAMJRK04E]].

## Remarks

Let $\xi_1, \xi_2, \dots$ be independent with $P(\xi_i = 1) = p$ and $P(\xi_i = -1) = 1 - p$, where $p \le 1/2$, and let $\mathcal{F}_n = \sigma(\xi_1, \dots, \xi_n)$.
Then $S_n = \xi_1 + \dots + \xi_n$ is a supermartingale: it is adapted, $\abs{S_n} \le n$, and $E[S_{n+1} \mid \mathcal{F}_n] = S_n + (2p - 1) \le S_n$.
For $p = 1/2$, the process $S_n^2$ is adapted and integrable but fails clause 3, since $E[S_{n+1}^2 \mid \mathcal{F}_n] = S_n^2 + 1$.
$(X_t)$ is a supermartingale if and only if $(-X_t)$ is a [[submartingale|EQ055QMACW]].
A process is a [[martingale|0CDVK9RQBH]] if and only if it is both a submartingale and a supermartingale.
Taking expectations in clause 3 shows that $t \mapsto E[X_t]$ is non-increasing.
