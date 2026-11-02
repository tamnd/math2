---
tag: HDFM8ZY7XG
kind: statement
role: theorem
name: Bernstein's theorem on inverse approximation
msc: [41A27, 42A10, 41A17]
uses: [F0YGC89S9R, J3NJQ5FZJ5, 012PBA0FMD, YDN0T4MEX0]
about: [TDKKST5AWA]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein%27s_theorem_(approximation_theory)
same_as:
  wikidata: Q4894565
  wikipedia: Bernstein's theorem (approximation theory)
---

## Statement

Let $f \colon \R \to \C$ be continuous and $2\pi$-periodic, let $r \ge 0$ be an integer, and let $0 < \alpha < 1$.
For $n \ge 1$, let $E_n(f)$ be the uniform distance from $f$ to the [[trigonometric polynomials|J3NJQ5FZJ5]] of degree at most $n$.
Assume that there is a constant $M$ with $E_n(f) \le M n^{-(r + \alpha)}$ for all $n \ge 1$.
Then $f$ has $r$ continuous derivatives, and $f^{(r)}$ is [[Hölder continuous|012PBA0FMD]] with exponent $\alpha$.

## Remarks

Proof idea: let $T_k$ be a best approximation of degree $2^k$ and write $f = T_0 + \sum_{k \ge 0} (T_{k+1} - T_k)$.
Each block $T_{k+1} - T_k$ has degree at most $2^{k+1}$ and size $O(2^{-k(r + \alpha)})$.
[[Bernstein's inequality|F0YGC89S9R]] bounds its $j$-th derivative by $O(2^{k(j - r - \alpha)})$, so the series of $r$-th derivatives converges uniformly.
Splitting the sum at $2^k \approx 1/\abs{x - y}$ gives the Hölder bound for $f^{(r)}$.

Example: if $E_n(f) \le M n^{-1/2}$ for all $n$, then $\abs{f(x) - f(y)} \le M' \abs{x - y}^{1/2}$.

The hypothesis $\alpha < 1$ is necessary.
For $\alpha = 1$ and $r = 0$, the condition $E_n(f) = O(1/n)$ does not imply that $f$ is Lipschitz.
It characterises the larger Zygmund class, defined by $\abs{f(x + h) - 2f(x) + f(x - h)} = O(h)$.

## Explanations

### L1 human

If a function can be approximated very well by trigonometric polynomials of low degree, it must be smooth.
The faster the error goes down, the more derivatives the function has.
This is the reverse of Jackson's inequality.

### L2 human

With Jackson's inequality it gives a two-way bridge: for $0 < \alpha < 1$, $E_n(f) = O(n^{-r-\alpha})$ exactly when $f^{(r)}$ is Hölder continuous with exponent $\alpha$.
So smoothness can be read off from approximation rates, which is the starting point of approximation spaces and Besov spaces.
The same telescoping argument over dyadic degrees appears in wavelet and Littlewood–Paley theory.
