---
tag: 5J73GZAZKS
kind: proof
name: Proof of the Wronskian test for linear independence of solutions
msc: [34A30]
proves: 0MHE4B1QCQ
uses: [0N5NF1RGBP, 0EQZSAB9EC, 0GK68PZ6KH, 0F2VBPXNP9, 0M0TKFRX2A, 03Q7RE2HXR, 0912EEEVCT, 0EVHJFTG9Z]
sources:
  - url: https://en.wikipedia.org/wiki/Wronskian
    locator: Application to linear differential equations
---

## Proof

1. Let $S$ be the space of solutions on $I$ of the [[homogeneous linear equation|0EQZSAB9EC]]. For $x \in I$, let $\Phi_x(y) = \left(y(x), y'(x), \dots, y^{(n-1)}(x)\right)$ for $y \in S$.
2. By the [[dimension theorem for the solution space|0GK68PZ6KH]], $\Phi_x : S \to \R^n$ is a linear bijection for each $x \in I$.
3. For $x \in I$, let $M(x)$ be the $n \times n$ matrix whose column $j$ is $\Phi_x(y_j)$. By the definition of the [[Wronskian|0N5NF1RGBP]], $W(x) = \det M(x)$.
4. For $c = (c_1, \dots, c_n) \in \R^n$, let $y_c = \sum_j c_j y_j$. By the [[superposition principle|0F2VBPXNP9]], $y_c \in S$. By linearity of $\Phi_x$, $\Phi_x(y_c) = M(x)\, c$.
5. (a) implies (c). Assume (a), and suppose $W(x) = 0$ for some $x \in I$. Then [[$M(x)$ is not invertible|03Q7RE2HXR]].
6. The linear map $c \mapsto M(x) c$ of $\R^n$ is then not bijective. By [[the injective endomorphism theorem|0912EEEVCT]], it is not injective. So there is $c \ne 0$ with $M(x) c = 0$.
7. By step 4, $\Phi_x(y_c) = 0$. Since $\Phi_x$ is injective, $y_c = 0$ on $I$.
8. So $\sum_j c_j y_j = 0$ on $I$ with $c \ne 0$. This contradicts the [[linear independence|0EVHJFTG9Z]] in (a). Hence $W(x) \ne 0$ for each $x \in I$.
9. (c) implies (b). The interval $I$ is not empty, so take any $x_0 \in I$.
10. (b) implies (a). Let $W(x_0) \ne 0$, and let $c \in \R^n$ with $\sum_j c_j y_j = 0$ on $I$. So $y_c = 0$, and all its derivatives vanish on $I$, by [[linearity of differentiation|0M0TKFRX2A]].
11. In particular $M(x_0)\, c = \Phi_{x_0}(y_c) = 0$, by step 4. Since $\det M(x_0) = W(x_0) \ne 0$, the matrix $M(x_0)$ is invertible.
12. Hence $c = M(x_0)^{-1} M(x_0)\, c = 0$. So $y_1, \dots, y_n$ are linearly independent on $I$.
13. The implications (a) to (c), (c) to (b) and (b) to (a) show that the three conditions are equivalent.

## Idea

The columns of the Wronskian matrix at $x$ are the initial values of the solutions at $x$. A solution is determined by its initial values at any one point. So a dependence among the columns at one point is a dependence among the solutions on all of $I$.
