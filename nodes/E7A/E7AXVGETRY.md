---
tag: E7AXVGETRY
kind: proof
name: Proof of the Cauchy–Riemann equations
msc: [30A99]
proves: 0T71SSYZ39
uses: [0D1C9Y1EXA, 02ZE6JHJ7G, 0135XZZQ8M]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations
    locator: Complex differentiability
---

## Proof

We compare the complex linear approximation of $f$ with the real linear approximations of $u$ and $v$.

1. For $h = s + it \ne 0$ with $s, t$ real and $z_0 + h \in U$, write $\Delta u(h) = u(x_0 + s, y_0 + t) - u(x_0, y_0)$ and $\Delta v(h) = v(x_0 + s, y_0 + t) - v(x_0, y_0)$. Then $f(z_0 + h) - f(z_0) = \Delta u(h) + i \Delta v(h)$, by the definition of [[real and imaginary parts|02ZE6JHJ7G]].
2. For real numbers $A, B$, we have $(A + iB) h = (As - Bt) + i (Bs + At)$.
3. Hence, for $A, B$ real,
$$f(z_0 + h) - f(z_0) - (A + iB) h = \big(\Delta u(h) - As + Bt\big) + i \big(\Delta v(h) - Bs - At\big).$$
Call the two real brackets $\varepsilon_1(h)$ and $\varepsilon_2(h)$.
4. We have $|\varepsilon_1|, |\varepsilon_2| \le |\varepsilon_1 + i \varepsilon_2| \le |\varepsilon_1| + |\varepsilon_2|$. So $(\varepsilon_1 + i\varepsilon_2)(h)/|h| \to 0$ as $h \to 0$ if and only if $\varepsilon_1(h)/|h| \to 0$ and $\varepsilon_2(h)/|h| \to 0$.
5. Also $|h| = \norm{(s, t)}$. Dividing by $h$ instead of $|h|$ does not change whether a quantity tends to $0$, because $\abs{h / |h|} = 1$.
6. Suppose first that $f$ is [[complex differentiable|0D1C9Y1EXA]] at $z_0$. Write $f'(z_0) = A + iB$ with $A, B$ real.
7. By the definition of $f'(z_0)$, the quotient $\big(f(z_0 + h) - f(z_0) - f'(z_0) h\big)/h$ tends to $0$. By steps 3 to 5, $\varepsilon_1(h)/\norm{(s,t)} \to 0$ and $\varepsilon_2(h)/\norm{(s,t)} \to 0$.
8. So $u$ is [[differentiable|0135XZZQ8M]] at $(x_0, y_0)$, and its derivative is the linear map $(s, t) \mapsto As - Bt$. Thus $u_x = A$ and $u_y = -B$ there.
9. In the same way, $v$ is differentiable at $(x_0, y_0)$ with derivative $(s, t) \mapsto Bs + At$. Thus $v_x = B$ and $v_y = A$ there.
10. Hence $u_x = A = v_y$ and $u_y = -B = -v_x$ at $(x_0, y_0)$. Also $f'(z_0) = A + iB = u_x + i v_x$.
11. Conversely, suppose that $u$ and $v$ are differentiable at $(x_0, y_0)$ and satisfy the two equations there. Put $A = u_x(x_0, y_0)$ and $B = v_x(x_0, y_0)$.
12. The equations give $u_y = -B$ and $v_y = A$ at $(x_0, y_0)$. So the derivatives of $u$ and $v$ are the maps $(s, t) \mapsto As - Bt$ and $(s, t) \mapsto Bs + At$.
13. By the definition of differentiability, $\varepsilon_1(h)/|h| \to 0$ and $\varepsilon_2(h)/|h| \to 0$ as $h \to 0$.
14. By steps 3 to 5, $\big(f(z_0 + h) - f(z_0)\big)/h - (A + iB) \to 0$ as $h \to 0$.
15. So $f$ is complex differentiable at $z_0$, and $f'(z_0) = A + iB = u_x(x_0, y_0) + i v_x(x_0, y_0)$.

## Idea

Multiplication by $A + iB$ is the real linear map of the plane with matrix $\begin{pmatrix} A & -B \\ B & A \end{pmatrix}$. So a complex derivative is a real derivative whose matrix has this special form. The Cauchy–Riemann equations say exactly that the Jacobian matrix of $(u, v)$ has this form.
