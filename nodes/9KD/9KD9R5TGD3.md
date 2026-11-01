---
tag: 9KD9R5TGD3
kind: definition
name: Tightness of measures
msc: [60B10, 28A33]
defines: MNMJC8YVBS
uses: [059TJN0NZ1, 0WQXY32Q8D, 0R6EWFKRCF, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Tightness_of_measures
---

## Definition

Let $E$ be a topological space with its [[Borel σ-algebra|0WQXY32Q8D]], and let $\mathcal{M}$ be a set of [[probability measures|059TJN0NZ1]] on $E$.
$\mathcal{M}$ is *tight* if for every $\varepsilon > 0$ there is a [[compact set|0R6EWFKRCF]] $K \subseteq E$ such that
$$\mu(E \setminus K) < \varepsilon \qquad \text{for all } \mu \in \mathcal{M}.$$
A sequence of random variables with values in $E$ is tight if the set of their laws is tight.

## Remarks

On $\R^d$, a family $\mathcal{M}$ is tight if and only if $\sup_{\mu \in \mathcal{M}} \mu(\set{x : \abs{x} > R}) \to 0$ as $R \to \infty$, because the compact sets are the closed bounded sets.
Example: the [[normal|05AQE0QR0D]] laws $N(m, 1)$ with $\abs{m} \le 1$ form a tight family. Given $\varepsilon$, choose $r$ with $P(\abs{Z} > r) < \varepsilon$ for $Z$ standard normal; then $K = [-1 - r, 1 + r]$ works, since $N(m, 1)(\R \setminus K) \le P(\abs{Z} > r)$.
Non-example: the point masses $\delta_n$, $n \in \N$, on $\R$. Each compact $K$ lies in some $[-R, R]$, and then $\delta_n(\R \setminus K) = 1$ for $n > R$.
Also non-tight: the normal laws $N(0, n)$, $n \ge 1$, whose mass spreads out.
A single Borel probability measure on a Polish space is tight, and so is every finite family.
On a Polish space, Prokhorov's theorem says that $\mathcal{M}$ is tight if and only if it is relatively compact for weak convergence.
Every sequence of real random variables that converges in distribution is tight.
