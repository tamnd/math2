---
tag: JYYGCVH387
kind: definition
name: Cluster expansion
msc: [82B05, 82B21, 82B20]
defines: XH2XEVGNSK
uses: [T4FZCAQC0D, 1C5S72A9JX, 0KWFFMDF8T, 0MZB06ST2B]
sources:
  - url: https://en.wikipedia.org/wiki/Cluster_expansion
---

## Definition

Let $\varphi \colon \R^d \to \R \cup \set{+\infty}$ be an even measurable pair potential that is bounded below, let $\beta > 0$, and let $f$ be its [[Mayer f-function|T4FZCAQC0D]], with $f_{ij} = f(x_i - x_j)$.
For a bounded region $\Lambda \subset \R^d$ and an activity $z > 0$, the [[grand canonical|1C5S72A9JX]] partition function is
$$\Xi_\Lambda(z) = \sum_{n \ge 0} \frac{z^n}{n!} \int_{\Lambda^n} \prod_{1 \le i < j \le n} (1 + f_{ij}) \, dx_1 \cdots dx_n.$$
For $n \ge 1$, let $\mathcal{C}_n$ be the set of [[connected graphs|0KWFFMDF8T]] with vertex set $\set{1, \dots, n}$.
The *cluster expansion* (Mayer expansion) of $\ln \Xi_\Lambda$ is the [[power series|0MZB06ST2B]]
$$\ln \Xi_\Lambda(z) = \sum_{n \ge 1} \frac{z^n}{n!} \int_{\Lambda^n} \sum_{G \in \mathcal{C}_n} \prod_{\set{i, j} \in E(G)} f_{ij} \, dx_1 \cdots dx_n.$$
It holds as an identity of formal power series in $z$.

## Remarks

In the thermodynamic limit it becomes $\beta p = \sum_{n \ge 1} b_n z^n$, with $b_n = \frac{1}{n!} \int_{(\R^d)^{n - 1}} \sum_{G \in \mathcal{C}_n} \prod_{\set{i,j} \in E(G)} f_{ij} \, dx_2 \cdots dx_n$ and $x_1 = 0$.
Here $p$ is the pressure, and the $b_n$ are the Mayer cluster coefficients.
Example: there is one connected graph on one vertex and one on two vertices, so $b_1 = 1$ and $b_2 = \frac{1}{2} \int_{\R^d} f(x) \, dx$.
Non-example: the sum over all graphs, connected or not, gives $\Xi_\Lambda$ itself rather than its logarithm, so it is not the cluster expansion.
For stable and regular pair potentials the series for $\beta p$ has a positive radius of convergence.
Abstract polymer versions replace particles by polymers and $f$ by an incompatibility relation.
