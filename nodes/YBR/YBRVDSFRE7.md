---
tag: YBRVDSFRE7
kind: proof
name: Proof of the mean value theorem from Rolle's theorem
msc: [26A24]
proves: 0BARQY52N5
uses: [0194DY35BG, 0P27W9RW0G, 0F1WR9C83K, 0Z9JB71BS0]
sources:
  - url: https://en.wikipedia.org/wiki/Mean_value_theorem
---

## Proof

We subtract a linear function from $f$ so that Rolle's theorem applies.

1. Let $r = \dfrac{f(b) - f(a)}{b - a}$. This is a real number because $b - a > 0$.
2. Define $g \colon [a, b] \to \R$ by $g(x) = f(x) - r (x - a)$.
3. The function $x \mapsto r(x - a)$ is [[continuous|0P27W9RW0G]] on $[a, b]$, and it has [[derivative|0F1WR9C83K]] $r$ at every point.
4. So $g$ is continuous on $[a, b]$, as a difference of continuous functions.
5. By the sum and [[constant multiple rule|0Z9JB71BS0]], $g$ is differentiable on $(a, b)$ with $g'(x) = f'(x) - r$.
6. We have $g(a) = f(a)$ and $g(b) = f(b) - (f(b) - f(a)) = f(a)$. So $g(a) = g(b)$.
7. By [[Rolle's theorem|0194DY35BG]], there is $c \in (a, b)$ with $g'(c) = 0$.
8. By step 5, $f'(c) - r = 0$. Hence $f'(c) = \dfrac{f(b) - f(a)}{b - a}$.

## Idea

The line through $(a, f(a))$ and $(b, f(b))$ has slope $r$. Subtracting it from $f$ gives a function with equal values at the endpoints. Rolle's theorem gives a point where its derivative vanishes, and there $f'$ equals $r$.
