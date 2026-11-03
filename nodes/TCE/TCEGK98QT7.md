---
tag: TCEGK98QT7
kind: definition
name: Inequalities in information theory
msc: [94A17, 94A15]
defines: 836E9NPN42
uses: [0X2J0VY6DN, 0DR81R1F2B, DZWEWHZ20N, A83CYGDXFG, PW6PXZ2WV4]
sources:
  - url: https://en.wikipedia.org/wiki/Inequalities_in_information_theory
---

## Definition

Let $n \ge 1$, and let $N = \set{1, \dots, n}$.
Let $X_1, \dots, X_n$ be [[discrete random variables|0X2J0VY6DN]] with finitely many values on a common probability space.
For a nonempty set $\alpha \subseteq N$, let $H(X_\alpha)$ be the [[joint entropy|DZWEWHZ20N]] of the family $(X_i)_{i \in \alpha}$.
Let $c_\alpha$ be real numbers, one for each nonempty $\alpha \subseteq N$.
The inequality
$$\sum_{\emptyset \ne \alpha \subseteq N} c_\alpha \, H(X_\alpha) \ge 0$$
is a *linear information inequality* on $n$ random variables if it holds for every such family $X_1, \dots, X_n$.
Here the [[joint law|0DR81R1F2B]] of the family is arbitrary.

## Remarks

Every [[mutual information|A83CYGDXFG]] and [[conditional mutual information|PW6PXZ2WV4]] is a linear combination of joint entropies.
The *basic* (or Shannon) inequalities are $H(X_\alpha) \ge 0$, $H(X_\alpha \mid X_\beta) \ge 0$, $I(X_\alpha; X_\beta) \ge 0$ and $I(X_\alpha; X_\beta \mid X_\gamma) \ge 0$.
An information inequality is *of Shannon type* when it is a non-negative linear combination of basic inequalities.

Example: $H(X_1) + H(X_2) - H(X_1, X_2) \ge 0$ is an information inequality on $2$ random variables, since its left side is $I(X_1; X_2)$.

Non-example: $H(X_1, X_2) - H(X_1) - H(X_2) \ge 0$ is not an information inequality: it fails for $X_1 = X_2$ a fair bit, where the left side is $1 - 2 = -1$ bit.

In geometric terms, the vectors $(H(X_\alpha))_\alpha \in \R^{2^n - 1}$ form a set $\Gamma_n^*$, and the information inequalities are the linear inequalities valid on it, so on the closed convex cone $\overline{\Gamma_n^*}$.
The Shannon-type inequalities cut out a polyhedral cone $\Gamma_n$ that contains it.
For $n \le 3$ the two cones agree, while for $n \ge 4$ the [[Zhang–Yeung inequality|Y39WB3892W]] shows that they differ.

## Explanations

### L1 human

An information inequality is a rule about the entropies of a collection of random variables that holds for every possible joint law.
