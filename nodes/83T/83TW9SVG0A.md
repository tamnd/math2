---
tag: 83TW9SVG0A
kind: definition
name: Basic hypergeometric series
msc: [33D15, 05A30]
defines: EB4N9RQR51
uses: [Y1X8ZZQ7VM, 0MZB06ST2B, 09FTAET5Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Basic_hypergeometric_series
---

## Definition

Let $q \in \C$ with $0 < \abs{q} < 1$, let $r, s \ge 0$ be integers, and let $a_1, \dots, a_r, b_1, \dots, b_s \in \C$ with $b_j \ne q^{-m}$ for all $j$ and all integers $m \ge 0$.
Write $(c_1, \dots, c_k; q)_n = (c_1; q)_n \cdots (c_k; q)_n$ with the [[q-Pochhammer symbol|Y1X8ZZQ7VM]].
The *basic hypergeometric series* is the [[power series|0MZB06ST2B]] in $z$
$${}_r\phi_s \left( \begin{matrix} a_1, \dots, a_r \\ b_1, \dots, b_s \end{matrix} ; q, z \right) = \sum_{n=0}^{\infty} \frac{(a_1, \dots, a_r; q)_n}{(b_1, \dots, b_s, q; q)_n} \left( (-1)^n q^{\binom{n}{2}} \right)^{1 + s - r} z^n.$$
The *bilateral basic hypergeometric series* is
$${}_r\psi_s \left( \begin{matrix} a_1, \dots, a_r \\ b_1, \dots, b_s \end{matrix} ; q, z \right) = \sum_{n=-\infty}^{\infty} \frac{(a_1, \dots, a_r; q)_n}{(b_1, \dots, b_s; q)_n} \left( (-1)^n q^{\binom{n}{2}} \right)^{s - r} z^n,$$
where $(a; q)_{-n} = 1 / (a q^{-n}; q)_n$ for $n \ge 1$.

## Remarks

For $r = s + 1$ the series ${}_r\phi_s$ converges for $\abs{z} < 1$; for $r \le s$ it converges for all $z \in \C$.
If some $a_i = q^{-N}$ with an integer $N \ge 0$, then $(a_i; q)_n = 0$ for $n > N$, and the series terminates.
The factor $\left( (-1)^n q^{\binom{n}{2}} \right)^{1+s-r}$ makes the limit $a_r \to \infty$ of ${}_r\phi_s(\dots; q, z/a_r)$ a series ${}_{r-1}\phi_s$.

Example: ${}_1\phi_0(a; -; q, z) = \sum_{n \ge 0} \frac{(a; q)_n}{(q; q)_n} z^n$, and here the ratio of the terms of index $n+1$ and $n$ is $\frac{1 - a q^n}{1 - q^{n+1}}\, z$, a rational function of $q^n$.
By the [[q-binomial theorem|VVT27RB46B]] it equals $\frac{(az; q)_\infty}{(z; q)_\infty}$ for $\abs{z} < 1$.

Non-example: $\sum_{n \ge 0} \frac{z^n}{n!}$ is a hypergeometric series but not a basic one, since the ratio $\frac{z}{n+1}$ is not a rational function of $q^n$.

As $q \to 1$, $\frac{(q^a; q)_n}{(1 - q)^n}$ tends to the Pochhammer symbol $(a)_n$, so ${}_{s+1}\phi_s(q^{a_1}, \dots; q^{b_1}, \dots; q, z)$ tends to ${}_{s+1}F_s(a_1, \dots; b_1, \dots; z)$.
