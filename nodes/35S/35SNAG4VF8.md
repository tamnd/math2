---
tag: 35SNAG4VF8
kind: proof
name: Proof of the implicit function theorem from the inverse function theorem
msc: ["26B10"]
proves: 0BXBADR94C
uses: [0K9HSJFCMJ, 0TCBZMEYGN, 0YF0VXKXGB, 0J9TVTNB4K, 0ZZQ2E1MTE, 03Q7RE2HXR, 0G65751VSW, 0KXSK8TEEB, 0EAAS2EHDR, 0S9EK5MQPE]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_function_theorem
    locator: Implicit function theorem
---

## Proof

We apply the inverse function theorem to the map $\Phi(x, y) = (x, F(x, y))$.

1. Let $\Omega$, $F$ and $(a, b)$ be as in the statement. Define $\Phi \colon \Omega \to \R^n \times \R^m$ by $\Phi(x, y) = (x, F(x, y))$.
2. The components of $\Phi$ are the coordinates $x_i$ and the components of $F$. So $\Phi$ is of [[class C^1|0TCBZMEYGN]], and its [[Jacobian matrix|0YF0VXKXGB]] at $(x, y)$ is the block matrix $\begin{pmatrix} I & 0 \\ D_x F(x, y) & D_y F(x, y) \end{pmatrix}$.
3. By the [[determinant of a block triangular matrix|0J9TVTNB4K]], applied to the transpose, and since [[a matrix and its transpose have the same determinant|0ZZQ2E1MTE]], $\det D\Phi(x, y) = \det D_y F(x, y)$.
4. Since $D_y F(a, b)$ is invertible, its determinant is not zero, so $\det D\Phi(a, b) \ne 0$.
5. By the [[inverse function theorem|0K9HSJFCMJ]] with $k = 1$, there are open sets $V' \subseteq \Omega$ with $(a, b) \in V'$ and $W'$ with $\Phi(a, b) = (a, 0) \in W'$. The map $\Phi$ is a bijection from $V'$ onto $W'$, with inverse $\Psi \colon W' \to V'$ of class $C^1$.
6. The map $\Phi$ does not change the first coordinate $x$. So $\Psi$ does not change it either: $\Psi(x, z) = (x, \eta(x, z))$ for some $\eta \colon W' \to \R^m$. The map $\eta$ is of class $C^1$, since its components are components of $\Psi$.
7. For $(x, z) \in W'$, the equation $\Phi(\Psi(x, z)) = (x, z)$ says $F(x, \eta(x, z)) = z$.
8. Since $V'$ is open, there is $r > 0$ such that every point within distance $r$ of $(a, b)$ lies in $V'$. Let $U_0 = \set{x : \norm{x - a} < r/2}$ and $V = \set{y : \norm{y - b} < r/2}$. If $x \in U_0$ and $y \in V$, then $\norm{(x, y) - (a, b)} \le \norm{x - a} + \norm{y - b} < r$. So $U_0 \times V \subseteq V'$.
9. Let $U = \set{x \in U_0 : (x, 0) \in W' \text{ and } \eta(x, 0) \in V}$. The map $x \mapsto (x, 0)$ is continuous and $W'$ is open, so the first condition defines an open set. On it, $x \mapsto \eta(x, 0)$ is [[continuous|0S9EK5MQPE]], and $V$ is open. So $U$ is open.
10. We have $\Psi(a, 0) = (a, b)$, since $\Phi(a, b) = (a, 0)$. So $\eta(a, 0) = b \in V$, and $a \in U$.
11. Define $g \colon U \to V$ by $g(x) = \eta(x, 0)$. By step 9, $g(x) \in V$. By step 7, $F(x, g(x)) = 0$ for $x \in U$.
12. Conversely, let $(x, y) \in U \times V$ with $F(x, y) = 0$. Then $(x, y) \in V'$ by step 8, and $\Phi(x, y) = (x, 0) = \Phi(x, g(x))$. Also $(x, g(x)) = \Psi(x, 0) \in V'$.
13. Since $\Phi$ is injective on $V'$, we get $y = g(x)$. With step 11: for $(x, y) \in U \times V$, $F(x, y) = 0$ if and only if $y = g(x)$.
14. The function $g$ is unique. If $\tilde g \colon U \to V$ has the same property, then $F(x, \tilde g(x)) = 0$ with $(x, \tilde g(x)) \in U \times V$, so $\tilde g(x) = g(x)$ by step 13.
15. The function $g$ is the composition of $x \mapsto (x, 0)$ with the $C^1$ map $\eta$. By the [[chain rule|0EAAS2EHDR]], $\partial g / \partial x_i (x) = \partial \eta / \partial x_i (x, 0)$, which is continuous. So $g$ is of class $C^1$.
16. Let $x \in U$. The maps $\Phi$ and $\Psi$ are differentiable, by [[continuous partials|0KXSK8TEEB]]. By the [[derivative of the inverse function|0G65751VSW]], $D\Phi(x, g(x))$ is invertible. By step 3 and [[the determinant criterion|03Q7RE2HXR]], $D_y F(x, g(x))$ is invertible.
17. Differentiate the identity $F(x, g(x)) = 0$ on the open set $U$ with the chain rule. This gives $D_x F(x, g(x)) + D_y F(x, g(x)) \, Dg(x) = 0$.
18. Multiplying on the left by $\big( D_y F(x, g(x)) \big)^{-1}$ gives $Dg(x) = -\big( D_y F(x, g(x)) \big)^{-1} D_x F(x, g(x))$.

## Idea

The map $(x, y) \mapsto (x, F(x, y))$ keeps $x$ and records the value of $F$. Its derivative is invertible exactly when $D_y F$ is, so it has a local inverse. Reading off the inverse at the points $(x, 0)$ gives the solution $y = g(x)$ of $F(x, y) = 0$, and differentiating $F(x, g(x)) = 0$ gives the formula for $Dg$.
