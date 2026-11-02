---
tag: SH7P72TJW8
kind: definition
name: Singular homology
msc: [55N10]
defines: M0Q5CFJ7ZH
uses: [0CNQXVBHCX, 0SY9ECQ19Q, 0WJX8MGG37]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_homology
---

## Definition

Let $X$ be a [[topological space|0CNQXVBHCX]].
For $n \ge 0$ let $\Delta^n = \set{(t_0, \dots, t_n) \in \R^{n+1} : t_i \ge 0, \ \sum_i t_i = 1}$ be the standard $n$-simplex, and for $0 \le i \le n$ let $\delta^i \colon \Delta^{n-1} \to \Delta^n$ be the map that inserts a $0$ in position $i$.
A *singular $n$-simplex* in $X$ is a [[continuous map|0SY9ECQ19Q]] $\sigma \colon \Delta^n \to X$.
Let $S_n(X)$ be the [[free abelian group|0WJX8MGG37]] on the singular $n$-simplices, and $S_n(X) = 0$ for $n < 0$.
The boundary map $\partial_n \colon S_n(X) \to S_{n-1}(X)$ is given on generators by
$$\partial_n \sigma = \sum_{i=0}^{n} (-1)^i \, \sigma \circ \delta^i,$$
and $\partial_0 = 0$.
Then $\partial_n \circ \partial_{n+1} = 0$, so $S_\bullet(X)$ is a chain complex.
The *$n$-th singular homology group* of $X$ is
$$H_n(X) = \ker \partial_n / \operatorname{im} \partial_{n+1}.$$

## Remarks

A continuous map $f \colon X \to Y$ induces $f_* \colon H_n(X) \to H_n(Y)$ by $\sigma \mapsto f \circ \sigma$, and homotopic maps induce the same homomorphism.
Homology with coefficients in an abelian group $A$ uses $S_n(X) \otimes A$.

Example: let $X$ be a point.
There is exactly one singular $n$-simplex $\sigma_n$ for each $n$, and $\partial_n \sigma_n = \sum_{i=0}^n (-1)^i \sigma_{n-1}$, which is $\sigma_{n-1}$ for even $n \ge 2$ and $0$ for odd $n$.
So $\partial_n$ is an isomorphism for even $n \ge 2$ and zero for odd $n$, which gives $H_0(X) \cong \Z$ and $H_n(X) = 0$ for $n \ge 1$.

Non-example: using all functions $\Delta^n \to X$, continuous or not, in place of singular simplices still gives a chain complex, but not singular homology.
Any two points of $X$ are then joined by a $1$-simplex, so its $H_0$ is $\Z$ for every nonempty $X$.
For $X$ a discrete space with two points, singular homology gives $H_0(X) \cong \Z^2$.
