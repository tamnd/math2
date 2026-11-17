---
tag: Z2JK9QHKWF
kind: example
name: The function f_ε0 is not provably total in PA
msc: ["03F30", "03F15"]
topics: [T6FK1E7GJ1]
audience: grad
not_instance_of:
  - target: Z742YPHPNS
    note: f_ε0 is total and computable, but it eventually dominates every function that PA proves total, so it is not provably total in PA
uses: [Z742YPHPNS, R6ZC4BJGXV, MPSCREYC3M, 0QFT7Z76N5]
sources:
  - url: https://en.wikipedia.org/wiki/Fast-growing_hierarchy
    locator: Points of interest
---

## Example

Let $f_\alpha$ be the [[fast-growing hierarchy|R6ZC4BJGXV]], with the fundamental sequence $\varepsilon_0[0] = 0$ and $\varepsilon_0[x + 1] = \omega^{\varepsilon_0[x]}$.
Then $f_{\varepsilon_0}(x) = f_{\varepsilon_0[x]}(x)$.

1. Small values: $\varepsilon_0[0] = 0$, $\varepsilon_0[1] = 1$ and $\varepsilon_0[2] = \omega$.
2. So $f_{\varepsilon_0}(0) = f_0(0) = 1$, $f_{\varepsilon_0}(1) = f_1(1) = 2$ and $f_{\varepsilon_0}(2) = f_\omega(2) = f_2(2) = 2^2 \cdot 2 = 8$.
3. $f_{\varepsilon_0}$ is total and computable, because each $f_\alpha(x)$ is computed by a terminating recursion on ordinal terms below $\varepsilon_0$.
4. **Cited lemma** (Wainer). Every function that $\mathsf{PA}$ proves total is eventually dominated by some $f_\alpha$ with $\alpha < \varepsilon_0$.
5. **Cited lemma** (domination in the hierarchy). For every $\alpha < \varepsilon_0$, $f_{\varepsilon_0}$ eventually dominates $f_\alpha$.
6. Suppose $f_{\varepsilon_0}$ were [[provably total|Z742YPHPNS]] in $\mathsf{PA}$. By step 4, some $\alpha < \varepsilon_0$ has $f_{\varepsilon_0}(x) < f_\alpha(x)$ for all large $x$.
7. By step 5, $f_\alpha(x) < f_{\varepsilon_0}(x)$ for all large $x$. Steps 6 and 7 contradict each other.
8. So $f_{\varepsilon_0}$ is not provably total in $\mathsf{PA}$.

## Remarks

The stronger theory $\mathsf{PA} + \mathrm{TI}(\varepsilon_0)$, with [[transfinite induction|0ZHQMQ2C1N]] up to $\varepsilon_0$, proves that $f_{\varepsilon_0}$ is total.
The same holds for [[Goodstein's theorem|XQMNJF241J]], whose length function grows at about the same rate.

## Explanations

### L1 human

The function $f_{\varepsilon_0}$ starts small: its values at $0$, $1$ and $2$ are $1$, $2$ and $8$.
From $3$ on it grows faster than any function that ordinary arithmetic can prove to be defined everywhere.
It is still a computable function, and stronger systems prove that it is total.

### L2 human

The argument has two cited facts: $\mathsf{PA}$-provably total functions sit below some $f_\alpha$, and $f_{\varepsilon_0}$ sits above every $f_\alpha$.
The typical use is as the standard yardstick: a function that dominates $f_{\varepsilon_0}$ is not provably total in $\mathsf{PA}$.
The trap: the values at small inputs say nothing about provability; only eventual growth matters.
