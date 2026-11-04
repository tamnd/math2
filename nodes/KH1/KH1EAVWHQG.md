---
tag: KH1EAVWHQG
kind: proof
name: Proof of the equivalence of norms in finite dimension by compactness of the unit sphere
msc: [46B20]
proves: 03MC70ZRNR
uses: [0J3578562S, 018W3V3TCT, 06MRNP4BNT, 059THXBRBB, 0FJZMBX0ZZ, 0E1MMCAY5B, 0TMZ21WKCN, 0YF82GBTND, 0B8GPXFSP7, 07PFYV65MB, 0P953MG05E, 0V4DET59NW]
sources:
  - url: https://en.wikipedia.org/wiki/Norm_(mathematics)
    locator: Equivalence
---

## Proof

We compare each norm with the sup norm of the coordinates in a basis, and use compactness of the unit sphere of that norm.

1. Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. If $V = \{0\}$, each norm is the zero function, and any two norms are [[equivalent|0J3578562S]] with $c = C = 1$. Let $V \neq \{0\}$.
2. $V$ is [[finite-dimensional|018W3V3TCT]], so a finite spanning set [[contains a basis|06MRNP4BNT]] $e_1, \ldots, e_n$, with $n \ge 1$. Write $x = \sum_{j} a_j(x) e_j$. The coordinates $a_j \colon V \to \mathbb{K}$ are linear, by the [[isomorphism with the coordinate space|059THXBRBB]].
3. Let $\|x\|_\infty = \max_j |a_j(x)|$. This is a norm. It vanishes only when all coordinates vanish, that is, at $x = 0$. Also $\|\lambda x\|_\infty = |\lambda| \|x\|_\infty$, and $|a_j(x + y)| \le |a_j(x)| + |a_j(y)|$ gives the triangle inequality.
4. Equivalence of norms is symmetric and transitive. If $c_a \|x\|_\infty \le \|x\|_a \le C_a \|x\|_\infty$ and $c_b \|x\|_\infty \le \|x\|_b \le C_b \|x\|_\infty$, then $(c_b / C_a) \|x\|_a \le \|x\|_b \le (C_b / c_a) \|x\|_a$.
5. So it suffices to fix a norm $\|\cdot\|$ on $V$ and find $c, C > 0$ with $c \|x\|_\infty \le \|x\| \le C \|x\|_\infty$ for all $x \in V$.
6. Upper bound. Let $C = \sum_j \|e_j\| > 0$. By the [[triangle inequality|0FJZMBX0ZZ]], $\|x\| \le \sum_j |a_j(x)| \, \|e_j\| \le C \|x\|_\infty$.
7. Let $m = n$ if $\mathbb{K} = \mathbb{R}$ and $m = 2n$ if $\mathbb{K} = \mathbb{C}$. Define $\Lambda \colon \mathbb{R}^m \to V$ by $\Lambda(t) = \sum_j t_j e_j$ in the real case, and $\Lambda(t) = \sum_j (t_{2j-1} + \mathrm{i} \, t_{2j}) e_j$ in the complex case.
8. $\Lambda$ is a bijection and is additive. Let $d_2$ be the [[Euclidean metric|0E1MMCAY5B]] on $\mathbb{R}^m$. Each coordinate of $\Lambda(t)$ has modulus at most $d_2(t, 0)$, so $\|\Lambda(t)\|_\infty \le d_2(t, 0)$.
9. Let $g(t) = \|\Lambda(t)\|$ and $h(t) = \|\Lambda(t)\|_\infty$. By the reverse triangle inequality in [[this result|0FJZMBX0ZZ]] and steps 6 and 8, $|g(t) - g(s)| \le \|\Lambda(t - s)\| \le C d_2(t, s)$.
10. In the same way, $|h(t) - h(s)| \le \|\Lambda(t - s)\|_\infty \le d_2(t, s)$. So $g$ and $h$ are [[Lipschitz|0TMZ21WKCN]].
11. A Lipschitz function satisfies the epsilon-delta condition with $\delta = \varepsilon / (C + 1)$. By [[continuity via open sets|0YF82GBTND]], $g$ and $h$ are continuous on $\mathbb{R}^m$.
12. Let $\Sigma = h^{-1}(\{1\})$. The set $\{1\}$ is closed in $\mathbb{R}$, so $\Sigma$ is closed, by [[continuity via closed sets|0B8GPXFSP7]].
13. $\Sigma$ is [[bounded|0P953MG05E]]. For $t \in \Sigma$, each $|t_k|$ is at most the modulus of a coordinate of $\Lambda(t)$, so $|t_k| \le 1$. Then $d_2(t, 0) \le \sqrt{m}$ and $d_2(t, s) \le 2\sqrt{m}$ for $t, s \in \Sigma$.
14. By the [[Heine–Borel theorem|07PFYV65MB]], $\Sigma$ is compact. It is nonempty, since $\Lambda^{-1}(e_1) \in \Sigma$.
15. By [[this result|0V4DET59NW]], $g$ attains a minimum $c$ on $\Sigma$, at some $t^\ast \in \Sigma$. As $h(t^\ast) = 1$, $\Lambda(t^\ast) \neq 0$, so $c = \|\Lambda(t^\ast)\| > 0$.
16. Lower bound. Let $x \in V$ with $x \neq 0$, and let $y = x / \|x\|_\infty$. Then $\|y\|_\infty = 1$, so $y = \Lambda(t)$ with $t \in \Sigma$, and $\|y\| = g(t) \ge c$.
17. Multiplying by $\|x\|_\infty$ gives $\|x\| \ge c \|x\|_\infty$. This also holds for $x = 0$.
18. With step 6, $\|\cdot\|$ is equivalent to $\|\cdot\|_\infty$. By steps 4 and 5, any two norms on $V$ are equivalent.

## Idea

Every norm is bounded above by a multiple of the sup norm of the coordinates, by the triangle inequality. The lower bound needs compactness: the unit sphere of the sup norm is closed and bounded in $\mathbb{R}^m$, so the continuous positive function $\|\cdot\|$ has a positive minimum on it. Scaling then gives the bound everywhere.
