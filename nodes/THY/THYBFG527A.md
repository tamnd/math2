---
tag: THYBFG527A
kind: definition
name: Random graph
msc: [05C80, 60C05]
defines: TNT3DG0HRJ
uses: [0JD5C82QMB, 0ZYBZ34RT2, 0VGMEBVW1M]
sources:
  - url: https://en.wikipedia.org/wiki/Random_graph
---

## Definition

Let $n \ge 1$, let $V = \set{1, \dots, n}$, and let $\mathcal{G}_n$ be the finite set of all simple [[graphs|0JD5C82QMB]] with vertex set $V$.
A random graph on $V$ is a [[probability measure|0VGMEBVW1M]] $\mathbb{P}$ on $\mathcal{G}_n$.
That is, it is a map $\mathbb{P} \colon \mathcal{G}_n \to [0, 1]$ with $\sum_{G \in \mathcal{G}_n} \mathbb{P}(G) = 1$.
Equivalently, it is the law of a random variable on a [[probability space|0ZYBZ34RT2]] with values in $\mathcal{G}_n$.
A model of random graphs is a choice of such a measure $\mathbb{P}_n$ for every $n$.
For $0 \le p \le 1$, the binomial model $G(n, p)$ is the measure with $\mathbb{P}(G) = p^{m} (1 - p)^{\binom{n}{2} - m}$, where $m$ is the number of edges of $G$.

## Remarks

In $G(n, p)$ the $\binom{n}{2}$ possible edges are present independently, each with probability $p$; the probabilities add up to $(p + (1 - p))^{\binom{n}{2}} = 1$ by the binomial theorem.
Example: $G(n, 1/2)$ gives each of the $2^{\binom{n}{2}}$ graphs in $\mathcal{G}_n$ the same probability, so it is the uniform random graph on $V$.
Non-example: giving each of the $8$ graphs on $\set{1, 2, 3}$ the weight $1/2$ is not a random graph, because the weights add up to $4$, not $1$.
A property holds asymptotically almost surely in a model if its probability tends to $1$ as $n \to \infty$.
Another standard model is $G(n, M)$, the uniform measure on the graphs in $\mathcal{G}_n$ with exactly $M$ edges.
