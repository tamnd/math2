---
tag: M0G4AASSG7
kind: statement
role: theorem
name: Viète's formula
msc: [40A20, 11Y60]
uses: [0C1VYVNV2N, H1Z2TKY3EQ, 08WFZP6P89]
about: [0C1VYVNV2N]
sources:
  - url: https://en.wikipedia.org/wiki/Vi%C3%A8te%27s_formula
same_as:
  wikidata: Q949597
  wikipedia: Viète's formula
---

## Statement

Let $a_1 = \sqrt{2}$ and $a_{n+1} = \sqrt{2 + a_n}$ for $n \ge 1$.
Then the infinite product $\prod_{n=1}^{\infty} a_n / 2$ [[converges|H1Z2TKY3EQ]], and
$$\prod_{n=1}^{\infty} \frac{a_n}{2} = \frac{\sqrt2}{2} \cdot \frac{\sqrt{2 + \sqrt2}}{2} \cdot \frac{\sqrt{2 + \sqrt{2 + \sqrt2}}}{2} \cdots = \frac{2}{\pi},$$
where $\pi$ is the number [[pi|0C1VYVNV2N]].

## Remarks

By induction, $a_n = 2 \cos(\pi / 2^{n+1})$, using $2\cos(\theta/2) = \sqrt{2 + 2\cos\theta}$ for $0 \le \theta \le \pi$.
The double-angle formula $\sin 2t = 2 \sin t \cos t$, applied $N$ times, gives
$$\sin x = 2^N \sin(x / 2^N) \prod_{n=1}^{N} \cos(x / 2^n).$$
For $x = \pi/2$ this says $\prod_{n=1}^{N} \cos(\pi / 2^{n+1}) = \frac{1}{2^N \sin(\pi / 2^{N+1})}$.
Since $2^{N+1} \sin(\pi / 2^{N+1}) \to \pi$, the right side tends to $2/\pi$.
The formula appeared in work of François Viète published in 1593.
It converges fast: each factor adds about $0.6$ correct decimal digits of $\pi$.

## Explanations

### L1 human

Viète's formula writes $2/\pi$ as an infinite product of nested square roots of $2$.
It comes from inscribing regular polygons with $4, 8, 16, \ldots$ sides in a circle and comparing their areas.
As the number of sides doubles, the polygons fill the circle, and the ratio of areas gives the next factor.

### L2 human

The proof uses only the [[sine and cosine|08WFZP6P89]] double-angle formula and the limit $\sin(t)/t \to 1$.
The same computation gives the product $\frac{\sin x}{x} = \prod_{n \ge 1} \cos(x / 2^n)$ for every $x \ne 0$.
Viète's formula is one of the first infinite products in mathematics, and the [[Wallis product|0XCYA4YERS]] is another classical product for $\pi$.
