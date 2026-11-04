---
tag: XEYCB0WF9Y
kind: proof
name: Proof of the Chevalley–Warning theorem
msc: [11T06]
proves: 08895Q5W96
uses: [08RTDHX1SK, 0H5WWC8RZX, 0P7CH1CND5, 0QWR8WTZEW, 0KJVQV3E0F]
sources:
  - url: https://en.wikipedia.org/wiki/Chevalley%E2%80%93Warning_theorem
    locator: Proof of Warning's theorem
---

## Proof

Let $q = \abs{\mathbb{F}}$. We use the convention $x^0 = 1$ for all $x \in \mathbb{F}$, including $x = 0$.

1. By [[the order of a finite field|0H5WWC8RZX]], $q = p^m$ for some $m \ge 1$. So $q \cdot 1 = 0$ in $\mathbb{F}$, by the definition of the [[characteristic|0P7CH1CND5]] $p$.
2. Lemma: $\sum_{x \in \mathbb{F}} x^k = 0$ for each integer $k$ with $0 \le k < q - 1$.
3. For $k = 0$, the sum is $q \cdot 1 = 0$ by step 1.
4. Let $1 \le k \le q - 2$. The polynomial $X^k - 1$ is nonzero of degree $k$, so it has at most $k < q - 1$ roots in $\mathbb{F}$ by [[the root bound|0KJVQV3E0F]].
5. The set $\mathbb{F} \setminus \set{0}$ has $q - 1$ elements. So there is $c \ne 0$ in $\mathbb{F}$ with $c^k \ne 1$.
6. Let $S = \sum_{x \in \mathbb{F}} x^k$. Since $x \mapsto cx$ is a bijection of $\mathbb{F}$, $S = \sum_{x} (cx)^k = c^k S$.
7. So $(c^k - 1) S = 0$ with $c^k - 1 \ne 0$, and $S = 0$. This proves the lemma.
8. Let $g = X_1^{e_1} \cdots X_n^{e_n}$ be a monomial of total degree $e_1 + \dots + e_n < n(q - 1)$. Then $e_j < q - 1$ for some $j$.
9. The sum of $g$ over $\mathbb{F}^n$ factors: $\sum_{a \in \mathbb{F}^n} g(a) = \prod_{j=1}^{n} \sum_{x \in \mathbb{F}} x^{e_j}$. By the lemma the factor for the $j$ of step 8 is $0$, so the sum is $0$.
10. A polynomial $P$ of total degree less than $n(q-1)$ is a linear combination of such monomials. By step 9 and linearity, $\sum_{a \in \mathbb{F}^n} P(a) = 0$.
11. Now put $P = \prod_{i=1}^{r} \left(1 - f_i^{\,q-1}\right)$. Its total degree is at most $(q - 1)(d_1 + \dots + d_r) < (q - 1) n$, by the hypothesis $d_1 + \dots + d_r < n$.
12. By [[the identity $x^q = x$ in a finite field|0QWR8WTZEW]], $y^{q-1} = 1$ for each $y \ne 0$ in $\mathbb{F}$. Also $0^{q-1} = 0$, since $q - 1 \ge 1$.
13. So for $a \in \mathbb{F}^n$, the factor $1 - f_i(a)^{q-1}$ is $1$ if $f_i(a) = 0$ and $0$ otherwise.
14. Hence $P(a) = 1$ if $a$ is a common zero of $f_1, \dots, f_r$, and $P(a) = 0$ otherwise.
15. Let $Z$ be the number of common zeros. By step 14, $\sum_{a \in \mathbb{F}^n} P(a) = Z \cdot 1$ in $\mathbb{F}$.
16. By steps 10 and 11, this sum is $0$. So $Z \cdot 1 = 0$ in $\mathbb{F}$.
17. Write $Z = sp + t$ with $0 \le t < p$. Then $t \cdot 1 = Z \cdot 1 - s (p \cdot 1) = 0$. Since $p$ is the least positive integer $m$ with $m \cdot 1 = 0$, we get $t = 0$.
18. So $p$ divides $Z$, the number of common zeros.

## Idea

The polynomial $\prod_i (1 - f_i^{q-1})$ is the indicator function of the common zero set, because $y^{q-1}$ is $1$ for $y \ne 0$ and $0$ for $y = 0$.
So summing it over $\mathbb{F}^n$ counts the zeros, as an element of $\mathbb{F}$.
But a polynomial of low degree sums to zero over $\mathbb{F}^n$, because some variable appears to a power below $q - 1$, and power sums of such exponents vanish.
