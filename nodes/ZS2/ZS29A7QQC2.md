---
tag: ZS29A7QQC2
kind: statement
role: proposition
name: Support of a convolution
msc: [44A35, 42A85]
uses: [2Z29JN3VES, 0R6EWFKRCF, XNBN31HQWB]
about: [2Z29JN3VES]
sources:
  - url: https://en.wikipedia.org/wiki/Convolution
---

## Statement

Let $n \ge 1$, and let $f, g \colon \R^n \to \C$ be continuous functions with compact supports $\operatorname{supp} f$ and $\operatorname{supp} g$.
Here the support of a function is the closure of the set where it is not $0$.
Then the [[convolution|2Z29JN3VES]] $f * g$ is continuous, and
$$\operatorname{supp}(f * g) \subseteq \operatorname{supp} f + \operatorname{supp} g = \set{a + b : a \in \operatorname{supp} f, \ b \in \operatorname{supp} g}.$$
In particular $f * g$ has compact support.

## Remarks

If $(f * g)(x) = \int f(y) g(x - y) \, dy \ne 0$, then $f(y) g(x - y) \ne 0$ for some $y$.
So $y \in \operatorname{supp} f$ and $x - y \in \operatorname{supp} g$, and $x = y + (x - y)$ lies in the [[sumset|XNBN31HQWB]] $\operatorname{supp} f + \operatorname{supp} g$.
This sumset is the image of the [[compact set|0R6EWFKRCF]] $\operatorname{supp} f \times \operatorname{supp} g$ under the continuous map $(a, b) \mapsto a + b$, so it is compact and hence closed, and it contains the closure of $\set{f * g \ne 0}$.

Example: if $f$ and $g$ are continuous, positive on $(0, 1)$ and zero elsewhere, then $f * g$ is positive exactly on $(0, 2)$, and $\operatorname{supp}(f * g) = [0, 2] = [0, 1] + [0, 1]$.

The inclusion can be strict, because of cancellation in the integral.
Let $\varphi$ be continuous, positive on $(0, 1)$ and zero elsewhere, and put $\psi = \varphi * \varphi$, supported on $[0, 2]$.
For $f(x) = \varphi(x) - \varphi(x - 2)$ and $g(x) = \varphi(x) + \varphi(x - 2)$ the cross terms cancel and $f * g(x) = \psi(x) - \psi(x - 4)$.
So $\operatorname{supp}(f * g) = [0, 2] \cup [4, 6]$, while $\operatorname{supp} f + \operatorname{supp} g = [0, 6]$.
For integrable functions the same statement holds with essential supports, in the form $\operatorname{supp}(f * g) \subseteq \overline{\operatorname{supp} f + \operatorname{supp} g}$.

## Explanations

### L1 human

If $f$ lives on a set $A$ and $g$ lives on a set $B$, then $f * g$ lives on the set of all sums $a + b$.
For instance, two bumps on $[0, 1]$ give a bump on $[0, 2]$.
So convolution can spread a function out, but only by a controlled amount.

### L2 human

This is why convolution with a [[mollifier|CQMK4YPE1J]] supported in a ball of radius $\varepsilon$ moves the support of a function by at most $\varepsilon$.
Together with [[smoothing by convolution|4P7KPA3Y7R]] it shows that smooth functions with compact support are dense in $L^p$ for $1 \le p < \infty$.
On the line, the [[Titchmarsh convolution theorem|WGY75H4VWW]] gives an equality for the convex hulls of the supports.
