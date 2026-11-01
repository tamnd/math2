---
tag: M8NA9X8BTV
kind: definition
name: Modular form
msc: [11F11, 11F03]
defines: GWKN5VG78A
uses: [X6XGGH5FPW, VEKV1EM77B, 0NAHXR1FRH, 0SG74WBFA2, 0V9PMN0RBH]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_form
---

## Definition

Let $k$ be an integer and let $\mathbb{H} = \set{\tau \in \C : \operatorname{Im} \tau > 0}$ be the [[upper half-plane|X6XGGH5FPW]].
A *modular form of weight $k$* for the [[modular group|VEKV1EM77B]] $\mathrm{SL}_2(\Z)$ is a function $f \colon \mathbb{H} \to \C$ such that:

1. $f$ is [[holomorphic|0NAHXR1FRH]] on $\mathbb{H}$;
2. $f\left(\frac{a\tau + b}{c\tau + d}\right) = (c\tau + d)^k f(\tau)$ for all $\tau \in \mathbb{H}$ and all $\begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \mathrm{SL}_2(\Z)$;
3. $f$ is bounded on the region $\set{\tau \in \mathbb{H} : \operatorname{Im} \tau \ge 1}$.

## Remarks

Condition 2 with $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ gives $f(\tau + 1) = f(\tau)$, so $f(\tau) = \sum_{n \in \Z} a_n q^n$ with $q = e^{2 \pi i \tau}$.
Condition 3 then says $a_n = 0$ for $n < 0$; this is "holomorphic at infinity".
Example: every constant function is a modular form of weight $0$.
Example: the [[Eisenstein series|EYREVY31BN]] $G_4$ is a nonzero modular form of weight $4$.
Non-example: the [[j-invariant|FEC2XH822R]] satisfies 1 and 2 with $k = 0$, but $j = q^{-1} + 744 + \cdots$ is unbounded as $\operatorname{Im} \tau \to \infty$, so 3 fails.
If $k$ is odd, the matrix $-I$ gives $f = (-1)^k f$, so $f = 0$.
For a [[congruence subgroup|1H6R856P3C]] $\Gamma$, condition 2 is required only for matrices in $\Gamma$.
Condition 3 is then required at every cusp: $(c\tau + d)^{-k} f(\gamma \tau)$ is bounded on $\operatorname{Im} \tau \ge 1$ for every $\gamma \in \mathrm{SL}_2(\Z)$.
The modular forms of weight $k$ form a finite-dimensional complex vector space $M_k$.
