---
tag: M64J6JAXDE
kind: proof
name: Proof of the inverse function theorem by the contraction mapping principle
msc: ["26B10"]
proves: 0K9HSJFCMJ
uses: [0TCBZMEYGN, 03W6Q1MFR5, 03Q7RE2HXR, 0KXSK8TEEB, 0YF0VXKXGB, 0ZTEH055YF, 0RFWW56Y22, 02CYB184RC, 0K06X9QXDX, 0YS40B38JD, 0ABP2F2ZP7, 0FBXJZX3MK, 0MT2S0ZX4Y, 0VK6VEH345, 0ENVM493VK, 0EAAS2EHDR, 0S9EK5MQPE]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_function_theorem
    locator: A proof using the contraction mapping principle
---

## Proof

We find the inverse as the fixed point of a contraction, then show that it is differentiable, and finally of class $C^k$ by induction.

1. Let $U$, $k$, $f$ and $a$ be as in the statement. Write $\norm{x}$ for the Euclidean norm, and $\norm{B}$ for the [[operator norm|0ZTEH055YF]] of a matrix $B$.
2. Let $A = Df(a)$. Its [[Jacobian determinant|03W6Q1MFR5]] is not zero, so [[$A$ is invertible|03Q7RE2HXR]]. Let $c = \norm{A^{-1}} > 0$ and $\lambda = 1/(2c)$.
3. Since $f$ is of [[class C^1|0TCBZMEYGN]], it is [[differentiable|0KXSK8TEEB]] on $U$, and $Df(x)$ is the [[Jacobian matrix|0YF0VXKXGB]] of partial derivatives at $x$.
4. For a matrix $B = (b_{ij})$ we have $\norm{B} \le (\sum_{i,j} b_{ij}^2)^{1/2}$. This follows from the [[Cauchy–Schwarz inequality|0RFWW56Y22]] applied to each row of $B$.
5. The partial derivatives of $f$ are continuous at $a$. By step 4, there is $r > 0$ such that the closed ball $\bar B = \set{x : \norm{x - a} \le r}$ lies in $U$ and $\norm{Df(x) - A} \le \lambda$ for all $x \in \bar B$.
6. For $y \in \R^n$ and $x \in U$, let $\varphi_y(x) = x + A^{-1}(y - f(x))$. Since $A^{-1}$ is injective, $f(x) = y$ if and only if $\varphi_y(x) = x$.
7. The map $\varphi_y$ is differentiable with $D\varphi_y(x) = I - A^{-1} Df(x) = A^{-1}(A - Df(x))$. For $x \in \bar B$, step 5 gives $\norm{D\varphi_y(x)} \le c \lambda = \tfrac{1}{2}$.
8. The ball $\bar B$ is [[convex|0K06X9QXDX]]. By the [[mean value inequality|02CYB184RC]] and step 7, $\norm{\varphi_y(x_1) - \varphi_y(x_2)} \le \tfrac{1}{2} \norm{x_1 - x_2}$ for all $x_1, x_2 \in \bar B$.
9. We have $\varphi_y(x_1) - \varphi_y(x_2) = (x_1 - x_2) - A^{-1}(f(x_1) - f(x_2))$. So step 8 and the triangle inequality give $\norm{x_1 - x_2} \le \tfrac{1}{2} \norm{x_1 - x_2} + c \norm{f(x_1) - f(x_2)}$.
10. Hence $\norm{x_1 - x_2} \le 2 c \norm{f(x_1) - f(x_2)}$ for all $x_1, x_2 \in \bar B$. In particular, $f$ is injective on $\bar B$.
11. Let $V = \set{x : \norm{x - a} < r}$. It is open, $a \in V$ and $V \subseteq U$. Let $W = f(V)$, so $f(a) \in W$.
12. We show that $W$ is open. Let $y_0 \in W$, with $y_0 = f(x_0)$ and $x_0 \in V$. Choose $\rho > 0$ with $K = \set{x : \norm{x - x_0} \le \rho} \subseteq V$. Let $y \in \R^n$ with $\norm{y - y_0} < \lambda \rho$.
13. For $x \in K$, step 8 gives $\norm{\varphi_y(x) - \varphi_y(x_0)} \le \rho / 2$. Also $\varphi_y(x_0) - x_0 = A^{-1}(y - y_0)$, whose norm is less than $c \lambda \rho = \rho / 2$. So $\norm{\varphi_y(x) - x_0} < \rho$, and $\varphi_y$ maps $K$ into $K$.
14. The set $K$ is [[closed|0YS40B38JD]] in $\R^n$, which is [[complete|0ABP2F2ZP7]]. So $K$ is a [[complete|0FBXJZX3MK]] nonempty metric space. By step 8, $\varphi_y$ is a [[contraction|0MT2S0ZX4Y]] of $K$ with constant $\tfrac{1}{2}$.
15. By the [[Banach fixed point theorem|0VK6VEH345]], $\varphi_y$ has a fixed point $x \in K \subseteq V$. By step 6, $f(x) = y$, so $y \in W$. Thus $W$ contains the ball of radius $\lambda \rho$ around $y_0$, and $W$ is open.
16. By steps 10 and 11, $f$ restricted to $V$ is a bijection from $V$ onto $W$. Let $g \colon W \to V$ be its inverse.
17. For $x \in V$, the matrix $Df(x)$ is invertible. Indeed, if $Df(x) h = 0$, then $\norm{h} = \norm{A^{-1} (A - Df(x)) h} \le c \lambda \norm{h} = \tfrac{1}{2} \norm{h}$, so $h = 0$.
18. Step 10 gives $\norm{g(y_1) - g(y_2)} \le 2c \norm{y_1 - y_2}$ for $y_1, y_2 \in W$. So $g$ is [[continuous|0S9EK5MQPE]].
19. Let $y \in W$, $x = g(y)$ and $T = Df(x)^{-1}$. Let $k \ne 0$ with $y + k \in W$, and let $h = g(y + k) - x$. Then $f(x + h) = y + k \ne y$, so $h \ne 0$. By step 18, $\norm{h} \le 2c \norm{k}$.
20. Since $f(x + h) - f(x) = k$ and $T Df(x) h = h$, we get $g(y + k) - g(y) - T k = h - T k = -T \big( f(x + h) - f(x) - Df(x) h \big)$.
21. So $\dfrac{\norm{g(y + k) - g(y) - T k}}{\norm{k}} \le 2 c \norm{T} \cdot \dfrac{\norm{f(x + h) - f(x) - Df(x) h}}{\norm{h}}$.
22. As $k \to 0$, also $h \to 0$ by step 19. Since $f$ is differentiable at $x$, the right side of step 21 tends to $0$. So $g$ is differentiable at $y$ with $Dg(y) = Df(g(y))^{-1}$. This is the formula $D(f^{-1})(f(x)) = Df(x)^{-1}$.
23. Identify $n \times n$ matrices with $\R^{n^2}$. The determinant is a polynomial in the entries, so the set $\mathcal{M}$ of invertible matrices is open. For $B \in \mathcal{M}$, each entry of $B^{-1}$ is an entry of the adjugate divided by $\det B$ ([[inverse via the adjugate|0ENVM493VK]]; for $n = 1$, $B^{-1} = 1/B$).
24. So each entry map $\Psi_{il}(B) = (B^{-1})_{il}$ is a polynomial divided by a nonvanishing polynomial on $\mathcal{M}$. Its partial derivatives of every order are again of this form, so $\Psi_{il}$ is of class $C^j$ on $\mathcal{M}$ for every $j$.
25. Lemma. Let $j \ge 1$, let $O \subseteq \R^N$ and $W' \subseteq \R^p$ be open, let $\Phi \colon O \to \R$ be of class $C^j$, and let $G \colon W' \to O$ be of class $C^j$. Then $\Phi \circ G$ is of class $C^j$. We prove this by induction on $j$.
26. Both $\Phi$ and $G$ are differentiable, so the [[chain rule|0EAAS2EHDR]] gives $\partial_i (\Phi \circ G) = \sum_l \big( (\partial_l \Phi) \circ G \big) \, \partial_i G_l$. For $j = 1$, the right side is continuous, so $\Phi \circ G$ is of class $C^1$.
27. Assume the lemma for $j$, and let $\Phi$ and $G$ be of class $C^{j+1}$. In step 26, $(\partial_l \Phi) \circ G$ is of class $C^j$ by the induction hypothesis, and so is $\partial_i G_l$.
28. A product $p q$ of two $C^j$ functions is $\mu \circ (p, q)$ with the polynomial $\mu(s, t) = s t$, so it is of class $C^j$ by the induction hypothesis. Sums of $C^j$ functions are of class $C^j$.
29. So every first partial derivative of $\Phi \circ G$ is of class $C^j$. Hence $\Phi \circ G$ is of class $C^{j+1}$, which proves the lemma.
30. By step 22, the partial derivatives of $g$ are $\partial_l g_i = \Psi_{il} \circ (Df \circ g)$ on $W$. The entries of $Df \circ g$ are the functions $(\partial_l f_i) \circ g$.
31. The functions $\partial_l f_i$ and $g$ are continuous, so $Df \circ g$ is continuous, and so is each $\partial_l g_i$. Hence $g$ is of class $C^1$.
32. Let $1 \le j < k$, and assume that $g$ is of class $C^j$. Each $\partial_l f_i$ is of class $C^{k-1}$, hence of class $C^j$. By the lemma, each $(\partial_l f_i) \circ g$ is of class $C^j$, so $Df \circ g \colon W \to \mathcal{M}$ is of class $C^j$.
33. By step 24 and the lemma, each $\partial_l g_i = \Psi_{il} \circ (Df \circ g)$ is of class $C^j$. So $g$ is of class $C^{j+1}$.
34. By induction, $g = f^{-1}$ is of class $C^k$ on $W$. With steps 11, 15, 16 and 22 this proves the theorem.

## Idea

To solve $f(x) = y$ near $a$, replace $f$ by its linear part $A$ and correct: the map $x \mapsto x + A^{-1}(y - f(x))$ has fixed points exactly at the solutions. Near $a$ its derivative is small, so it is a contraction and has a unique fixed point. The same estimate shows that the inverse is Lipschitz, which gives its derivative, and the formula $Dg = (Df \circ g)^{-1}$ lifts smoothness from $C^j$ to $C^{j+1}$.
