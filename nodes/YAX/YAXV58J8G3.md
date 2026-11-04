---
tag: YAXV58J8G3
kind: proof
name: Proof of the mean value theorem in several variables
msc: [26B05]
proves: 03HGK7EW6R
uses: [0135XZZQ8M, 0NS2QYVC4Y, 0A8TJ0VHC7, 0BARQY52N5, 0C13E623WD, 0F3K4C7XYW, 05NK26G0DR, 0FJZMBX0ZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Mean_value_theorem
    locator: Mean value theorem in several variables
---

## Proof

We restrict $f$ to the segment from $x$ to $y$ and apply the one-variable mean value theorem.

1. Let $U$, $f$, $x$ and $y$ be as in the statement. Define $\gamma(t) = x + t (y - x)$ for $t \in [0, 1]$. By hypothesis, $\gamma(t) \in U$ for each $t \in [0, 1]$.
2. Let $z \in U$. By [[linear maps on finite-dimensional spaces are continuous|0C13E623WD]] and [[bounded linear maps are continuous|0F3K4C7XYW]], there is $C \ge 0$ with $|Df(z) h| \le C \|h\|$ for each $h$.
3. Since $f$ is [[differentiable|0135XZZQ8M]] at $z$, there is $\delta > 0$ with $|f(z + h) - f(z) - Df(z) h| \le \|h\|$ for $\|h\| < \delta$ and $z + h \in U$. By the [[triangle inequality|0FJZMBX0ZZ]], $|f(z + h) - f(z)| \le (C + 1) \|h\|$ for these $h$. So $f$ is continuous at $z$.
4. Put $g(t) = f(\gamma(t))$ for $t \in [0, 1]$. Since $\|\gamma(t) - \gamma(t')\| = |t - t'| \, \|y - x\|$, the map $\gamma$ is continuous. By step 3, $g$ is a [[composition of continuous maps|05NK26G0DR]]. So $g$ is continuous on $[0, 1]$.
5. For $t \in (0, 1)$ and small $s \ne 0$, $(\gamma(t + s) - \gamma(t)) / s = y - x$. So $\gamma$ is differentiable on $(0, 1)$ with $\gamma'(t) = y - x$.
6. By the [[chain rule for a composition with a curve|0A8TJ0VHC7]] on the open interval $(0, 1)$, $g$ is differentiable at each $t \in (0, 1)$, with $g'(t) = Df(\gamma(t))(y - x)$.
7. By the definition of the [[gradient|0NS2QYVC4Y]], $g'(t) = \nabla f(\gamma(t)) \cdot (y - x)$ for $t \in (0, 1)$.
8. By the [[mean value theorem|0BARQY52N5]] for $g$ on $[0, 1]$, there is $c \in (0, 1)$ with $g(1) - g(0) = g'(c)$.
9. Since $g(1) = f(y)$ and $g(0) = f(x)$, steps 7 and 8 give $f(y) - f(x) = \nabla f\big(x + c (y - x)\big) \cdot (y - x)$.

## Idea

Along the straight segment from $x$ to $y$, the function $f$ becomes a function $g$ of one variable $t$. The one-variable mean value theorem gives a point where the slope of $g$ is its average slope. The chain rule identifies that slope with the gradient dotted with the direction $y - x$.
