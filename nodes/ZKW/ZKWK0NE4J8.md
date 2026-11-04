---
tag: ZKWK0NE4J8
kind: proof
name: Proof of the mean value inequality
msc: [26B05]
proves: 02CYB184RC
uses: [0135XZZQ8M, 0XPR1E85W0, 0BARQY52N5, 0A8TJ0VHC7, 0RFWW56Y22, 0ZTEH055YF, 0C13E623WD, 0F3K4C7XYW, 05NK26G0DR, 0FJZMBX0ZZ]
sources:
  - url: https://www.jirka.org/ra/realanal2.pdf
    locator: Lemma 8.4.1 and Proposition 8.4.2
  - url: https://en.wikipedia.org/wiki/Mean_value_theorem
    locator: Mean value theorem for vector-valued functions
---

## Proof

We apply the one-variable mean value theorem to the real function $\varphi(t) = w \cdot f(x + t (y - x))$, where $w = f(y) - f(x)$.

1. Let $U$, $f$, $x$, $y$ and $M$ be as in the statement. Put $w = f(y) - f(x)$. If $w = 0$, the inequality holds, since its right side is $\ge 0$. From now on, suppose that $w \ne 0$.
2. Let $z \in U$ and $L = Df(z)$. By [[linear maps on finite-dimensional spaces are continuous|0C13E623WD]] and [[bounded linear maps are continuous|0F3K4C7XYW]], there is $C \ge 0$ with $\|L h\| \le C \|h\|$ for each $h$.
3. Since $f$ is [[differentiable|0135XZZQ8M]] at $z$, there is $\delta > 0$ with $\|f(z + h) - f(z) - L h\| \le \|h\|$ for $\|h\| < \delta$ and $z + h \in U$. By the [[triangle inequality|0FJZMBX0ZZ]], $\|f(z + h) - f(z)\| \le (C + 1) \|h\|$ for these $h$. So $f$ is continuous at $z$.
4. Define $\gamma(t) = x + t (y - x)$ for $t \in [0, 1]$. By hypothesis $\gamma(t) \in U$. Also $\|\gamma(t) - \gamma(t')\| = |t - t'| \, \|y - x\|$, so $\gamma$ is continuous.
5. Put $\varphi(t) = w \cdot f(\gamma(t))$ for $t \in [0, 1]$, with the dot product of [[Euclidean space|0XPR1E85W0]]. By the [[Cauchy–Schwarz inequality|0RFWW56Y22]], $|w \cdot v - w \cdot v'| \le \|w\| \, \|v - v'\|$, so $v \mapsto w \cdot v$ is continuous.
6. By steps 3, 4 and 5, $\varphi$ is a [[composition of continuous maps|05NK26G0DR]]. So $\varphi$ is continuous on $[0, 1]$.
7. For $t \in (0, 1)$ and small $s \ne 0$, $(\gamma(t + s) - \gamma(t)) / s = y - x$. So $\gamma$ is differentiable on $(0, 1)$ with $\gamma'(t) = y - x$.
8. By the [[chain rule for a composition with a curve|0A8TJ0VHC7]] on the open interval $(0, 1)$, $f \circ \gamma$ is differentiable at each $t \in (0, 1)$. Its derivative is $(f \circ \gamma)'(t) = Df(\gamma(t))(y - x)$.
9. For $t \in (0, 1)$ and small $s \ne 0$, $(\varphi(t + s) - \varphi(t)) / s = w \cdot q(s)$, where $q(s) = ((f \circ \gamma)(t + s) - (f \circ \gamma)(t)) / s$. By steps 5 and 8, this tends to $w \cdot Df(\gamma(t))(y - x)$.
10. So $\varphi$ is differentiable on $(0, 1)$ with $\varphi'(t) = w \cdot Df(\gamma(t))(y - x)$.
11. By the [[mean value theorem|0BARQY52N5]], there is $c \in (0, 1)$ with $\varphi(1) - \varphi(0) = \varphi'(c)$.
12. The left side is $w \cdot f(y) - w \cdot f(x) = w \cdot w = \|w\|^2$. By step 10 and the Cauchy–Schwarz inequality, $\|w\|^2 \le \|w\| \, \|Df(\gamma(c))(y - x)\|$.
13. Let $T = Df(\gamma(c))$ and $v = y - x$. If $v \ne 0$, then $v / \|v\|$ has norm $1$. By the definition of the [[operator norm|0ZTEH055YF]], $\|T v\| = \|v\| \, \|T(v / \|v\|)\| \le \|T\| \, \|v\|$. If $v = 0$, both sides are $0$.
14. The point $\gamma(c)$ lies on the segment $[x, y]$, so $\|T\| \le M$ by hypothesis. Steps 12 and 13 give $\|w\|^2 \le \|w\| \, M \, \|y - x\|$.
15. Dividing by $\|w\| > 0$ gives $\|f(y) - f(x)\| \le M \, \|y - x\|$.

## Idea

The mean value theorem has no equality form for vector-valued maps, but it does apply to one real component. The trick is to take the component along the direction $w = f(y) - f(x)$ of the total change. The change of that component is $\|w\|^2$, and Cauchy–Schwarz bounds its derivative by $\|w\|$ times $M \|y - x\|$.
