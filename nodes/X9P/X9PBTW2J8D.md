---
tag: X9PBTW2J8D
kind: definition
name: Hecke operator
msc: [11F25, 11F11]
defines: S4SV3QZ8B1
uses: [GWKN5VG78A, A50Y012RBP, X6XGGH5FPW]
sources:
  - url: https://en.wikipedia.org/wiki/Hecke_operator
---

## Definition

Let $k$ be an integer, let $\mathbb{H}$ be the [[upper half-plane|X6XGGH5FPW]], and let $M_k$ be the space of [[modular forms|GWKN5VG78A]] of weight $k$ for $\mathrm{SL}_2(\Z)$.
For an integer $n \ge 1$, the *Hecke operator* $T_n \colon M_k \to M_k$ is given by
$$(T_n f)(\tau) = n^{k-1} \sum_{\substack{ad = n \\ a, d \ge 1}} \ \sum_{b = 0}^{d - 1} d^{-k} f\left(\frac{a\tau + b}{d}\right).$$

## Remarks

If $f = \sum_{m \ge 0} c(m) q^m$ with $q = e^{2 \pi i \tau}$, then $T_n f = \sum_{m \ge 0} \gamma(m) q^m$ with
$$\gamma(m) = \sum_{d \mid \gcd(m, n)} d^{k-1} c(mn/d^2).$$
The operators commute, $T_m T_n = T_{mn}$ when $\gcd(m, n) = 1$, and $T_p T_{p^r} = T_{p^{r+1}} + p^{k-1} T_{p^{r-1}}$ for primes $p$ and $r \ge 1$.
They map the [[cusp forms|A50Y012RBP]] $S_k$ into $S_k$.
Example: $S_{12} = \C \Delta$ is one-dimensional, so $T_n \Delta$ is a multiple of $\Delta$; comparing the coefficients of $q$ gives $T_n \Delta = \tau(n) \Delta$.
Non-example: the map $f(\tau) \mapsto f(n\tau)$ alone does not preserve $M_k$.
For instance, $E_4(2\tau) = 1 + 240 q^2 + \cdots$ is not a multiple of $E_4 = 1 + 240 q + \cdots$, while $M_4 = \C E_4$.
