---
tag: 4P7KPA3Y7R
kind: statement
role: proposition
name: Smoothing by convolution
msc: [44A35, 42A85]
uses: [2Z29JN3VES, 0V33BNKZ9S, 9FN0PFZZXZ]
about: [2Z29JN3VES]
sources:
  - url: https://en.wikipedia.org/wiki/Convolution
---

## Statement

Let $n \ge 1$ and let $k \ge 0$ be an integer or $k = \infty$.
Let $f \colon \R^n \to \C$ be locally integrable, that is, integrable on every compact set.
Let $g \colon \R^n \to \C$ be a $C^k$ function with compact support.
Then the [[convolution|2Z29JN3VES]] $f * g$ is a $C^k$ function on $\R^n$, and $\partial^\alpha (f * g) = f * \partial^\alpha g$ for every multi-index $\alpha$ with $\abs{\alpha} \le k$.
In particular, if $g$ is a [[smooth function|0V33BNKZ9S]] with compact support, then $f * g$ is smooth.

## Remarks

For $k = 0$, continuity of $f * g$ follows from the uniform continuity of $g$ and the integrability of $f$ on compact sets.
The case $k \ge 1$ follows by induction from the [[derivative of a convolution|9FN0PFZZXZ]], applied to the $C^{k-1}$ functions $\partial_j g$.
The case $k = \infty$ is the conjunction of all finite cases.

Example: $f = \mathbf{1}_{[0, 1]}$ is discontinuous on $\R$.
If $0 < \varepsilon < 1/2$ and $\varphi$ is a smooth function with support in $[-\varepsilon, \varepsilon]$ and integral $1$, then $f * \varphi$ is smooth, equals $1$ on $[\varepsilon, 1 - \varepsilon]$ and $0$ outside $[-\varepsilon, 1 + \varepsilon]$.

The smoothness comes only from $g$: if $g$ is merely continuous, $f * g$ need not be differentiable.
For $f = g = \mathbf{1}_{[0, 1]}$, neither factor is continuous, yet $f * g$ is the continuous tent function, which is not differentiable at $0$, $1$, $2$.

## Explanations

### L1 human

Averaging a rough function against a smooth bump produces a smooth function.
The result is at least as smooth as the bump, however rough the original function was.
This is how blurring removes sharp edges from a picture.

### L2 human

With a [[mollifier|CQMK4YPE1J]] $\varphi_\varepsilon$, the functions $f * \varphi_\varepsilon$ are smooth and tend to $f$ in $L^p$ as $\varepsilon \to 0$ when $f \in L^p$, $1 \le p < \infty$.
This is the standard way to approximate integrable or continuous functions by smooth ones.
It is used to prove density theorems, to define weak derivatives through smooth approximations, and to regularize distributions.
