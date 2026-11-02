---
tag: MM07SS0PB4
kind: definition
name: Borel functional calculus
msc: [47A60, 47B15]
defines: 92433H25TC
uses: [HM2HHE3J51, X71XRPJR7D, ATGT25E5FF, 0WQXY32Q8D, JB7S6WPZ77, BMKATJ802A]
sources:
  - url: https://en.wikipedia.org/wiki/Borel_functional_calculus
---

## Definition

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]], and let $N$ be a bounded normal operator on $H$ with [[spectrum|BMKATJ802A]] $\sigma(N)$.
Let $E$ be the [[projection-valued measure|ATGT25E5FF]] of $N$ given by the [[spectral theorem for bounded normal operators|X71XRPJR7D]], and write $E_{x,y}(B) = \ip{E(B) x}{y}$.
For a bounded [[Borel|0WQXY32Q8D]] measurable function $f \colon \sigma(N) \to \C$, let $f(N)$ be the unique bounded operator on $H$ with
$$\ip{f(N) x}{y} = \int_{\sigma(N)} f(\lambda) \, d E_{x,y}(\lambda) \quad \text{for all } x, y \in H.$$
The map $f \mapsto f(N)$, from the bounded Borel functions on $\sigma(N)$ to the bounded operators on $H$, is the *Borel functional calculus* of $N$.

## Remarks

The map $f \mapsto f(N)$ is linear and multiplicative, sends $\overline{f}$ to $f(N)^*$, and satisfies $\norm{f(N)} \le \sup_{\sigma(N)} \abs{f}$.
For $f(\lambda) = \lambda$ it gives $N$, and on continuous functions it agrees with the [[continuous functional calculus|JB7S6WPZ77]].
If $f_n \to f$ pointwise with $\sup_n \sup_{\sigma(N)} \abs{f_n} < \infty$, then $f_n(N) x \to f(N) x$ for every $x \in H$.
Example: for a Borel set $B$, the indicator function $1_B$ gives $1_B(N) = E(B)$, the spectral projection of $N$ for $B$.
For instance, if $N$ is the multiplication by $t$ on $L^2([0,1])$, then $f(N)$ is the multiplication by $f(t)$.
Non-example: let $N$ be the diagonal operator $N e_n = e_n / n$ on $\ell^2$, so $\sigma(N) = \set{1/n : n \ge 1} \cup \set{0}$.
The function $f(\lambda) = 1/\lambda$ for $\lambda \ne 0$, $f(0) = 0$, is Borel but not bounded, and the formula would give $f(N) e_n = n e_n$, which is not a bounded operator.
Changing $f$ on a set $B$ with $E(B) = 0$ does not change $f(N)$.
For unbounded self-adjoint operators, the same formula defines $f(A)$ for every bounded Borel function on $\R$, and for unbounded $f$ on a suitable dense domain.
