---
tag: W9V9JSAWYK
kind: example
name: Laplacian on the Sierpiński gasket
msc: ["31E05", "28A80"]
illustrates: [VXB4G47Z3T]
sources:
  - url: https://en.wikipedia.org/wiki/Analysis_on_fractals
---

## Example

Let $p_1, p_2, p_3$ be the vertices of an equilateral triangle in $\R^2$ and let $F_i(x) = (x + p_i)/2$ for $i = 1, 2, 3$.
The Sierpiński gasket $K$ is the unique nonempty compact set with $K = F_1(K) \cup F_2(K) \cup F_3(K)$, the attractor of this [[iterated function system|75B8VHDGSA]].
Let $V_0 = \set{p_1, p_2, p_3}$ and $V_{m+1} = F_1(V_m) \cup F_2(V_m) \cup F_3(V_m)$.
Let $\Gamma_m$ be the graph on $V_m$ in which $x \sim_m y$ when $x$ and $y$ are two vertices of one triangle $F_{w_1} \circ \cdots \circ F_{w_m}(\text{triangle } p_1 p_2 p_3)$.
For $u \colon V_m \to \R$, set
$$\mathcal{E}_m(u) = \left(\frac{5}{3}\right)^m \sum_{x \sim_m y} (u(x) - u(y))^2,$$
the sum over edges of $\Gamma_m$.

The factor $5/3$ is the one that makes these energies compatible.
Take $u(p_1) = 1$ and $u(p_2) = u(p_3) = 0$, so $\mathcal{E}_0(u) = 2$.
Among all extensions of $u$ to $V_1$, the one of least energy $\mathcal{E}_1$ follows the "$1/5$–$2/5$ rule".
At the midpoint of $p_j p_k$ its value is $(2 u(p_j) + 2 u(p_k) + u(p_i))/5$, where $i$ is the third index.
Here this gives $2/5$ at the midpoints of $p_1 p_2$ and $p_1 p_3$, and $1/5$ at the midpoint of $p_2 p_3$.
The three small triangles contribute $18/25$, $6/25$ and $6/25$ to the sum, in total $6/5$, and $(5/3) \cdot (6/5) = 2 = \mathcal{E}_0(u)$.

Because of this compatibility, $\mathcal{E}_m(u|_{V_m})$ is nondecreasing in $m$ for every $u$, and its limit $\mathcal{E}(u)$ is a [[resistance form|THCM7DWHNY]] on $K$.
Let $\mu$ be the self-similar probability measure that gives mass $3^{-m}$ to each level-$m$ cell.
For a suitable function $u$ and a point $x \in V_m \setminus V_0$, the Laplacian of $u$ with respect to $\mu$ is
$$\Delta_\mu u(x) = \frac{3}{2} \lim_{m \to \infty} 5^m \sum_{y \sim_m x} (u(y) - u(x)).$$
The factor $5^m = (5/3)^m \cdot 3^m$ combines the energy scaling with the measure scaling.
The function on $V_1$ found above satisfies $\sum_{y \sim_1 x} (u(y) - u(x)) = 0$ at each of the three midpoints.
For example, at the midpoint of $p_2 p_3$ the neighbours have values $0, 0, 2/5, 2/5$, and $4/5 - 4 \cdot (1/5) = 0$.
Its continuation by the same rule at all levels is a harmonic function on $K$, that is, $\Delta_\mu u = 0$ off $V_0$.

## Remarks

The eigenvalue counting function of $-\Delta_\mu$ with Dirichlet conditions on $V_0$ grows like $\lambda^{d_s/2}$ up to bounded factors, with spectral dimension $d_s = 2 \log 3 / \log 5 \approx 1.365$.
This differs from the [[Hausdorff dimension|SSNFTHZ6YJ]] $\log 3 / \log 2 \approx 1.585$ of the gasket.

## Explanations

### L1 human

The Sierpiński gasket is a triangle with holes at every scale, so ordinary derivatives make no sense on it.
Instead, one looks at finer and finer triangle networks inside the gasket and computes how the value at each vertex differs from the values at its neighbours.
A small calculation on a single triangle shows that energies must be multiplied by $5/3$ at each step for the networks to agree.
With this scaling the network Laplacians converge, and their limit is the Laplacian of the gasket.
Harmonic functions are then easy to compute: the value at each new midpoint is a fixed mix of $2/5$, $2/5$ and $1/5$ of the corner values.
