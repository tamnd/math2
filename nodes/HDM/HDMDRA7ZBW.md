---
tag: HDMDRA7ZBW
kind: proof
name: Proof that C^1 functions are strictly differentiable
msc: ["26B05"]
proves: 0STPPDXGME
uses: [0146MBQNNE, 0TCBZMEYGN, 0KXSK8TEEB, 0YF0VXKXGB, 0ZTEH055YF, 0RFWW56Y22, 02CYB184RC, 0K06X9QXDX]
sources:
  - url: https://en.wikipedia.org/wiki/Strict_differentiability
    locator: Basic definition
---

## Proof

We apply the mean value inequality to $f$ minus its linear part at $a$.

1. Let $U$ and $f$ be as in the statement, and let $a \in U$. Write $\norm{B}$ for the [[operator norm|0ZTEH055YF]] of a matrix $B$.
2. Since $f$ is of [[class C^1|0TCBZMEYGN]], it is [[differentiable|0KXSK8TEEB]] at each point $z \in U$, and $Df(z)$ is the [[Jacobian matrix|0YF0VXKXGB]] of partial derivatives at $z$.
3. For a matrix $B = (b_{ij})$, the [[Cauchy–Schwarz inequality|0RFWW56Y22]] on each row gives $\norm{B} \le (\sum_{i, j} b_{ij}^2)^{1/2}$.
4. Let $\varepsilon > 0$. The partial derivatives of $f$ are continuous at $a$. By step 3, there is $r > 0$ such that the ball $B_r = \set{z : \norm{z - a} < r}$ lies in $U$ and $\norm{Df(z) - Df(a)} \le \varepsilon$ for $z \in B_r$.
5. Let $g(z) = f(z) - Df(a) z$ for $z \in U$. A linear map is its own derivative, so $g$ is differentiable on $U$ with $Dg(z) = Df(z) - Df(a)$.
6. The ball $B_r$ is [[convex|0K06X9QXDX]], so it contains the segment between any two of its points. By the [[mean value inequality|02CYB184RC]] and step 4, $\norm{g(x) - g(y)} \le \varepsilon \norm{x - y}$ for $x, y \in B_r$.
7. Since $g(x) - g(y) = f(x) - f(y) - Df(a)(x - y)$, this says $\norm{f(x) - f(y) - Df(a)(x - y)} \le \varepsilon \norm{x - y}$ for $x, y \in B_r$.
8. If $\norm{(x, y) - (a, a)} < r$, then $\norm{x - a} < r$ and $\norm{y - a} < r$, so $x, y \in B_r$. For such pairs with $x \ne y$, step 7 gives $\frac{\norm{f(x) - f(y) - Df(a)(x - y)}}{\norm{x - y}} \le \varepsilon$.
9. Since $\varepsilon > 0$ was arbitrary, this quotient tends to $0$ as $(x, y) \to (a, a)$ with $x \ne y$. So $f$ is [[strictly differentiable|0146MBQNNE]] at $a$, with linear map $Df(a)$.

## Idea

Subtracting the linear map $Df(a)$ leaves a function whose derivative is small near $a$, because $Df$ is continuous. The mean value inequality turns a small derivative into a small Lipschitz constant, and this is exactly the estimate that strict differentiability asks for.
