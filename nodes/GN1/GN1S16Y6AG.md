---
tag: GN1S16Y6AG
kind: proof
name: Proof of the Cauchy mean value theorem from Rolle's theorem
msc: [26A24]
proves: 02SYZAWM2K
uses: [0194DY35BG, 0P27W9RW0G, 0Z9JB71BS0]
sources:
  - url: https://en.wikipedia.org/wiki/Mean_value_theorem
    locator: Cauchy's mean value theorem
---

## Proof

We apply Rolle's theorem to a suitable linear combination of $f$ and $g$.

1. Let $A = f(b) - f(a)$ and $B = g(b) - g(a)$. These are real constants.
2. Define $h \colon [a, b] \to \R$ by $h(x) = A \, g(x) - B \, f(x)$.
3. A linear combination of [[continuous|0P27W9RW0G]] functions is continuous, so $h$ is continuous on $[a, b]$.
4. By the sum and [[constant multiple rule|0Z9JB71BS0]], $h$ is differentiable on $(a, b)$ with $h'(x) = A \, g'(x) - B \, f'(x)$.
5. Expanding, $h(a) = f(b) g(a) - f(a) g(a) - g(b) f(a) + g(a) f(a) = f(b) g(a) - f(a) g(b)$.
6. Expanding, $h(b) = f(b) g(b) - f(a) g(b) - g(b) f(b) + g(a) f(b) = f(b) g(a) - f(a) g(b)$.
7. So $h(a) = h(b)$. By [[Rolle's theorem|0194DY35BG]], there is $c \in (a, b)$ with $h'(c) = 0$.
8. By step 4, $A \, g'(c) = B \, f'(c)$. That is, $(f(b) - f(a)) \, g'(c) = (g(b) - g(a)) \, f'(c)$.

## Idea

The coefficients of $h$ make the endpoint values of $f$ and $g$ cancel, so $h(a) = h(b)$. Rolle's theorem then gives a point where $h' = 0$. At that point the claimed relation between $f'$ and $g'$ holds.
