---
tag: TASMEPWNA6
kind: definition
name: Lévy–Prokhorov metric
msc: [60B10, 28A33]
defines: 8GZK8NC3VQ
uses: [0VKD1TP7F3, 059TJN0NZ1, 0WQXY32Q8D, 0QF1MZ9FRG, MBW9JCGZC1, 0ACRGYNHSR]
sources:
  - url: https://en.wikipedia.org/wiki/L%C3%A9vy%E2%80%93Prokhorov_metric
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]] with its [[Borel σ-algebra|0WQXY32Q8D]] $\mathcal{B}$.
Let $\mathcal{P}(X)$ be the set of Borel [[probability measures|059TJN0NZ1]] on $X$.
For $A \subseteq X$ and $\varepsilon > 0$, let $A^\varepsilon = \set{x \in X : d(x, a) < \varepsilon \text{ for some } a \in A}$.
The *Lévy–Prokhorov metric* is the map $\pi \colon \mathcal{P}(X) \times \mathcal{P}(X) \to [0, 1]$ given by
$$\pi(\mu, \nu) = \inf \set{\varepsilon > 0 : \mu(A) \le \nu(A^\varepsilon) + \varepsilon \text{ and } \nu(A) \le \mu(A^\varepsilon) + \varepsilon \text{ for all } A \in \mathcal{B}}.$$
The value is an [[infimum|0QF1MZ9FRG]].

## Remarks

The function $\pi$ is a metric on $\mathcal{P}(X)$, and $\pi \le 1$ because every $\varepsilon \ge 1$ satisfies both inequalities.
If $X$ is separable, then $\pi(\mu_n, \mu) \to 0$ if and only if $\mu_n$ [[converges weakly|MBW9JCGZC1]] to $\mu$.
If $X$ is separable and complete, then so is $(\mathcal{P}(X), \pi)$.

Example: let $\delta_x$ be the [[Dirac measure|0ACRGYNHSR]] at $x$, and let $x, y \in X$.
If $\varepsilon > d(x, y)$, then every Borel set $A$ containing $x$ has $y \in A^\varepsilon$, so $\delta_x(A) \le \delta_y(A^\varepsilon)$, and symmetrically.
Hence $\pi(\delta_x, \delta_y) = \min(d(x, y), 1)$.

Non-example: for $\varepsilon < \min(d(x, y), 1)$ the value $\varepsilon$ is not admissible.
Take $A = \set{x}$: then $y \notin A^\varepsilon$, and $1 \le 0 + \varepsilon$ fails.

On $\R$, the points $1/n$ and $0$ give $\pi(\delta_{1/n}, \delta_0) = 1/n$, while the total variation distance stays equal to $1$.

## Explanations

### L1 human

The metric allows an error of $\varepsilon$ both in position and in mass.
Its smallest admissible $\varepsilon$ measures how far apart the two measures are.
