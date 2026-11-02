---
tag: JXDKJCBXJ8
kind: statement
role: theorem
name: Young's convolution inequality
msc: [44A35, 26D15, "46E30"]
uses: [SASP14MA1Z, 2Z2QVWZ262]
about: [SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Young%27s_convolution_inequality
same_as:
  wikidata: Q30752114
  wikipedia: Young's convolution inequality
---

## Statement

Let $n \ge 1$ and consider [[Lp spaces|SASP14MA1Z]] on $\R^n$ with [[Lebesgue measure|2Z2QVWZ262]].
Let $1 \le p, q, r \le \infty$ with
$$\frac{1}{p} + \frac{1}{q} = 1 + \frac{1}{r}.$$
Let $f \in L^p(\R^n)$ and $g \in L^q(\R^n)$.
Then the convolution
$$(f * g)(x) = \int_{\R^n} f(y) \, g(x - y) \, dy$$
converges absolutely for almost every $x \in \R^n$, the function $f * g$ lies in $L^r(\R^n)$, and
$$\norm{f * g}_r \le \norm{f}_p \norm{g}_q.$$

## Remarks

The case $p = 1$ and $q = r$ follows from Minkowski's inequality for integrals: $f * g$ is an average of translates of $g$, each of norm $\norm{g}_q$.
The case $r = \infty$, with $p$ and $q$ conjugate, is Hölder's inequality applied for each fixed $x$; then $f * g$ is defined everywhere.
The general case follows from these two by the [[Riesz–Thorin theorem|AGRKRG1TMJ]], or directly by a three-factor Hölder inequality.

Example: with $p = q = 1$, one gets $r = 1$ and $\norm{f * g}_1 \le \norm{f}_1 \norm{g}_1$.
So $L^1(\R^n)$ is a Banach algebra under convolution.

The exponent relation is forced by scaling.
If $f_\lambda(x) = f(\lambda x)$, then $\norm{f_\lambda}_p = \lambda^{-n/p} \norm{f}_p$ and $f_\lambda * g_\lambda = \lambda^{-n} (f * g)_\lambda$.
An inequality $\norm{f * g}_r \le C \norm{f}_p \norm{g}_q$ for all $\lambda > 0$ therefore requires $1 + 1/r = 1/p + 1/q$.

The same inequality holds with the same proof on any unimodular locally compact group with Haar measure.
The constant $1$ is not sharp on $\R^n$ when $1 < p, q, r < \infty$; the sharp constant is known.

## Explanations

### L1 human

Convolution smears one function out by another, like blurring a picture with a lens.
Young's inequality says how big the blurred result can be in terms of the sizes of the two ingredients.
The exponents must fit together in one specific way, which a change of scale explains.

### L2 human

Young's inequality is the basic estimate for convolution operators $f \mapsto f * g$ with a fixed kernel $g$.
With $g \in L^1$ it shows that mollification $f * \varphi_\varepsilon$ is bounded on every $L^p$, which is the first step of approximation by smooth functions.
With $g$ a power such as $\abs{x}^{-\alpha}$, which is not in any $L^q(\R^n)$, Young's inequality does not apply, and one needs the Hardy–Littlewood–Sobolev inequality, which uses weak $L^q$ instead.
