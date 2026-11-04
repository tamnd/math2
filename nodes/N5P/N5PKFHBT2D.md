---
tag: N5PKFHBT2D
kind: proof
name: Proof that a function with positive derivative is strictly increasing
msc: [26A24]
proves: 07J5X2T1ZX
uses: [0BARQY52N5, 0TR9SR9FTB, 0TK8Y3J5RW]
sources:
  - url: https://proofwiki.org/wiki/Real_Function_with_Strictly_Positive_Derivative_is_Strictly_Increasing
---

## Proof

We apply the mean value theorem on each subinterval.

1. Let $x, y \in I$ with $x < y$. We must show $f(x) < f(y)$.
2. Since $I$ is an [[interval|0TK8Y3J5RW]], every $z$ with $x \le z \le y$ lies in $I$. So $[x, y] \subseteq I$.
3. Each $z \in (x, y)$ is an interior point of $I$, because the open interval $(x, y)$ contains $z$ and lies in $I$.
4. So $f$ is differentiable at each point of $(x, y)$, with $f'(z) > 0$ there.
5. The function $f$ is continuous on $I$, so it is continuous on $[x, y]$.
6. By the [[mean value theorem|0BARQY52N5]], there is $c \in (x, y)$ with $f(y) - f(x) = f'(c)(y - x)$.
7. Here $f'(c) > 0$ by step 4, and $y - x > 0$. So $f(y) - f(x) > 0$.
8. Thus $f(x) < f(y)$ whenever $x < y$ in $I$, so $f$ is [[strictly increasing|0TR9SR9FTB]] on $I$.

## Idea

The mean value theorem turns the sign of the derivative into the sign of a difference of values. A positive slope at one point between $x$ and $y$ forces $f(y) > f(x)$. Continuity is needed only so that the theorem also applies when $x$ or $y$ is an endpoint of $I$.
