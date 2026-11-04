---
tag: XY7D3X10QR
kind: proof
name: Proof that the real part of a holomorphic function is harmonic
msc: [31A05]
proves: 031BG625Y3
uses: [0DG0Z72CQD, 0QEBN8DGVE, 0T71SSYZ39, 0NNQY8WCW6, 0TCBZMEYGN, 0W5NJQ8MKY, 02ZE6JHJ7G]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_function
    locator: Connections with complex function theory
---

## Proof

We differentiate the Cauchy–Riemann equations once more and use the symmetry of mixed partial derivatives.

1. Since $f$ is [[holomorphic|0DG0Z72CQD]] on $U$, [[holomorphic functions are infinitely differentiable|0QEBN8DGVE]]. So, as a function of $(x, y)$, $f$ has continuous partial derivatives of all orders on $U$.
2. The partial derivatives of $f$ are those of $u$ plus $i$ times those of $v$, by the definition of [[real and imaginary parts|02ZE6JHJ7G]]. So all partial derivatives of $u$ and $v$ exist and are continuous on $U$.
3. In particular, $u$ and $v$ are of [[class $C^2$|0TCBZMEYGN]] on $U$. This is the first claim.
4. Since $f$ is complex differentiable at each point of $U$, the [[Cauchy–Riemann equations|0T71SSYZ39]] hold at each point of $U$: $u_x = v_y$ and $u_y = -v_x$ on $U$.
5. These are equalities of functions on the open set $U$. So we may differentiate both sides. Differentiating $u_x = v_y$ in $x$ gives $u_{xx} = (v_y)_x$.
6. Differentiating $u_y = -v_x$ in $y$ gives $u_{yy} = -(v_x)_y$.
7. Since $v$ is of class $C^2$, [[Schwarz's theorem|0NNQY8WCW6]] gives $(v_y)_x = (v_x)_y$ on $U$.
8. Adding steps 5 and 6 and using step 7 gives $u_{xx} + u_{yy} = (v_y)_x - (v_x)_y = 0$ on $U$.
9. Differentiating $u_y = -v_x$ in $x$ gives $(u_y)_x = -v_{xx}$. Differentiating $u_x = v_y$ in $y$ gives $(u_x)_y = v_{yy}$.
10. Schwarz's theorem for $u$ gives $(u_y)_x = (u_x)_y$. So $v_{xx} + v_{yy} = -(u_y)_x + (u_x)_y = 0$ on $U$.
11. By steps 3, 8 and 10, $u$ and $v$ are of class $C^2$ with zero Laplacian. So they are [[harmonic|0W5NJQ8MKY]] on $U$.

## Idea

The Cauchy–Riemann equations tie the first derivatives of $u$ to those of $v$. Differentiating once more, the two second derivatives $u_{xx}$ and $u_{yy}$ become the same mixed derivative of $v$ with opposite signs. The real work is hidden in step 1: we need to know that $f$ has second derivatives at all.
