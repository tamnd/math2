---
tag: NJWE69ZN4B
kind: definition
name: Gene regulatory network
msc: [92C42, 92C40]
defines: NP473H6VVV
uses: [0KFYGSHHF5, 0NT64JV96A, W9X8CVFSQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Gene_regulatory_network
---

## Definition

A *gene regulatory network* on a finite set $V$ of genes is a signed [[directed graph|0KFYGSHHF5]] $(V, A, \sigma)$.
An arc $(j, i) \in A$ means that the product of gene $j$ regulates the expression of gene $i$.
The sign $\sigma \colon A \to \set{+1, -1}$ marks each arc as activation ($+1$) or repression ($-1$).
A *continuous model* of the network is a system of [[ordinary differential equations|0NT64JV96A]]
$$\frac{dx_i}{dt} = f_i\big(x_{j} : (j, i) \in A\big) - \gamma_i\, x_i, \qquad i \in V.$$
Here $x_i \ge 0$ is the concentration of the product of gene $i$ and $\gamma_i > 0$ is its degradation rate.
Each $f_i \ge 0$ is increasing in $x_j$ when $\sigma(j, i) = +1$ and decreasing in $x_j$ when $\sigma(j, i) = -1$.

## Remarks

The functions $f_i$ are often built from [[Hill functions|W9X8CVFSQ2]].
Example: the toggle switch has $V = \set{1, 2}$, arcs $(1, 2)$ and $(2, 1)$ both with sign $-1$, and the model $\dot x_1 = \alpha/(1 + x_2^n) - x_1$, $\dot x_2 = \alpha/(1 + x_1^n) - x_2$.
Each $f_i$ is decreasing in its argument, as required, and for $n \ge 2$ and $\alpha$ large enough the model has two stable equilibria.
Non-example: a model with $\dot x_1 = x_2 - x_1$ for an arc $(2, 1)$ marked $-1$ is not consistent with the graph, since $f_1$ increases in $x_2$.
A network may also be modelled by a Boolean network, in which each gene is on or off.
