---
tag: 0WCKRBHFFD
kind: definition
name: Clique number
msc: [05C69]
defines: 04MQSQ1F5Q
uses: [0G52BPNPKG]
sources:
  - url: https://en.wikipedia.org/wiki/Clique_(graph_theory)
    locator: Definitions
---

## Definition

Let $G$ be a finite [[graph|0JD5C82QMB]].
The clique number $\omega(G)$ is the largest number of vertices of a [[clique|0G52BPNPKG]] in $G$.

## Remarks

The vertices of a clique need different colours. Thus $\omega(G) \le \chi(G)$, where $\chi(G)$ is the [[chromatic number|0C5M7AM6FH]].
For the [[complete graph|03WKB2H474]], $\omega(K_n) = n$. For the [[cycle graph|0QQ0F12962]] $C_n$ with $n \ge 4$, $\omega(C_n) = 2$.
The inequality $\omega(G) \le \chi(G)$ can be strict: for $C_5$, $\omega = 2$ and $\chi = 3$.

## Explanations

### L1 human

The clique number is the size of the largest group of vertices that are all joined to each other.
It gives a lower bound for the number of colours that a graph needs.
