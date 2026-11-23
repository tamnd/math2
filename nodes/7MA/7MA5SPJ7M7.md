---
tag: 7MA5SPJ7M7
kind: example
name: A uniform limit of uniformly continuous functions is uniformly continuous
msc: ["00A35", "40A30", "26A15"]
topics: [MEKKHHQTKB]
audience: ug2
instance_of: [VXV7M0QDH6]
uses: [VXV7M0QDH6, 0M4JJT780X, 08HJRTG5N7, 03HF5PMY5T]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_convergence
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Uniform_limit_theorem
    locator: lead section
---

## Example

Let $S \subseteq \mathbb{R}$, and let each $f_n \colon S \to \mathbb{R}$ be [[uniformly continuous|0M4JJT780X]].
Suppose that $f_n \to f$ [[uniformly on $S$|08HJRTG5N7]].
We prove by an [[epsilon over three argument|VXV7M0QDH6]] that $f$ is uniformly continuous on $S$.

1. Let $\varepsilon > 0$.
   We must find $\delta > 0$ with $\lvert f(x) - f(y) \rvert < \varepsilon$ for all $x, y \in S$ with $\lvert x - y \rvert < \delta$.
2. By uniform convergence, fix an index $N$ with $\lvert f_N(z) - f(z) \rvert < \varepsilon/3$ for all $z \in S$.
   This $N$ does not depend on any point.
3. Since $f_N$ is uniformly continuous, there is $\delta > 0$ with $\lvert f_N(x) - f_N(y) \rvert < \varepsilon/3$ for all $x, y \in S$ with $\lvert x - y \rvert < \delta$.
4. Let $x, y \in S$ with $\lvert x - y \rvert < \delta$.
   By the [[triangle inequality|03HF5PMY5T]],
   $$\lvert f(x) - f(y) \rvert \le \lvert f(x) - f_N(x) \rvert + \lvert f_N(x) - f_N(y) \rvert + \lvert f_N(y) - f(y) \rvert.$$
5. The outer terms are less than $\varepsilon/3$ by step 2, with $z = x$ and $z = y$, and the middle term is less than $\varepsilon/3$ by step 3.
6. So $\lvert f(x) - f(y) \rvert < \varepsilon$, and $\delta$ depends only on $\varepsilon$, so $f$ is uniformly continuous.

## Remarks

The proof is the proof of the [[uniform limit theorem|0X9XT05JVC]] with one change: the $\delta$ of step 3 does not depend on a point.
The three terms pass this uniformity from $f_N$ to $f$.
With pointwise convergence the result fails: the functions $x^n$ on $[0, 1]$ are uniformly continuous, and their pointwise limit is not even continuous, as [[the failed argument for x^n|JKPVHGFN1R]] shows.

A concrete case shows what passes to the limit and what does not.
On $[0, \infty)$, let $f_n(x) = \sqrt{x + 1/n}$ and $f(x) = \sqrt{x}$.
For every $x \ge 0$,
$$\sqrt{x + 1/n} - \sqrt{x} = \frac{1/n}{\sqrt{x + 1/n} + \sqrt{x}} \le \frac{1/n}{\sqrt{1/n}} = \frac{1}{\sqrt n},$$
so the convergence is uniform.
Each $f_n$ is Lipschitz with constant $\frac{\sqrt n}{2}$, since $f_n'(x) = \frac{1}{2\sqrt{x + 1/n}} \le \frac{\sqrt n}{2}$.
The limit $\sqrt{x}$ is uniformly continuous, by the example, but it is not Lipschitz near $0$.
So uniform continuity, a property of the form "for each $\varepsilon$ there is $\delta$", survives the limit, while a fixed Lipschitz bound need not, because the constants grow with $n$.

## Explanations

### L1 human

A function is uniformly continuous when one closeness rule for the inputs works everywhere at once.
Suppose each function of a sequence has such a rule, and the functions approach a limit at the same speed everywhere.
Pick one function of the sequence that is within a third of the tolerance of the limit at every point.
Its closeness rule, with the two small errors at the ends, gives a rule for the limit.

### L2 human

We run the proof for $f_n(x) = \sqrt{x + 1/n}$ on $[0, \infty)$ with $\varepsilon = 0.3$.

1. Step 2 asks for $N$ with $\frac{1}{\sqrt N} < 0.1$, and $N = 101$ works, since $\sqrt{101} > 10$.
2. Step 3 asks for a $\delta$ for $f_{101}$ and the tolerance $0.1$.
   Since $f_{101}$ is Lipschitz with constant $\frac{\sqrt{101}}{2} < 5.03$, the choice $\delta = 0.1/5.03 \approx 0.0199$ works.
3. For $\lvert x - y \rvert < \delta$, the three terms are each less than $0.1$, so $\lvert \sqrt{x} - \sqrt{y} \rvert < 0.3$.

The result shows that a function defined as a uniform limit, such as a power series on a compact interval, is uniformly continuous.
Watch out: a $\delta$ in step 3 that is good only near one point gives continuity, not uniform continuity.
