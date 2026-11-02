---
tag: 5V9ZHDZ0EZ
kind: example
name: Grandi's series
msc: [40A05, 40G05, 40G10]
instance_of: [0JWMJSTBSG]
uses: [N8ZGG7EW6J, EZXPY4A19C, 8DJPSYSHGJ]
sources:
  - url: https://en.wikipedia.org/wiki/Grandi%27s_series
same_as:
  wikidata: Q967588
  wikipedia: Grandi's series
---

## Example

*Grandi's series* is the series
$$\sum_{n=0}^{\infty} (-1)^n = 1 - 1 + 1 - 1 + \cdots.$$
Its partial sums are $s_N = \sum_{n=0}^{N} (-1)^n$, which equal $1$ for even $N$ and $0$ for odd $N$.
So the partial sums have no limit, and the series is a [[divergent series|0JWMJSTBSG]].
Its terms do not tend to $0$, which already rules out convergence.

## Remarks

Several summation methods assign it the value $1/2$.
[[Cesàro summation|N8ZGG7EW6J]]: the averages $(s_0 + \cdots + s_N)/(N+1)$ equal $1/2$ for odd $N$ and $(N/2 + 1)/(N+1)$ for even $N$, so they tend to $1/2$.
[[Abel summation|EZXPY4A19C]]: for $0 < x < 1$, $\sum_{n \ge 0} (-1)^n x^n = 1/(1 + x)$, which tends to $1/2$ as $x \to 1^-$.
[[Borel summation|8DJPSYSHGJ]] also gives $1/2$, since it sums the geometric series $\sum z^n$ to $1/(1 - z)$ at $z = -1$.
The value $1/2$ is forced for any linear and stable method that sums the series: if $S = 1 - 1 + 1 - \cdots$, stability and linearity give $S = 1 - S$.

## Explanations

### L1 human

Add $1$, subtract $1$, add $1$, subtract $1$, forever.
The running total jumps between $1$ and $0$ and never settles, so the series has no sum in the ordinary sense.
On average the running total is $1/2$, and this is the value that the usual summation methods give it.
