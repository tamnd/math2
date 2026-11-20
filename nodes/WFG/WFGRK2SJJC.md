---
tag: WFGRK2SJJC
kind: proof
name: Proof of the classification of the orthogonal group of the plane
msc: ["15B10", "51F15"]
topics: [AZS5BPF5H3]
audience: ug1
proves: C97Z06HHB2
uses: [F7M8ZXB4P7, 04R3CY41VJ, FEER10D15S]
methods: [0NTF6DMVAP, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_matrix
    locator: Lower dimensions
---

## Proof

Let $D = \operatorname{diag}(1, -1)$.

**Part 1.**

1. Let $Q$ be a real $2 \times 2$ orthogonal matrix. Its columns are orthonormal, by [[the equivalent conditions|F7M8ZXB4P7]].
2. The first column $(a, c)$ has $a^2 + c^2 = 1$. So it is a point of the unit circle, and $(a, c) = (\cos\theta, \sin\theta)$ for some $\theta \in \R$.
3. The second column is a unit vector orthogonal to $(\cos\theta, \sin\theta)$. The vectors orthogonal to it are the multiples of $(-\sin\theta, \cos\theta)$, and the unit vectors among them are $\pm(-\sin\theta, \cos\theta)$.
4. Case $+$: $Q = R(\theta)$, and $\det Q = \cos^2\theta + \sin^2\theta = 1$.
5. Case $-$: $Q = \begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix} = S(\theta/2)$, and $\det Q = -\cos^2\theta - \sin^2\theta = -1$.

**Part 2.**

6. Let $u = (-\sin\alpha, \cos\alpha)$, a unit vector orthogonal to $(\cos\alpha, \sin\alpha)$.
7. By part 4 of [[the reflection theorem|FEER10D15S]], the reflection $s_u$ has the matrix $I - 2uu^T = \begin{pmatrix} 1 - 2\sin^2\alpha & 2\sin\alpha\cos\alpha \\ 2\sin\alpha\cos\alpha & 1 - 2\cos^2\alpha \end{pmatrix}$.
8. By the double angle formulas, $1 - 2\sin^2\alpha = \cos 2\alpha$, $2\sin\alpha\cos\alpha = \sin 2\alpha$ and $1 - 2\cos^2\alpha = -\cos 2\alpha$. So $s_u = S(\alpha)$.
9. The mirror of $s_u$ is $u^\perp$, the line through $0$ and $(\cos\alpha, \sin\alpha)$.

**Part 3.**

10. The entries of $R(\theta)R(\varphi)$ are $\cos\theta\cos\varphi - \sin\theta\sin\varphi = \cos(\theta + \varphi)$ and $\sin\theta\cos\varphi + \cos\theta\sin\varphi = \sin(\theta + \varphi)$, with the signs of $R$. So $R(\theta)R(\varphi) = R(\theta + \varphi)$. These are the addition formulas, which follow from [[Euler's formula|04R3CY41VJ]] $e^{i\theta}e^{i\varphi} = e^{i(\theta + \varphi)}$.
11. Direct multiplication gives $S(\alpha) = R(2\alpha)D$: the product $R(2\alpha)D$ negates the second column of $R(2\alpha)$.
12. Direct multiplication gives $DR(\theta)D = R(-\theta)$, because $\cos$ is even and $\sin$ is odd. As $D^2 = I$, this says $DR(\theta) = R(-\theta)D$.
13. $S(\alpha)S(\beta) = R(2\alpha)DR(2\beta)D = R(2\alpha)R(-2\beta) = R(2(\alpha - \beta))$, by steps 11, 12 and 10.
14. $R(\theta)S(\alpha) = R(\theta)R(2\alpha)D = R(\theta + 2\alpha)D = S\left(\alpha + \frac{\theta}{2}\right)$, by steps 10 and 11.
15. $S(\alpha)R(\theta) = R(2\alpha)DR(\theta) = R(2\alpha)R(-\theta)D = R(2\alpha - \theta)D = S\left(\alpha - \frac{\theta}{2}\right)$, by steps 11, 12 and 10. $\blacksquare$

## Idea

The first column of an orthogonal $2 \times 2$ matrix is a point of the unit circle, and the second column is a quarter turn of it in one of two directions.
All products follow from $S(\alpha) = R(2\alpha)D$ and $DR(\theta)D = R(-\theta)$.

## Variants

- Part 1 also follows from [[the index-two theorem|XAVVA317M0]]: $SO(2) = \set{R(\theta)}$, and the other coset is $SO(2)D = \set{R(2\alpha)D}$.
- In complex notation, $R(\theta)$ is $z \mapsto e^{i\theta}z$ and $S(\alpha)$ is $z \mapsto e^{2i\alpha}\overline{z}$. Then $S(\alpha)S(\beta)z = e^{2i\alpha}\overline{e^{2i\beta}\overline{z}} = e^{2i(\alpha - \beta)}z$.
