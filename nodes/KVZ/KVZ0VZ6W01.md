---
tag: KVZ0VZ6W01
kind: definition
name: Dedekind eta function
msc: [11F20]
defines: MX3CVYMNDV
uses: [X6XGGH5FPW, 0NAHXR1FRH, 0J0FCWV32D]
sources:
  - url: https://en.wikipedia.org/wiki/Dedekind_eta_function
---

## Definition

Let $\mathbb{H}$ be the [[upper half-plane|X6XGGH5FPW]], and for $\tau \in \mathbb{H}$ let $q = e^{2 \pi i \tau}$, so that $\abs{q} < 1$.
The *Dedekind eta function* is the function $\eta \colon \mathbb{H} \to \C$ given by
$$\eta(\tau) = e^{\pi i \tau / 12} \prod_{n = 1}^{\infty} (1 - q^n).$$

## Remarks

The product converges absolutely and locally uniformly, since $\sum_n \abs{q}^n < \infty$.
So $\eta$ is [[holomorphic|0NAHXR1FRH]] on $\mathbb{H}$, and it has no zeros there.
It satisfies $\eta(\tau + 1) = e^{\pi i / 12} \eta(\tau)$ and $\eta(-1/\tau) = \sqrt{-i\tau}\, \eta(\tau)$, with the principal branch of the square root.
Example: $\eta(\tau)^{24} = q \prod_{n \ge 1} (1 - q^n)^{24} = \Delta(\tau)$, the [[cusp form|A50Y012RBP]] of weight $12$.
Non-example: $\eta$ itself is not invariant under $\tau \mapsto \tau + 1$, because of the factor $e^{\pi i / 12}$, so it is not a modular form for $\mathrm{SL}_2(\Z)$.
By the [[pentagonal number theorem|PMYDHW00KF]], $\prod_{n \ge 1} (1 - q^n) = \sum_{m \in \Z} (-1)^m q^{m(3m - 1)/2}$.
