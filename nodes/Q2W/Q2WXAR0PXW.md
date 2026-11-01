---
tag: Q2WXAR0PXW
kind: definition
name: Topology of uniform convergence
msc: [54C35, "54E35"]
defines: YW5P7NEKR4
uses: [0VKD1TP7F3, 0YVKNB7V5F, 08VZ57PT26, 0WS9P12FQR]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_convergence
---

## Definition

Let $X$ be a set, let $(Y, d)$ be a [[metric space|0VKD1TP7F3]], and let $Y^X$ be the set of all maps from $X$ to $Y$.
The uniform metric on $Y^X$ is
$$\bar d(f, g) = \sup_{x \in X} \min\bigl(d(f(x), g(x)), 1\bigr).$$
The *topology of uniform convergence* on $Y^X$ is the [[metric topology|0YVKNB7V5F]] of $\bar d$.
On a subset of $Y^X$, it is the [[subspace topology|0WS9P12FQR]].

## Remarks

The cut-off at $1$ makes $\bar d$ finite even for unbounded maps; it does not change which sequences converge.
A sequence $(f_n)$ converges to $f$ in this topology if and only if $f_n \to f$ [[uniformly|08VZ57PT26]] on $X$.
On bounded maps, the sup metric $\sup_x d(f(x), g(x))$ gives the same topology.
If $(Y, d)$ is complete, then $(Y^X, \bar d)$ is complete.
If $X$ is a topological space, the set $C(X, Y)$ of continuous maps is closed in $Y^X$, since a uniform limit of continuous maps is continuous.

Example: on $\R^{[0, 1]}$, let $f_n(x) = x / n$.
Then $\bar d(f_n, 0) \le 1/n$, so $f_n \to 0$ in this topology.

Non-example: let $f_n(x) = x^n$ on $X = [0, 1)$ and $Y = \R$.
Then $f_n \to 0$ pointwise, but $\bar d(f_n, 0) = 1$ for every $n$, since $x^n$ takes values close to $1$ near $x = 1$.
So $(f_n)$ converges in the topology of pointwise convergence, but not in the topology of uniform convergence.
