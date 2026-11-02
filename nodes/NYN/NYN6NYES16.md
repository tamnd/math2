---
tag: NYN6NYES16
kind: statement
role: theorem
name: Recurrence and capacity of graphs
msc: [31C20, 60J10, 05C81]
uses: [T7KRE7J3B4, XAE5YJ3H68, PBZTBWZ4GS, 04VZE3FZXF, KX4152NVW8, 8BPMHA5MT4, BEQH6AZPYM]
about: [PBZTBWZ4GS, XAE5YJ3H68]
sources:
  - url: https://en.wikipedia.org/wiki/Random_walk
---

## Statement

Let $(G, c)$ be an infinite [[electrical network|T7KRE7J3B4]] with vertex set $V$, and let $c(x) = \sum_y c(x, y)$.
Let $(X_n)$ be the [[random walk|04VZE3FZXF]] on $V$ with transition probabilities $p(x, y) = c(x, y)/c(x)$.
Fix $a \in V$ and finite sets $V_1 \subseteq V_2 \subseteq \cdots$ with union $V$ and $a \in V_1$.
Let $G_n$ be the finite network obtained from $G$ by gluing all vertices outside $V_n$ into one vertex $z_n$.
Edges with both ends outside $V_n$ are deleted, and the edge from $x \in V_n$ to $z_n$ gets the sum of the conductances $c(x, y)$ over $y \notin V_n$.
Then the [[effective resistances|XAE5YJ3H68]] $R_{\mathrm{eff}}(a, z_n)$ in $G_n$ increase to a limit $R(a \leftrightarrow \infty) \in (0, \infty]$ that does not depend on the choice of the sets $V_n$.
Moreover
$$\mathbb{P}_a\big[X_n \ne a \text{ for all } n \ge 1\big] = \frac{1}{c(a)\, R(a \leftrightarrow \infty)},$$
with $1/\infty = 0$.
In particular the walk is [[recurrent|PBZTBWZ4GS]] if and only if $R(a \leftrightarrow \infty) = \infty$, that is, if and only if the capacity $1/R(a \leftrightarrow \infty)$ of $a$ is $0$.

## Remarks

For a finite network, the probability that the walk from $a$ reaches $b$ before returning to $a$ is $1/\big(c(a) R_{\mathrm{eff}}(a, b)\big)$.
This follows from the fact that $x \mapsto \mathbb{P}_x[\text{hit } b \text{ before } a]$ is harmonic off $\set{a, b}$, so it is $1 - v$ for the voltage $v$ with $v(a) = 1$ and $v(b) = 0$.
The statement follows by applying this to $G_n$ and letting $n \to \infty$.
The limit increases because $G_{n+1}$ arises from $G_n$ by un-gluing vertices, which raises resistance by the [[Rayleigh monotonicity law|KX4152NVW8]].
Example: on $\Z^2$ with unit conductances, the edges between the boundary of the box $[-k, k]^2$ and the next box form $4(2k + 1)$ disjoint cutsets.
The Nash-Williams inequality gives $R(0 \leftrightarrow \infty) \ge \sum_{k \ge 0} \frac{1}{4(2k + 1)} = \infty$, so the simple random walk on $\Z^2$ is recurrent.
On $\Z^3$ the resistance to infinity is finite, which gives the transience part of [[Pólya's recurrence theorem|BEQH6AZPYM]].

## Explanations

### L1 human

Imagine the graph as an infinite network of wires and connect one pole of a battery to a vertex $a$ and the other pole to infinity.
If the resistance between $a$ and infinity is infinite, no current escapes, and a random walker started at $a$ comes back to $a$ with probability $1$.
If the resistance is finite, current escapes, and the walker has a positive chance never to return.
This turns a question about random paths into a question about circuits.

### L2 human

The theorem lets one decide recurrence with the tools of electrical networks.
Lower bounds on resistance come from gluing vertices, as in the Nash-Williams inequality; upper bounds come from flows of finite energy, by [[Thomson's principle|8BPMHA5MT4]].
Recurrence is a property of the graph and the conductances, not of the starting vertex.
Indeed $R(a \leftrightarrow \infty)$ is finite for one vertex exactly when it is finite for all vertices of the connected graph.
Comparisons between graphs, for example under bounded changes of conductances, preserve recurrence and transience.
