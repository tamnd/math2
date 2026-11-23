---
tag: 3C8ZS1TPAC
kind: example
name: The integral of x times ln x squared by a parameter
msc: ["00A35", "26A42"]
topics: [X1NSTVGDNQ]
audience: ug1
instance_of: [8NJ0VN9Z97]
uses: [8NJ0VN9Z97, 0AR06W1E1B]
sources:
  - url: https://en.wikipedia.org/wiki/Leibniz_integral_rule
    locator: lead section
---

## Example

We compute
$$I = \int_0^1 x (\ln x)^2 \, dx$$
by [[generalization|8NJ0VN9Z97]]: the exponent $1$ of $x$ becomes a parameter $t$.

1. We notice where the logarithm comes from.
   For $x > 0$, $\frac{\partial}{\partial t} x^t = x^t \ln x$, so each factor $\ln x$ is the trace of one derivative in the exponent.
2. We generalize.
   For $t \in \left[\frac{1}{2}, 2\right]$ let $F(t) = \int_0^1 x^t \, dx$, which exists since $t > -1$, and $F(t) = \frac{1}{t + 1}$.
3. We set up the conditions for [[differentiation under the integral sign|0AR06W1E1B]].
   Let $f(x, t) = x^t$, with $\partial_t f = x^t \ln x$ and $\partial_t^2 f = x^t (\ln x)^2$ for $0 < x \le 1$, and give all three the value $0$ at $x = 0$.
4. We check continuity.
   For $t \ge \frac{1}{2}$ and $0 < x \le 1$, the three functions are at most $x^{1/2}$, $x^{1/2} |\ln x|$ and $x^{1/2} (\ln x)^2$ in size, and these bounds tend to $0$ as $x \to 0^{+}$.
   So the three functions are continuous on $[0, 1] \times \left[\frac{1}{2}, 2\right]$, and the theorem applies twice.
5. We differentiate twice under the integral sign:
   $$F''(t) = \int_0^1 x^t (\ln x)^2 \, dx.$$
6. We differentiate the closed form: $F'(t) = -\frac{1}{(t + 1)^2}$ and $F''(t) = \frac{2}{(t + 1)^3}$.
7. We specialize to $t = 1$:
   $$I = F''(1) = \frac{2}{8} = \frac{1}{4}.$$

Check by integration by parts, with $u = (\ln x)^2$ and $dv = x \, dx$:
$$I = \left[\frac{x^2}{2} (\ln x)^2\right]_0^1 - \int_0^1 x \ln x \, dx = 0 - \left(-\frac{1}{4}\right) = \frac{1}{4},$$
where $\int_0^1 x \ln x \, dx = -\frac{1}{4}$ comes from a second integration by parts.

## Remarks

The given integral has no parameter, so the derivative of step 5 was not available until we made one.
The family $F(t)$ is easier than the given integral, because its value is a simple function of $t$.
The same family gives, by $m$ differentiations,
$$\int_0^1 x^t (\ln x)^m \, dx = \frac{(-1)^m \, m!}{(t + 1)^{m+1}}, \qquad t > -1.$$

Step 4 is the step that a quick use of the trick skips.
We chose exponents in $\left[\frac{1}{2}, 2\right]$ so that the functions stay continuous at $x = 0$, and any closed interval of positive exponents that contains $1$ would also do.

## Explanations

### L1 human

The integral is hard because of the factor $(\ln x)^2$.
The trick is to look at the easier integral of $x^t$, which is $\frac{1}{t + 1}$ for every $t$ above $-1$.
Changing $t$ a little changes $x^t$ by an amount with $\ln x$ in it.
So taking the rate of change in $t$ twice puts $(\ln x)^2$ into the integral, and on the easy side it turns $\frac{1}{t + 1}$ into $\frac{2}{(t + 1)^3}$.
At $t = 1$ this is $\frac{1}{4}$.

### L2 human

We use the same family for $J = \int_0^1 x^2 \ln x \, dx$.
One factor $\ln x$ needs one derivative, so $J = F'(2)$, and
$$J = -\frac{1}{(2 + 1)^2} = -\frac{1}{9}.$$
Check by parts:
$$J = \left[\frac{x^3}{3} \ln x\right]_0^1 - \int_0^1 \frac{x^2}{3} \, dx = 0 - \frac{1}{9} = -\frac{1}{9}.$$

This is the typical use: a factor $\ln x$ in the integrand points to a derivative with respect to an exponent.
Watch out for the range of the parameter.
For $t \le -1$ the integral $F(t)$ diverges, so the family cannot be used there, and the formula $\frac{1}{t + 1}$ is not the value of any integral.
