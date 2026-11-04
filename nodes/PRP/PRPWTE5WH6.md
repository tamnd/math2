---
tag: PRPWTE5WH6
kind: proof
name: Proof that angles in the same segment are equal
msc: [51M04]
proves: 0GS0AW6JRY
uses: [0GA1V8NN8C, 049DCJZ448, 03YN70NK0Z, 0GJAJC6TNZ, 060W5CBZP6, 0MP9BCF6DP, VQ4Q2V45RP, 00KDZRW4C0, 0P4NQD746K]
sources:
  - url: https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_l%27angle_inscrit_et_de_l%27angle_au_centre
    locator: Version relative aux angles orientés de droites
---

## Proof

We compare both angles with the angle at the centre.

1. The points are [[concyclic|049DCJZ448]] in $\mathbb{R}^2$, so they lie on a [[circle|060W5CBZP6]] with a centre $O$ and a radius $r \geq 0$. Since $A \neq B$, we have $r > 0$.
2. By the [[inscribed angle theorem|0GA1V8NN8C]] with $V = C$ and with $V = D$, we get $2\,\measuredangle ACB = \measuredangle AOB = 2\,\measuredangle ADB$. This is the first claim.
3. Let $\theta_C$ and $\theta_D$ be real numbers that represent the [[oriented angles|03YN70NK0Z]] $\measuredangle ACB$ and $\measuredangle ADB$. By step 2, $2\theta_C - 2\theta_D \in 2\pi\mathbb{Z}$, so $\theta_C - \theta_D \in \pi\mathbb{Z}$.
4. Hence either $\theta_C \equiv \theta_D$ or $\theta_C \equiv \theta_D + \pi$ modulo $2\pi$.
5. For the second part, put $f(X) = \det(B - A, X - A)$ for $X \in \mathbb{R}^2$, with the [[determinant|00KDZRW4C0]]. Since $B - A \neq 0$, $f(X) = 0$ if and only if $X$ is on the [[line|0MP9BCF6DP]] $AB$.
6. The points of the line $AB$ are $A + t(B - A)$. Such a point is on the circle when $\norm{A - O + t(B - A)}^2 = r^2$. This is a quadratic equation in $t$ with the leading coefficient $\norm{B - A}^2 > 0$.
7. So the line meets the circle in at most two points, namely $A$ and $B$. Hence $C$ and $D$ are not on the line $AB$, and $f(C) \neq 0$, $f(D) \neq 0$.
8. Let $X$, $Y$ be points off the line $AB$. They are on the same side of it when the [[segment|VQ4Q2V45RP]] $XY$ misses the line. The determinant is linear in its second column, so $f((1 - t)X + tY) = (1 - t)f(X) + t f(Y)$.
9. If $f(X)$ and $f(Y)$ have the same sign, then $(1 - t)f(X) + tf(Y)$ has that sign for $0 \leq t \leq 1$. So the segment misses the line.
10. If they have opposite signs, then $t = \frac{f(X)}{f(X) - f(Y)}$ lies in $(0, 1)$ and makes the value zero. So the segment meets the line. Thus $X$, $Y$ are on the same side if and only if $f(X) f(Y) > 0$.
11. By the definition of the oriented angle, $\sin\theta_C = \frac{\det(A - C, B - C)}{\norm{A - C}\norm{B - C}}$.
12. Since $B - C = (B - A) + (A - C)$, we get $\det(A - C, B - C) = \det(A - C, B - A) = \det(B - A, C - A) = f(C)$. So $\sin\theta_C$ has the sign of $f(C)$. In the same way, $\sin\theta_D$ has the sign of $f(D)$.
13. The [[angle|0GJAJC6TNZ]] $\angle ACB$ is the unique number in $[0, \pi]$ whose cosine is $\cos\theta_C$, since both equal $\frac{(A - C) \cdot (B - C)}{\norm{A - C}\norm{B - C}}$. The same holds for $\angle ADB$ and $\theta_D$.
14. Suppose that $C$ and $D$ are on the same side. Then $\sin\theta_C$ and $\sin\theta_D$ have the same sign by steps 10 and 12. Since [[sine has period $2\pi$|0P4NQD746K]] and $\sin(\theta + \pi) = -\sin\theta$, the case $\theta_C \equiv \theta_D + \pi$ is excluded.
15. So $\theta_C \equiv \theta_D$, hence $\cos\theta_C = \cos\theta_D$. By step 13, $\angle ACB = \angle ADB$.
16. Suppose that $C$ and $D$ are on opposite sides. Then the sines have opposite signs, so $\theta_C \not\equiv \theta_D$. By step 4, $\theta_C \equiv \theta_D + \pi$, so $\cos\theta_C = -\cos\theta_D$.
17. The number $\pi - \angle ADB$ lies in $[0, \pi]$, and its cosine is $-\cos\angle ADB = -\cos\theta_D = \cos\theta_C$. By step 13, $\angle ACB = \pi - \angle ADB$, that is, $\angle ACB + \angle ADB = \pi$.

## Idea

Both inscribed angles are half the central angle, but only up to a half turn. The sign of the sine of an oriented angle tells on which side of $AB$ the vertex lies. On the same side the half turn cannot appear, and on opposite sides it must appear.
