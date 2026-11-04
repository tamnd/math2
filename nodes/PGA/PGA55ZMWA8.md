---
tag: PGA55ZMWA8
kind: proof
name: Proof of Liouville's theorem on Diophantine approximation
msc: [11J68]
proves: 0N3WFZEFPM
uses: [0MB4TGMXG6, 0J1R5NP36S, 079EGSD32Y, 0MES3KS0ZC, 0BARQY52N5, 0WS1A8E2P9, 0MH1WK89PP, 0A3GWZ86AY]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville_number
    locator: Liouville numbers and transcendence
---

## Proof

1. By the definition of the degree of an [[algebraic number|0MB4TGMXG6]], there is a polynomial of degree $d$ with rational coefficients that vanishes at $\alpha$. Multiplying by a common denominator of its coefficients, we get such a polynomial $f$ with integer coefficients.
2. Claim: $f$ has no rational root. Suppose $f(r) = 0$ with $r \in \Q$. By [[division by the monic polynomial|0MES3KS0ZC]] $X - r$ over $\Q$, $f = (X - r) g + c$ with $c \in \Q$ and $g \in \Q[X]$ of degree $d - 1$. Evaluating at $r$ gives $c = 0$.
3. Since $d \ge 2$, $\alpha$ is not rational, so $\alpha \ne r$. Then $0 = f(\alpha) = (\alpha - r) g(\alpha)$ gives $g(\alpha) = 0$. So $\alpha$ is a root of a nonzero rational polynomial of degree $d - 1 < d$, which contradicts the minimality of $d$. This proves the claim.
4. The [[derivative|0MH1WK89PP]] $f'$ is a polynomial, so it is continuous. By the [[extreme value theorem|0WS1A8E2P9]], $\abs{f'}$ has a maximum $M \ge 0$ on $[\alpha - 1, \alpha + 1]$.
5. Put $c = \dfrac{1}{2 \max(1, M)}$. Then $0 < c \le \frac{1}{2}$. Let $p$ and $q$ be integers with $q > 0$.
6. Case $\abs{\alpha - p/q} \ge 1$. Then $\abs{\alpha - p/q} \ge 1 > \frac{1}{2} \ge c \ge c/q^d$.
7. Case $\abs{\alpha - p/q} < 1$. Write $f = \sum_{j=0}^{d} b_j X^j$ with integers $b_j$. Then $q^d f(p/q) = \sum_{j=0}^{d} b_j p^j q^{d-j}$ is an integer.
8. By step 2, $f(p/q) \ne 0$. So $\abs{q^d f(p/q)} \ge 1$, that is, $\abs{f(p/q)} \ge 1/q^d$.
9. Also $p/q \ne \alpha$, since $\alpha$ is irrational. By the [[mean value theorem|0BARQY52N5]], $f(p/q) - f(\alpha) = f'(t)(p/q - \alpha)$ for some $t$ between $\alpha$ and $p/q$. Then $t \in [\alpha - 1, \alpha + 1]$.
10. Since $f(\alpha) = 0$, steps 4, 8 and 9 give $\frac{1}{q^d} \le \abs{f(p/q)} \le M \abs{\alpha - p/q}$.
11. In particular $M > 0$, and $\abs{\alpha - p/q} \ge \frac{1}{M q^d} > \frac{c}{q^d}$, because $c < 1/M$.
12. In both cases $\abs{\alpha - p/q} > c/q^d$. This proves the first part.
13. Now let $x$ be a [[Liouville number|0J1R5NP36S]]. Suppose that $x$ is algebraic, of degree $d$. Since a nonzero constant has no root, $d \ge 1$.
14. Suppose $d = 1$. Then $u x + v = 0$ for some integers $u \ne 0$ and $v$, as in step 1. So $x = a/b$ with integers $a$, $b$ and $b \ge 1$. Choose $n$ with $2^{n-1} > b$.
15. The definition gives integers $p$, $q$ with $q \ge 2$ and $0 < \abs{a/b - p/q} < 1/q^n$. The number $\abs{aq - bp}$ is a positive integer, so $\abs{a/b - p/q} = \abs{aq - bp}/(bq) \ge 1/(bq)$.
16. So $1/(bq) < 1/q^n$, that is, $q^{n-1} < b$. But $q^{n-1} \ge 2^{n-1} > b$, a contradiction. So $d \ge 2$.
17. Let $c > 0$ be the constant of the first part for $x$. By the [[Archimedean property|0A3GWZ86AY]] and $2^k \ge k$, there is an integer $n > d$ with $2^{n-d} \ge 1/c$.
18. The definition gives integers $p$, $q$ with $q \ge 2$ and $\abs{x - p/q} < 1/q^n$.
19. Since $q^{n-d} \ge 2^{n-d} \ge 1/c$, we get $\frac{1}{q^n} = \frac{1}{q^d q^{n-d}} \le \frac{c}{q^d}$. So $\abs{x - p/q} < c/q^d$, against the first part.
20. So $x$ is not algebraic, that is, $x$ is [[transcendental|079EGSD32Y]].

## Idea

If $p/q$ is not a root of the integer polynomial $f$, then $f(p/q)$ is a fraction with denominator $q^d$, so it is at least $1/q^d$ in size.
But $f(\alpha) = 0$, so the mean value theorem makes $f(p/q)$ small when $p/q$ is close to $\alpha$.
A Liouville number has approximations that are too good for any fixed $d$, so it cannot be algebraic.
