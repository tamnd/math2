---
tag: 8X1RZXWP62
kind: example
name: A continuous solution of an integral equation is smooth
msc: ["00A35", "34A12"]
topics: [MEKKHHQTKB]
audience: ug2
instance_of: [YKA0ADKYFR]
uses: [YKA0ADKYFR, 0NHGY0N0JB, 0ASJVEFA9J, 0V33BNKZ9S, 0J0FCWV32D]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus
    locator: lead section
---

## Example

Let $f \colon \mathbb{R} \to \mathbb{R}$ be continuous, and assume that
$$f(x) = 1 + \int_0^x t\, f(t)\, dt \qquad \text{for each } x \in \mathbb{R}.$$
We prove by a regularity [[bootstrap|YKA0ADKYFR]] that $f$ is [[smooth|0V33BNKZ9S]], and then we find $f$.

1. The integrand $g(t) = t f(t)$ is continuous, as a product of two continuous functions.
2. By the [[fundamental theorem of calculus|0NHGY0N0JB]], $x \mapsto \int_0^x g(t)\, dt$ is differentiable with derivative $g(x)$.
3. So $f$ is differentiable with $f'(x) = x f(x)$, and the right side is continuous, so $f \in C^1$.
   This is the first gain, from $C^0$ to $C^1$.
4. Induction step: if $f \in C^k$ with $k \ge 1$, then $x f(x)$ is in $C^k$, so $f' \in C^k$ and $f \in C^{k+1}$.
5. By [[mathematical induction|0ASJVEFA9J]] with base case step 3, $f \in C^k$ for every $k$, so $f \in C^\infty$.
6. To find $f$, let $h(x) = f(x) e^{-x^2/2}$.
   Then $h'(x) = f'(x) e^{-x^2/2} - x f(x) e^{-x^2/2} = 0$ by step 3.
7. So $h$ is constant, with $h(0) = f(0) = 1$, and $f(x) = e^{x^2/2}$.

Check: $1 + \int_0^x t\, e^{t^2/2}\, dt = 1 + \left[ e^{t^2/2} \right]_0^x = e^{x^2/2}$.

## Remarks

The equation gives back one derivative more than it receives, since an integral is one degree smoother than its integrand, and this gain drives the induction.
The bootstrap can start even lower.
If $f$ is only Riemann integrable on each bounded interval, the right side is still continuous in $x$, so $f$ is continuous and step 1 applies.

The induction step also gives formulas: $f^{(k)} = p_k f$, with polynomials $p_0 = 1$ and $p_{k+1} = p_k' + x p_k$.
A regularity bootstrap alone stops at $C^\infty$ and does not prove that $f$ is real analytic.
Here $f$ is analytic anyway, as the [[exponential|0J0FCWV32D]] of a polynomial.
The same scheme shows that solutions of $y' = F(x, y)$ with smooth $F$ are smooth: $y \in C^k$ gives $F(x, y(x)) \in C^k$, so $y \in C^{k+1}$.

## Explanations

### L1 human

The equation says that $f$ at $x$ is $1$ plus an area under a curve built from $f$.
An area under a curve changes smoothly as we move its right edge, even when the curve itself has corners.
So $f$ is smoother than we assumed.
But then the curve under the area is smoother too, so $f$ is smoother again.
Repeating this, $f$ is as smooth as we like.

### L2 human

We compute the first derivatives of $f = e^{x^2/2}$ from the formula $f^{(k)} = p_k f$ and check them.

1. $p_1 = p_0' + x p_0 = x$, so $f' = x f$, which agrees with direct differentiation.
2. $p_2 = p_1' + x p_1 = 1 + x^2$, so $f'' = (1 + x^2) f$.
3. Directly, $f'' = e^{x^2/2} + x \cdot x e^{x^2/2} = (1 + x^2) e^{x^2/2}$, which agrees.
4. $p_3 = 2x + x(1 + x^2) = 3x + x^3$, so $f'''(0) = 0$ and $f'''(1) = 4 e^{1/2}$.

A regularity bootstrap shows that a weak or continuous solution of a differential or integral equation is smooth.
Watch out: do not differentiate the equation before knowing that $f$ is differentiable.
Step 3 must come first, and it uses only the continuity of $f$.
