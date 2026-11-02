---
tag: SRW9PD2RSA
kind: statement
role: theorem
name: Equioscillation theorem
msc: [41A50, 41A10, 41A52]
uses: [7N4988HN3P, YDN0T4MEX0, 1G0B73WPX8, XNPVW5Z126]
about: [7N4988HN3P]
sources:
  - url: https://en.wikipedia.org/wiki/Equioscillation_theorem
same_as:
  wikidata: Q5384549
  wikipedia: Equioscillation theorem
---

## Statement

Let $a < b$, let $f \colon [a, b] \to \R$ be continuous, and let $n \ge 0$.
Let $\mathcal{P}_n$ be the set of real [[polynomial functions|1G0B73WPX8]] of degree at most $n$, and let $\norm{g} = \max_{a \le x \le b} \abs{g(x)}$.
Then $p \in \mathcal{P}_n$ is a [[best approximation|7N4988HN3P]] of $f$ from $\mathcal{P}_n$ if and only if there are $n + 2$ points $a \le x_0 < x_1 < \cdots < x_{n+1} \le b$ and a sign $\sigma \in \set{-1, 1}$ with
$$f(x_i) - p(x_i) = \sigma (-1)^i \norm{f - p} \quad \text{for } i = 0, 1, \dots, n + 1.$$
Moreover, the best approximation from $\mathcal{P}_n$ exists and is unique.

## Remarks

The idea of the proof: if the error $e = f - p$ alternates at $n + 2$ points with full size $\norm{e}$, the [[de la Vallée Poussin lower bound|XNPVW5Z126]] gives $E_n(f) \ge \norm{e}$, so $p$ is best.
Conversely, suppose $e$ has fewer than $n + 2$ alternation points.
Then one can split $[a, b]$ into at most $n + 1$ pieces on which the extreme values of $e$ have one sign.
A polynomial $q$ of degree at most $n$ with the same sign pattern then makes $\norm{f - p - t q} < \norm{e}$ for small $t > 0$.
Uniqueness follows: if $p_1, p_2$ are best, then $(p_1 + p_2)/2$ is best, and at its $n + 2$ alternation points $p_1 = p_2$, so $p_1 - p_2$ has $n + 2$ zeros.

Example: for $f(x) = x^2$ on $[0, 1]$ and $n = 1$, the line $p(x) = x - 1/8$ is the best approximation.
The error $x^2 - x + 1/8$ takes the values $1/8, -1/8, 1/8$ at $0, 1/2, 1$, which is $n + 2 = 3$ alternating extreme values, and $\norm{f - p} = 1/8$, so the [[error of best approximation|YDN0T4MEX0]] is $E_1(f) = 1/8$.
Another example: the monic polynomial of degree $n + 1$ of least norm on $[-1, 1]$ is $2^{-n} T_{n+1}$, where $T_{n+1}$ is the [[Chebyshev polynomial|M6EAR1JHPP]], because $T_{n+1}$ attains $\pm 1$ alternately at $n + 2$ points.

## Explanations

### L1 human

The best polynomial approximation in the uniform sense is recognized by the shape of its error curve.
The error must reach its largest size $n + 2$ times, with alternating signs, like a wave of constant height.
If the error had fewer such peaks, you could tilt the polynomial a little and lower all the peaks at once.

### L2 human

The theorem, due to Chebyshev, is the main characterization of minimax approximation by polynomials.
It is the basis of the Remez algorithm, which moves a set of $n + 2$ reference points until the error equioscillates.
It holds in the same form when $\mathcal{P}_n$ is replaced by any Haar subspace of dimension $n + 1$ on $[a, b]$.
It also gives the extremal property of Chebyshev polynomials and many sharp constants in approximation theory.
