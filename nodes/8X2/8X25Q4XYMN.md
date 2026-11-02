---
tag: 8X25Q4XYMN
kind: concept
name: Summability method
msc: [40C99, 40A05]
sources:
  - url: https://en.wikipedia.org/wiki/Divergent_series
---

## Summary

A summability method is a rule that assigns a value to some sequences, including some that do not converge.
Applied to partial sums, it assigns values to some series.
Ordinary convergence is the simplest such rule; [[Cesàro summation|N8ZGG7EW6J]], [[Abel summation|EZXPY4A19C]] and [[Borel summation|8DJPSYSHGJ]] are classical ones that extend it.
Summability methods give useful values to [[divergent series|0JWMJSTBSG]] in analysis, number theory and physics.
They are studied through properties such as being [[regular|29C7C41A52]], [[linear and stable|N6Z14G81VF]].

## Explanations

### L1 human

The series $1 - 1 + 1 - 1 + \cdots$ has no sum, because its partial sums jump between $1$ and $0$.
A summability method is a different way of reading off a number from such a sequence of partial sums.
Taking running averages, for example, gives $\frac12$ for this series.
Different methods can sum different series, and a good method should give the usual sum whenever the series converges.
