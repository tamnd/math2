---
tag: NDVJ9VWA71
kind: example
name: Wilkinson's polynomial
msc: [65H04, 65G50, 12D10]
illustrates: [AB3S6MHJ8X]
uses: [019MA1VTR2, 1G0B73WPX8, AB3S6MHJ8X]
sources:
  - url: https://en.wikipedia.org/wiki/Wilkinson%27s_polynomial
same_as:
  wikidata: Q2613931
  wikipedia: Wilkinson's polynomial
---

## Example

*Wilkinson's polynomial* is the [[polynomial|1G0B73WPX8]]
$$w(x) = \prod_{i=1}^{20} (x - i) = (x - 1)(x - 2) \cdots (x - 20) = x^{20} - 210 x^{19} + \cdots + 20!.$$
Its [[roots|019MA1VTR2]] $1, 2, \ldots, 20$ are simple and well separated, yet they are extremely sensitive to the coefficients.
James H. Wilkinson changed the coefficient $-210$ of $x^{19}$ to $-210 - 2^{-23}$, a relative change of about $6 \times 10^{-10}$.
The perturbed polynomial has only $10$ real roots, and the roots near $10, \ldots, 19$ turn into five complex conjugate pairs.
For example, the roots $16$ and $17$ become approximately $16.73 \pm 2.81\,i$.
Check of the sensitivity: if $a$ is the coefficient of $x^{19}$ and $r$ a simple root, differentiating $w(r) = 0$ with respect to $a$ gives
$$\frac{\partial r}{\partial a} = -\frac{r^{19}}{w'(r)}.$$
For $r = 20$, $w'(20) = 19!$, so $\abs{\partial r/\partial a} = 20^{19}/19! \approx 4.3 \times 10^{7}$: the root-finding problem has a huge [[condition number|AB3S6MHJ8X]] with respect to this coefficient.

## Remarks

The difficulty lies in the problem, not in the algorithm: any method that works with the coefficients in floating-point arithmetic, where they are rounded, inherits this sensitivity.
The same roots are perfectly well conditioned as functions of the factors $(x - i)$, which shows that the choice of representation of a polynomial matters.

## Explanations

### L1 human

The polynomial with roots $1, 2, \ldots, 20$ looks harmless, since its roots are evenly spaced whole numbers.
But if one changes one coefficient by about one part in a billion, several roots move far away and even become complex numbers.
This shows that finding roots from the coefficients of a polynomial can be a badly conditioned problem.
