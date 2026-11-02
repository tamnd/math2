---
tag: 2PSDHH34BJ
kind: statement
role: theorem
name: Ziggurat algorithm
msc: [65C10]
uses: [R1QBNFTHFP, 0ZY9DX8FBF, 0AREFQ9Z65, 05AQE0QR0D]
about: [R1QBNFTHFP]
sources:
  - url: https://en.wikipedia.org/wiki/Ziggurat_algorithm
same_as:
  wikidata: Q2894386
  wikipedia: Ziggurat algorithm
---

## Statement

Let $f \colon [0, \infty) \to (0, \infty)$ be continuous, non-increasing and integrable.
Let $n \ge 2$, let $0 = x_0 < x_1 < \cdots < x_{n-1} = r$, and let $v > 0$ be such that:

1. $x_i \bigl(f(x_{i-1}) - f(x_i)\bigr) = v$ for $1 \le i \le n-1$;
2. $r f(r) + \int_r^\infty f(x)\, dx = v$.

Define the layers $L_i = [0, x_i] \times [f(x_i), f(x_{i-1})]$ for $1 \le i \le n-1$ and the base $L_n = \set{(x, y) : 0 \le x \le r,\ 0 \le y \le f(r)} \cup \set{(x, y) : x > r,\ 0 \le y \le f(x)}$.
The *ziggurat algorithm* repeats the following trial until it returns a value.
It chooses $i \in \set{1, \ldots, n}$ uniformly at random, draws a point $(X, Y)$ uniformly from $L_i$, and returns $X$ if $Y \le f(X)$.
Then the returned value has [[probability density|0ZY9DX8FBF]] $f / \int_0^\infty f$, and each trial returns a value with probability $\int_0^\infty f / (n v)$.

## Remarks

Each layer has area $v$ by clauses 1 and 2, and the layers overlap only in boundary segments of measure zero.
So a uniform choice of layer followed by a uniform point in it gives a point uniform on the union $Z = L_1 \cup \cdots \cup L_n$.
Since $f$ is non-increasing, $Z$ contains the region $\set{(x, y) : x \ge 0,\ 0 \le y \le f(x)}$ under the graph.
A uniform point of $Z$ conditioned to lie under the graph is uniform there, and its first coordinate has density proportional to $f$.
This is [[rejection sampling|R1QBNFTHFP]] with a uniform envelope on $Z$.
The speed comes from a shortcut: in layer $i \le n-1$, if $X < x_{i-1}$ then $Y \le f(x_{i-1}) \le f(X)$, so the point is accepted without evaluating $f$.
For large $n$, such as $n = 128$ or $256$, almost all trials end this way, after one random integer, one multiplication and one comparison.
A uniform point of the base $L_n$ is drawn as follows.
With probability $r f(r)/v$ it is a uniform point of the rectangle $[0, r] \times [0, f(r)]$.
Otherwise $X$ is drawn from the tail density proportional to $f$ on $(r, \infty)$, which needs a separate tail sampler, and $Y$ is uniform on $[0, f(X)]$.
For the standard [[normal distribution|05AQE0QR0D]], one samples $\abs{Z}$ with $f(x) = e^{-x^2/2}$ and attaches a random sign.
The numbers $x_i$, $r$ and $v$ are computed once, by solving the equations of clauses 1 and 2 numerically.

## Explanations

### L1 human

Picture the area under a decreasing density curve covered by a stack of horizontal slabs of equal area, like a stepped pyramid, the ziggurat.
Pick a slab at random and a random point in it.
Most of each slab lies completely under the curve, and a point there is accepted at once.
Only near the right edge of a slab, or in the bottom slab with its infinite tail, is extra work needed.
The result is an exact sampler that, most of the time, costs almost nothing.

### L2 human

The algorithm, due to Marsaglia and Tsang, is a form of rejection sampling with a piecewise constant envelope that fits the density tightly.
It is used for normal and exponential random numbers in many numerical libraries.
For symmetric densities such as the normal, it samples the right half and attaches a random sign; often the sign comes from a spare bit of the same random integer.
Its exactness depends on good uniform variates and an exact tail sampler; the tail of the normal is usually handled by a method of Marsaglia based on exponential variates.
