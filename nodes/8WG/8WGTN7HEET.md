---
tag: 8WGTN7HEET
kind: proof
name: Proof that the derivative vanishes at a local extremum
msc: ["26B05"]
proves: 0F405477F8
uses: [04CPG9K1C4, 05AXG3QRKR, 0PCVBRV9VJ, 0135XZZQ8M, 0NS2QYVC4Y, 0YF0VXKXGB]
sources:
  - url: https://en.wikipedia.org/wiki/Interior_extremum_theorem
    locator: Extension
---

## Proof

We restrict $f$ to a line through $a$ and use the one-variable theorem.

1. Let $U$, $f$ and $a$ be as in the statement. Assume first that $f$ has a [[local maximum|04CPG9K1C4]] at $a$.
2. There is $\varepsilon > 0$ with $f(x) \le f(a)$ for all $x \in U$ with $\norm{x - a} < \varepsilon$. Since $U$ is open, we may shrink $\varepsilon$ so that all $x$ with $\norm{x - a} < \varepsilon$ lie in $U$.
3. Let $i$ be an index for which $\partial f / \partial x_i (a)$ exists. Let $e_i$ be the $i$-th standard basis vector, and define $\varphi(t) = f(a + t e_i)$ on the open interval $I = (-\varepsilon, \varepsilon)$.
4. For $t \in I$ we have $\norm{(a + t e_i) - a} = \abs{t} < \varepsilon$, so $\varphi(t) \le f(a) = \varphi(0)$. Thus $\varphi$ has a local maximum at $0$.
5. By the definition of the [[partial derivative|05AXG3QRKR]], $\varphi$ is differentiable at $0$ with $\varphi'(0) = \partial f / \partial x_i (a)$.
6. By [[Fermat's theorem on stationary points|0PCVBRV9VJ]], $\varphi'(0) = 0$. So $\partial f / \partial x_i (a) = 0$.
7. If $f$ has a local minimum at $a$, then $-f$ has a local maximum at $a$, and $\partial (-f)/\partial x_i (a) = -\partial f / \partial x_i (a)$. So step 6 applied to $-f$ gives again $\partial f / \partial x_i (a) = 0$.
8. Now let $f$ be [[differentiable|0135XZZQ8M]] at $a$. Then every partial derivative exists at $a$, and $Df(a) e_i = \partial f / \partial x_i (a)$, since $Df(a)$ has the [[Jacobian matrix|0YF0VXKXGB]] of partial derivatives.
9. By steps 6 and 7, all these partial derivatives are $0$. So the [[gradient|0NS2QYVC4Y]] $\nabla f(a)$, the vector of partial derivatives, is $0$.
10. The linear map $Df(a)$ vanishes on each basis vector $e_i$, so it is the zero linear map.

## Idea

Along each coordinate line through $a$, the function still has a local extremum at $a$. So the one-variable Fermat theorem makes each partial derivative zero. Openness of $U$ is used to make the line segment around $a$ lie in the domain on both sides.
