---
tag: J10YF5CXX9
kind: definition
name: Graphical model
msc: [62H22]
defines: Q3FQAD1BXG
uses: [00C0BR7D7H, 0DR81R1F2B, 0THJ7416DX, 0PNRKMRC55]
sources:
  - url: https://en.wikipedia.org/wiki/Graphical_model
---

## Definition

Let $G = (V, E)$ be a finite [[graph|00C0BR7D7H]], directed or undirected, and let $X = (X_v)_{v \in V}$ be a family of [[random variables|0PNRKMRC55]] indexed by the vertices.
A *Markov property* for $G$ is a list of [[conditional independence|0THJ7416DX]] statements $X_A \perp X_B \mid X_S$, for subsets $A, B, S \subseteq V$, that is read off the graph.
The *graphical model* of $G$ is the set of all [[joint distributions|0DR81R1F2B]] of $X$ that satisfy the Markov property of $G$.
For a directed acyclic graph it is called a Bayesian network, and for an undirected graph a Markov random field.

## Remarks

Here $X_A = (X_v)_{v \in A}$.
Example: the undirected path $1 - 2 - 3$ gives the model of all distributions with $X_1 \perp X_3 \mid X_2$.
A Markov chain $X_1, X_2, X_3$ lies in this model.
Non-example: let $X_1, X_2$ be independent fair coins and $X_3 = X_1$.
Then $X_1$ and $X_3$ are dependent given $X_2$, so this distribution is not in the model of the path.
A complete graph imposes no condition, so its model contains all joint distributions.
Often the model is restricted further to a parametric family, such as the Gaussian graphical models.
