---
tag: QB6RCHAYK0
kind: proof
name: Proof of the impossibility of trisecting the angle
msc: [12F05]
proves: 0EWXPZCSZ0
uses: [0FMN2MN7TM, 00J3DCCEK5, 03MTBVG3VE, 03H7WZ4T3K, 0819CQ1V8H, 0VNE161QCK, 0GK1WB9R98, 06K7SARZKR, 0N5QW9K7MH, 0SSSM1D475, 0PN9WMRWT7, 04R3CY41VJ, 0BJV24C4SY, 0KW2X0TFBX, 0ZB7J071WQ]
sources:
  - url: https://en.wikipedia.org/wiki/Angle_trisection
    locator: Proof of impossibility
---

## Proof

Let $\theta = \pi/9$, let $c = \cos\theta$ and $s = \sin\theta$, and let $\mathcal{C}$ be the set of the [[constructible numbers|0FMN2MN7TM]].

1. By [[de Moivre's formula|03MTBVG3VE]], $\cos 3\theta + i \sin 3\theta = (c + i s)^3 = c^3 + 3 i c^2 s - 3 c s^2 - i s^3$.
2. Comparing real parts, and using [[$s^2 = 1 - c^2$|03H7WZ4T3K]], we get $\cos 3\theta = c^3 - 3c(1 - c^2) = 4c^3 - 3c$.
3. Since $\cos 3\theta = \cos(\pi/3) = 1/2$, we get $8c^3 - 6c - 1 = 0$. So $u = 2c$ is a root of $g = x^3 - 3x - 1$.
4. By the [[rational root theorem|0819CQ1V8H]], a rational root of $g$ is $\pm 1$. But $g(1) = -3$ and $g(-1) = 1$. So $g$ has no rational root.
5. A cubic with no root in $\Q$ is [[irreducible over $\Q$|0VNE161QCK]]. So the [[minimal polynomial|0GK1WB9R98]] of $u$, which [[divides|06K7SARZKR]] the monic $g$, equals $g$.
6. By the [[degree of a simple extension|0N5QW9K7MH]], $[\Q(u) : \Q] = 3$. Since $c = u/2$ and $u = 2c$, we have $\Q(c) = \Q(u)$, so $[\Q(c) : \Q] = 3$.
7. The degree of a constructible number is a [[power of $2$|0SSSM1D475]], and $3$ is not. So $\cos(\pi/9) \notin \mathcal{C}$.

Now we turn to the construction problem. The angle $\pi/3$ has vertex $0$ and sides through $1$ and $\omega = e^{i\pi/3}$. A [[trisection|00J3DCCEK5]] would construct a point $w \neq 0$ on the ray from $0$ at angle $\pi/9$.

8. By the [[field theorem|0PN9WMRWT7]], $\mathcal{C}$ is a subfield of $\C$ closed under square roots, and it is the smallest such subfield.
9. By [[Euler's formula|04R3CY41VJ]], $\omega = 1/2 + i\sqrt{3}/2$. Here $i$ is a square root of $-1$ and $\sqrt 3$ a square root of $3$, so $\omega \in \mathcal{C}$. So the angle $\pi/3$ can be drawn.
10. Let $\overline{\mathcal{C}}$ be the set of the [[conjugates|0BJV24C4SY]] of the elements of $\mathcal{C}$. Conjugation preserves the field operations, so $\overline{\mathcal{C}}$ is a subfield of $\C$.
11. If $w' = \bar z$ with $z \in \mathcal{C}$ and $t^2 = w'$, then $\bar t^2 = z$, so $\bar t \in \mathcal{C}$ and $t \in \overline{\mathcal{C}}$. So $\overline{\mathcal{C}}$ is closed under square roots.
12. By minimality, $\mathcal{C} \subseteq \overline{\mathcal{C}}$. So each $z \in \mathcal{C}$ is $\bar u$ for some $u \in \mathcal{C}$, and then $\bar z = u \in \mathcal{C}$.
13. Suppose that the point $w$ is constructed. The given points $0$, $1$ and $\omega$ lie in $\mathcal{C}$, so $w \in \mathcal{C}$. Then $\bar w \in \mathcal{C}$, so [[$w \bar w = \abs{w}^2$|0ZB7J071WQ]] is in $\mathcal{C}$. Its square root, the [[modulus|0KW2X0TFBX]] $\abs{w}$, is in $\mathcal{C}$.
14. Since $w$ lies on the ray at angle $\theta$, we have $w = \abs{w} e^{i\theta}$, so $e^{i\theta} = w / \abs{w} \in \mathcal{C}$.
15. Then $\cos\theta = (e^{i\theta} + \overline{e^{i\theta}})/2 \in \mathcal{C}$, by Euler's formula and step 12. This contradicts step 7.
16. So the angle $\pi/3$ cannot be trisected with straightedge and compass, and $\cos(\pi/9)$ is not constructible.

## Idea

The triple angle formula makes $2\cos(\pi/9)$ a root of the irreducible cubic $x^3 - 3x - 1$. So its degree over $\Q$ is $3$, which is not a power of $2$. A trisection would produce the point $e^{i\pi/9}$, and then its real part would be constructible.
