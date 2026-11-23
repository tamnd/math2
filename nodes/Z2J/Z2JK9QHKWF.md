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

The function $f_{\varepsilon_0}$ starts with the small values $1, 2, 8$, and yet $\mathsf{PA}$ cannot prove that it is defined everywhere.
Let $f_\alpha$ be the [[fast-growing hierarchy|R6ZC4BJGXV]] with $f_0(x) = x + 1$, $f_{\alpha+1}(x) = f_\alpha^x(x)$, and the fundamental sequence $\varepsilon_0[0] = 0$, $\varepsilon_0[x + 1] = \omega^{\varepsilon_0[x]}$.
Then $f_{\varepsilon_0}(x) = f_{\varepsilon_0[x]}(x)$.

1. The first terms of the fundamental sequence are
   $$\varepsilon_0[0] = 0, \qquad \varepsilon_0[1] = \omega^0 = 1, \qquad \varepsilon_0[2] = \omega^1 = \omega.$$
2. So $f_{\varepsilon_0}(0) = f_0(0) = 1$ and $f_{\varepsilon_0}(1) = f_1(1) = 2$.
   Also $f_{\varepsilon_0}(2) = f_\omega(2) = f_2(2) = 2 \cdot 2^2 = 8$.
3. $f_{\varepsilon_0}$ is total and computable, because each $f_\alpha(x)$ is computed by a terminating recursion on ordinal terms below $\varepsilon_0$.
4. **Cited lemma** (Wainer; Schwichtenberg).
   Every function that $\mathsf{PA}$ proves total is eventually dominated by some $f_\alpha$ with $\alpha < \varepsilon_0$.
5. **Cited lemma** (domination in the hierarchy).
   For every $\alpha < \varepsilon_0$, $f_{\varepsilon_0}$ eventually dominates $f_\alpha$.
6. Suppose $f_{\varepsilon_0}$ were [[provably total|Z742YPHPNS]] in $\mathsf{PA}$.
   By step 4, some $\alpha < \varepsilon_0$ has $f_{\varepsilon_0}(x) < f_\alpha(x)$ for all large $x$.
7. By step 5, $f_\alpha(x) < f_{\varepsilon_0}(x)$ for all large $x$, and this contradicts step 6.
8. So $f_{\varepsilon_0}$ is not provably total in $\mathsf{PA}$.

## Remarks

The example shows that the definition of "provably total" fails for a function that is perfectly computable.
The failure is in the theory, not in the function: $\mathsf{PA}$ plus [[transfinite induction|0ZHQMQ2C1N]] up to $\varepsilon_0$ proves that $f_{\varepsilon_0}$ is total, and so does $\mathsf{ZFC}$.

Lower the index and the function becomes provably total.
For each fixed $\alpha < \varepsilon_0$, $\mathsf{PA}$ proves that $f_\alpha$ is total, since it proves transfinite induction up to $\alpha$.
So $\varepsilon_0$ is the exact boundary for $\mathsf{PA}$, and it is the ordinal of [[Gentzen's consistency proof|QPV0HNP22S]] of 1936.
The length function of [[Goodstein's theorem|XQMNJF241J]] sits at the same boundary, and $\mathsf{PA}$ fails to prove it total for the same reason.

## Explanations

### L1 human

The function $f_{\varepsilon_0}$ starts small: its values at $0$, $1$ and $2$ are $1$, $2$ and $8$.
At $3$ the value is already far too large to write down, and from then on it grows faster than any function that ordinary arithmetic can prove to be defined everywhere.
It is still a computable function, and stronger systems prove that it is total.

### L2 human

We unfold $f_{\varepsilon_0}(3)$ by hand to see where the growth comes from.
First $\varepsilon_0[3] = \omega^{\varepsilon_0[2]} = \omega^\omega$, so $f_{\varepsilon_0}(3) = f_{\omega^\omega}(3)$.
Next $(\omega^\omega)[3] = \omega^3$, so $f_{\varepsilon_0}(3) = f_{\omega^3}(3)$, and then $(\omega^3)[3] = \omega^2 \cdot 3$.
Every limit step keeps the argument $3$, but every successor step iterates, and $f_{\omega}(3)$ alone is already $3 \cdot 2^{402653211}$.
The example shows the typical use of $f_{\varepsilon_0}$ as a yardstick: a function that eventually dominates it is not provably total in $\mathsf{PA}$.
The trap is to judge by small inputs, since only eventual growth matters for provability.
