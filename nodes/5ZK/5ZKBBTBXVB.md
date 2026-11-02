---
tag: 5ZKBBTBXVB
kind: definition
name: Log-gamma function
msc: [33B15]
defines: JT95B44G4G
uses: [0V3FZMVB4K, 0NAHXR1FRH, 04DXAFN2ES]
sources:
  - url: https://en.wikipedia.org/wiki/Gamma_function
---

## Definition

Let $\Gamma$ be the [[gamma function|0V3FZMVB4K]], holomorphic and without zeros on $\C \setminus \set{0, -1, -2, \ldots}$, and let $D = \C \setminus (-\infty, 0]$.
The *log-gamma function* is the unique [[holomorphic function|0NAHXR1FRH]] $\operatorname{Log}\Gamma \colon D \to \C$ such that:

1. $e^{\operatorname{Log}\Gamma(z)} = \Gamma(z)$ for every $z \in D$;
2. $\operatorname{Log}\Gamma(x)$ is real for every real $x > 0$.

On $(0, \infty)$ it equals the real function $x \mapsto \ln\Gamma(x)$, with $\ln$ the [[natural logarithm|04DXAFN2ES]].

## Remarks

Existence: $D$ is simply connected and $\Gamma$ has no zeros on $D$, so $\Gamma$ has a holomorphic logarithm on $D$.
This logarithm is unique up to adding $2\pi i k$, and condition 2 fixes $k$.
Example: $\operatorname{Log}\Gamma(3) = \ln 2$, which is real, and $e^{\ln 2} = 2 = \Gamma(3)$.
Non-example: the composition $z \mapsto \operatorname{Log}(\Gamma(z))$ with the principal logarithm satisfies condition 1 but is not continuous on $D$.
The reason is that the argument of $\Gamma(x + iy)$ grows without bound as $y \to \infty$, so $\Gamma(z)$ crosses the negative real axis.
The functional equation becomes $\operatorname{Log}\Gamma(z + 1) = \operatorname{Log}\Gamma(z) + \operatorname{Log} z$ on $D$.
Its derivative is the digamma function $\psi = \Gamma'/\Gamma$.

## Explanations

### L1 human

The log-gamma function is the logarithm of the gamma function, chosen so that it is smooth and real on the positive axis.
