---
tag: 8JZZNXKWCX
kind: definition
name: Little q-Jacobi polynomials
msc: [33D45, 33C45]
defines: Z4NV7VK9T9
uses: [EB4N9RQR51, Y1X8ZZQ7VM]
sources:
  - url: https://en.wikipedia.org/wiki/Little_q-Jacobi_polynomials
---

## Definition

Let $0 < q < 1$, let $a, b$ be real numbers, and let $n \ge 0$ be an integer.
Write $(c; q)_k$ for the [[q-Pochhammer symbol|Y1X8ZZQ7VM]].
Assume $aq^{j} \ne 1$ for $j = 1, \ldots, n$.
The *little $q$-Jacobi polynomial* of degree $n$ is
$$p_n(x; a, b \mid q) = {}_2\phi_1\!\left( \begin{matrix} q^{-n}, \; abq^{n+1} \\ aq \end{matrix} ; q, \, qx \right) = \sum_{k=0}^{n} \frac{(q^{-n}; q)_k \, (abq^{n+1}; q)_k}{(aq; q)_k \, (q; q)_k} (qx)^k,$$
where ${}_2\phi_1$ is the [[basic hypergeometric series|EB4N9RQR51]].
The series stops at $k = n$, because $(q^{-n}; q)_k = 0$ for $k > n$.

## Remarks

Orthogonality: if $0 < aq < 1$ and $bq < 1$, then for $m \ne n$
$$\sum_{k=0}^{\infty} \frac{(bq; q)_k}{(q; q)_k} (aq)^k \, p_m(q^k) \, p_n(q^k) = 0,$$
and the weights $\frac{(bq; q)_k}{(q; q)_k} (aq)^k$ are positive.

Example: for $n = 1$ the sum has two terms, and $(1 - q^{-1}) q / (1 - q) = -1$ gives
$$p_1(x) = 1 - \frac{1 - abq^2}{1 - aq} \, x.$$
Check of orthogonality to $p_0 = 1$ when $b = 0$: the weights are $w_k = (aq)^k / (q; q)_k$, and the $q$-binomial theorem gives $\sum_k w_k = 1/(aq; q)_\infty$ and $\sum_k w_k q^k = 1/(aq^2; q)_\infty$.
So $\sum_k w_k p_1(q^k) = \frac{1}{(aq; q)_\infty} - \frac{1}{(1 - aq)(aq^2; q)_\infty} = 0$, since $(aq; q)_\infty = (1 - aq)(aq^2; q)_\infty$.

Non-example: for $b = 0$ the monomial $x$ is not the little $q$-Jacobi polynomial of degree $1$, since $x$ is not orthogonal to $p_0 = 1$ for these positive weights: $\sum_k w_k q^k > 0$.

Limit: $\lim_{q \to 1} p_n(x; q^\alpha, q^\beta \mid q) = P_n^{(\alpha, \beta)}(1 - 2x) / P_n^{(\alpha, \beta)}(1)$, where $P_n^{(\alpha,\beta)}$ is the [[Jacobi polynomial|TRD7DSF2KR]].
