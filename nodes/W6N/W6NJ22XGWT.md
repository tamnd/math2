---
tag: W6NJ22XGWT
kind: example
name: The integral inner product on polynomials of degree at most 2
msc: ["15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
instance_of: [0NB0AWGJBW, 0QVNCJXRY3, 0MFJJV97RJ]
uses: [0VGSYBWHV2, 0JGZCDT5DN, 0W29TBTY12, 0MBWQKM8QR, 0KJVQV3E0F, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Examples
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Example

Let $V = \mathcal{P}_2(\mathbb{R})$ be the [[space of real polynomials|0JGZCDT5DN]] of degree at most $2$.
For $p, q \in V$ put
$$\ip{p}{q} = \int_0^1 p(t) \, q(t) \, dt,$$
where the integral is the [[Riemann integral|0W29TBTY12]].
We check that the integral exists and that the three axioms of an [[inner product|0VGSYBWHV2]] hold, and then we compute some values.

1. The integral exists, because $pq$ is a polynomial and so is [[continuous|0X3WGX95FE]] on $[0, 1]$.
2. Linearity in the first slot holds by the linearity of the integral: $\int_0^1 (ap + br) q = a\int_0^1 pq + b\int_0^1 rq$.
3. Symmetry holds, because $p(t)q(t) = q(t)p(t)$ for each $t$.
Over $\mathbb{R}$ this is conjugate symmetry.
4. For positivity, let $p \neq 0$.
A nonzero polynomial of degree at most $2$ has [[at most $2$ roots|0KJVQV3E0F]], so there is a point $t_0 \in (0, 1)$ with $p(t_0) \neq 0$.
5. By continuity there is $\delta > 0$ with $[t_0 - \delta, t_0 + \delta] \subseteq [0, 1]$ and $\abs{p(t)} \geq \abs{p(t_0)}/2$ on this interval.
6. So $p(t)^2 \geq c$ with $c = p(t_0)^2/4 > 0$ on an interval of length $2\delta$, and $p(t)^2 \geq 0$ on all of $[0, 1]$.
7. By the [[monotonicity of the integral|0MBWQKM8QR]], $\ip{p}{p} = \int_0^1 p^2 \geq 2\delta c > 0$.
8. On the monomials the inner product is
$$\ip{t^j}{t^k} = \int_0^1 t^{j + k} \, dt = \frac{1}{j + k + 1}.$$
So $\ip{1}{1} = 1$, $\ip{1}{t} = \frac12$, $\ip{t}{t} = \ip{1}{t^2} = \frac13$, $\ip{t}{t^2} = \frac14$ and $\ip{t^2}{t^2} = \frac15$.
9. Let $p = 1 + t$ and $q = t$.
By step 8 and linearity, $\ip{p}{q} = \ip{1}{t} + \ip{t}{t} = \frac12 + \frac13 = \frac56$.
10. The [[induced norms|0MFJJV97RJ]] are given by
$$\norm{p}^2 = \ip{1}{1} + 2\ip{1}{t} + \ip{t}{t} = 1 + 1 + \tfrac13 = \tfrac73, \qquad \norm{q}^2 = \tfrac13.$$
11. The [[Cauchy-Schwarz inequality|0RFWW56Y22]] holds, since $\ip{p}{q}^2 = \frac{25}{36}$ and $\norm{p}^2 \norm{q}^2 = \frac79 = \frac{28}{36}$.
12. The polynomials $1$ and $t - \frac12$ are [[orthogonal|0Y2X7P2WB7]], since $\int_0^1 (t - \frac12) \, dt = \frac12 - \frac12 = 0$.

So $(\mathcal{P}_2(\mathbb{R}), \ip{\cdot}{\cdot})$ is an [[inner product space|0QVNCJXRY3]].

## Remarks

The example shows that functions can carry a geometry of lengths and angles.
The positivity argument in steps 4 to 7 uses only that a nonzero polynomial is not zero on a whole interval.
So the same proof works for $\mathcal{P}_n(\mathbb{R})$ for every $n$, and for continuous functions on $[0, 1]$.

On all Riemann integrable functions the formula is not positive definite.
A function that is $1$ at one point and $0$ elsewhere is not zero, but the integral of its square is $0$.
The numbers $\frac{1}{j + k + 1}$ of step 8 form the [[Gram matrix of $1, t, t^2$|JNME2MD8GM]], which is a Hilbert matrix.
If you change the interval to $[-1, 1]$, the [[Gram-Schmidt process|0VT6P0GNQR]] applied to $1, t, t^2, t^3$ gives multiples of the [[Legendre polynomials|JPDVZM20EX]].

## Explanations

### L1 human

Two polynomials can be multiplied, and the product can be integrated from $0$ to $1$.
The result is one number, and it plays the role of the dot product.
For the polynomial $t$ paired with itself, we integrate $t^2$ and get $\frac13$.
So the length of $t$ for this rule is $\frac{1}{\sqrt{3}}$.
A polynomial that is not zero is not zero on a whole interval, so its square has a positive integral.

### L2 human

Here is a typical question: which constant is closest to $t$ on $[0, 1]$, in this inner product?
The answer is the projection of $t$ onto the constant polynomials.
The constant $1$ has $\norm{1}^2 = 1$ and $\ip{t}{1} = \frac12$, so the [[vector projection|0JW13B48YP]] formula, with the inner product in place of the dot product, gives
$$\frac{\ip{t}{1}}{\ip{1}{1}} \cdot 1 = \frac12.$$
Check: the error $t - \frac12$ is orthogonal to $1$, by step 12.
By the [[closest point theorem|0MCDDSCB9Z]], $\frac12$ is the best constant approximation of $t$ in this norm, and it is the mean value of $t$ on the interval.
This is the least squares idea: approximate a function by a simpler one, measured by an integral of squared errors.
Watch out: the values depend on the interval, so $\ip{1}{t} = 0$ on $[-1, 1]$ but $\ip{1}{t} = \frac12$ on $[0, 1]$.
