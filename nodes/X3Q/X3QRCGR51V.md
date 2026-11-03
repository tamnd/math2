---
tag: X3QRCGR51V
kind: definition
name: Cavity method
msc: [82B44, 82B20, 60K35]
defines: 2B02SYNNJS
uses: [00C0BR7D7H, 059TJN0NZ1, DG9F3W6MZM]
sources:
  - url: https://en.wikipedia.org/wiki/Cavity_method
---

## Definition

Let $G = (V, E)$ be a finite [[graph|00C0BR7D7H]], and let $\mathcal{X}$ be a finite set.
For each edge $\set{i, j} \in E$, let $\psi_{ij} \colon \mathcal{X} \times \mathcal{X} \to (0, \infty)$.
For each vertex $i \in V$, let $\phi_i \colon \mathcal{X} \to (0, \infty)$.
Let $\mu$ be the [[Gibbs measure|DG9F3W6MZM]] on $\mathcal{X}^V$ with $\mu(x) \propto \prod_{\set{i,j} \in E} \psi_{ij}(x_i, x_j) \prod_{i \in V} \phi_i(x_i)$.
Let $\set{i, j}$ be an edge, and let $G_{ij}$ be the graph $G$ with this edge removed.
The *cavity distribution* $\nu_{i \to j}$ is the marginal law of $x_i$ under the Gibbs measure of $G_{ij}$.
Write $\partial i$ for the set of neighbours of $i$.
The *cavity equations* are
$$\nu_{i \to j}(x_i) = \frac{1}{z_{i \to j}} \, \phi_i(x_i) \prod_{k \in \partial i \setminus \set{j}} \sum_{x_k \in \mathcal{X}} \psi_{ik}(x_i, x_k) \, \nu_{k \to i}(x_k),$$
where $z_{i \to j}$ makes $\nu_{i \to j}$ a [[probability measure|059TJN0NZ1]] on $\mathcal{X}$.
The *cavity method* is the following procedure for a large graph.
It assumes that the cavity distributions satisfy the cavity equations up to a small error.
It solves these equations and computes the marginals and the free energy of $\mu$ from the solution.

## Remarks

If $G$ is a tree, the cavity equations hold exactly.
Indeed, remove the edge $\set{i, j}$ and then the vertex $i$.
The component of $i$ splits into subtrees hanging from the neighbours $k \ne j$, and these subtrees are independent given $x_i$.
Example: on the path $1 - 2 - 3$, the cavity distribution $\nu_{2 \to 3}$ is proportional to $\phi_2(x_2) \sum_{x_1} \psi_{12}(x_2, x_1) \phi_1(x_1)$, since $\nu_{1 \to 2} \propto \phi_1$.

Non-example: on a cycle of length $3$, removing one edge leaves a path.
The two other neighbours of a vertex are still joined there, so the cavity equations are only an approximation.

The version above is called replica symmetric.
On random graphs with many pure states, the one-step replica symmetry breaking cavity method replaces each $\nu_{i \to j}$ by a probability law over cavity distributions.
On trees, the cavity equations are the equations of belief propagation.
