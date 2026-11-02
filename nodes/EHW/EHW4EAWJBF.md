---
tag: EHW4EAWJBF
kind: definition
name: Multiresolution analysis
msc: [42C40, 65T60]
defines: 1GHQMBR7DE
uses: [SASP14MA1Z, 0S9GGTR0EX, 0BSJSX7ME2]
sources:
  - url: https://en.wikipedia.org/wiki/Multiresolution_analysis
---

## Definition

A *multiresolution analysis* of $L^2(\R)$ (see [[Lp space|SASP14MA1Z]]) is a sequence $(V_j)_{j \in \Z}$ of closed linear subspaces of $L^2(\R)$ with these properties.

1. Nesting: $V_j \subseteq V_{j+1}$ for all $j \in \Z$.
2. Scaling: for all $j \in \Z$ and $f \in L^2(\R)$, $f \in V_j$ if and only if the function $x \mapsto f(2x)$ lies in $V_{j+1}$.
3. Separation and density: $\bigcap_{j \in \Z} V_j = \set{0}$, and $\bigcup_{j \in \Z} V_j$ is [[dense|0BSJSX7ME2]] in $L^2(\R)$.
4. Scaling function: there is $\varphi \in V_0$ such that the translates $(\varphi(\cdot - k))_{k \in \Z}$ form an [[orthonormal basis|0S9GGTR0EX]] of $V_0$.

## Remarks

Some authors only ask in clause 4 that the translates of $\varphi$ form a Riesz basis of $V_0$; an orthonormalization step then yields a function as in clause 4.
Clauses 1 to 3 imply that $f \in V_0$ if and only if $f(2^j \cdot) \in V_j$.
Let $W_j$ be the orthogonal complement of $V_j$ in $V_{j+1}$.
Then $L^2(\R)$ is the orthogonal direct sum of all $W_j$.
There is an orthonormal [[wavelet|4PZ35C0GV3]] $\psi$ whose integer translates form an orthonormal basis of $W_0$.

Example: let $V_j$ be the set of $f \in L^2(\R)$ that are constant on each interval $[k 2^{-j}, (k+1) 2^{-j})$, $k \in \Z$.
Nesting and scaling are clear, and step functions on dyadic intervals are dense in $L^2(\R)$.
A function in every $V_j$ is constant on $[0, 2^{-j})$ and on $[-2^{-j}, 0)$ for all $j \le 0$, hence constant on $[0, \infty)$ and on $(-\infty, 0)$, hence $0$ since it is square-integrable.
With $\varphi = 1_{[0, 1)}$, clause 4 holds; this is the Haar multiresolution analysis.

Non-example: $V_j = L^2(\R)$ for all $j$ satisfies nesting, scaling and density, but $\bigcap_j V_j = L^2(\R) \ne \set{0}$, so separation fails.
