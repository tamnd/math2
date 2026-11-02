---
tag: 5F9MP8VCJ4
kind: definition
name: Real Hardy space H1
msc: [42B30, 42B35]
defines: 75WGJ014GR
uses: [SASP14MA1Z, FRNDFJ9WQ5, NSCEBXM7ZM, AES2T5JPFP]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy_space
---

## Definition

Let $n \ge 1$ and let $L^1(\R^n)$ be the [[Lp space|SASP14MA1Z]] of integrable functions for Lebesgue measure.
For $j = 1, \dots, n$ let $R_j$ be the $j$-th [[Riesz transform|FRNDFJ9WQ5]], which maps each $f \in L^1(\R^n)$ to a [[tempered distribution|AES2T5JPFP]] $R_j f$.
The *real Hardy space* $H^1(\R^n)$ is the set of $f \in L^1(\R^n)$ such that each $R_j f$, $j = 1, \dots, n$, is given by a function in $L^1(\R^n)$.
It is a Banach space with the norm
$$\norm{f}_{H^1} = \norm{f}_{L^1} + \sum_{j=1}^n \norm{R_j f}_{L^1}.$$

## Remarks

For $n = 1$ the only Riesz transform is the [[Hilbert transform|NSCEBXM7ZM]] $H$, so $H^1(\R) = \set{f \in L^1(\R) : Hf \in L^1(\R)}$.
Equivalent definitions use maximal functions or atoms.
Fix a Schwartz function $\varphi$ with $\int \varphi = 1$ and let $\varphi_t(x) = t^{-n}\varphi(x/t)$.
Then $f \in H^1(\R^n)$ exactly when $f$ is a tempered distribution with $\sup_{t > 0} \abs{f * \varphi_t} \in L^1(\R^n)$, and the two norms are comparable.
Every $f \in H^1(\R^n)$ has $\int f = 0$.

Example: $n = 1$ and $a = \mathbf{1}_{[0, 1]} - \mathbf{1}_{[-1, 0]}$.
For $\abs{x} > 2$, using $\int a = 0$, $Ha(x) = \frac{1}{\pi} \int a(y) \left( \frac{1}{x - y} - \frac{1}{x} \right) dy$, which is bounded by $C/x^2$.
Near the points $-1$, $0$ and $1$, $Ha$ has only logarithmic singularities, which are integrable.
So $Ha \in L^1(\R)$ and $a \in H^1(\R)$.

Non-example: $f = \mathbf{1}_{[0, 1]}$ on $\R$ is integrable but not in $H^1(\R)$.
Its Hilbert transform is $Hf(x) = \frac{1}{\pi} \log \abs{\frac{x}{x - 1}}$, which behaves like $\frac{1}{\pi x}$ as $\abs{x} \to \infty$, so it is not integrable.
This agrees with the fact that $\int f = 1 \ne 0$.
