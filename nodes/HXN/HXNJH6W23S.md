---
tag: HXNJH6W23S
kind: statement
role: theorem
name: Hausdorff–Young inequality
msc: ["42B10", "42A38", "42A16"]
uses: [DPVM34ADZV, SASP14MA1Z, AGRKRG1TMJ, HPZHRZ0502]
about: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Hausdorff%E2%80%93Young_inequality
same_as:
  wikidata: Q5682823
  wikipedia: Hausdorff–Young inequality
---

## Statement

Let $n \ge 1$, let $1 \le p \le 2$, and let $q$ be the conjugate exponent, $\frac{1}{p} + \frac{1}{q} = 1$.
Let $\hat f(\xi) = \int_{\R^n} f(x) e^{-2\pi i x \cdot \xi}\, dx$ be the [[Fourier transform|DPVM34ADZV]] of $f \in L^1(\R^n)$.
Then for every $f \in L^1(\R^n) \cap L^p(\R^n)$,
$$\norm{\hat f}_{L^q(\R^n)} \le \norm{f}_{L^p(\R^n)}.$$
Consequently the Fourier transform extends uniquely to a bounded linear map from [[$L^p(\R^n)$|SASP14MA1Z]] to $L^q(\R^n)$ of norm at most $1$.

## Remarks

The two endpoint cases are known: for $p = 1$, $\abs{\hat f(\xi)} \le \norm{f}_1$ for every $\xi$, and for $p = 2$, the [[Plancherel theorem|HPZHRZ0502]] gives $\norm{\hat f}_2 = \norm{f}_2$.
The [[Riesz–Thorin theorem|AGRKRG1TMJ]] interpolates between them and gives the inequality for $1 < p < 2$.

The constant $1$ is not sharp for $1 < p < 2$; the sharp constant is given by the Babenko–Beckner inequality.
The restriction $p \le 2$ is necessary: for $p > 2$ there are functions in $L^p(\R^n)$ whose Fourier transform, as a tempered distribution, is not a function.

There is a version for Fourier series on the circle $\mathbb{T} = \R / \Z$ with normalized measure: for $1 \le p \le 2$ and $f \in L^p(\mathbb{T})$, $\left(\sum_{k \in \Z} \abs{\hat f(k)}^q\right)^{1/q} \le \norm{f}_{L^p(\mathbb{T})}$.

Example: for $f(x) = e^{-\pi x^2}$ on $\R$, $\hat f = f$, and $\norm{f}_r = r^{-1/(2r)}$ for every $r > 0$.
So $\norm{\hat f}_q / \norm{f}_p = \left( p^{1/p} / q^{1/q} \right)^{1/2}$, and the theorem says that this number is at most $1$.

## Explanations

### L1 human

The Fourier transform cannot make a function much bigger in a suitable average sense.
If $f$ is $p$-th power integrable with $p$ between $1$ and $2$, then its transform is $q$-th power integrable for the conjugate exponent $q$, with norm no larger.

### L2 human

The inequality is the first example of an $L^p$ estimate obtained by interpolation, and it is the model for the Riesz–Thorin method.
It shows that the Fourier transform is defined as a function on $L^p$ for $1 \le p \le 2$.
It is used in restriction theory, in the theory of Fourier multipliers and in the entropic uncertainty principle.
On locally compact abelian groups the same statement holds, with the dual group in place of the frequency space.
