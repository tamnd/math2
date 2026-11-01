---
tag: BBR7QAD87Y
kind: definition
name: Expander graph
msc: [05C48, 05C50]
defines: DXJXVFV79H
uses: [0KA4S8R39M, Y7S6W12N64]
sources:
  - url: https://en.wikipedia.org/wiki/Expander_graph
---

## Definition

Let $d \ge 3$ be an integer and let $\varepsilon > 0$.
For a finite graph $G$ with at least $2$ vertices, let $h(G)$ be its [[Cheeger constant|Y7S6W12N64]].
It is the minimum of $\abs{\partial S} / \abs{S}$ over the sets $S$ of vertices with $1 \le \abs{S} \le \abs{V(G)}/2$.
Here $\partial S$ is the set of edges with exactly one end in $S$.
A finite graph $G$ is an $\varepsilon$-expander if $h(G) \ge \varepsilon$.
A family of expander graphs of degree $d$ is a sequence $(G_n)_{n \ge 1}$ of finite $d$-[[regular graphs|0KA4S8R39M]] such that:

1. The number of vertices of $G_n$ tends to infinity as $n \to \infty$.
2. There is $\varepsilon > 0$ such that $h(G_n) \ge \varepsilon$ for every $n$.

## Remarks

The complete graph $K_4$ is a $2$-expander: a set $S$ of $1$ or $2$ vertices has $\abs{S}(4 - \abs{S})$ edges leaving it, so the ratio is $4 - \abs{S} \ge 2$.
The cycles $C_n$ do not form a family of expanders: they are $2$-regular, and an arc $S$ of $\floor{n/2}$ consecutive vertices has $\abs{\partial S} = 2$, so $h(C_n) \le 2/\floor{n/2} \to 0$, and clause 2 fails.
Families of expanders of every degree $d \ge 3$ exist.
For example, for each $d \ge 3$ there is $\varepsilon > 0$ such that a random $d$-regular graph on $n$ vertices is an $\varepsilon$-expander with probability tending to $1$ as $n \to \infty$.
An equivalent spectral form uses the second largest eigenvalue $\lambda_2$ of the adjacency matrix.
The discrete Cheeger inequalities say $\frac{d - \lambda_2}{2} \le h(G) \le \sqrt{2d(d - \lambda_2)}$ for a $d$-regular graph $G$.
So clause 2 holds if and only if the spectral gap $d - \lambda_2(G_n)$ is bounded away from $0$.
