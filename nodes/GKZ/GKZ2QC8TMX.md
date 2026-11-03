---
tag: GKZ2QC8TMX
kind: definition
name: Cross-entropy
msc: [94A17, 68T05]
defines: K6MCP56ETX
uses: [0D6J4B671D, Y86E072V0V, PQBW43X5RE, 55WNT5655E]
sources:
  - url: https://en.wikipedia.org/wiki/Cross-entropy
---

## Definition

Let $\mathcal{X}$ be a countable set, and let $p$ and $q$ be [[probability mass functions|0D6J4B671D]] on $\mathcal{X}$.
The *cross-entropy* of $q$ relative to $p$ is
$$H(p, q) = -\sum_{x \in \mathcal{X} \,:\, p(x) > 0} p(x) \log q(x) \in [0, \infty],$$
with the convention $-\log 0 = +\infty$.

## Remarks

If the [[Shannon entropy|Y86E072V0V]] $H(p)$ is finite, then $H(p, q) = H(p) + D(p \,\|\, q)$, where $D$ is the [[Kullback–Leibler divergence|PQBW43X5RE]].
By [[Gibbs' inequality|55WNT5655E]], $H(p, q) \ge H(p)$, with equality exactly when $q = p$.
For laws with densities $p$ and $q$ with respect to a common measure $\mu$, the sum becomes $-\int p \log q \, d\mu$.

Example: on $\set{0, 1}$ with $p = (\frac12, \frac12)$ and $q = (\frac14, \frac34)$, $H(p, q) = \frac12 \log_2 4 + \frac12 \log_2 \frac43 = 2 - \frac12 \log_2 3 \approx 1.21$ bits, while $H(p) = 1$ bit.

Non-example: the cross-entropy is not symmetric; with the same $p$ and $q$, $H(q, p) = \frac14 + \frac34 = 1$ bit, which differs from $H(p, q)$.

The notation $H(p, q)$ clashes with the [[joint entropy|DZWEWHZ20N]] $H(X, Y)$; some authors write $H_p(q)$ or $H^{\times}(p, q)$ instead.

## Explanations

### L1 human

Cross-entropy is the average surprise when outcomes come from $p$ but surprise is measured with the model $q$.
