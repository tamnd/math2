---
tag: ZYDN0V3WWY
kind: definition
name: Littelmann path model
msc: [17B10, "05E10"]
defines: 8MZDQR6G45
uses: [EY9DN7QAX1, BB098JPWGA, CSBM217V1N, XV6Q01FVAS, C5W8BE1DRY, KFVNC2W720]
sources:
  - url: https://en.wikipedia.org/wiki/Littelmann_path_model
---

## Definition

Let $\mathfrak{g}$ be a complex [[semisimple Lie algebra|EY9DN7QAX1]] with [[Cartan subalgebra|BB098JPWGA]] $\mathfrak{h}$ and [[simple roots|CSBM217V1N]] $\alpha_1, \dots, \alpha_r$.
Let $X \subset \mathfrak{h}^*$ be the weight lattice, let $X_\R$ be its real span, and let $\alpha^\vee$ be the [[coroot|XV6Q01FVAS]] of a simple root $\alpha$.
A *path* is a piecewise linear map $\pi \colon [0, 1] \to X_\R$ with $\pi(0) = 0$, taken up to reparametrisation.
For a path $\pi$ and a simple root $\alpha$, put $h(t) = \ip{\pi(t)}{\alpha^\vee}$ and let $m$ be the minimum of $h$ on $[0, 1]$.
The *root operator* $f_\alpha$ is defined as follows.

1. If $h(1) - m < 1$, then $f_\alpha \pi = 0$.
2. Otherwise let $t_0$ be the largest $t$ with $h(t) = m$, and $t_1$ the smallest $t \ge t_0$ with $h(t) = m + 1$.
3. Then $f_\alpha \pi(t) = \pi(t)$ for $t \le t_0$, $f_\alpha \pi(t) = \pi(t_0) + s_\alpha(\pi(t) - \pi(t_0))$ for $t_0 \le t \le t_1$, and $f_\alpha \pi(t) = \pi(t) - \alpha$ for $t \ge t_1$.

Here $s_\alpha(x) = x - \ip{x}{\alpha^\vee} \alpha$ is the simple reflection.
For a dominant integral weight $\lambda$, let $\pi_\lambda(t) = t\lambda$.
The *path model* of $\lambda$ is the set $B(\lambda)$ of nonzero paths $f_{\alpha_{i_1}} \cdots f_{\alpha_{i_k}} \pi_\lambda$, over all $k \ge 0$ and all sequences of simple roots.

## Remarks

Littelmann's character formula states $\operatorname{ch} L(\lambda) = \sum_{\pi \in B(\lambda)} e^{\pi(1)}$, where $L(\lambda)$ is the irreducible module of [[highest weight|C5W8BE1DRY]] $\lambda$.
The same formula holds if $\pi_\lambda$ is replaced by any path from $0$ to $\lambda$ that stays in the dominant chamber.
Example: for $\mathfrak{sl}_2(\C)$, identify $X_\R$ with $\R$ by $\lambda \mapsto \lambda(h)$, so that $\alpha = 2$ and $\ip{x}{\alpha^\vee} = x$.
For $\pi_n(t) = nt$ one finds that $f_\alpha^k \pi_n$ goes down to $-k$ and then up, ending at $n - 2k$, for $0 \le k \le n$.
For $k = n$ the end value is $-n$ and the minimum is $-n$, so clause 1 gives $f_\alpha^{n+1} \pi_n = 0$.
The endpoints $n, n - 2, \dots, -n$ are the [[weights|KFVNC2W720]] of $L(n)$, each with multiplicity one.
Non-example: the path $\pi(t) = -t$ does not stay in the dominant chamber, and $f_\alpha \pi = 0$ by clause 1.
Its set of endpoints is $\set{-1}$, which is not the set of weights of any representation.
