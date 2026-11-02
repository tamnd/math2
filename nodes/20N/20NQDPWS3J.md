---
tag: 20NQDPWS3J
kind: definition
name: Self-similar measure
msc: [28A80]
defines: R8A7XTNZ1B
uses: [059TJN0NZ1, 3N66TM3TSQ, 0QN69YA357]
sources:
  - url: https://en.wikipedia.org/wiki/Self-similarity
---

## Definition

Let $n \ge 1$ and $N \ge 2$.
For $i = 1, \dots, N$ let $S_i \colon \R^n \to \R^n$ be a similarity with ratio $r_i \in (0, 1)$, that is, $\abs{S_i(x) - S_i(y)} = r_i \abs{x - y}$ for all $x, y$.
Let $p_1, \dots, p_N > 0$ with $p_1 + \cdots + p_N = 1$.
A Borel [[probability measure|059TJN0NZ1]] $\mu$ on $\R^n$ is *self-similar* for $(S_i, p_i)$ if
$$\mu = \sum_{i=1}^{N} p_i \, (S_i)_* \mu,$$
where $(S_i)_* \mu = \mu \circ S_i^{-1}$ is the [[pushforward measure|3N66TM3TSQ]].

## Remarks

Each $S_i$ is a [[contraction|0QN69YA357]].
Hutchinson's theorem says that there is exactly one compactly supported such $\mu$.
It is the fixed point of a contraction on a space of measures, and its support is the attractor of $(S_i)$.
Example: on $\R$ let $S_1(x) = x/2$, $S_2(x) = x/2 + 1/2$ and $p_1 = p_2 = 1/2$, and let $\lambda$ be Lebesgue measure on $[0,1]$.
The measure $(S_1)_* \lambda$ is uniform on $[0, 1/2]$ with density $2$, and $(S_2)_* \lambda$ is uniform on $[1/2, 1]$ with density $2$.
Their average has density $1$ on $[0,1]$, so it equals $\lambda$, and $\lambda$ is self-similar.
Non-example: with the same maps and $p_1 = 1/3$, $p_2 = 2/3$, the average has density $2/3$ on $[0, 1/2]$, so $\lambda$ is not self-similar for these weights.
The Cantor measure is self-similar for $S_1(x) = x/3$, $S_2(x) = x/3 + 2/3$ and $p_1 = p_2 = 1/2$.
