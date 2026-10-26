---
tag: 0GZNSHMG4Q
kind: example
name: Dirichlet integral
msc: [26A42, 40A10]
instance_of: [05KQ3F99BQ]
uses: [0VCTBJMEJF, 03GP7KMBYM, 08Y1BBQTK9]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_integral
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Improper_integral
    locator: Improper Riemann integrals and Lebesgue integrals
same_as:
  wikidata: Q778099
  wikipedia: Dirichlet integral
---

## Example

The improper integral of $\frac{\sin x}{x}$ over $(0, \infty)$ converges, and
$$\int_0^\infty \frac{\sin x}{x} \, dx = \frac{\pi}{2}.$$
The integrand extends continuously to $x = 0$ with value $1$. So only the upper limit is improper.
[[Integration by parts|08Y1BBQTK9]] gives $\int_1^b \frac{\sin x}{x} \, dx = \cos 1 - \frac{\cos b}{b} - \int_1^b \frac{\cos x}{x^2} \, dx$. The last integral converges absolutely, so the limit exists.

## Remarks

The integral does not converge [[absolutely|03GP7KMBYM]]: $\int_0^\infty \frac{|\sin x|}{x} \, dx = \infty$.
So $\frac{\sin x}{x}$ is not Lebesgue integrable on $(0, \infty)$.
The value $\pi/2$ needs other methods, such as differentiation under the integral sign or contour integration.

## Explanations

### L1 human

The area under $\frac{\sin x}{x}$ alternates in sign, and the pieces shrink.
The positive and negative pieces cancel to give the value $\pi/2$.
