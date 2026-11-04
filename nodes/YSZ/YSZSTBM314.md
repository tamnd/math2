---
tag: YSZSTBM314
kind: proof
name: Proof of the classification of isometries of the plane
msc: [51F20]
proves: 0P0XDY9FZN
uses: [0J1N3WTKM4, 087VJM5Q77, 0HFREYRSZP, 06BRDF3F0E, 0167F9B344, 0NPPGHQNXQ, 0S52TNNTH9, 05FKHRT0B4, 0JWM6GJNQW, 096V7H13H9, 09DZ8CD1AK, 0W02QESPJQ, 0BRXFNQ5JV, 04R3CY41VJ, 03H7WZ4T3K, 028XEQCE88, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_plane_isometry
    locator: Classification
---

## Proof

We first write $f$ as $x \mapsto Mx + b$, and then sort the cases by $M$.

1. Put $g(x) = f(x) - f(0)$. Since $f$ is a [[Euclidean isometry|0J1N3WTKM4]], $\norm{g(x) - g(y)} = \norm{f(x) - f(y)} = \norm{x - y}$ for all $x, y$. With $y = 0$, $\norm{g(x)} = \norm{x}$.
2. By the [[polarisation identity|05FKHRT0B4]], $g(x) \cdot g(y) = \frac{1}{2}(\norm{g(x)}^2 + \norm{g(y)}^2 - \norm{g(x) - g(y)}^2)$. By step 1 this equals $x \cdot y$, the [[dot product|0S52TNNTH9]] of $x$ and $y$.
3. Let $e_1$, $e_2$ be the standard basis and $c_j = g(e_j)$. By step 2, $c_1$, $c_2$ are orthonormal. An [[orthonormal family is linearly independent|0JWM6GJNQW]], so $c_1$, $c_2$ form a [[basis|096V7H13H9]] of $\mathbb{R}^2$.
4. By the [[coordinates in an orthonormal basis|09DZ8CD1AK]], $g(x) = (g(x) \cdot c_1)c_1 + (g(x) \cdot c_2)c_2$. By step 2, this is $x_1 c_1 + x_2 c_2$ for $x = (x_1, x_2)$.
5. So $f(x) = Mx + b$, where $b = f(0)$ and $M$ is the matrix with the orthonormal columns $c_1$, $c_2$. Thus $M$ is an [[orthogonal matrix|0W02QESPJQ]].
6. Since $\norm{c_1} = 1$, the [[polar form|0BRXFNQ5JV]] of the complex number with the coordinates of $c_1$ and [[Euler's formula|04R3CY41VJ]] give a real $\theta$ with $c_1 = (\cos\theta, \sin\theta)$.
7. Put $m = (-\sin\theta, \cos\theta)$. By the [[Pythagorean identity|03H7WZ4T3K]], $c_1$, $m$ are orthonormal. Expanding $c_2$ in this basis gives $c_2 = (c_2 \cdot c_1)c_1 + (c_2 \cdot m)m = \lambda m$, with $\lambda = c_2 \cdot m$.
8. From $\norm{c_2} = 1$ we get $\abs{\lambda} = 1$, so $\lambda = 1$ or $\lambda = -1$.
9. Case $\lambda = 1$ and $\theta \in 2\pi\mathbb{Z}$. Then $M$ is the identity matrix and $f(x) = x + b$. If $b = 0$, $f$ is the identity. Otherwise, $f$ is the [[translation|087VJM5Q77]] by $b \neq 0$.
10. Case $\lambda = 1$ and $\theta \notin 2\pi\mathbb{Z}$. Then $M = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$, and $\cos\theta \neq 1$.
11. The [[determinant|00KDZRW4C0]] of $M - I$ is $(\cos\theta - 1)^2 + \sin^2\theta = 2 - 2\cos\theta > 0$. So $I - M$ is invertible.
12. Put $c = (I - M)^{-1} b$. Then $c + M(p - c) = Mp + (I - M)c = Mp + b = f(p)$. So $f$ is the [[rotation|0HFREYRSZP]] about $c$ through the angle $\theta \notin 2\pi\mathbb{Z}$.
13. Case $\lambda = -1$. Then $M = \begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix}$. Put $s = \sin\frac{\theta}{2}$, $k = \cos\frac{\theta}{2}$ and the unit vector $n = (s, -k)$.
14. By the [[angle addition formulas|028XEQCE88]] and the Pythagorean identity, $\cos\theta = 1 - 2s^2 = 2k^2 - 1$ and $\sin\theta = 2sk$. So $M = I - 2nn^T$, that is, $Mx = x - 2(x \cdot n)n$.
15. Put $\beta = b \cdot n$ and $w = b - \beta n$, so $w \cdot n = 0$. Then $f(x) = x - 2(x \cdot n - \tfrac{\beta}{2})n + w$.
16. Let $H = \set{x : x \cdot n = \beta/2}$. Since $n \cdot n = 1$, step 15 says $f = T_w \circ \sigma_H$, with the [[reflection|06BRDF3F0E]] $\sigma_H$ and the translation $T_w$.
17. If $w = 0$, then $f = \sigma_H$ is a reflection in a line. If $w \neq 0$, then $f$ is a [[glide reflection|0167F9B344]] with the nonzero glide vector $w$, since $w \cdot n = 0$.
18. So $f$ has at least one of the five types. It remains to see that no map has two types. We count fixed points.
19. The identity fixes every point. A translation by $v \neq 0$ fixes none, since $p + v \neq p$.
20. A rotation $p \mapsto c + M(p - c)$ with $\theta \notin 2\pi\mathbb{Z}$ fixes $p$ if and only if $(M - I)(p - c) = 0$. By step 11, this means $p = c$. So it has exactly one fixed point.
21. A reflection $\sigma_H(x) = x - 2\frac{x \cdot a - \kappa}{a \cdot a} a$, with $a \neq 0$ and $H = \set{x : x \cdot a = \kappa}$, fixes $x$ if and only if $x \cdot a = \kappa$. So its fixed set is the line $H$, which has more than one point but is not the whole plane.
22. Let $T_w \circ \sigma_H$ be a glide reflection, with $w \neq 0$ and $w \cdot a = 0$. If $x$ were fixed, then $w = 2\frac{x \cdot a - \kappa}{a \cdot a} a$. Taking the dot product with $w$ would give $\norm{w}^2 = 0$, a contradiction. So it has no fixed point.
23. By steps 19 to 22, only a translation and a glide reflection could coincide. For a translation $f$, $f(x) - f(0) = x$ for all $x$.
24. For a glide reflection, $f(x) - f(0) = \sigma_H(x) - \sigma_H(0) = x - 2\frac{x \cdot a}{a \cdot a} a$. At $x = a$ this is $-a \neq a$. So a glide reflection is not a translation, and $f$ has exactly one of the five types.

## Idea

An isometry that fixes the origin keeps dot products, so it is an orthogonal matrix. A $2 \times 2$ orthogonal matrix is a rotation matrix or the matrix of a reflection. Then the translation part either moves the centre of the rotation, or splits into a shift of the mirror and a glide along it. Fixed points tell the five types apart.
