---
tag: 0TKZCSGCCA
kind: definition
name: Minimum degree
msc: [05C07]
defines: 0ZFZ8ZG3EN
uses: [0T0F6CCS9W]
sources:
  - url: https://en.wikipedia.org/wiki/Degree_(graph_theory)
    locator: Special values
---

## Definition

Let $G$ be a finite [[graph|0JD5C82QMB]] with a nonempty vertex set $V$.
The minimum degree of $G$ is
$$\delta(G) = \min_{v \in V} \deg(v),$$
the smallest [[degree|0T0F6CCS9W]] of a vertex of $G$.

## Remarks

The [[maximum degree|0KNAN9F27P]] $\Delta(G)$ is the largest degree. Always $\delta(G) \le \Delta(G)$.
Each [[cycle graph|0QQ0F12962]] has $\delta = 2$, and each tree with at least two vertices has $\delta = 1$.
A condition on $\delta(G)$ gives a Hamiltonian cycle in [[Dirac's theorem|0TC99BRSSB]].

## Explanations

### L1 human

The minimum degree is the smallest number of edges at any vertex.
If $\delta(G) = 3$, then each vertex has at least three neighbours.
