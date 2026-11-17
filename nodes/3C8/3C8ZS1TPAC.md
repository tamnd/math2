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

Problem: compute $I = \int_0^1 x (\ln x)^2 \, dx$.
We use [[generalization|8NJ0VN9Z97]]: the exponent $1$ of $x$ becomes a parameter $t$.

1. Notice that $\frac{\partial}{\partial t} x^t = x^t \ln x$ for $x > 0$. So each factor $\ln x$ comes from one derivative in the exponent.
2. Generalize. For $t \in \left[\frac{1}{2}, 2\right]$ let $F(t) = \int_0^1 x^t \, dx$. Since $t > -1$, the integral exists and $F(t) = \frac{1}{t + 1}$.
3. Check the conditions for [[differentiation under the integral sign|0AR06W1E1B]]. Put $f(x, t) = x^t$ and its derivatives $\partial_t f = x^t \ln x$ and $\partial_t^2 f = x^t (\ln x)^2$ for $0 < x \le 1$, and put all three equal to $0$ at $x = 0$.
4. For $t \ge \frac{1}{2}$, each of the three functions tends to $0$ as $x \to 0^{+}$, because $x^{1/2} (\ln x)^2 \to 0$. So they are continuous on $[0, 1] \times \left[\frac{1}{2}, 2\right]$, and the theorem applies twice.
5. Differentiate twice under the integral sign: $F''(t) = \int_0^1 x^t (\ln x)^2 \, dx$.
6. Differentiate the closed form: $F'(t) = -\frac{1}{(t + 1)^2}$ and $F''(t) = \frac{2}{(t + 1)^3}$.
7. Specialize to $t = 1$: $I = F''(1) = \frac{2}{8} = \frac{1}{4}$.

Check by integration by parts.
With $u = (\ln x)^2$ and $dv = x \, dx$, we get $I = \left[\frac{x^2}{2} (\ln x)^2\right]_0^1 - \int_0^1 x \ln x \, dx = 0 - \left(-\frac{1}{4}\right) = \frac{1}{4}$, since $\int_0^1 x \ln x \, dx = -\frac{1}{4}$ by a second integration by parts.

## Remarks

The given integral has no parameter, so the derivative of step 5 was not available.
The general integral $F(t)$ is easier than the given one, because its value is a simple function of $t$.
The same family gives every integral $\int_0^1 x^t (\ln x)^m \, dx = \frac{(-1)^m m!}{(t + 1)^{m+1}}$ for $t > -1$, by $m$ differentiations.

Step 4 is the step that a quick use of the trick skips.
The interval $\left[\frac{1}{2}, 2\right]$ is chosen so that the functions stay continuous at $x = 0$; any closed interval of exponents above $0$ that contains $1$ would also do.

## Explanations

### L1 human

The integral is hard because of the $(\ln x)^2$.
The trick is to look at the easier integral of $x^t$, which is $\frac{1}{t + 1}$ for every $t$ above $-1$.
Changing $t$ a little changes $x^t$ by a factor with $\ln x$ in it.
So taking the rate of change twice in $t$ puts $(\ln x)^2$ into the integral, and on the easy side it turns $\frac{1}{t + 1}$ into $\frac{2}{(t + 1)^3}$.
At $t = 1$ this is $\frac{1}{4}$.

### L2 human

We use the same family once more, for $J = \int_0^1 x^2 \ln x \, dx$.

1. One factor $\ln x$ needs one derivative: $J = F'(2)$, where $F(t) = \frac{1}{t + 1}$.
2. $F'(t) = -\frac{1}{(t + 1)^2}$, so $J = -\frac{1}{9}$.
3. Check by parts: $J = \left[\frac{x^3}{3} \ln x\right]_0^1 - \int_0^1 \frac{x^2}{3} \, dx = 0 - \frac{1}{9} = -\frac{1}{9}$.

The typical use: a factor $\ln x$ in the integrand is the trace of a derivative with respect to an exponent.

A trap: for exponents $t \le -1$ the integral $F(t)$ diverges, so the family cannot be used there, and the formula $\frac{1}{t + 1}$ has no meaning as the value of an integral.
