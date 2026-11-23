---
tag: 52DMP8VXW4
kind: example
name: A uniform limit of Riemann integrable functions is Riemann integrable
msc: ["00A35", "40A30", "26A42"]
topics: [MEKKHHQTKB]
audience: ug2
instance_of: [VXV7M0QDH6]
uses: [VXV7M0QDH6, 0F2QCWVFT7, 0QRQVH0CRW, 017DH8WXTE, 08HJRTG5N7]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_convergence
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Darboux_integral
    locator: lead section
---

## Example

Let $a < b$, let each $f_n \colon [a, b] \to \mathbb{R}$ be [[Riemann integrable|0F2QCWVFT7]], and suppose that $f_n \to f$ [[uniformly on $[a, b]$|08HJRTG5N7]].
We prove by an [[epsilon over three argument|VXV7M0QDH6]] that $f$ is Riemann integrable.
For a bounded $g$ and a partition $P$ of $[a, b]$, write $U(g, P)$ and $L(g, P)$ for the [[upper and lower Darboux sums|0QRQVH0CRW]].

1. The function $f$ is bounded: some $f_{N_0}$ satisfies $\lvert f_{N_0} - f \rvert < 1$ everywhere, so $\lvert f \rvert < \sup \lvert f_{N_0} \rvert + 1$.
2. Let $\varepsilon > 0$.
   By [[Riemann's criterion|017DH8WXTE]], it is enough to find a partition $P$ with $U(f, P) - L(f, P) < \varepsilon$.
3. By uniform convergence, fix an index $N$ and a number $\eta < \frac{\varepsilon}{3(b - a)}$ with $\lvert f_N(x) - f(x) \rvert \le \eta$ for all $x \in [a, b]$.
4. Since $f_N$ is Riemann integrable, there is a partition $P$ with $U(f_N, P) - L(f_N, P) < \varepsilon/3$.
5. On each interval $I$ of $P$, $f(x) \le f_N(x) + \eta$ gives $\sup_I f \le \sup_I f_N + \eta$, and in the same way $\inf_I f \ge \inf_I f_N - \eta$.
6. Multiply by the lengths and add over the intervals of $P$; the lengths add up to $b - a$, so
   $$U(f, P) \le U(f_N, P) + \eta (b - a), \qquad L(f, P) \ge L(f_N, P) - \eta (b - a).$$
7. Therefore
   $$U(f, P) - L(f, P) \le \eta (b - a) + \big( U(f_N, P) - L(f_N, P) \big) + \eta (b - a) < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.$$

The three terms of step 7 are the three terms of the method: the outer ones compare $f$ with $f_N$, and the middle one is a property of $f_N$ alone.

## Remarks

The order of the choices is the same as in the [[uniform limit theorem|0X9XT05JVC]]: the index $N$ is fixed first, and the partition $P$ depends on $N$.
The estimate of step 6 also gives $\left\lvert \int_a^b f_n - \int_a^b f \right\rvert \le (b - a) \sup \lvert f_n - f \rvert$, which says that [[uniform limits commute with integration|0BWGW68B66]].

A concrete case has infinitely many jumps.
Let $H(t) = 1$ for $t \ge 0$ and $H(t) = 0$ for $t < 0$, and let $f(x) = \sum_{k = 1}^{\infty} 2^{-k} H(x - \frac1k)$ on $[0, 1]$.
The partial sum $f_n$ is a step function with $n$ jumps, so it is Riemann integrable.
The tail gives $\lvert f(x) - f_n(x) \rvert \le \sum_{k > n} 2^{-k} = 2^{-n}$ for all $x$, so the convergence is uniform.
By the example, $f$ is Riemann integrable, although it jumps by $2^{-k}$ at each point $\frac1k$.

With [[pointwise convergence|056FSKG32J]] the result fails.
List the rationals of $[0, 1]$ as $r_1, r_2, \ldots$, and let $f_n$ be $1$ at $r_1, \ldots, r_n$ and $0$ elsewhere.
Each $f_n$ has integral $0$, but the pointwise limit is $1$ on the rationals and $0$ on the irrationals, so every upper sum of the limit is $1$ and every lower sum is $0$.

## Explanations

### L1 human

The integral of a function is squeezed between an upper estimate and a lower estimate made of rectangles.
A function is Riemann integrable when the rectangles can bring the two estimates as close as we like.
Suppose a nice function stays within a thin band around $f$ everywhere.
Then the rectangles for $f$ differ from those for the nice function by at most the width of the band.
So choose the band thin enough first, and then rectangles that work for the nice function.

### L2 human

We follow the steps for the concrete case of the remarks, with $\varepsilon = \frac14$ on $[0, 1]$.

1. Step 3 asks for $\eta < \frac{1}{12}$.
   Since $\lvert f - f_n \rvert \le 2^{-n}$ and $2^{-4} = \frac{1}{16} < \frac{1}{12}$, take $N = 4$ and $\eta = \frac{1}{16}$.
2. Step 4 asks for a partition with $U(f_4, P) - L(f_4, P) < \frac{1}{12}$.
   The function $f_4$ jumps at $\frac14, \frac13, \frac12, 1$, by $\frac{1}{16}, \frac18, \frac14, \frac12$, which add up to $\frac{15}{16}$.
3. Put each jump inside its own interval of length $\frac{1}{20}$, so that $f_4$ is constant on the other intervals.
   Then $U(f_4, P) - L(f_4, P) \le \frac{15}{16} \cdot \frac{1}{20} < \frac{1}{12}$.
4. So $U(f, P) - L(f, P) < \frac{1}{16} + \frac{1}{12} + \frac{1}{16} = \frac{5}{24} < \frac14$.

The result applies to any function defined by a uniformly convergent series of step functions or of continuous functions, and the series can then be integrated term by term.
Watch out: the partition must fit the jumps of the chosen $f_N$, so choose it after $N$, not before.
