---
tag: 69YNG4T8XW
kind: statement
role: theorem
name: Consensus dynamics on graphs
msc: [93D50, 93A16, 05C50]
uses: [0JD5C82QMB, 7YBM0AXY23, 0FFAYNMAJZ, 0ZND7NQ970, 0R5HTV7REV]
about: [TN6M6DVZRP]
sources:
  - url: https://en.wikipedia.org/wiki/Consensus_dynamics
---

## Statement

Let $G$ be a finite simple [[graph|0JD5C82QMB]] on the vertices $1, \dots, n$, and let $L$ be its [[Laplacian matrix|7YBM0AXY23]].
Consider the consensus dynamics
$$\dot{x}_i(t) = \sum_{j \sim i} \big(x_j(t) - x_i(t)\big), \qquad i = 1, \dots, n,$$
where $j \sim i$ means that $ij$ is an edge; in vector form, $\dot{x} = -L x$.
Let $\bar{x} = \frac{1}{n} \sum_{i} x_i(0)$ and let $\mathbf{1}$ be the all-ones vector.
If $G$ is [[connected|0FFAYNMAJZ]], then for every initial value $x(0) \in \R^n$
$$\norm{x(t) - \bar{x} \mathbf{1}} \le e^{-\lambda_2 t} \norm{x(0) - \bar{x} \mathbf{1}}, \qquad t \ge 0,$$
where $\lambda_2 > 0$ is the second smallest [[eigenvalue|0ZND7NQ970]] of $L$.
In particular every $x_i(t)$ tends to the average $\bar{x}$ of the initial values.

## Remarks

Since $\mathbf{1}^{T} L = 0$, the sum $\sum_i x_i(t)$ is constant in time.
The matrix $L$ is symmetric and positive semidefinite, and for a connected graph its kernel is spanned by $\mathbf{1}$, so $\lambda_2 > 0$.
The vector $x(t) - \bar{x}\mathbf{1} = e^{-Lt}(x(0) - \bar{x}\mathbf{1})$ stays orthogonal to $\mathbf{1}$, where $e^{-Lt}$ has norm at most $e^{-\lambda_2 t}$.
Example: two vertices joined by one edge give $\dot{x}_1 = x_2 - x_1$ and $\dot{x}_2 = x_1 - x_2$.
Then $x_1 - x_2$ decays like $e^{-2t}$, matching $\lambda_2 = 2$, while $x_1 + x_2$ is constant.
Connectivity is necessary: if $G$ has two components, each component converges to the average of its own initial values, and these can differ.
For a [[directed graph|0R5HTV7REV]] with in-degree Laplacian, all states converge to a common value for every initial condition if and only if the graph has a directed spanning tree.
The common value is the average when the digraph is moreover balanced.

## Explanations

### L1 human

Each agent repeatedly moves its value toward the values of its neighbours.
If the network is connected, the disagreements die out and everyone ends up at the same value.
The total never changes, so that common value is the average of the starting values.
How fast agreement happens is measured by one number of the network, its algebraic connectivity $\lambda_2$.

### L2 human

The result is the basic model of distributed averaging, flocking and sensor fusion in multi-agent systems.
Its proof is a spectral argument on the [[Laplacian matrix|TN6M6DVZRP]], so the rate depends on the algebraic connectivity, which is small for long paths and large for well connected graphs.
Discrete-time versions use $x(k+1) = (I - \varepsilon L) x(k)$, which converges to the average when $G$ is connected and $0 < \varepsilon < 2/\lambda_n$, with $\lambda_n$ the largest eigenvalue of $L$.
Variants allow edge weights, switching graphs and communication delays.
