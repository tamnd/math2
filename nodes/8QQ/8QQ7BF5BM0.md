---
tag: 8QQ7BF5BM0
kind: definition
name: Solving linear difference equations by the Z-transform
msc: [39A06, 44A55]
defines: DAVT2ZWAF7
uses: [0NDVHBVBXB, EPG6JPVJE7, JWH2KYCGBQ, PH61T3B7W7, 030VFEREKG]
sources:
  - url: https://en.wikipedia.org/wiki/Z-transform
    locator: Linear constant-coefficient difference equation
---

## Definition

Let $k \ge 1$, let $a_0, \ldots, a_k$ be complex numbers with $a_0 \ne 0$, let $(f_n)_{n \ge 0}$ be a sequence with a [[unilateral Z-transform|EPG6JPVJE7]] $F$, and let $c_0, \ldots, c_{k-1}$ be complex numbers.
Consider the [[linear recurrence with constant coefficients|0NDVHBVBXB]]
$$a_0 y_{n+k} + a_1 y_{n+k-1} + \cdots + a_k y_n = f_n \quad (n \ge 0), \qquad y_j = c_j \ (0 \le j < k).$$
The *Z-transform method* solves it in three steps.

1. Apply the unilateral Z-transform and the [[shift property|JWH2KYCGBQ]], $\mathcal{Z}\{(y_{n+m})_{n \ge 0}\} = z^m \left( Y(z) - \sum_{j<m} y_j z^{-j} \right)$, to get $P(z) Y(z) = F(z) + Q(z)$, where $P(z) = \sum_{m=0}^{k} a_{k-m} z^m$ and $Q$ is a polynomial built from $c_0, \ldots, c_{k-1}$.
2. Solve: $Y(z) = (F(z) + Q(z)) / P(z)$.
3. Recover $(y_n)$ from $Y$ by the [[inverse Z-transform|PH61T3B7W7]], in practice by a [[partial fraction decomposition|030VFEREKG]] and known transform pairs.

## Remarks

Example: the Fibonacci recurrence $y_{n+2} = y_{n+1} + y_n$ with $y_0 = 0$, $y_1 = 1$.
Step 1 gives $z^2 (Y - z^{-1}) = z Y + Y$, so $Y(z) = z/(z^2 - z - 1)$.
With $\varphi = (1 + \sqrt 5)/2$ and $\psi = (1 - \sqrt 5)/2$, one has $Y(z) = \frac{1}{\sqrt 5}\left( \frac{z}{z - \varphi} - \frac{z}{z - \psi} \right)$, and the pair $a^n \leftrightarrow z/(z - a)$ gives $y_n = (\varphi^n - \psi^n)/\sqrt 5$.
Non-example: the recurrence $y_{n+1} = y_n^2$ is not linear; the transform of $(y_n^2)$ is not a function of $Y(z)$ alone, so step 1 gives no algebraic equation for $Y$.
The polynomial $P$ is the characteristic polynomial of the recurrence, so the poles of $Y$ that do not come from $F$ lie among its roots.
