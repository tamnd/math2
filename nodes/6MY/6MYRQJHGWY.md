---
tag: 6MYRQJHGWY
kind: proof
name: Proof of the tangent–secant theorem by the power of a point
msc: [51M04]
proves: 0QX7E9KAAX
uses: [0T7DX8NY1X, 060W5CBZP6, 0NPPGHQNXQ, 02E9VT1RVQ, 0MP9BCF6DP, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Power_of_a_point
    locator: "Secants theorem, chords theorem: common proof"
---

## Proof

We show that both sides equal the [[power|02E9VT1RVQ]] $k = d(P, O)^2 - r^2$ of $P$.

1. Let $O$ be the centre and $r > 0$ the radius of the [[circle|060W5CBZP6]] $C$, and let $d$ be the [[Euclidean distance|0NPPGHQNXQ]]. Put $k = \norm{P - O}^2 - r^2$.
2. For a unit vector $u$, put $q(t) = t^2 + pt + k$ with $p = 2\, u \cdot (P - O)$. With the [[dot product|0S52TNNTH9]], $\norm{P + tu - O}^2 - r^2 = q(t)$. So $P + tu \in C$ if and only if $q(t) = 0$.
3. Since $P$ is outside $C$, $P \neq T$. Let $u = (T - P)/\norm{T - P}$ and $t_0 = \norm{T - P} = d(P, T)$.
4. The tangent line $\ell$ contains $P$ and $T$, so it is the [[line|0MP9BCF6DP]] $\set{P + tu : t \in \mathbb{R}}$. Also $T = P + t_0 u$, so $q(t_0) = 0$.
5. Put $t_1 = -p - t_0$, so $p = -(t_0 + t_1)$. From $q(t_0) = 0$ we get $k = -t_0^2 - pt_0 = t_0 t_1$.
6. Then $q(t) = t^2 - (t_0 + t_1)t + t_0 t_1 = (t - t_0)(t - t_1)$, so $q(t_1) = 0$. Hence $P + t_1 u \in \ell \cap C$.
7. Since $\ell$ is [[tangent|0T7DX8NY1X]] at $T$, $\ell \cap C = \set{T}$. So $P + t_1 u = T = P + t_0 u$, and $t_1 = t_0$.
8. By steps 5 and 7, $k = t_0^2 = d(P, T)^2$.
9. Now let $u'$ be a unit direction vector of the second line, so this line is $\set{P + tu'}$. Then $G_1 = P + s_1 u'$ and $G_2 = P + s_2 u'$, with $s_1 \neq s_2$ since $G_1 \neq G_2$.
10. Let $q'(t) = t^2 + p't + k$ with $p' = 2\, u' \cdot (P - O)$. By step 2 for $u'$, $q'(s_1) = q'(s_2) = 0$.
11. Subtracting, $0 = (s_1 - s_2)(s_1 + s_2 + p')$, so $p' = -(s_1 + s_2)$. Then $0 = q'(s_1) = k - s_1 s_2$, so $s_1 s_2 = k$.
12. Since $u'$ is a unit vector, $d(P, G_1)\, d(P, G_2) = \abs{s_1}\abs{s_2} = \abs{k}$.
13. By step 8, $k = d(P, T)^2 \geq 0$, so $\abs{k} = k$. Hence $d(P, T)^2 = d(P, G_1)\, d(P, G_2)$.

## Idea

On each line through $P$, the points of the circle are the roots of a quadratic equation with the constant term $k$. For the tangent the two roots coincide, so $k$ is the square of the tangent length. For the secant, $k$ is the product of the two distances.
