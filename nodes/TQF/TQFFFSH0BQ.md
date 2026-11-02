---
tag: TQFFFSH0BQ
kind: concept
name: Local regression
msc: [62G08, 62J02]
sources:
  - url: https://en.wikipedia.org/wiki/Local_regression
same_as:
  wikidata: Q6664520
  wikipedia: Local regression
---

## Summary

Local regression estimates a regression function $m(x) = E[Y \mid X = x]$ by fitting a low-degree polynomial near each point $x$.
The fit at $x$ is a [[weighted least squares|H5CGZHBR58]] fit.
Data points close to $x$ get large weights, and distant points get small or zero weights.
It needs no global formula for $m$, so it is a basic tool of [[nonparametric statistics|VFAJ1EG3X5]].
The methods LOESS and LOWESS are popular versions of it.

## Explanations

### L1 human

Imagine a cloud of points that follows a curved trend.
A single straight line cannot follow the curve, but over a short window the curve looks almost straight.
So at each point $x$ one draws a line through the nearby data only, and keeps the height of that line at $x$.
Sliding the window along the axis traces a smooth curve through the cloud.
For example, with a window of width $1$ around $x = 3$, only data with $X$ between $2$ and $4$ matter for the estimate at $3$.
