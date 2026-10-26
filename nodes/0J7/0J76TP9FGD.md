---
tag: 0J76TP9FGD
kind: statement
role: theorem
name: Rearrangements of an absolutely convergent series have the same sum
msc: [40A05]
uses: [0W3K3QPEWT, 0HRJ2Y74T3]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_convergence
    locator: Rearrangements and unconditional convergence
---

## Statement

Let $\sum a_n$ be a real series that [[converges absolutely|0W3K3QPEWT]], with sum $A$.
Let $\sigma \colon \mathbb{N} \to \mathbb{N}$ be a bijection.
Then the [[rearrangement|0HRJ2Y74T3]] $\sum a_{\sigma(n)}$ converges absolutely, and its sum is $A$.

## Remarks

Given $\varepsilon > 0$, choose $N$ with $\sum_{n > N} |a_n| < \varepsilon$. For large $m$, the first $m$ terms of the rearrangement include $a_0, \dots, a_N$. So the two partial sums differ by less than $\varepsilon$.
By the [[Riemann rearrangement theorem|0E7VBYGFF7]], the converse also holds for real series.
Mathlib states a general form for sums over a type, as `Equiv.tsum_eq`.

## Explanations

### L1 human

When the series converges absolutely, the far terms have a small total size, whatever their order.
So a new order changes the partial sums only by a small amount.
