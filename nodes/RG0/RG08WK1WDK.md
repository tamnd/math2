---
tag: RG08WK1WDK
kind: proof
name: Proof that finite-dimensional normed spaces are complete
msc: [46B99]
proves: 0ABP2F2ZP7
uses: [0BDTTM24DP, 08EWT7J0SC, 0MCK8K2D7Z, 03MC70ZRNR, 0J3578562S, 018W3V3TCT, 06MRNP4BNT, 059THXBRBB, E3CPZNJZNG, 06JYPJ4WHH]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_space
    locator: Complete norms and equivalent norms
---

## Proof

We compare the norm with the sup norm of the coordinates and use completeness of $\mathbb{R}$ in each coordinate.

1. Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. If $V = \{0\}$, each sequence is constant and converges, so $V$ is complete. Let $V \neq \{0\}$.
2. Since $V$ is [[finite-dimensional|018W3V3TCT]], it has a [[basis|06MRNP4BNT]] $e_1, \ldots, e_n$. Write $x = \sum_j a_j(x) e_j$, with linear coordinates $a_j$, by [[this result|059THXBRBB]].
3. Let $\|x\|_\infty = \max_j |a_j(x)|$. It is a norm: it vanishes only when all coordinates vanish, it is homogeneous, and $|a_j(x + y)| \le |a_j(x)| + |a_j(y)|$. By the [[equivalence of norms in finite dimension|03MC70ZRNR]], there are $c, C > 0$ with $c \|x\|_\infty \le \|x\| \le C \|x\|_\infty$ for all $x$, by the definition of [[equivalent norms|0J3578562S]].
4. Let $(x_k)$ be a [[Cauchy sequence|0MCK8K2D7Z]] in $(V, \|\cdot\|)$. Fix $j$. Then $|a_j(x_k) - a_j(x_l)| \le \|x_k - x_l\|_\infty \le \|x_k - x_l\| / c$. So $(a_j(x_k))_k$ is a Cauchy sequence in $\mathbb{K}$.
5. Its real parts and imaginary parts form Cauchy sequences in $\mathbb{R}$, since $|\operatorname{Re} z| \le |z|$ and $|\operatorname{Im} z| \le |z|$.
6. By the [[completeness of the real numbers|E3CPZNJZNG]], both converge. So $a_j(x_k) \to \alpha_j$ for some $\alpha_j \in \mathbb{K}$.
7. Let $x = \sum_j \alpha_j e_j$. Then $a_j(x_k - x) = a_j(x_k) - \alpha_j$, so $\|x_k - x\| \le C \max_j |a_j(x_k) - \alpha_j|$.
8. Given $\varepsilon > 0$, for each $j$ there is $N_j$ with $|a_j(x_k) - \alpha_j| < \varepsilon / C$ for $k \ge N_j$. For $k \ge \max_j N_j$, we get $\|x_k - x\| < \varepsilon$.
9. So $(x_k)$ [[converges|06JYPJ4WHH]] to $x$. Each Cauchy sequence converges, so $V$ is [[complete|08EWT7J0SC]], and $V$ is a [[Banach space|0BDTTM24DP]].

## Idea

All norms on a finite-dimensional space are equivalent, so we may measure with the largest coordinate. Then a Cauchy sequence of vectors gives finitely many Cauchy sequences of numbers, which converge because $\mathbb{R}$ is complete.
