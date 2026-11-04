---
tag: 19VV6JCYN4
kind: proof
name: Proof that uniformly continuous functions map Cauchy sequences to Cauchy sequences
msc: [26A15]
proves: 026FDZFRXS
uses: [0Q4DR37DVE, 0QZMTN5AXX]
sources:
  - url: https://www.jirka.org/ra/html/sec_unifcont.html
    locator: Lemma 3.4.5
---

## Proof

1. Let $\varepsilon > 0$.
2. Since $f$ is [[uniformly continuous|0Q4DR37DVE]], there is $\delta > 0$ with $\abs{f(x) - f(y)} < \varepsilon$ for all $x, y \in D$ with $\abs{x - y} < \delta$.
3. Since $(x_n)$ is a [[Cauchy sequence|0QZMTN5AXX]], there is $N$ with $\abs{x_m - x_n} < \delta$ for all $m, n \ge N$.
4. Let $m, n \ge N$. The points $x_m$ and $x_n$ lie in $D$ and satisfy $\abs{x_m - x_n} < \delta$. So step 2 gives $\abs{f(x_m) - f(x_n)} < \varepsilon$.
5. Since $\varepsilon > 0$ was arbitrary, $(f(x_n))$ is a Cauchy sequence.

## Idea

Uniform continuity turns "inputs within $\delta$" into "outputs within $\varepsilon$", with one $\delta$ for all points. A Cauchy sequence eventually has all its terms within $\delta$ of each other. So the images are eventually within $\varepsilon$ of each other.
