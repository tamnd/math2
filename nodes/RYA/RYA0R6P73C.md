---
tag: RYA0R6P73C
kind: definition
name: Height function
msc: [11G50, 14G40]
defines: F1FF505PWH
uses: [MWBDFS2KJ5, BT5V3TSNY6, 0MNF0BYFQC]
sources:
  - url: https://en.wikipedia.org/wiki/Height_function
---

## Definition

Let $\overline{\Q}$ be an algebraic closure of $\Q$ and let $n \ge 1$.
Let $P = [x_0 : \cdots : x_n] \in \mathbb{P}^n(\overline{\Q})$ be a point of projective space, and let $K$ be an [[algebraic number field|MWBDFS2KJ5]] that contains $x_0, \ldots, x_n$.
For each [[place|BT5V3TSNY6]] $v$ of $K$, let $\abs{\cdot}_v$ be the absolute value of $v$ that extends the usual or a $p$-adic absolute value of $\Q$.
Let $n_v = [K_v : \Q_v]$ be the local degree.
The *absolute logarithmic height* of $P$ is
$$h(P) = \frac{1}{[K : \Q]} \sum_{v} n_v \log \max\left(\abs{x_0}_v, \ldots, \abs{x_n}_v\right).$$
It does not depend on the choice of $K$ or of homogeneous coordinates.

More generally, let $V$ be a projective variety over $\overline{\Q}$ and let $\phi \colon V \to \mathbb{P}^n$ be a morphism.
The *height function* relative to $\phi$ is $h_\phi = h \circ \phi \colon V(\overline{\Q}) \to \R$.
The height of an [[algebraic number|0MNF0BYFQC]] $\alpha$ is $h(\alpha) = h([1 : \alpha])$.

## Remarks

Independence of the coordinates follows from the product formula $\prod_v \abs{x}_v^{n_v} = 1$ for $x \in K^\times$.

Example: for $P = [a_0 : \cdots : a_n] \in \mathbb{P}^n(\Q)$ with $a_i \in \Z$ and $\gcd(a_0, \ldots, a_n) = 1$, take $K = \Q$.
Each $p$-adic term is $\log 1 = 0$, since some $a_i$ is not divisible by $p$, so $h(P) = \log \max_i \abs{a_i}$.
For the rational number $2/3$, that is $[3 : 2]$, this gives $h = \log 3$.

Non-example: the rule $P \mapsto \log \max_i \abs{a_i}$ for arbitrary integer coordinates, without the coprimality condition, is not a function on $\mathbb{P}^n(\Q)$.
The coordinates $[1 : 1]$ and $[2 : 2]$ give the same point but the values $\log 1$ and $\log 2$.

Northcott's theorem: for all $B$ and $d$, the set of $P \in \mathbb{P}^n(\overline{\Q})$ with $h(P) \le B$ and $[\Q(P) : \Q] \le d$ is finite.
The multiplicative height is $H = e^h$.
On an elliptic curve, the Néron–Tate height $\hat{h}(P) = \lim_{m \to \infty} 4^{-m} h_x(2^m P)$, with $h_x$ the height relative to the $x$-coordinate, is a positive semi-definite quadratic form on $E(\overline{\Q})$; some authors include a factor $\frac{1}{2}$.
