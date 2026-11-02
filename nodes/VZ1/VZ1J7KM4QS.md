---
tag: VZ1J7KM4QS
kind: statement
role: theorem
name: Akra–Bazzi theorem
msc: [68W40, 39A22]
uses: [0TGV80E6A4, 0FYX44GP92]
about: [0FYX44GP92]
sources:
  - url: https://en.wikipedia.org/wiki/Akra%E2%80%93Bazzi_method
---

## Statement

Let $k \ge 1$, and let $a_1, \dots, a_k > 0$ and $0 < b_1, \dots, b_k < 1$ be real constants.
Let $g \colon [1, \infty) \to [0, \infty)$ satisfy the polynomial growth condition: there are constants $c_1, c_2 > 0$ such that $c_1 g(x) \le g(u) \le c_2 g(x)$ for all $x \ge 1$, all $i$ and all $u \in [b_i x, x]$.
Let $h_1, \dots, h_k$ be real functions with $\abs{h_i(x)} = O(x / (\log x)^2)$, in [[big O notation|0TGV80E6A4]].
Let $x_0$ be large enough, and let $T \colon [1, \infty) \to \R$ be positive and bounded above and below by positive constants on $[1, x_0]$, and satisfy the recurrence
$$T(x) = g(x) + \sum_{i=1}^{k} a_i\, T\big(b_i x + h_i(x)\big) \qquad (x > x_0).$$
Let $p$ be the unique real number with $\sum_{i=1}^{k} a_i b_i^p = 1$.
Then
$$T(x) = \Theta\left( x^p \left( 1 + \int_1^x \frac{g(u)}{u^{p+1}}\, du \right) \right),$$
where $f(x) = \Theta(F(x))$ means that $c F(x) \le f(x) \le C F(x)$ for some constants $0 < c \le C$ and all large $x$.

## Remarks

The number $p$ exists and is unique because $s \mapsto \sum a_i b_i^s$ is continuous and strictly decreasing, with limits $\infty$ and $0$.
The proof is by induction on $x$: one guesses the bound with suitable constants and checks that the recurrence preserves it.
The growth condition on $g$ is used to compare $g$ at $b_i x$ and at $x$.
The perturbations $h_i$ cover floors and ceilings, such as $T(\lceil x/2 \rceil)$, which appear in real algorithms.
Example: for $T(x) = T(x/3) + T(2x/3) + x$, one has $p = 1$ since $1/3 + 2/3 = 1$, and $\int_1^x u/u^2\, du = \log x$, so $T(x) = \Theta(x \log x)$.
The growth condition on $g$ is needed.
For $T(x) = T(x/2) + 2^x$, one has $p = 0$, and the formula would give the order $2^x / x$, since $\int_1^x 2^u u^{-1}\, du$ grows like $2^x/(x \log 2)$; but $T(x) \ge 2^x$.
Here $g(x) = 2^x$ fails the growth condition, as $g(x)/g(x/2) = 2^{x/2}$ is unbounded.

## Explanations

### L1 human

Divide-and-conquer algorithms split a problem of size $x$ into smaller pieces of sizes $b_i x$, solve them, and pay $g(x)$ to split and combine.
Their running time satisfies a recurrence like the one above.
The theorem gives the order of growth of the running time directly, without solving the recurrence.
For merge sort, $T(x) = 2 T(x/2) + x$ gives $p = 1$ and $T(x) = \Theta(x \log x)$.

### L2 human

The theorem generalizes the master theorem of algorithm analysis, which handles only equal subproblem sizes $T(x) = a T(x/b) + g(x)$.
Here the pieces may have different sizes $b_i x$, and small perturbations $h_i$ are allowed.
To use it, first solve $\sum a_i b_i^p = 1$ for $p$, then compute the integral of $g(u)/u^{p+1}$.
If $g(x) = x^q$ with $q < p$, the integral stays bounded and $T = \Theta(x^p)$; if $q = p$, one gets $\Theta(x^p \log x)$; if $q > p$, one gets $\Theta(x^q)$.
In Mathlib a version is `AkraBazziRecurrence.isTheta_asympBound`.
