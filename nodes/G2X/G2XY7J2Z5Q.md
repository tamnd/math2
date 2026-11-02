---
tag: G2XY7J2Z5Q
kind: definition
name: Bayesian network
msc: [62H22, 68T37]
defines: 21JT983G60
uses: [Q3FQAD1BXG, 0KFYGSHHF5, 0ZN9EZTEM6, 0THJ7416DX]
sources:
  - url: https://en.wikipedia.org/wiki/Bayesian_network
---

## Definition

Let $G = (V, E)$ be a finite [[directed graph|0KFYGSHHF5]] with no directed cycles, that is, a directed acyclic graph.
For $v \in V$ let $\operatorname{pa}(v)$ be the set of parents of $v$, the vertices $u$ with an edge $u \to v$.
Let $X = (X_v)_{v \in V}$ be random variables with a joint density or probability mass function $p$.
Then $X$ is a *Bayesian network* with respect to $G$ if
$$p(x) = \prod_{v \in V} p(x_v \mid x_{\operatorname{pa}(v)})$$
for all $x$, where $p(x_v \mid x_{\operatorname{pa}(v)})$ is the [[conditional density|0ZN9EZTEM6]] of $X_v$ given $X_{\operatorname{pa}(v)}$.

## Remarks

The factorisation is equivalent to the local Markov property.
Each $X_v$ is [[conditionally independent|0THJ7416DX]] of its non-descendants given its parents.
Example: for the chain $A \to B \to C$, the definition asks $p(a, b, c) = p(a) p(b \mid a) p(c \mid b)$.
Dividing by $p(b)$ gives $p(a, c \mid b) = p(a \mid b) p(c \mid b)$, so $A \perp C \mid B$.
Non-example: the graph $A \to B \to A$ has a directed cycle, so it does not define a Bayesian network; a product $p(a \mid b) p(b \mid a)$ is in general not a joint distribution.
Different graphs can give the same model: $A \to B \to C$ and $A \leftarrow B \leftarrow C$ both encode exactly $A \perp C \mid B$.
