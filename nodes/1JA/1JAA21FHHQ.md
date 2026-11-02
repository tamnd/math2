---
tag: 1JAA21FHHQ
kind: statement
role: proposition
name: Fundamental strip of a Mellin transform
msc: [44A15]
uses: [SGZZ4Y0D36, N5PVGRJE1T, 0TGV80E6A4, X7GTF3D98F]
about: [SGZZ4Y0D36, N5PVGRJE1T]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Statement

Let $f \colon (0, \infty) \to \C$ be integrable on every compact subinterval $[u, v] \subset (0, \infty)$.
Let $a, b \in \R$ with $b < a$, and assume that
$$f(x) = O(x^{-a}) \text{ as } x \to \infty, \qquad f(x) = O(x^{-b}) \text{ as } x \to 0^+.$$
Then $f$ is [[Mellin convergent|SGZZ4Y0D36]] at every $s \in \C$ with $b < \operatorname{Re} s < a$.
So the [[Mellin transform|N5PVGRJE1T]] $\mathcal{M}f(s)$ is defined on the open strip $b < \operatorname{Re} s < a$.

Here $O$ is [[big O notation|0TGV80E6A4]].

## Remarks

Let $\sigma = \operatorname{Re} s$.
Choose $0 < \delta < 1 < R$ with $\abs{f(x)} \le C x^{-b}$ on $(0, \delta]$ and $\abs{f(x)} \le C x^{-a}$ on $[R, \infty)$.
Then $x^{\sigma - 1} \abs{f(x)} \le C x^{\sigma - b - 1}$ on $(0, \delta]$, which is integrable since $\sigma - b > 0$.
Also $x^{\sigma - 1} \abs{f(x)} \le C x^{\sigma - a - 1}$ on $[R, \infty)$, which is integrable since $\sigma - a < 0$.
On $[\delta, R]$, $f$ is integrable and $x^{\sigma - 1}$ is bounded.

The largest open strip $\alpha < \operatorname{Re} s < \beta$ on which $f$ is Mellin convergent is called the fundamental strip and is written $\langle \alpha, \beta \rangle$.
Example: $f(x) = e^{-x}$ is $O(x^0)$ at $0$ and $O(x^{-a})$ at $\infty$ for every $a$, so its fundamental strip is $\langle 0, \infty \rangle$, where $\mathcal{M}f = \Gamma$.
Example: $f(x) = 1/(1 + x)$ is $O(1)$ at $0$ and $O(x^{-1})$ at $\infty$, giving the strip $\langle 0, 1 \rangle$.
The strict inequalities are needed: for this $f$ at $s = 1$, the bound $x^{\sigma - a - 1} = x^{-1}$ is not integrable at $\infty$, and indeed $\int_0^\infty dx/(1+x)$ diverges.

## Explanations

### L1 human

The Mellin integral has two dangerous ends, $0$ and $\infty$.
Assume that $f$ grows at most like $x^{-b}$ near $0$ and decays at least like $x^{-a}$ near $\infty$.
Then both ends are safe for every $s$ whose real part lies strictly between $b$ and $a$.
So the transform lives on a vertical strip whose edges are read off from the behaviour of $f$ at the two ends.

### L2 human

This is the first step in every computation with Mellin transforms: one finds the strip before anything else.
The edges of the strip are tied to the asymptotics of $f$.
Conversely, under suitable conditions, poles of the continued transform beyond the strip give terms of the asymptotic expansion of $f$ at $0$ or at $\infty$.
On the open strip the transform is also holomorphic, which is the companion result on differentiability of the Mellin transform.
Under the substitution $x = e^{-u}$, the statement becomes the familiar fact that a function with exponential decay at both ends of $\R$ has a two-sided Laplace transform on a strip.
