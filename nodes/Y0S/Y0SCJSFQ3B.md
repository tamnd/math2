---
tag: Y0SCJSFQ3B
kind: definition
name: Toric ideal
msc: [13F65, 14M25]
defines: XZBPKQWD0P
uses: [04C5ZBG1WT, 0SDC934R52, 0VTH8KPCG2, 0JN0SQG2JH, 00MHHZ9SNE]
sources:
  - url: https://en.wikipedia.org/wiki/Toric_ideal
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]], let $d, n \ge 1$, and let $a_1, \ldots, a_n \in \Z^d$.
For $a = (c_1, \ldots, c_d) \in \Z^d$, write $t^a = t_1^{c_1} \cdots t_d^{c_d}$ in the Laurent polynomial ring $k[t_1^{\pm 1}, \ldots, t_d^{\pm 1}]$.
Let $\varphi \colon k[x_1, \ldots, x_n] \to k[t_1^{\pm 1}, \ldots, t_d^{\pm 1}]$ be the $k$-algebra [[homomorphism|0VTH8KPCG2]] with $\varphi(x_i) = t^{a_i}$.
The *toric ideal* of $A = (a_1, \ldots, a_n)$ is the [[kernel|0JN0SQG2JH]] $I_A = \ker \varphi$.

## Remarks

The ideal $I_A$ is [[prime|00MHHZ9SNE]], since $k[x_1, \ldots, x_n]/I_A$ is isomorphic to a subring of a domain.
Let $A$ also denote the $d \times n$ integer matrix with columns $a_i$.
Then $I_A$ is generated, as a $k$-vector space and hence as an ideal, by the binomials $x^u - x^v$ with $u, v \in \N^n$ and $Au = Av$.

Example: $d = 2$, $n = 3$ and $a_1 = (1, 0)$, $a_2 = (1, 1)$, $a_3 = (1, 2)$, so $\varphi(x_1) = t_1$, $\varphi(x_2) = t_1 t_2$, $\varphi(x_3) = t_1 t_2^2$.
Since $\varphi(x_1 x_3) = t_1^2 t_2^2 = \varphi(x_2^2)$, the binomial $x_1 x_3 - x_2^2$ lies in $I_A$, and in fact $I_A = (x_1 x_3 - x_2^2)$.

Non-example: if the characteristic of $k$ is not $2$, the binomial ideal $(x^2 - y^2)$ of $k[x, y]$ is not a toric ideal.
It is not prime, because $(x - y)(x + y) \in (x^2 - y^2)$ while neither factor is.
