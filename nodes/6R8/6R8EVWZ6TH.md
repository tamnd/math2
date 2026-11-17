---
tag: 6R8EVWZ6TH
kind: example
name: Thomae's function is a pathological function
msc: ["00A35", "26A15"]
topics: [Z2WNQ1DNTX]
audience: ug2
instance_of: [WMBZPYPN2D]
uses: [0HJ28H9Y95, 0NCJ5WXN6Z, 0DZXAXEJQ9, 0X3WGX95FE, 0W29TBTY12, WMBZPYPN2D]
sources:
  - url: https://en.wikipedia.org/wiki/Thomae%27s_function
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Pathological_(mathematics)
    locator: lead section
---

## Example

[[Thomae's function|0HJ28H9Y95]] $f \colon \mathbb{R} \to \mathbb{R}$ is $f(x) = 0$ for irrational $x$, and $f(p/q) = 1/q$ for a rational number $p/q$ in lowest terms with $q > 0$.
We check that $f$ is [[continuous|0X3WGX95FE]] exactly at the irrational numbers.

1. Values. $f(0) = f(0/1) = 1$, $f(\tfrac{1}{2}) = \tfrac{1}{2}$, $f(\tfrac{2}{3}) = \tfrac{1}{3}$ and $f(\sqrt{2}) = 0$.
2. Discontinuity at a [[rational|0NCJ5WXN6Z]] point $a = p/q$. Here $f(a) = 1/q > 0$. Every interval around $a$ contains irrational points $x$, where $f(x) = 0$. So $f(x)$ does not tend to $f(a)$ as $x \to a$.
3. Continuity at an [[irrational|0DZXAXEJQ9]] point $a$. Let $\varepsilon > 0$ and choose an integer $N \ge 1/\varepsilon$. Only finitely many rationals $p/q$ with $q \le N$ lie in $(a - 1, a + 1)$, and none of them equals $a$.
4. Choose $\delta > 0$ so small that $(a - \delta, a + \delta)$ contains none of these finitely many rationals. For $x$ in this interval, either $x$ is irrational and $f(x) = 0$, or $x = p/q$ with $q > N$ and $f(x) < 1/N \le \varepsilon$.
5. So $|f(x) - f(a)| < \varepsilon$ for $|x - a| < \delta$, and $f$ is continuous at $a$.

The function is continuous on a dense set and discontinuous on another dense set, which defeats the picture of a graph drawn without lifting the pen.

## Remarks

Thomae's function is [[Riemann integrable|0W29TBTY12]] on $[0, 1]$, with integral $0$, although it has infinitely many discontinuities.
No function is continuous exactly at the rationals; this follows from the [[Baire category theorem|0A7KGAYHGV]].
So the pathology of Thomae's function cannot be reversed.
Today the function is a standard example in a first course of analysis, which shows that the word "pathological" is relative to time.

## Explanations

### L1 human

Thomae's function is $0$ at every irrational number.
At a fraction $p/q$ in lowest terms, its value is $1/q$.
So the function jumps up at every fraction, and fractions are everywhere on the line.
But the jumps get smaller as the denominators grow.
Because of this, the function is continuous at the irrational numbers and not at the fractions.

### L2 human

We test continuity at the irrational point $a = \sqrt{2}/2 \approx 0.7071$ with $\varepsilon = \tfrac{1}{4}$.

1. Take $N = 4$. The rationals in $(0, 1)$ with denominator at most $4$ are $\tfrac{1}{4}, \tfrac{1}{3}, \tfrac{1}{2}, \tfrac{2}{3}, \tfrac{3}{4}$.
2. The nearest of these to $a$ is $\tfrac{2}{3} \approx 0.6667$, at distance about $0.040$, and $\tfrac{3}{4}$ is at distance about $0.043$.
3. So $\delta = 0.04$ works: every $x$ with $|x - a| < 0.04$ has $f(x) < \tfrac{1}{4}$.

The typical use of the function is as a counterexample: a function can be integrable and have a dense set of discontinuities.
A trap: the function is not continuous at $0$, since $0 = 0/1$ is rational with $f(0) = 1$.
