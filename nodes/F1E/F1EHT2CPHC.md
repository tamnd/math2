---
tag: F1EHT2CPHC
kind: object
name: Feigenbaum constants
msc: ["37E20", "37E05", "37G15"]
uses: [NQDTTZ59X8, QN9X9BNKTX]
sources:
  - url: https://en.wikipedia.org/wiki/Feigenbaum_constants
same_as:
  wikidata: Q673184
  wikipedia: Feigenbaum constants
---

## Description

The Feigenbaum constants are two real numbers that describe the cascade of [[period-doubling bifurcations|NQDTTZ59X8]] of a one-parameter family of unimodal maps with a quadratic maximum.
Let $f_r$ be such a family, for example the [[logistic map|QN9X9BNKTX]] $f_r(x) = r x (1 - x)$.
Let $r_n$ be the parameter at which the attracting orbit of period $2^{n-1}$ loses stability and an attracting orbit of period $2^n$ appears.
For the logistic map $r_1 = 3$ and $r_2 = 1 + \sqrt 6 \approx 3.4495$.
The first Feigenbaum constant is
$$\delta = \lim_{n \to \infty} \frac{r_n - r_{n-1}}{r_{n+1} - r_n} = 4.669201609\ldots.$$
Let $c$ be the critical point, and let $R_n$ be the parameter, between $r_n$ and $r_{n+1}$, at which $c$ is periodic of least period $2^n$.
Let $d_n = f_{R_n}^{2^{n-1}}(c) - c$, the signed distance from $c$ to the point of its orbit halfway around the cycle.
The second Feigenbaum constant is
$$\alpha = \lim_{n \to \infty} \abs{\frac{d_n}{d_{n+1}}} = 2.502907875\ldots.$$

## Remarks

Check for the logistic map: the period-$2$ orbit is stable while $\abs{(f_r^2)'} < 1$ on it, and solving gives $r_2 = 1 + \sqrt 6$; the parameters $r_n$ accumulate at $r_\infty \approx 3.5699$.
The ratios $d_n / d_{n+1}$ alternate in sign, which is why $\alpha$ is often given as $-2.5029\ldots$.
The constants are universal: they take the same values for every smooth family of unimodal maps with a nondegenerate quadratic maximum that has such a cascade.
Feigenbaum explained this by a renormalization operator acting on maps of the interval, with a fixed point whose unstable eigenvalue is $\delta$ and whose scaling factor is $\alpha$.
Lanford gave a computer-assisted proof of the existence of this fixed point in 1982.
It is not known whether $\delta$ or $\alpha$ is irrational.

## Explanations

### L1 human

When a parameter is turned up, many systems double their period again and again: a cycle of $2$, then $4$, $8$, and so on, until chaos.
The gaps between these doublings shrink, each about $4.669$ times smaller than the one before.
The same number appears for dripping taps, electronic circuits and many simple formulas, which made it a surprise when Feigenbaum found it in the 1970s.
