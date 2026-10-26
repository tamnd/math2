---
tag: 06B8BNJCD6
kind: statement
role: theorem
name: Heine–Cantor theorem
aliases: [heine-cantor-theorem]
msc: ["54E45"]
uses: [0QPHW703PV, 0SY9ECQ19Q, 0FHSDCQACY, 0K8SGQSV7G]
sources:
  - url: https://en.wikipedia.org/wiki/Heine%E2%80%93Cantor_theorem
    locator: lead section
same_as:
  wikidata: Q765987
  wikipedia: Heine–Cantor theorem
---

## Statement

Let $X$ and $Y$ be [[metric spaces|063W5JMY85]] and let $f \colon X \to Y$ be a [[continuous map|0SY9ECQ19Q]].
If $X$ is [[compact|0QPHW703PV]], then $f$ is [[uniformly continuous|0FHSDCQACY]].

## Remarks

Proof by contradiction: if $f$ is not uniformly continuous, there are $\varepsilon > 0$ and points $x_n, y_n$ with $d(x_n, y_n) \to 0$ and $d(f(x_n), f(y_n)) \ge \varepsilon$. By [[sequential compactness|0K8SGQSV7G]], a subsequence of $(x_n)$ converges to some $x$, and the matching subsequence of $(y_n)$ also converges to $x$. Continuity at $x$ gives a contradiction.
For example, each continuous $f \colon [a, b] \to \mathbb{R}$ is uniformly continuous. This fact is used to show that $f$ is Riemann integrable.
The theorem fails on $\mathbb{R}$: $x \mapsto x^2$ is continuous but not uniformly continuous.

## Explanations

### L1 human

On a compact space, continuity at each point is enough to get one $\delta$ for the whole space.
Compactness rules out regions where the function becomes steeper and steeper without end.
