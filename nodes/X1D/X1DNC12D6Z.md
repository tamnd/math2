---
tag: X1DNC12D6Z
kind: example
name: A palindromic quartic equation solved by symmetry
msc: ["00A35", "12D10"]
topics: [MEKKHHQTKB]
audience: school
instance_of: [H840D9TM2X]
uses: [H840D9TM2X, 019MA1VTR2, 0VHSHB9B6J]
sources:
  - url: https://en.wikipedia.org/wiki/Reciprocal_polynomial
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Symmetry_in_mathematics
    locator: lead section
---

## Example

We solve
$$x^4 + x^3 - 4x^2 + x + 1 = 0$$
over the real numbers by a [[symmetry argument|H840D9TM2X]].
The coefficients $1, 1, -4, 1, 1$ read the same forward and backward, so the polynomial is palindromic.

1. At $x = 0$ the left side is $1$, so every solution is nonzero.
2. For $x \neq 0$, replacing $x$ by $1/x$ and multiplying by $x^4$ gives $1 + x - 4x^2 + x^3 + x^4$, the same polynomial.
   So $x$ is a solution exactly when $1/x$ is, and $x \mapsto 1/x$ is a symmetry of the equation on $\mathbb{R} \setminus \{0\}$.
3. The quantity $t = x + \frac{1}{x}$ does not change under this symmetry, so we rewrite the equation in $t$.
4. Divide by $x^2$, which is allowed since $x \neq 0$, and group the pairs:
   $$\left(x^2 + \frac{1}{x^2}\right) + \left(x + \frac{1}{x}\right) - 4 = 0.$$
5. Since $t^2 = x^2 + 2 + \frac{1}{x^2}$, the equation becomes $(t^2 - 2) + t - 4 = 0$, that is, $(t - 2)(t + 3) = 0$.
6. For $t = 2$: $x^2 - 2x + 1 = 0$, so $x = 1$.
7. For $t = -3$: $x^2 + 3x + 1 = 0$, so $x = \frac{-3 \pm \sqrt 5}{2}$.
8. Every step from step 4 on is reversible for $x \neq 0$, so the solutions are $1$ and $\frac{-3 \pm \sqrt 5}{2}$.

Check by expansion:
$$(x^2 - 2x + 1)(x^2 + 3x + 1) = x^4 + 3x^3 + x^2 - 2x^3 - 6x^2 - 2x + x^2 + 3x + 1 = x^4 + x^3 - 4x^2 + x + 1.$$
So the [[roots|019MA1VTR2]] are $1$, twice, and the two roots of $x^2 + 3x + 1$.

## Remarks

The symmetry halves the degree: a palindromic quartic in $x$ becomes a quadratic in $t$.
The roots come in pairs $\{x, 1/x\}$, as the symmetry predicts.
The two roots of step 7 form such a pair, since their product is the constant term $1$, and the root $1$ is its own partner.
The variable $t$ is the elementary [[symmetric polynomial|0VHSHB9B6J]] $e_1$ of the pair $x$ and $1/x$, whose product $e_2$ is always $1$.

A palindromic polynomial of odd degree has the root $-1$, and dividing by $x + 1$ leaves a palindromic polynomial of even degree, so the method still applies.
Change one coefficient and the symmetry is gone.
For $x^4 + 2x^3 - 4x^2 + x + 1$, the map $x \mapsto 1/x$ gives $x^4 + x^3 - 4x^2 + 2x + 1$, a different polynomial, and the step to $t$ no longer works.

## Explanations

### L1 human

The equation has a mirror property: its coefficients read the same from left to right and from right to left.
Because of this, if a number solves it, then one divided by that number also solves it.
So the solutions come in pairs, like $2$ and $\tfrac12$.
You can look for the sum of a pair instead of the numbers themselves, and the sum solves a simpler equation.

### L2 human

We apply the same steps to $2x^4 - 5x^3 + 6x^2 - 5x + 2 = 0$.

1. The coefficients $2, -5, 6, -5, 2$ are palindromic, and $x = 0$ is not a solution.
2. Divide by $x^2$: $2\left(x^2 + \frac{1}{x^2}\right) - 5\left(x + \frac{1}{x}\right) + 6 = 0$.
3. With $t = x + \frac1x$, this is $2(t^2 - 2) - 5t + 6 = 2t^2 - 5t + 2 = 0$, so $t = 2$ or $t = \tfrac12$.
4. For $t = 2$, $x = 1$, a double root.
5. For $t = \tfrac12$, $x^2 - \tfrac12 x + 1 = 0$ has discriminant $\tfrac14 - 4 < 0$, so it has no real solution.
6. So the only real solution is $x = 1$.

The method fits any polynomial or system whose form does not change under an exchange or an inversion of the unknowns.
Watch out: check that $x = 0$ is not a solution before you divide by $x^2$.
