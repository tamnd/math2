---
tag: ZGJV8MYPMH
kind: definition
name: Homotopy K-theory
msc: [19D25, 19D35]
defines: 1WC029DKQ1
uses: [0B1261B5ED, QE20P81GXX, 3YDPFTQTJ6, 1GHF4EKBXS, WK0A32TZHB, TG6WHHR7CF, P976WYEFMB, 5GVFZWMWC8]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity, and let $R[\Delta^\bullet]$ be the simplicial ring with $R[\Delta^p] = R[t_0, \ldots, t_p]/(t_0 + \cdots + t_p - 1)$, as in [[Karoubi–Villamayor K-theory|QE20P81GXX]].
Let $K^B$ denote the nonconnective K-theory [[spectrum|1GHF4EKBXS]] of Bass and Thomason.
Its homotopy groups are the K-groups in degrees $n \ge 0$ and the [[negative K-groups|3YDPFTQTJ6]] in degrees $n < 0$.
The *homotopy K-theory* spectrum of $R$ is the [[geometric realization|TG6WHHR7CF]] (homotopy colimit over $\Delta^{\mathrm{op}}$) of the [[simplicial|WK0A32TZHB]] spectrum $p \mapsto K^B(R[\Delta^p])$:
$$KH(R) = \operatorname{hocolim}_{p \in \Delta^{\mathrm{op}}} K^B(R[\Delta^p]).$$
Its [[homotopy groups|P976WYEFMB]] $KH_n(R) = \pi_n KH(R)$, $n \in \Z$, are the homotopy K-groups of $R$.

## Remarks

The inclusion $R = R[\Delta^0] \to R[\Delta^\bullet]$ gives a natural map $K^B(R) \to KH(R)$.
The functor $KH$ is homotopy invariant: $KH_n(R) \cong KH_n(R[t])$ for all $n \in \Z$.

Example: let $R$ be a regular Noetherian ring.
Then each $R[\Delta^p]$ is regular, $K_n(R[\Delta^p]) \cong K_n(R)$ by homotopy invariance, and the negative K-groups vanish.
So the simplicial spectrum is constant up to equivalence, and $KH_n(R) \cong K_n(R)$ for $n \ge 0$ while $KH_n(R) = 0$ for $n < 0$.

Non-example: ordinary [[K-theory|5GVFZWMWC8]] is not homotopy invariant, so the map $K^B(R) \to KH(R)$ is not always an equivalence.
For $R = k[\varepsilon]/(\varepsilon^2)$ over a field $k$, the class of the unit $1 + \varepsilon t$ shows that $K_1(R[t]) \ne K_1(R)$, while $KH_1(R[t]) \cong KH_1(R)$.
