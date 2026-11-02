---
tag: GS4RC7A7DJ
kind: statement
role: theorem
name: Weyl's criterion
msc: [11K06, 11J71]
uses: [RT62ZAN3JB, 97PBMQCPPM, 07GJV36896, NCCGNTBEYV]
about: [XM6DH57BWY]
sources:
  - url: https://en.wikipedia.org/wiki/Equidistributed_sequence
---

## Statement

Let $(x_n)_{n \ge 1}$ be a sequence of real numbers.
Then $(x_n)$ is [[equidistributed modulo one|RT62ZAN3JB]] if and only if, for every nonzero integer $h$,
$$\lim_{N \to \infty} \frac{1}{N} \sum_{n=1}^{N} e^{2 \pi i h x_n} = 0.$$
Here $e^{2\pi i t}$ is the [[complex exponential|07GJV36896]].

## Remarks

Equidistribution modulo one is equivalent to $\frac{1}{N} \sum_{n \le N} f(x_n) \to \int_0^1 f(t) \, dt$ for every continuous function $f \colon \R \to \C$ of period $1$.
The functions $t \mapsto e^{2\pi i h t}$ are such functions, with integral $0$ for $h \ne 0$, which gives one direction.
For the other direction, the condition gives the limit for every trigonometric polynomial.
Uniform approximation by the Weierstrass theorem extends it to every continuous periodic $f$.
Finally, squeezing the indicator of an interval between continuous functions gives the counting condition.
Example: for irrational $\alpha$ and $x_n = n \alpha$, the sum is a geometric sum bounded by $2 / \abs{1 - e^{2\pi i h \alpha}}$, so the averages tend to $0$; this proves the [[equidistribution theorem|NCCGNTBEYV]].
For a rational $\alpha = p/q$ the test fails at $h = q$, where every term equals $1$.
The same criterion holds in $\R^k$, with $h$ running over nonzero vectors of $\Z^k$ and $h x_n$ replaced by the dot product $h \cdot x_n$.

## Explanations

### L1 human

To check that a sequence spreads evenly around a circle, it is enough to test it against waves.
For each frequency $h$, average the points $e^{2\pi i h x_n}$ on the unit circle.
The sequence is evenly spread exactly when all these averages tend to zero.

### L2 human

The criterion turns a question about counting points in intervals into estimates of [[exponential sums|97PBMQCPPM]].
It gives a short proof that $(n\alpha)$ is equidistributed for irrational $\alpha$.
With Weyl differencing, it also shows that $p(n)$ is equidistributed for a real polynomial $p$ with an irrational coefficient other than the constant term.
Its proof is a first example of approximating indicator functions by trigonometric polynomials, a basic method of Fourier analysis.
