---
tag: AHR5BBHR9Q
kind: proof
name: Proof that holomorphic functions with nonzero derivative are conformal
msc: [30C35]
proves: 0Q7M6K6VD7
uses: [0DG0Z72CQD, 0D1C9Y1EXA, 0VHNKP1N3K, 0135XZZQ8M, 0YF0VXKXGB, 0QRBVFJ50X, 0KW2X0TFBX]
sources:
  - url: https://en.wikipedia.org/wiki/Conformal_map
    locator: In two dimensions
---

## Proof

1. Let $U \subseteq \C$ be open, let $f : U \to \C$ be [[holomorphic|0DG0Z72CQD]], and let $z_0 \in U$ with $f'(z_0) \ne 0$. Identify $\C$ with $\R^2$ by $x + iy \leftrightarrow (x, y)$.
2. Since $f$ is holomorphic, it is [[complex differentiable|0D1C9Y1EXA]] at $z_0$. Write $a = f'(z_0)$ and $a = \alpha + i\beta$ with $\alpha, \beta \in \R$.
3. Let $L : \R^2 \to \R^2$ be the map $L(h) = a h$, a product of complex numbers. It is $\R$-linear, because complex multiplication distributes over sums and commutes with real scalars.
4. For $h \ne 0$ with $z_0 + h \in U$, we have $\frac{\abs{f(z_0 + h) - f(z_0) - a h}}{\abs{h}} = \abs{\frac{f(z_0 + h) - f(z_0)}{h} - a}$. Here $\abs{\cdot}$ is the [[modulus|0KW2X0TFBX]], which is the Euclidean norm on $\R^2$.
5. By step 2, the right side of step 4 tends to $0$ as $h \to 0$. So $f$ is [[differentiable at $z_0$|0135XZZQ8M]] as a map from an open subset of $\R^2$ to $\R^2$, with derivative $L$.
6. Write $f = u + iv$ with $u, v$ real valued. Restricting $h$ in step 2 to real numbers $t \ne 0$ gives $\lim_{t \to 0} \frac{f(z_0 + t) - f(z_0)}{t} = a$.
7. Taking real and imaginary parts in step 6 gives the partial derivatives $u_x(z_0) = \alpha$ and $v_x(z_0) = \beta$.
8. Restricting $h$ in step 2 to $h = it$ with real $t \ne 0$ gives $\lim_{t \to 0} \frac{f(z_0 + it) - f(z_0)}{t} = i a = -\beta + i\alpha$.
9. Taking real and imaginary parts in step 8 gives $u_y(z_0) = -\beta$ and $v_y(z_0) = \alpha$.
10. By steps 7 and 9, the [[Jacobian matrix|0YF0VXKXGB]] of $f$ at $z_0$ is
$$J = \begin{pmatrix} \alpha & -\beta \\ \beta & \alpha \end{pmatrix}.$$
11. Let $\lambda = \abs{a} = \sqrt{\alpha^2 + \beta^2}$. Since $a \ne 0$, we have $\lambda > 0$.
12. Let $Q = \lambda^{-1} J$, so $J = \lambda Q$. Then $Q^T Q = \lambda^{-2} \begin{pmatrix} \alpha^2 + \beta^2 & 0 \\ 0 & \alpha^2 + \beta^2 \end{pmatrix} = I_2$, so $Q$ is [[orthogonal|0QRBVFJ50X]].
13. Also $\det Q = \lambda^{-2}(\alpha^2 + \beta^2) = 1$. So $Q$ is a rotation matrix.
14. By steps 5, 10, 12 and 13, $f$ is [[conformal|0VHNKP1N3K]] at $z_0$.
15. If $f'(z) \ne 0$ for each $z \in U$, then steps 1 to 14 apply at each $z \in U$. So $f$ is conformal on $U$.

## Idea

The complex derivative says that near $z_0$ the map $f$ is close to multiplication by the number $a = f'(z_0)$. As a real linear map, multiplication by $a$ has the matrix with rows $(\alpha, -\beta)$ and $(\beta, \alpha)$. This matrix is $\abs{a}$ times a rotation, which is exactly the definition of conformal.
