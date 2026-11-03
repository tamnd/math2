---
tag: JPE8WBW7KP
kind: definition
name: Hopfield network
msc: [92B20, 68T07, 82C32]
defines: 4F93W6QJP7
uses: [0VR671PHE5, 01REYCJ371, R6QVS6P21N, VQZVSFF179]
sources:
  - url: https://en.wikipedia.org/wiki/Hopfield_network
---

## Definition

Let $n \ge 1$, let $W = (w_{ij})$ be a real [[symmetric matrix|0VR671PHE5]] of size $n \times n$ with $w_{ii} = 0$ for all $i$, and let $\theta \in \R^n$ be a vector of thresholds.
The *Hopfield network* with weights $W$ and thresholds $\theta$ has state space $\set{-1, 1}^n$.
Its asynchronous dynamics updates one unit $i$ at a time by
$$s_i \leftarrow \begin{cases} 1 & \text{if } \sum_{j} w_{ij} s_j > \theta_i, \\ -1 & \text{if } \sum_{j} w_{ij} s_j < \theta_i, \\ s_i & \text{otherwise,} \end{cases}$$
and leaves the other units unchanged.
Its *energy* is
$$H(s) = -\frac{1}{2} \sum_{i, j} w_{ij} s_i s_j + \sum_i \theta_i s_i.$$

## Remarks

If unit $i$ changes from $s_i$ to $s_i'$, then $H$ changes by $-(s_i' - s_i)\big(\sum_j w_{ij} s_j - \theta_i\big) < 0$, using $w_{ij} = w_{ji}$ and $w_{ii} = 0$.
So $H$ is a [[Lyapunov function|01REYCJ371]] for the dynamics, and after finitely many changes the state is a [[fixed point|R6QVS6P21N]] of every update.
Example: for patterns $\xi^1, \dots, \xi^p \in \set{-1, 1}^n$, the [[Hebbian|VQZVSFF179]] weights $w_{ij} = \frac{1}{n} \sum_{\mu} \xi^\mu_i \xi^\mu_j$ for $i \ne j$, $w_{ii} = 0$, with $\theta = 0$, give a Hopfield network.
With one pattern ($p = 1$) and $n \ge 2$, the state $\xi^1$ is fixed, since $\sum_j w_{ij} \xi^1_j = \frac{n-1}{n} \xi^1_i$ has the sign of $\xi^1_i$.
Non-example: a network with $w_{12} = 1$ and $w_{21} = -1$ is not a Hopfield network, because $W$ is not symmetric; with two units and synchronous updates it can cycle forever.
With Hebbian weights and many random patterns, recall works only while $p$ stays below roughly $0.14\, n$.
