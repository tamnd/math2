---
tag: EMKG76V8PS
kind: proof
name: Proof that a differentiable function is convex iff its derivative is increasing
msc: [26A51]
proves: 005JT76HCK
uses: [0VV0HSW1ZS, 0BY5FTHEEE, 0BARQY52N5, 0F1WR9C83K, 07ZMX4ANJS, 0TK8Y3J5RW]
sources:
  - url: https://proofwiki.org/wiki/Real_Function_is_Convex_iff_Derivative_is_Increasing
---

## Proof

We prove the two directions separately. For $u \ne v$ in $I$ write $s(u, v) = \dfrac{f(v) - f(u)}{v - u}$, the slope of the chord. Note that $s(u, v) = s(v, u)$.

*Convex implies $f'$ increasing.*

1. Assume $f$ is [[convex|0VV0HSW1ZS]]. Let $x < y$ in $I$; we show $f'(x) \le f'(y)$.
2. For each $t$ with $x < t < y$, the [[slope inequalities|0BY5FTHEEE]] give $s(x, t) \le s(x, y) \le s(t, y)$.
3. By the definition of the [[derivative|0F1WR9C83K]], $s(x, t) = \dfrac{f(x + h) - f(x)}{h}$ with $h = t - x$. So $s(x, t) \to f'(x)$ as $t \to x^+$.
4. Suppose $f'(x) > s(x, y)$. Put $\varepsilon = f'(x) - s(x, y)$. By step 3 there is $t \in (x, y)$ with $s(x, t) > f'(x) - \varepsilon = s(x, y)$.
5. This contradicts step 2. So $f'(x) \le s(x, y)$.
6. Likewise $s(t, y) = \dfrac{f(y + h) - f(y)}{h}$ with $h = t - y < 0$. So $s(t, y) \to f'(y)$ as $t \to y^-$.
7. Suppose $f'(y) < s(x, y)$. With $\varepsilon = s(x, y) - f'(y)$, step 6 gives $t \in (x, y)$ with $s(t, y) < s(x, y)$. This contradicts step 2.
8. So $f'(x) \le s(x, y) \le f'(y)$. Hence $f'$ is increasing on $I$.

*$f'$ increasing implies convex.*

9. Assume $f'$ is increasing on $I$. Let $u, v \in I$ and $\lambda \in [0, 1]$. We show $f(\lambda u + (1 - \lambda) v) \le \lambda f(u) + (1 - \lambda) f(v)$.
10. If $u = v$, or $\lambda \in \set{0, 1}$, both sides are equal. Exchanging $u$ with $v$ and $\lambda$ with $1 - \lambda$ leaves the claim unchanged. So we may assume $u < v$ and $0 < \lambda < 1$.
11. Let $p = \lambda u + (1 - \lambda) v$. Then $p - u = (1 - \lambda)(v - u) > 0$ and $v - p = \lambda (v - u) > 0$. So $u < p < v$.
12. Since $I$ is an [[interval|0TK8Y3J5RW]], $[u, v] \subseteq I$. The function $f$ is differentiable on $I$, hence [[continuous|07ZMX4ANJS]] on $I$.
13. By the [[mean value theorem|0BARQY52N5]] on $[u, p]$ and on $[p, v]$, there are $c_1 \in (u, p)$ and $c_2 \in (p, v)$ with $s(u, p) = f'(c_1)$ and $s(p, v) = f'(c_2)$.
14. Since $c_1 < c_2$ and $f'$ is increasing, $s(u, p) \le s(p, v)$.
15. By step 11 this reads $\dfrac{f(p) - f(u)}{(1 - \lambda)(v - u)} \le \dfrac{f(v) - f(p)}{\lambda (v - u)}$.
16. Multiplying by $\lambda (1 - \lambda)(v - u) > 0$ gives $\lambda (f(p) - f(u)) \le (1 - \lambda)(f(v) - f(p))$.
17. Rearranging, $f(p) \le \lambda f(u) + (1 - \lambda) f(v)$. So $f$ is convex.

## Idea

For a convex function, the slope of a chord over $[x, y]$ lies between the tangent slopes at $x$ and at $y$, since chord slopes increase. Conversely, the mean value theorem turns chord slopes into values of $f'$. If $f'$ is increasing, chords to the left of a point are less steep than chords to the right, and that is convexity.
