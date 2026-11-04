---
tag: A4K6K70RWW
kind: proof
name: Proof that power series converge uniformly on smaller intervals inside the radius of convergence
msc: [30B10, 40A30]
proves: 0BWXV7GADW
uses: [0VP56B4EMX, 0660QX1VPR, 0BTMQ04556, 01X5CVV1Q5, 0NX5NWAFC9]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/analysis_ii_thm_proof.pdf
    locator: Section 2.2, Power series
---

## Proof

We dominate the terms by a convergent geometric series and apply the Weierstrass M-test.

1. Let $\sum a_n (x - c)^n$ be a [[power series|0VP56B4EMX]] with [[radius of convergence|0660QX1VPR]] $R > 0$. Let $A = \set{ t \ge 0 : (|a_n| t^n) \text{ is bounded} }$, so that $R = \sup A$.
2. Let $0 < r < R$. Choose a real number $s$ with $r < s < R$. For example, take $s = \frac{r + R}{2}$ if $R < \infty$, and $s = r + 1$ if $R = \infty$.
3. Since $s < R = \sup A$, the number $s$ is not an upper bound of $A$, by the definition of the [[supremum|0BTMQ04556]]. So there is $t \in A$ with $t > s$.
4. Since $t \in A$, there is $C \ge 0$ with $|a_n| t^n \le C$ for all $n$. Since $0 < s < t$, also $|a_n| s^n \le |a_n| t^n \le C$ for all $n$.
5. Let $q = \frac{r}{s}$. Then $0 < q < 1$.
6. Let $x \in [c - r, c + r]$. Then $|x - c| \le r$, so by step 4,
$$|a_n (x - c)^n| \le |a_n| r^n = |a_n| s^n q^n \le C q^n.$$
7. Let $M_n = C q^n$. Since $|q| < 1$, the [[geometric series|01X5CVV1Q5]] $\sum_{n=0}^{\infty} M_n$ converges.
8. By steps 6 and 7, the [[Weierstrass M-test|0NX5NWAFC9]] applies to the functions $x \mapsto a_n (x - c)^n$ on $[c - r, c + r]$.
9. So the power series converges absolutely and uniformly on $[c - r, c + r]$.

## Idea

Slightly beyond $r$, at some $s < R$, the terms $|a_n| s^n$ stay bounded. On $[c - r, c + r]$, each term is then at most a constant times $(r/s)^n$. These bounds form a convergent geometric series that does not depend on $x$, so the M-test gives uniform convergence.
