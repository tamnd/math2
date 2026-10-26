---
tag: ~ae45adc5
kind: statement
role: proposition
name: Completeness via Cauchy sequences
msc: ["54E50"]
uses: [~aae963c7, ~1928f03d, ~529f53f6]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_sequence
    locator: In a metric space
  - url: https://en.wikipedia.org/wiki/Complete_metric_space
    locator: Definition
---

## Statement

Let $(X, d)$ be a [[metric space|~200ea42b]].
Then $X$ is [[complete|~aae963c7]] if and only if each [[Cauchy sequence|~1928f03d]] in $X$ has a [[convergent|~529f53f6]] subsequence.

## Remarks

The key fact: if a Cauchy sequence $(x_n)$ has a subsequence that converges to $x$, then $x_n \to x$. For $\varepsilon > 0$, choose $N$ for $\varepsilon / 2$ in the Cauchy condition and a term $x_{n_k}$ with $n_k \ge N$ and $d(x_{n_k}, x) < \varepsilon / 2$.
A consequence: a metric space in which each sequence has a convergent subsequence is complete. Thus each [[sequentially compact|~67eb1a63]] metric space is complete.

## Explanations

### L1 human

To show that a space is complete, you need not find the limit of a whole Cauchy sequence.
It is enough to find a limit of some subsequence, and then the whole sequence follows it.
