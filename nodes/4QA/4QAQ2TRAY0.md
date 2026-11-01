---
tag: 4QAQ2TRAY0
kind: definition
name: Percolation theory
msc: [60K35, 82B43]
defines: BH7YPXCYDK
uses: [00C0BR7D7H, 0JG9W3KA6B, 059TJN0NZ1]
sources:
  - url: https://en.wikipedia.org/wiki/Percolation_theory
---

## Definition

Let $G = (V, E)$ be a [[graph|00C0BR7D7H]] with countably many vertices, each of finite degree, and let $p \in [0, 1]$.
*Bernoulli bond percolation* on $G$ with parameter $p$ is the product [[probability measure|059TJN0NZ1]] $P_p$ on $\Omega = \set{0, 1}^E$.
Under $P_p$ the coordinates $\omega(e)$, $e \in E$, are independent and $P_p(\omega(e) = 1) = p$.
An edge $e$ is *open* if $\omega(e) = 1$ and *closed* otherwise.
The *open cluster* $C(x)$ of a vertex $x$ is the vertex set of the [[connected component|0JG9W3KA6B]] of $x$ in the subgraph $(V, \set{e : \omega(e) = 1})$.
For a fixed vertex $o$, the *percolation probability* is $\theta(p) = P_p(\abs{C(o)} = \infty)$.
Site percolation is defined in the same way, with open and closed vertices in place of edges.
Percolation theory is the study of these random clusters.

## Remarks

Example: on the line graph $\Z$, a cluster is infinite only if all edges on one side of $o$ up to infinity are open.
This has probability $\lim_n p^n = 0$ for $p < 1$, so $\theta(p) = 0$ for $p < 1$ and $\theta(1) = 1$.
Non-example: a random subgraph in which two edges at the same vertex are never both open is not Bernoulli percolation, since its edge states are not independent.
The function $\theta$ is nondecreasing in $p$, by coupling all $P_p$ with one family of uniform random variables on $[0, 1]$.
