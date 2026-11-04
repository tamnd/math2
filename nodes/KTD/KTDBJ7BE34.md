---
tag: KTDBJ7BE34
kind: proof
name: Proof that a polynomial over a field has at most as many roots as its degree
msc: ["12E05"]
proves: 0KJVQV3E0F
uses: [0QA8CHH8MG, 09S3PFBEPM, 0B5Z1EC66J, 0T233AZ1GE, 0K3MWA7DMC, 03XVP8Q4GY, 00EHX6FWC0, 0125QVNCFQ, 0GJM24EXP9, 0DPF6WRZW6]
sources:
  - url: https://proofwiki.org/wiki/Polynomial_Factor_Theorem
---

## Proof

Let $K$ be a [[field|0QA8CHH8MG]]. For a nonzero $h \in K[x]$, let $Z(h)$ be the set of [[roots|00EHX6FWC0]] of $h$ in $K$. For $d \in K$, let $m_h(d)$ be the [[multiplicity|03XVP8Q4GY]] of $d$ as a root of $h$. We prove by induction on $n \ge 0$ this claim: every nonzero $f \in K[x]$ of [[degree|0DPF6WRZW6]] $n$ has $Z(f)$ finite and $\sum_{d \in Z(f)} m_f(d) \le n$.

1. The field $K$ is an [[integral domain|09S3PFBEPM]]: $1 \ne 0$, and if $a b = 0$ with $a \neq 0$, then $b = a^{-1} a b = 0$.
2. So $K[x]$ is an integral domain by [[the theorem on polynomial rings|0B5Z1EC66J]], and $\deg(g h) = \deg g + \deg h$ by the [[degree of a product|0T233AZ1GE]]. Nonzero factors [[cancel|0GJM24EXP9]] in $K$ and in $K[x]$.
3. Let $h \neq 0$ and $d \in Z(h)$. By the [[factor theorem|0K3MWA7DMC]], $x - d$ divides $h$, so $m_h(d) \ge 1$. Conversely, if $m_h(d) \ge 1$, then $x - d$ divides $h$ and $d \in Z(h)$.
4. By step 3, the claim gives $\abs{Z(f)} \le \sum_{d \in Z(f)} m_f(d) \le n$. So the claim implies both parts of the statement.
5. Let $f \neq 0$ have degree $n$. If $f$ has no root, then $Z(f)$ is empty and the sum is $0 \le n$. This covers $n = 0$: a nonzero constant $a$ has the value $a \neq 0$ everywhere.
6. Now let $n \ge 1$, assume the claim for degree $n - 1$, and let $c$ be a root of $f$. By the factor theorem, $f = (x - c) g$ with $g \in K[x]$.
7. Since $f \neq 0$, also $g \neq 0$. By step 2, $n = 1 + \deg g$, so $\deg g = n - 1$.
8. For $d \in K$, the [[evaluation homomorphism|0125QVNCFQ]] gives $f(d) = (d - c) g(d)$. By step 1, $f(d) = 0$ exactly when $d = c$ or $g(d) = 0$. So $Z(f) = Z(g) \cup \set{c}$.
9. By the induction hypothesis, $Z(g)$ is finite, so $Z(f)$ is finite.
10. Let $d \neq c$. We show by induction on $m \ge 0$ that for every $g_0 \in K[x]$, if $(x - d)^m$ divides $(x - c) g_0$, then $(x - d)^m$ divides $g_0$. The case $m = 0$ is trivial.
11. Let $m \ge 1$ and $(x - c) g_0 = (x - d)^m k$ with $k \in K[x]$. Evaluating at $d$ gives $(d - c) g_0(d) = 0$. Since $d - c \neq 0$, step 1 gives $g_0(d) = 0$.
12. By the factor theorem, $g_0 = (x - d) g_1$ with $g_1 \in K[x]$. Then $(x - d)(x - c) g_1 = (x - d)(x - d)^{m-1} k$.
13. Cancelling the nonzero factor $x - d$ gives $(x - c) g_1 = (x - d)^{m-1} k$. By the induction hypothesis of step 10, $(x - d)^{m-1}$ divides $g_1$, so $(x - d)^m$ divides $g_0$.
14. If $(x - d)^m$ divides $g$, then it divides $f = (x - c) g$. With step 10 for $g_0 = g$, this gives $m_f(d) = m_g(d)$ for each $d \neq c$.
15. Let $m \ge 1$. If $(x - c)^m k = (x - c) g$, then cancelling $x - c$ gives $g = (x - c)^{m-1} k$. Conversely, $g = (x - c)^{m-1} k$ gives $f = (x - c)^m k$.
16. So $(x - c)^m$ divides $f$ exactly when $(x - c)^{m-1}$ divides $g$, for each $m \ge 1$. Taking the largest such $m$ gives $m_f(c) = 1 + m_g(c)$.
17. If $c \notin Z(g)$, then $m_g(c) = 0$ by step 3. So in all cases $m_g(c) + \sum_{d \in Z(g), d \neq c} m_g(d) = \sum_{d \in Z(g)} m_g(d)$.
18. By steps 8, 14, 16 and 17, $\sum_{d \in Z(f)} m_f(d) = 1 + m_g(c) + \sum_{d \in Z(g), d \neq c} m_g(d) = 1 + \sum_{d \in Z(g)} m_g(d)$.
19. By the induction hypothesis for $g$, this is at most $1 + (n - 1) = n$. This proves the claim, and with step 4 the statement.

## Idea

Each root $c$ splits off a linear factor: $f = (x - c) g$, and $g$ has degree one less. The roots of $f$ are $c$ and the roots of $g$, because a field has no zero divisors. The factor $x - c$ adds exactly one to the multiplicity of $c$ and leaves the other multiplicities unchanged, so induction on the degree gives the bound.
