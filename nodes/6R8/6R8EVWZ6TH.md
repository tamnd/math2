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

[[Thomae's function|0HJ28H9Y95]] $f \colon \mathbb{R} \to \mathbb{R}$ is defined by
$$f(x) = \begin{cases} \dfrac{1}{q} & \text{if } x = \dfrac{p}{q} \text{ in lowest terms, with } q > 0, \\[2mm] 0 & \text{if } x \text{ is irrational.} \end{cases}$$
We check that $f$ is [[continuous|0X3WGX95FE]] exactly at the irrational numbers, which makes it a [[pathological|WMBZPYPN2D]] function.

1. We compute some values.
   $f(0) = f(0/1) = 1$, $f(\tfrac{1}{2}) = \tfrac{1}{2}$, $f(\tfrac{2}{3}) = \tfrac{1}{3}$, $f(\tfrac{3}{4}) = \tfrac{1}{4}$ and $f(\sqrt{2}) = 0$.
2. $f$ is discontinuous at each [[rational|0NCJ5WXN6Z]] point $a = p/q$.
   Here $f(a) = 1/q > 0$.
   Every interval around $a$ contains irrational points $x$, where $f(x) = 0$.
   So $f(x)$ does not tend to $f(a)$ as $x \to a$.
3. Let $a$ be [[irrational|0DZXAXEJQ9]], and let $\varepsilon > 0$.
   Choose an integer $N \ge 1/\varepsilon$.
   Only finitely many rationals $p/q$ with $q \le N$ lie in $(a - 1, a + 1)$, at most $2q + 1$ for each $q$, and none of them equals $a$.
4. Choose $\delta > 0$ so small that $(a - \delta, a + \delta)$ contains none of these finitely many rationals.
   For $x$ in this interval, either $x$ is irrational and $f(x) = 0$, or $x = p/q$ with $q > N$ and $f(x) = 1/q < 1/N \le \varepsilon$.
5. So $|f(x) - f(a)| < \varepsilon$ whenever $|x - a| < \delta$, and $f$ is continuous at $a$.

The function is continuous on one dense set and discontinuous on another dense set, which defeats the picture of a graph drawn without lifting the pen.

## Remarks

Thomae's function is [[Riemann integrable|0W29TBTY12]] on $[0, 1]$ with integral $0$, although it has infinitely many discontinuities.
So it also shows that a function can be integrable and discontinuous on a dense set.

The pathology cannot be reversed.
No function from $\mathbb{R}$ to $\mathbb{R}$ is continuous exactly at the rationals, and this follows from the [[Baire category theorem|0A7KGAYHGV]].

If you change the value $1/q$ to the constant $1$ at every rational, you get the Dirichlet function, which is discontinuous everywhere.
The shrinking heights $1/q$ are what make continuity at the irrationals possible.
Today Thomae's function is a standard example in a first course of analysis, which shows that the word "pathological" is relative to time.

## Explanations

### L1 human

Thomae's function is $0$ at every irrational number.
At a fraction $p/q$ in lowest terms, its value is $1/q$.
So the function jumps up at every fraction, and fractions are everywhere on the line.
But the jumps get smaller as the denominators grow.
Because of this, the function is continuous at the irrational numbers and not at the fractions.

### L2 human

We test continuity at the irrational point $a = \sqrt{2}/2 \approx 0.7071$ with $\varepsilon = \tfrac{1}{4}$, following steps 3 and 4.
Take $N = 4$.
The rationals in $(0, 1)$ with denominator at most $4$ are $\tfrac{1}{4}, \tfrac{1}{3}, \tfrac{1}{2}, \tfrac{2}{3}, \tfrac{3}{4}$, and the nearest to $a$ are
$$\left|a - \tfrac{2}{3}\right| \approx 0.0404, \qquad \left|a - \tfrac{3}{4}\right| \approx 0.0429.$$
So $\delta = 0.04$ works: every rational $x$ with $|x - a| < 0.04$ has denominator at least $5$, and so $f(x) \le \tfrac{1}{5} < \tfrac{1}{4}$.
A smaller $\varepsilon$ needs a larger $N$, more excluded fractions and a smaller $\delta$, but the method is the same.
Watch out at $0$: it is the rational $0/1$, so $f(0) = 1$ and $f$ is not continuous there.
