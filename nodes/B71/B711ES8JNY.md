---
tag: B711ES8JNY
kind: proof
name: Proof that C^1 vector fields satisfy the Picard–Lindelöf hypotheses
msc: [34A12]
proves: 03Z9V0Y78A
uses: [0J7HF2PF1H, 055VVSN00V, 0DC3MPR7C9, 07PFYV65MB, 0V4DET59NW, 0RFWW56Y22, 02CYB184RC]
sources:
  - url: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem
    locator: Theorem
---

## Proof

Here $\norm{\cdot}$ is the Euclidean norm, and $Df(z)$ is the Jacobian matrix of $f$ at $z$. Its entries $\partial f_i / \partial x_j$ are continuous on $U$, since $f$ is continuously differentiable.

1. Since $U$ is open, there is $r > 0$ such that the [[open ball|0DC3MPR7C9]] of radius $r$ around $x_0$ lies in $U$. Let $a = r/2 > 0$.
2. The closed ball $B = \set{x : \norm{x - x_0} \le a}$ lies in that open ball, so $B \subseteq U$. It is closed, bounded and nonempty, so it is compact by the [[Heine–Borel theorem|07PFYV65MB]].
3. The function $z \mapsto \norm{f(z)}$ is continuous on $U$. By [[the extreme value theorem on compact sets|0V4DET59NW]], it has a maximum $L \ge 0$ on $B$. So $\norm{f(x)} \le L$ for $x \in B$.
4. The function $z \mapsto \left(\sum_{i, j} \left(\partial f_i / \partial x_j (z)\right)^2\right)^{1/2}$ is continuous on $U$. Let $K \ge 0$ be its maximum on $B$.
5. Let $z \in B$ and $h \in \R^n$. Entry $i$ of $Df(z) h$ is the dot product of row $i$ of $Df(z)$ with $h$. The [[Cauchy–Schwarz inequality|0RFWW56Y22]] bounds it, and summing the squares gives $\norm{Df(z) h} \le K \norm{h}$.
6. So the operator norm of $Df(z)$ is at most $K$ for each $z \in B$.
7. Let $x, y \in B$ and $0 \le s \le 1$. Then $\norm{x + s(y - x) - x_0} \le (1 - s) \norm{x - x_0} + s \norm{y - x_0} \le a$. So the segment $[x, y]$ lies in $B \subseteq U$.
8. By the [[mean value inequality|02CYB184RC]] and step 6, $\norm{f(y) - f(x)} \le K \norm{y - x}$ for all $x, y \in B$.
9. Let $\varepsilon = a/(L + 1) > 0$ and $J = [t_0 - \varepsilon, t_0 + \varepsilon]$. Let $g : J \times \R^n \to \R^n$ be any function with $g(t, x) = f(x)$ for $t \in J$ and $x \in B$.
10. Condition (1) of the [[Picard–Lindelöf hypotheses|0J7HF2PF1H]]: for each $t \in J$, $x \mapsto g(t, x) = f(x)$ is $K$-[[Lipschitz|055VVSN00V]] on $B$, by step 8.
11. Condition (2): for each $x \in B$, $t \mapsto g(t, x) = f(x)$ is constant, hence continuous on $J$.
12. Condition (3): $\norm{g(t, x)} = \norm{f(x)} \le L$ for $t \in J$ and $x \in B$, by step 3.
13. Condition (4): here $\max(t_{\max} - t_0, t_0 - t_{\min}) = \varepsilon$, and $L \varepsilon = L a/(L + 1) \le a$.
14. So $g$ satisfies the hypotheses at $(t_0, x_0)$ on $J$ with the constants $a, L, K$.

## Idea

A small closed ball around $x_0$ is compact. On it, the continuous functions $\norm{f}$ and $\norm{Df}$ are bounded, which gives the bound $L$ and, through the mean value inequality, the Lipschitz constant $K$. A short time interval then keeps $L \varepsilon \le a$.
