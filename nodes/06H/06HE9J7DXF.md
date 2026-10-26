---
tag: 06HE9J7DXF
kind: example
name: Uniform metric on bounded functions
aliases: [sup-metric-on-bounded-functions]
msc: ["46E99"]
instance_of: [0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_norm
    locator: Uniform metric
---

## Example

Let $S$ be a nonempty set.
Let $B(S)$ be the set of bounded functions $f \colon S \to \mathbb{R}$, that is, the functions for which there is a real $M$ with $|f(s)| \le M$ for all $s \in S$.
For $f, g \in B(S)$, let
$$d_\infty(f, g) = \sup_{s \in S} |f(s) - g(s)|.$$
Then $d_\infty$ is a [[metric|063W5JMY85]] on $B(S)$, the uniform metric.

## Remarks

The [[supremum|0BTMQ04556]] is finite, because $|f(s) - g(s)| \le |f(s)| + |g(s)|$ and both functions are bounded.
A sequence $(f_k)$ converges to $f$ in this metric if and only if $f_k \to f$ uniformly on $S$.
For $S = \{1, \ldots, n\}$, it is the [[sup metric on R^n|0VTAXQEWQD]].
It is $d_\infty(f, g) = \|f - g\|_\infty$ for the [[sup norm|0PARCKE8WP]].

## Explanations

### L1 human

Two functions are close in the uniform metric when their graphs are close at every point at the same time.
For example, on $[0, 1]$ the distance between $f(x) = x$ and $g(x) = x^2$ is $1/4$, the largest gap, at $x = 1/2$.
