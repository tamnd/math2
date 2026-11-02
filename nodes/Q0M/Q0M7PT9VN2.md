---
tag: Q0M7PT9VN2
kind: statement
role: theorem
name: Error bound for the trapezoidal rule
msc: [65D32, 41A55, 65D30]
uses: [FH0538XCZR, 0Y9D2FJRQ4, HASA2XSG66, 0N91N98EG5]
about: [FH0538XCZR]
sources:
  - url: https://en.wikipedia.org/wiki/Trapezoidal_rule
---

## Statement

Let $a < b$, let $f \colon [a, b] \to \R$ be twice continuously differentiable, let $N \ge 1$, $h = (b - a)/N$, and let $T_N(f)$ be the composite [[trapezoidal rule|FH0538XCZR]] with $N$ subintervals.
Then there is $\xi \in [a, b]$ with
$$\int_a^b f(x)\, dx - T_N(f) = -\frac{(b - a)\, h^2}{12}\, f''(\xi).$$
In particular,
$$\left| \int_a^b f(x)\, dx - T_N(f) \right| \le \frac{(b - a)\, h^2}{12} \max_{a \le x \le b} \abs{f''(x)}.$$

## Remarks

On one subinterval $[x_{i-1}, x_i]$, the [[interpolation error formula|HASA2XSG66]] gives $f(x) - L(x) = \tfrac{1}{2} f''(\eta_x)(x - x_{i-1})(x - x_i)$ for the linear interpolant $L$.
Since $(x - x_{i-1})(x - x_i) \le 0$ there, the [[mean value theorem for integrals|0N91N98EG5]] gives the local error $-\tfrac{h^3}{12} f''(\xi_i)$.
Summing over the $N$ subintervals and using the intermediate value theorem for $f''$ gives the global formula with $N h^3 = (b - a) h^2$.
Example: $f(x) = x^2$ on $[0, 1]$ with $N = 2$: the error is $\tfrac{1}{3} - \tfrac{3}{8} = -\tfrac{1}{24}$, and the formula gives $-\tfrac{1 \cdot 1/4}{12} \cdot 2 = -\tfrac{1}{24}$.
Without the smoothness hypothesis the rate $h^2$ can fail: for $f(x) = \sqrt{x}$ on $[0, 1]$, whose second derivative is unbounded near $0$, the error is only of order $h^{3/2}$.
Mathlib proves the bound in the form `trapezoidal_error_le_of_c2`.

## Explanations

### L1 human

The trapezoidal rule replaces the curve by straight chords, and the mistake on each piece depends on how much the curve bends there.
The theorem says the total mistake is at most a constant times the largest bending times the square of the piece width.
So using twice as many pieces makes the error about four times smaller.
The sign also tells something: for a convex function, with $f'' \ge 0$, the trapezoidal rule overestimates the integral.

### L2 human

This bound is the model for error analysis of composite [[Newton–Cotes formulas|BQPQAY1FDJ]]: a local error of order $h^{d+2} f^{(d+1)}$ summed over $N$ pieces gives a global error of order $h^{d+1}$.
It also tells how many subintervals are needed for a given tolerance, once a bound on $\abs{f''}$ is known.
The Euler–Maclaurin formula refines it into an expansion of the error in even powers of $h$, which is the basis of Richardson extrapolation and [[Romberg's method|VP40T7MHGM]].
For smooth periodic functions all the correction terms vanish, which explains the very fast convergence of the trapezoidal rule in that case.
