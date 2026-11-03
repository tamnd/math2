---
tag: XZR1FVGMKZ
kind: definition
name: DeGroot learning
msc: [91D30, 91D15, 60J20]
defines: YRRS4BWA6Z
uses: [0G48PYM96Q, 62NS7PV1M9, 0KFYGSHHF5]
sources:
  - url: https://en.wikipedia.org/wiki/DeGroot_learning
---

## Definition

Let $n \ge 1$ agents be indexed by $1, \dots, n$.
Let $T = (T_{ij})$ be a row-stochastic $n \times n$ real matrix: $T_{ij} \ge 0$ for all $i, j$ and $\sum_{j=1}^{n} T_{ij} = 1$ for each $i$.
The entry $T_{ij}$ is the weight agent $i$ puts on agent $j$.
Let $p(0) \in \R^n$ be the vector of initial opinions.
*DeGroot learning* is the process
$$p(t+1) = T \, p(t) \qquad (t = 0, 1, 2, \dots),$$
so that $p(t) = T^t p(0)$.
The agents *reach a consensus* if $p(t)$ converges to a vector with all coordinates equal.

## Remarks

Call $T$ primitive if $T^m$ has all entries positive for some $m \ge 1$.
If $T$ is primitive, the [[Perron–Frobenius theorem|62NS7PV1M9]] shows that $T^t$ converges to the matrix $\mathbf{1}\pi^{\mathsf T}$.
Here $\pi$ is the unique probability vector with $\pi^{\mathsf T} T = \pi^{\mathsf T}$.
So every opinion converges to $\pi^{\mathsf T} p(0) = \sum_j \pi_j p_j(0)$, and $\pi_j$ measures the influence of agent $j$.
Example: $n = 2$, $T = \begin{pmatrix} 1/2 & 1/2 \\ 1/2 & 1/2 \end{pmatrix}$ and $p(0) = (0, 1)$ give $p(1) = (1/2, 1/2)$, a consensus at once.
Non-example of consensus: $T = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is row-stochastic but not primitive, and $p(0) = (0, 1)$ gives opinions that swap forever.
The matrix $T$ is the transition matrix of a [[Markov chain|0G48PYM96Q]], and its positive entries define a [[directed graph|0KFYGSHHF5]] of who listens to whom.
