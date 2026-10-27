---
tag: 08FPABDQ4C
kind: definition
name: Uniform convergence
msc: [40A30]
defines: 08VZ57PT26
uses: [056FSKG32J]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_convergence
    locator: Definition
inventory: [KYNMF0N33A]
---

## Definition

Let $S$ be a set, and let $f_n \colon S \to \mathbb{R}$ for $n \ge 1$ and $f \colon S \to \mathbb{R}$ be functions.
The sequence $(f_n)$ converges uniformly to $f$ if for every $\varepsilon > 0$ there is $N$ such that
$$|f_n(x) - f(x)| < \varepsilon \quad \text{for all } n \ge N \text{ and all } x \in S.$$

## Remarks

Here $N$ depends only on $\varepsilon$, not on $x$. Uniform convergence implies [[pointwise convergence|056FSKG32J]].
Equivalently, $\sup_{x \in S} |f_n(x) - f(x)| \to 0$ as $n \to \infty$.
For example, $\frac{\sin(n x)}{n} \to 0$ uniformly on $\mathbb{R}$. Mathlib defines it as `TendstoUniformly`.

## Explanations

### L1 human

Uniform convergence means that the whole graph of $f_n$ lies in a thin band around the graph of $f$.
The width of the band tends to $0$, at the same rate for all points.
