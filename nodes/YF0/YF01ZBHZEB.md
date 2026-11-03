---
tag: YF01ZBHZEB
kind: definition
name: Bond percolation
msc: [82B43, 60K35]
defines: PZZA8SEXYC
uses: [00C0BR7D7H, 059TJN0NZ1, 0386Y0Z7Y7, 0JG9W3KA6B]
sources:
  - url: https://en.wikipedia.org/wiki/Percolation_theory
---

## Definition

Let $G = (V, E)$ be a [[graph|00C0BR7D7H]] with a countable set of edges $E$, and let $p \in [0, 1]$.
Let $\Omega = \set{0, 1}^E$ carry the product $\sigma$-algebra.
*Bond percolation* on $G$ with parameter $p$ is the product [[probability measure|059TJN0NZ1]] $P_p$ on $\Omega$ defined as follows.
Under $P_p$ the coordinates $\omega(e)$, $e \in E$, are independent.
Each $\omega(e)$ has the [[Bernoulli distribution|0386Y0Z7Y7]] with parameter $p$.
For $\omega \in \Omega$, an edge $e$ is *open* if $\omega(e) = 1$ and *closed* if $\omega(e) = 0$.
The *open cluster* $C(x)$ of a vertex $x$ is the vertex set of the [[connected component|0JG9W3KA6B]] of $x$ in the subgraph $(V, \set{e \in E : \omega(e) = 1})$.

## Remarks

Example: let $G$ be the path with vertices $a, b, c$ and edges $e_1 = \set{a, b}$ and $e_2 = \set{b, c}$.
Then $c \in C(a)$ exactly when $\omega(e_1) = \omega(e_2) = 1$.
By independence, $P_p(c \in C(a)) = p \cdot p = p^2$.

Non-example: on the same path, let $\omega(e_1) = \omega(e_2)$, with this common value equal to $1$ with probability $p$.
Each edge is still open with probability $p$, but the two states are not independent, so this is not bond percolation.
Here $c \in C(a)$ has probability $p$, not $p^2$.

Site percolation is the analogue in which vertices, not edges, are open or closed at random.
For a fixed vertex $o$, the function $\theta(p) = P_p(\abs{C(o)} = \infty)$ is the percolation probability; it is nondecreasing in $p$.
The [[percolation threshold|MP8VSZK19A]] is $p_c = \sup \set{p : \theta(p) = 0}$.
On the square lattice $\Z^2$ with nearest-neighbour edges, $p_c = 1/2$ by [[Kesten's theorem|B8Y0ZRQP17]].
