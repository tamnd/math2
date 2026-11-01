---
tag: NTFND9FRDN
kind: definition
name: Stopped process
msc: [60G40, 60G05]
defines: NG35MGYDZR
uses: [0QH5ENKZM1, HNK1Y62G7V, WND87FBAKC, YRNFE016FF]
sources:
  - url: https://en.wikipedia.org/wiki/Stopped_process
---

## Definition

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \in T}, P)$ be a probability space with a [[filtration|HNK1Y62G7V]], where $T \subseteq [0, \infty)$.
Let $X = (X_t)_{t \in T}$ be a [[stochastic process|0QH5ENKZM1]] with values in a measurable space $S$, and let $\tau$ be a [[stopping time|WND87FBAKC]].
The *stopped process* $X^\tau = (X^\tau_t)_{t \in T}$ is defined by
$$X^\tau_t(\omega) = X_{\min(t, \tau(\omega))}(\omega) \quad \text{for } t \in T \text{ and } \omega \in \Omega.$$

## Remarks

The notation $t \wedge \tau = \min(t, \tau)$ is standard, so $X^\tau_t = X_{t \wedge \tau}$.
On the event $\set{\tau = \infty}$, the stopped process equals $X$.

In discrete time, if $X$ is [[adapted|YRNFE016FF]], then so is $X^\tau$, because
$$X^\tau_n = X_0 + \sum_{k=1}^{n} \mathbf{1}_{\set{\tau \ge k}} (X_k - X_{k-1})$$
for real-valued $X$, and $\set{\tau \ge k} = \Omega \setminus \set{\tau \le k - 1} \in \mathcal{F}_{k-1}$.
The same formula shows that a stopped [[martingale|0D0GBNDKDH]] is a martingale.
In continuous time, the stopped process of a progressively measurable process is progressively measurable.

Example: let $S$ be a simple symmetric [[random walk|04VZE3FZXF]] started at $0$ and let $\tau$ be the first time with $\abs{S_n} = 5$.
Then $\abs{S^\tau_n} \le 5$ for all $n$, so $S^\tau$ is a bounded martingale.

Non-example: if $\tau$ is not a stopping time, the formula still defines a process, but it need not be adapted.
Take the walk above and let $\sigma$ be the last visit to $0$ before time $10$.
The value $S^\sigma_1$ equals $S_1$ if the walk returns to $0$ between times $1$ and $10$, and $0$ otherwise.
This is not determined by $\mathcal{F}_1$, so $S^\sigma$ is not adapted.
