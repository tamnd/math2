---
tag: 9GWGW4YRD9
kind: definition
name: Cobweb plot
msc: ["37E05", 26A18, 37M99]
defines: B0K8MDA7CJ
uses: [AYVTR2ES5B, R6QVS6P21N]
sources:
  - url: https://en.wikipedia.org/wiki/Cobweb_plot
---

## Definition

Let $I \subseteq \R$ be an interval, let $f \colon I \to I$ be a map, and let $x_0 \in I$.
Let $x_n = f^n(x_0)$ for $n \ge 0$, where $f^n$ is the $n$-th [[iterate|AYVTR2ES5B]] of $f$, so that $x_{n+1} = f(x_n)$.
Consider the points $P_{2n} = (x_n, x_n)$ and $P_{2n+1} = (x_n, x_{n+1})$ for $n \ge 0$.
The *cobweb plot* of the orbit of $x_0$ is the polygonal path $P_0 P_1 P_2 \cdots$.
It is drawn together with the graph of $f$ and the diagonal $\set{(x, x) : x \in I}$.

## Remarks

The points $(x_n, x_{n+1})$ lie on the graph of $f$ and the points $(x_n, x_n)$ lie on the diagonal.
So the path alternates vertical segments to the graph and horizontal segments to the diagonal.
A [[fixed point|R6QVS6P21N]] $p$ of $f$ is a point where the graph meets the diagonal, and the path starting at $x_0 = p$ stays at $(p, p)$.

Example: let $f(x) = x/2 + 1$ on $\R$ and $x_0 = 0$.
The orbit is $0, 1, 3/2, 7/4, \dots$, with $x_n = 2 - 2^{1-n}$ for $n \ge 0$.
The cobweb path goes from $(0, 0)$ up to $(0, 1)$, across to $(1, 1)$, up to $(1, 3/2)$, and so on, a staircase that climbs to the fixed point $(2, 2)$.

Non-example: the plot of the points $(n, x_n)$ against the time $n$ is a time series plot.
It is not a cobweb plot, because it does not use the graph of $f$ and the diagonal.
