---
tag: HP97SGN9A3
kind: definition
name: Askey–Wilson polynomials
msc: [33D45, 33D15]
defines: RSNZNG0WA1
uses: [EB4N9RQR51, Y1X8ZZQ7VM]
sources:
  - url: https://en.wikipedia.org/wiki/Askey–Wilson_polynomials
---

## Definition

Let $q \in \C$ with $0 < \abs{q} < 1$, and let $a, b, c, d \in \C$ with $a \ne 0$.
Write $(c_1, \dots, c_k; q)_n = (c_1; q)_n \cdots (c_k; q)_n$ with the [[q-Pochhammer symbol|Y1X8ZZQ7VM]].
For an integer $n \ge 0$ and $x = \cos\theta$, the *Askey–Wilson polynomial* of degree $n$ is
$$p_n(x; a, b, c, d \mid q) = a^{-n} (ab, ac, ad; q)_n\; {}_4\phi_3 \left( \begin{matrix} q^{-n},\ abcd\, q^{n-1},\ a e^{i\theta},\ a e^{-i\theta} \\ ab,\ ac,\ ad \end{matrix} ; q, q \right),$$
where ${}_4\phi_3$ is the terminating [[basic hypergeometric series|EB4N9RQR51]].

## Remarks

Since $(a e^{i\theta}, a e^{-i\theta}; q)_k = \prod_{j=0}^{k-1} (1 - 2 a q^j x + a^2 q^{2j})$, each term is a polynomial in $x$, and $p_n$ is a polynomial of degree at most $n$ with leading coefficient $2^n (abcd\, q^{n-1}; q)_n$.
The factor $a^{-n} (ab, ac, ad; q)_n$ cancels the denominators, and $p_n$ is symmetric in $a, b, c, d$.

Example: $n = 1$.
The ${}_4\phi_3$ has two terms, and since $\frac{(1 - q^{-1})\, q}{1 - q} = -1$,
$$p_1(x) = a^{-1} \left[ (1 - ab)(1 - ac)(1 - ad) - (1 - abcd)(1 - 2ax + a^2) \right] = 2(1 - abcd)\, x + (abc + abd + acd + bcd) - (a + b + c + d).$$

Orthogonality: if $0 < q < 1$ and $a, b, c, d$ are real with absolute values less than $1$, then for $m \ne n$
$$\int_{-1}^{1} p_m(x)\, p_n(x)\, w(x)\, \frac{dx}{\sqrt{1 - x^2}} = 0, \qquad w(\cos\theta) = \frac{(e^{2i\theta}, e^{-2i\theta}; q)_\infty}{(a e^{i\theta}, a e^{-i\theta}, b e^{i\theta}, b e^{-i\theta}, c e^{i\theta}, c e^{-i\theta}, d e^{i\theta}, d e^{-i\theta}; q)_\infty}.$$

Non-example: for parameters as in the orthogonality statement, $x^2$ is not $p_2$, since $p_2$ is orthogonal to the constant $p_0 = 1$ for the positive weight $w$, while $\int x^2 w(x) \frac{dx}{\sqrt{1-x^2}} > 0$.
