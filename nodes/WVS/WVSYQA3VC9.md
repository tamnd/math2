---
tag: WVSYQA3VC9
kind: statement
role: proposition
name: Ihara's formula
sources:
  - wikipedia: en:1342362@r1367258385
    locator: Ihara zeta function, section Ihara's formula
    note: adopted
    mention: wikipedia://en/1342362#VQFM
    sections: [Statement]
inventory: [XFGTEN5NXG]
---

## Statement

Ihara (and Sunada in the graph-theoretic setting) showed that for regular graphs the zeta function is a rational function. If $G$ is a $q+1$-regular graph with [[adjacency matrix|08B9CX109G]] $A$ then

$$\zeta_G(u) = \frac{1}{(1-u^2)^{r(G)-1}\det(I - Au + qu^2I)},$$

where $r(G)$ is the circuit rank of $G$. If $G$ is connected and has $n$ vertices, $r(G)-1=(q-1)n/2$.

The Ihara zeta-function is in fact always the reciprocal of a graph polynomial:

$$\zeta_G(u) = \frac{1}{\det (I-Tu)}~,$$

where $T$ is Ki-ichiro Hashimoto's edge adjacency operator. Hyman Bass gave a determinant formula involving the adjacency operator.
