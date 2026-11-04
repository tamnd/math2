---
tag: XQKD3E9N1X
kind: proof
name: Proof of Menelaus's theorem by a linear function
msc: [51M04]
proves: 07NSKDGS7S
uses: [0CTNFGYMM2, 0MP9BCF6DP, 0AFNNTRTJE, 0KJH6SRFZK, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Menelaus%27s_theorem
    locator: A standard proof
---

## Proof

We measure signed distances to $\ell$ with a determinant.

1. Write the [[line|0MP9BCF6DP]] $\ell$ as $\set{p + tv : t \in \mathbb{R}}$, with a point $p$ and a nonzero vector $v$. For $X \in \mathbb{R}^2$ put $f(X) = \det(v, X - p)$, the [[determinant|00KDZRW4C0]] of the $2 \times 2$ matrix with the columns $v$ and $X - p$.
2. For a vector $u$, $\det(v, u) = 0$ if and only if $u$ is a multiple of $v$, because $v \neq 0$. So $f(X) = 0$ if and only if $X \in \ell$.
3. The determinant is linear in its second column. So for an [[affine combination|0KJH6SRFZK]] $X = (1 - s)Y + sZ$ we have $f(X) = (1 - s) f(Y) + s f(Z)$.
4. Put $a = f(A)$, $b = f(B)$ and $c = f(C)$. They are nonzero by step 2, because $\ell$ does not pass through the vertices $A$, $B$, $C$ of the [[triangle|0CTNFGYMM2]].
5. Let $X = (1 - s)Y + sZ$ with $Y \neq Z$, $s \neq 1$. Then $X - Y = s(Z - Y)$ and $Z - X = (1 - s)(Z - Y)$. So the signed ratio is $\frac{YX}{XZ} = \frac{s}{1 - s}$.

**The direct statement.**

6. The point $D$ is on the line $BC$, so $D = (1 - s)B + sC$ for some $s \in \mathbb{R}$. Since $D \in \ell$, steps 2 and 3 give $(1 - s)b + sc = 0$.
7. If $s = 1$, this gives $c = 0$, against step 4. So $s \neq 1$, and also $s \neq 0$ since $b \neq 0$.
8. By steps 5 and 6, $\frac{BD}{DC} = \frac{s}{1 - s} = -\frac{b}{c}$.
9. In the same way, $\frac{CE}{EA} = -\frac{c}{a}$ and $\frac{AF}{FB} = -\frac{a}{b}$.
10. Multiplying, $\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = \left(-\frac{a}{b}\right)\left(-\frac{b}{c}\right)\left(-\frac{c}{a}\right) = -1$.

**The converse.**

11. Let $D$, $E$, $F$ be as in the converse. Put $x = \frac{BD}{DC}$, $y = \frac{CE}{EA}$ and $z = \frac{AF}{FB}$, so $xyz = -1$.
12. From $D - B = x(C - D)$ we get $(1 + x)D = B + xC$. If $x = -1$, this gives $B = C$, which is false. So $1 + x \neq 0$. Also $x \neq 0$, because $D \neq B$.
13. In the same way, $(1 + y)E = C + yA$ and $(1 + z)F = A + zB$.
14. Then $(1 + y)E - y(1 + z)F = C + yA - yA - yzB = C - yzB$.
15. Since $xyz = -1$ and $x \neq 0$, we have $-yz = \frac{1}{x}$. So the right side of step 14 is $C + \frac{1}{x}B = \frac{1 + x}{x} D$ by step 12.
16. The coefficients on the left of step 14 add up to $1 + y - y - yz = 1 - yz = \frac{1 + x}{x}$.
17. Divide step 14 by $\frac{1 + x}{x} \neq 0$. This gives $D = \lambda E + \mu F$ with $\lambda + \mu = 1$, so $D$ is an affine combination of $E$ and $F$.
18. The points $E$ and $F$ are distinct, because $E = F$ would lie on $CA$ and $AB$, so it would be the vertex $A$. So $E$ and $F$ span a line, and $D = F + \lambda(E - F)$ lies on it.
19. So $D$, $E$ and $F$ are [[collinear|0AFNNTRTJE]].

## Idea

The function $f$ is a signed distance to $\ell$, up to a constant factor. A point of a side lies on $\ell$ exactly when the signed distances of the two endpoints balance. So each ratio is minus a quotient of two of them. The three quotients cancel and leave the three minus signs.
