---
tag: SVXSFJEC8P
kind: proof
name: Proof of the orthogonal decomposition along a nonzero vector
msc: ["15A63", "51N20"]
topics: [VKVAJ94SKZ]
audience: school
proves: NA6Q7ME9G0
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0S52TNNTH9, 0XKBKGTCPC]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_projection
    locator: Definitions in terms of a and b
---

## Proof

We first show that $c$ is forced (uniqueness), then that this $c$ works (existence), and then the minimum property.

1. Since $v \neq 0$, some $v_i \neq 0$. So $v \cdot v = v_1^2 + \dots + v_n^2 > 0$.
2. Uniqueness. Assume $u = cv + q$ and $q \cdot v = 0$.
3. We take the [[dot product|0S52TNNTH9]] of both sides with $v$. By linearity, $u \cdot v = c\,(v \cdot v) + q \cdot v$.
4. With $q \cdot v = 0$, step 3 gives $u \cdot v = c\,(v \cdot v)$.
5. By step 1 we can divide by $v \cdot v$. So $c = \dfrac{u \cdot v}{v \cdot v}$.
6. Then $q = u - cv$ is determined by $c$. So at most one pair $(c, q)$ exists, and it is the pair of part 2.
7. Existence. Let $c = \dfrac{u \cdot v}{v \cdot v}$ and $q = u - cv$. Then $u = cv + q$.
8. By linearity, $q \cdot v = u \cdot v - c\,(v \cdot v) = u \cdot v - u \cdot v = 0$. So the pair satisfies part 1.
9. Minimum. Let $t$ be a real number. Then $u - tv = q + (c - t)v$, by step 7.
10. We expand: $\|q + (c - t)v\|^2 = \|q\|^2 + 2(c - t)\,(q \cdot v) + (c - t)^2 \|v\|^2$.
11. Step 10 uses $\|w\|^2 = w \cdot w$, the [[definition of the length|0XKBKGTCPC]], and the bilinearity and symmetry of the dot product.
12. With $q \cdot v = 0$, step 10 gives $\|u - tv\|^2 = \|q\|^2 + (c - t)^2 \|v\|^2 \geq \|q\|^2$.
13. Equality holds if and only if $(c - t)^2 \|v\|^2 = 0$. Since $\|v\| > 0$, this means $t = c$.
14. Lengths are nonnegative, so step 12 gives $\|u - tv\| \geq \|q\|$. This proves part 3 and the theorem.

## Idea

Dotting the equation $u = cv + q$ with $v$ kills $q$ and leaves one linear equation for $c$.
That equation has exactly one solution because $v \cdot v > 0$.
For the minimum, any other multiple $tv$ differs from $cv$ along $v$, and Pythagoras adds a positive square.

## Variants

- Calculus proof of part 3: the function $f(t) = \|u - tv\|^2 = \|u\|^2 - 2t\,(u \cdot v) + t^2\,(v \cdot v)$ is a quadratic in $t$ with positive leading coefficient. Its derivative $-2\,(u \cdot v) + 2t\,(v \cdot v)$ vanishes only at $t = c$, which gives the minimum.
- Completing the square in the same quadratic gives $f(t) = (v \cdot v)(t - c)^2 + \|u\|^2 - \frac{(u \cdot v)^2}{v \cdot v}$, without calculus.
- In the plane and in space, the geometric proof drops the perpendicular from the tip of $u$ to the line of $v$; its foot is $cv$ by right-triangle trigonometry.
