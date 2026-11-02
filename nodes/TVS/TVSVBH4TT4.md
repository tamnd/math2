---
tag: TVSVBH4TT4
kind: statement
role: theorem
name: Boole's rule
msc: [65D32, 41A55]
uses: [BQPQAY1FDJ, ZYT1JNT1Y0, WMTZG71K2Y]
about: [BQPQAY1FDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Boole%27s_rule
same_as:
  wikidata: Q4943343
  wikipedia: Boole's rule
---

## Statement

Let $h > 0$, let $x_k = x_0 + kh$ for $k = 0, \ldots, 4$, and let $f \in C^6[x_0, x_4]$ with $f_k = f(x_k)$.
Then there is $\xi \in (x_0, x_4)$ with
$$\int_{x_0}^{x_4} f(x) \, dx = \frac{2h}{45} \big( 7 f_0 + 32 f_1 + 12 f_2 + 32 f_3 + 7 f_4 \big) - \frac{8 h^7}{945} f^{(6)}(\xi).$$

## Remarks

The rule is the closed [[Newton–Cotes formula|BQPQAY1FDJ]] with five nodes: its weights are the integrals of the Lagrange basis polynomials of the five equally spaced nodes.
By symmetry it is exact for all polynomials of degree at most $5$, one more than the interpolation degree, so its [[degree of exactness|ZYT1JNT1Y0]] is $5$.
The error constant can be read off from $f(x) = x^6$ on $[0, 4]$ with $h = 1$: the integral is $\frac{4^7}{7}$, the rule gives $\frac{4^7}{7} + \frac{128}{21}$, and $\frac{8}{945} \cdot 720 = \frac{128}{21}$.
Check of the weights: $\frac{2h}{45}(7 + 32 + 12 + 32 + 7) = 4h$, the length of the interval.
The composite rule on $4m$ subintervals has error $O(h^6)$ for $f \in C^6$.

## Explanations

### L1 human

Boole's rule estimates an integral from five equally spaced samples.
It fits a polynomial of degree four through the samples and integrates that polynomial instead.
The weights $7, 32, 12, 32, 7$ come out of this fit, and the rule is exact for all polynomials up to degree five.

### L2 human

Boole's rule is the next member after the trapezoidal rule, Simpson's rule and Simpson's $3/8$ rule in the closed Newton–Cotes family.
It equals one step of [[Richardson extrapolation|WMTZG71K2Y]] applied to Simpson's rule with steps $2h$ and $h$, as in the Romberg method.
Higher Newton–Cotes rules eventually have negative weights and become unstable, so in practice one uses composite rules of low order or Gaussian rules instead.
