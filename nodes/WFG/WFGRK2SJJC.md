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

We place the first column of an orthogonal matrix on the unit circle, find the two choices for the second column, and then derive all products from two small identities.
Let $D = \operatorname{diag}(1, -1)$.

**Part 1.**

1. Let $Q$ be a real $2 \times 2$ orthogonal matrix. Its columns are orthonormal, by [[the equivalent conditions for an orthogonal matrix|F7M8ZXB4P7]].
2. The first column $(a, c)$ has $a^2 + c^2 = 1$, so it is a point of the unit circle. Hence $(a, c) = (\cos\theta, \sin\theta)$ for some $\theta \in \R$.
3. The second column is a unit vector orthogonal to $(\cos\theta, \sin\theta)$. The vectors $(x, y)$ with $x\cos\theta + y\sin\theta = 0$ are the multiples of $(-\sin\theta, \cos\theta)$, and the two unit vectors among them are $\pm(-\sin\theta, \cos\theta)$.
4. With the sign $+$, $Q = R(\theta)$, and $\det Q = \cos^2\theta + \sin^2\theta = 1$.
5. With the sign $-$,
$$Q = \begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix} = S\left(\tfrac{\theta}{2}\right), \qquad \det Q = -\cos^2\theta - \sin^2\theta = -1.$$

**Part 2.**

6. Let $u = (-\sin\alpha, \cos\alpha)$, a unit vector orthogonal to the line through $0$ and $(\cos\alpha, \sin\alpha)$.
7. By [[the properties of reflections|FEER10D15S]], the reflection $s_u$ in the line $u^\perp$ has the matrix $I - 2uu^{\mathsf{T}}$. Since $uu^{\mathsf{T}} = \begin{pmatrix} \sin^2\alpha & -\sin\alpha\cos\alpha \\ -\sin\alpha\cos\alpha & \cos^2\alpha \end{pmatrix}$, this is
$$I - 2uu^{\mathsf{T}} = \begin{pmatrix} 1 - 2\sin^2\alpha & 2\sin\alpha\cos\alpha \\ 2\sin\alpha\cos\alpha & 1 - 2\cos^2\alpha \end{pmatrix}.$$
8. The double angle formulas give $1 - 2\sin^2\alpha = \cos 2\alpha$, $2\sin\alpha\cos\alpha = \sin 2\alpha$ and $1 - 2\cos^2\alpha = -\cos 2\alpha$. So $s_u = S(\alpha)$.
9. The mirror of $s_u$ is the line $u^\perp$, which is the line through $0$ and $(\cos\alpha, \sin\alpha)$ by step 6.

**Part 3.**

10. The entries of $R(\theta) R(\varphi)$ are $\cos\theta\cos\varphi - \sin\theta\sin\varphi$ and $\sin\theta\cos\varphi + \cos\theta\sin\varphi$, with the signs of $R$. By the addition formulas, which follow from [[Euler's formula|04R3CY41VJ]] $e^{i\theta} e^{i\varphi} = e^{i(\theta + \varphi)}$, these are $\cos(\theta + \varphi)$ and $\sin(\theta + \varphi)$. So $R(\theta) R(\varphi) = R(\theta + \varphi)$.
11. Multiplying by $D$ on the right negates the second column, so $R(2\alpha) D = S(\alpha)$.
12. Multiplying by $D$ on both sides negates the off-diagonal entries. Since $\cos$ is even and $\sin$ is odd, this gives $D R(\theta) D = R(-\theta)$, and since $D^2 = I$, also $D R(\theta) = R(-\theta) D$.
13. By steps 11, 12 and 10,
$$S(\alpha) S(\beta) = R(2\alpha) D R(2\beta) D = R(2\alpha) R(-2\beta) = R\big(2(\alpha - \beta)\big).$$
14. By steps 10 and 11,
$$R(\theta) S(\alpha) = R(\theta) R(2\alpha) D = R(\theta + 2\alpha) D = S\left(\alpha + \tfrac{\theta}{2}\right).$$
15. By steps 11, 12 and 10,
$$S(\alpha) R(\theta) = R(2\alpha) D R(\theta) = R(2\alpha) R(-\theta) D = R(2\alpha - \theta) D = S\left(\alpha - \tfrac{\theta}{2}\right). \qquad \blacksquare$$

## Idea

The first column of an orthogonal $2 \times 2$ matrix is a point of the unit circle, so it is $(\cos\theta, \sin\theta)$.
The second column must be a quarter turn of the first, and there are only two quarter turns, one in each direction.
One choice gives a rotation, and the other gives a reflection.
For the products, everything follows from two identities: a reflection is a rotation times $D$, and $D$ reverses a rotation when it passes through it.

## Variants

Part 1 also follows from [[the index-two theorem|XAVVA317M0]].
It gives $SO(2) = \{ R(\theta) \}$, and the other coset is $SO(2) D = \{ R(2\alpha) D \} = \{ S(\alpha) \}$.

In complex notation, identify $(x, y)$ with $z = x + iy$.
Then $R(\theta)$ is $z \mapsto e^{i\theta} z$ and $S(\alpha)$ is $z \mapsto e^{2i\alpha} \overline{z}$, and the product rule for reflections becomes one line:
$$S(\alpha) S(\beta) z = e^{2i\alpha} \overline{e^{2i\beta} \overline{z}} = e^{2i\alpha} e^{-2i\beta} z = e^{2i(\alpha - \beta)} z.$$
