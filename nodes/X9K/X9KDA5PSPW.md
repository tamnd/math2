---
tag: X9KDA5PSPW
kind: proof
name: Proof that continuous partial derivatives imply differentiability
msc: [26B05]
proves: 0KXSK8TEEB
uses: [09EGC6F8PT, 05AXG3QRKR, 0135XZZQ8M, 0NS0X75RS1, 0BARQY52N5, 07ZMX4ANJS, 01ZQQDCERP, 0DC3MPR7C9]
sources:
  - url: https://www.jirka.org/ra/realanal2.pdf
    locator: Proposition 8.4.6
---

## Proof

We treat one component at a time, and we move from $a$ to $a + h$ one coordinate at a time with the mean value theorem.

1. Let $U$, $f$ and $a$ be as in the statement. Fix $j \in \{1, \dots, m\}$ and write $g = f_j \colon U \to \mathbb{R}$. Write $\partial_i g$ for the [[partial derivative|05AXG3QRKR]] $\partial g / \partial x_i$.
2. Since $U$ is [[open|01ZQQDCERP]], there is $\rho > 0$ such that the [[open ball|0DC3MPR7C9]] $B(a, \rho)$ lies in $U$.
3. Let $L \colon \mathbb{R}^n \to \mathbb{R}$ be the linear map $L h = \sum_{i=1}^n \partial_i g(a) \, h_i$. We show that $g$ is [[differentiable|0135XZZQ8M]] at $a$ with $Dg(a) = L$.
4. Let $h = (h_1, \dots, h_n)$ with $\|h\| < \rho$. Put $p_0 = a$ and $p_k = a + h_1 e_1 + \dots + h_k e_k$ for $1 \le k \le n$, where $e_k$ is the $k$-th standard basis vector. Then $p_n = a + h$.
5. For each $k$ and each real $s$ between $0$ and $h_k$, the vector $p_{k-1} + s e_k - a$ is $(h_1, \dots, h_{k-1}, s, 0, \dots, 0)$. Its norm is at most $\|h\|$, because $s^2 \le h_k^2$.
6. Fix $k$. Let $J$ be the set of real $s$ with $\|p_{k-1} + s e_k - a\| < \rho$. It is an open interval, and by step 5 it contains the closed interval between $0$ and $h_k$. Put $\varphi(s) = g(p_{k-1} + s e_k)$ for $s \in J$.
7. For $s \in J$, the point $p_{k-1} + s e_k$ lies in $U$. By the definition of $\partial_k g$ at that point, $\varphi$ is differentiable at $s$ with $\varphi'(s) = \partial_k g(p_{k-1} + s e_k)$.
8. Since [[differentiable functions are continuous|07ZMX4ANJS]], $\varphi$ is continuous on $J$.
9. Suppose that $h_k \ne 0$. By the [[mean value theorem|0BARQY52N5]] for $\varphi$ between $0$ and $h_k$, there is $\theta_k$ strictly between $0$ and $h_k$ with $\varphi(h_k) - \varphi(0) = \varphi'(\theta_k) \, h_k$.
10. Put $q_k = p_{k-1} + \theta_k e_k$. Then step 9 says $g(p_k) - g(p_{k-1}) = \partial_k g(q_k) \, h_k$. By step 5, $\|q_k - a\| \le \|h\|$.
11. If $h_k = 0$, then $p_k = p_{k-1}$. Put $q_k = p_{k-1}$. Then again $g(p_k) - g(p_{k-1}) = 0 = \partial_k g(q_k) \, h_k$ and $\|q_k - a\| \le \|h\|$.
12. Summing over $k$, the sum telescopes:
$$g(a + h) - g(a) - L h = \sum_{k=1}^n \big(g(p_k) - g(p_{k-1})\big) - \sum_{k=1}^n \partial_k g(a) h_k = \sum_{k=1}^n \big(\partial_k g(q_k) - \partial_k g(a)\big) h_k.$$
13. Since $|h_k| \le \|h\|$, this gives $|g(a + h) - g(a) - L h| \le \|h\| \sum_{k=1}^n |\partial_k g(q_k) - \partial_k g(a)|$.
14. Let $\varepsilon > 0$. Each $\partial_k g$ is continuous at $a$. So there is $\eta > 0$ with $|\partial_k g(q) - \partial_k g(a)| < \varepsilon / n$ for each $k$ and each $q \in U$ with $\|q - a\| < \eta$.
15. Let $0 < \|h\| < \min(\rho, \eta)$. By steps 10 and 11, $\|q_k - a\| < \eta$ for each $k$. By steps 13 and 14, $|g(a + h) - g(a) - L h| < n (\varepsilon / n) \|h\| = \varepsilon \|h\|$.
16. So $|g(a + h) - g(a) - L h| / \|h\| \to 0$ as $h \to 0$. Thus $f_j = g$ is differentiable at $a$.
17. Step 16 holds for each $j$. By the [[componentwise criterion for differentiability|0NS0X75RS1]], $f$ is differentiable at $a$.

## Idea

Going from $a$ to $a + h$ along the coordinate directions splits the change of $f$ into $n$ changes in one variable. The mean value theorem turns each of them into a partial derivative at a nearby point, times $h_k$. Continuity at $a$ makes these partial derivatives close to their values at $a$, and that is exactly the linear approximation.
