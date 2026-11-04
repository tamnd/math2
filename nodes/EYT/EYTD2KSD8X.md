---
tag: EYTD2KSD8X
kind: proof
name: Proof of the existence of nontrivial solutions of Pell's equation by Dirichlet approximation
msc: [11D09]
proves: 0EM6C9SZN5
uses: [0AF3DANJ76, 0N10YRNNWV, 04JAY9DGB7, 0HGVCWQGY3, 0FS3RHF6KE, 0K2DMACEZ4]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/ugradnumthy/pelleqn2.pdf
    locator: Lemma 2.1 and Theorem 2.3
---

## Proof

1. Since $d$ is not a perfect square, $\sqrt{d}$ is irrational by [[the irrationality of square roots of non-squares|0N10YRNNWV]].
2. Claim: there are infinitely many pairs of integers $(p, q)$ with $q \ge 1$ and $\abs{p - q\sqrt{d}} < 1/q$.
3. For a positive integer $N$, [[Dirichlet's approximation theorem|04JAY9DGB7]] gives integers $p$, $q$ with $1 \le q \le N$ and $\abs{q\sqrt{d} - p} \le \frac{1}{N+1} < \frac{1}{N} \le \frac{1}{q}$. So at least one such pair exists.
4. Suppose only finitely many pairs had this property. By step 1, $p - q\sqrt{d} \ne 0$ for each of them. Let $\mu > 0$ be the least value of $\abs{p - q\sqrt{d}}$ over them.
5. Choose $N$ with $\frac{1}{N+1} < \mu$. Step 3 gives a pair with the property and $\abs{p - q\sqrt{d}} < \mu$. It is not in the finite list, a contradiction. This proves the claim.
6. For each pair of step 2, $\abs{p + q\sqrt{d}} \le \abs{p - q\sqrt{d}} + 2q\sqrt{d} < \frac{1}{q} + 2q\sqrt{d}$.
7. So $\abs{p^2 - d q^2} = \abs{p - q\sqrt{d}} \cdot \abs{p + q\sqrt{d}} < \frac{1}{q}\left(\frac{1}{q} + 2q\sqrt{d}\right) \le 1 + 2\sqrt{d}$.
8. Also $p^2 - d q^2 \ne 0$, since otherwise $\sqrt{d} = \abs{p}/q$ would be rational.
9. So $p^2 - dq^2$ takes values in the finite set of nonzero integers $k$ with $\abs{k} < 1 + 2\sqrt{d}$. By the [[infinite pigeonhole principle|0FS3RHF6KE]], some such $k$ equals $p^2 - dq^2$ for infinitely many pairs of step 2.
10. Each such pair gives a pair of residues $(p \bmod \abs{k}, q \bmod \abs{k})$, and there are only $k^2$ of these. By the [[pigeonhole principle|0HGVCWQGY3]], there are two different pairs $(p_1, q_1) \ne (p_2, q_2)$ among them with $p_1 \equiv p_2$ and $q_1 \equiv q_2 \pmod{\abs{k}}$.
11. Put $X = p_1 p_2 - d q_1 q_2$ and $Y = q_1 p_2 - p_1 q_2$. Then $(p_1 + q_1\sqrt{d})(p_2 - q_2\sqrt{d}) = X + Y\sqrt{d}$.
12. Modulo $\abs{k}$, step 10 gives $X \equiv p_1^2 - d q_1^2 = k \equiv 0$ and $Y \equiv q_1 p_1 - p_1 q_1 = 0$. So $X = kx$ and $Y = ky$ for integers $x$ and $y$.
13. Expanding both sides, as in the [[Brahmagupta–Fibonacci identity|0K2DMACEZ4]], gives $X^2 - dY^2 = (p_1^2 - d q_1^2)(p_2^2 - d q_2^2) = k^2$.
14. By steps 12 and 13, $k^2 (x^2 - d y^2) = k^2$. Since $k \ne 0$, $x^2 - d y^2 = 1$.
15. Suppose $y = 0$. Then $Y = 0$, so $p_2/q_2 = p_1/q_1$. Put $t = q_2/q_1 > 0$; then $p_2 = t p_1$ and $q_2 = t q_1$.
16. Then $k = p_2^2 - d q_2^2 = t^2 (p_1^2 - d q_1^2) = t^2 k$, so $t^2 = 1$ and $t = 1$. This gives $(p_2, q_2) = (p_1, q_1)$, contrary to step 10. So $y \ne 0$.
17. So [[Pell's equation|0AF3DANJ76]] has a solution $(x, y)$ with $y \ne 0$. Replacing $x$ by $\abs{x}$ and $y$ by $\abs{y}$, we may take $x \ge 1$ and $y \ge 1$.
18. For infinitely many solutions, put $u = x + y\sqrt{d}$. Then $u \ge 1 + \sqrt{d} > 1$.
19. Define integers $x_n$, $y_n$ for $n \ge 0$ by $x_0 = 1$, $y_0 = 0$, $x_{n+1} = x x_n + d y y_n$ and $y_{n+1} = y x_n + x y_n$.
20. By induction on $n$, $x_n + y_n \sqrt{d} = u^n$ and $x_n - y_n\sqrt{d} = (x - y\sqrt{d})^n$. Both follow by multiplying out $(x \pm y\sqrt{d})(x_n \pm y_n\sqrt{d})$.
21. Multiplying the two formulas of step 20 gives $x_n^2 - d y_n^2 = (x^2 - d y^2)^n = 1$. So each $(x_n, y_n)$ is a solution.
22. Since $u > 1$, the numbers $u^n$ are pairwise different. So the pairs $(x_n, y_n)$ are pairwise different, and Pell's equation has infinitely many integer solutions.

## Idea

Dirichlet's theorem gives infinitely many fractions $p/q$ near $\sqrt{d}$, and for them $p^2 - dq^2$ stays bounded.
So one value $k$ repeats infinitely often, and two of these pairs agree modulo $k$.
Dividing one by the other, in the form $(p_1 + q_1\sqrt{d})(p_2 - q_2\sqrt{d})/k$, gives a solution of norm $1$.
Powers of one solution then give infinitely many.
