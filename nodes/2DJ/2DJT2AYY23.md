---
tag: 2DJT2AYY23
kind: definition
name: Köthe–Toeplitz dual
msc: [46A45]
defines: VJVDDR8BCE
uses: [XYTN19EPF2, 0CVVKY7GY2, 08P6T2WH6R]
sources:
  - url: https://en.wikipedia.org/wiki/Beta-dual_space
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, let $\omega$ be the space of all sequences in $\mathbb{K}$, and let $X \subseteq \omega$ be a [[sequence space|XYTN19EPF2]].
The *$\alpha$-dual* of $X$ is
$$X^\alpha = \set{a \in \omega : \textstyle\sum_{n} \abs{a_n x_n} < \infty \text{ for every } x \in X}.$$
The *$\beta$-dual* of $X$ is
$$X^\beta = \set{a \in \omega : \textstyle\sum_{n} a_n x_n \text{ converges for every } x \in X}.$$
The $\alpha$-dual is called the Köthe–Toeplitz dual of $X$, and the $\beta$-dual is also called the generalized Köthe–Toeplitz dual.

## Remarks

Both duals are sequence spaces, and $X^\alpha \subseteq X^\beta$ because absolutely [[convergent series|0CVVKY7GY2]] converge.
If $X \subseteq Y$, then $Y^\alpha \subseteq X^\alpha$ and $Y^\beta \subseteq X^\beta$.

Example: $(\ell^1)^\alpha = (\ell^1)^\beta = \ell^\infty$, with $\ell^1$ and $\ell^\infty$ as in the [[spaces ℓ^p|08P6T2WH6R]].
If $a$ is bounded, then $\sum \abs{a_n x_n} \le \sup_n \abs{a_n} \sum \abs{x_n}$ for every $x \in \ell^1$.
If $a$ is unbounded, choose indices $n_1 < n_2 < \cdots$ with $\abs{a_{n_k}} \ge k^2$, and let $x_{n_k} = \overline{a_{n_k}} / \abs{a_{n_k}} \cdot k^{-2}$ and $x_n = 0$ otherwise.
Then $x \in \ell^1$, but the terms $a_{n_k} x_{n_k} = \abs{a_{n_k}} k^{-2} \ge 1$ do not tend to $0$, so $a \notin (\ell^1)^\beta$.

Non-example: $a = (n)_{n \ge 1}$ is not in $(\ell^1)^\beta$; for $x_n = 1/n^2$ the series $\sum a_n x_n = \sum 1/n$ diverges.

Other standard values: $\omega^\beta$ is the space $\varphi$ of sequences with finitely many nonzero terms, $\varphi^\beta = \omega$, and $(c_0)^\beta = (\ell^\infty)^\beta = \ell^1$.
