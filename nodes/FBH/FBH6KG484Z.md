---
tag: FBH6KG484Z
kind: statement
role: theorem
name: Carleson's theorem
msc: [42A20, 42B25]
uses: [SASP14MA1Z, G12KXDHPPS, 5NN2YZZR3V, RARTMA0ZEC]
about: [G12KXDHPPS, V6Q24CHJG8]
sources:
  - url: https://en.wikipedia.org/wiki/Carleson%27s_theorem
same_as:
  wikidata: Q5041174
  wikipedia: Carleson's theorem
---

## Statement

Let $f \colon \R \to \C$ be a $2\pi$-periodic function that is square integrable on $[-\pi, \pi]$, that is, $f \in L^2(\mathbb{T})$ (see [[Lp space|SASP14MA1Z]]).
For $k \in \Z$ let $\hat f(k) = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) e^{-ikt} \, dt$ be its [[Fourier coefficients|5NN2YZZR3V]].
For $N \ge 0$ let $S_N f(x) = \sum_{k=-N}^{N} \hat f(k) e^{ikx}$ be the partial sums of its [[Fourier series|G12KXDHPPS]].
Then $S_N f(x) \to f(x)$ as $N \to \infty$ for [[almost every|RARTMA0ZEC]] $x \in \R$.

## Remarks

The proof reduces the theorem to an estimate for the maximal operator $Cf(x) = \sup_N \abs{S_N f(x)}$, namely that it is of weak type $(2, 2)$.
Convergence holds at every point for trigonometric polynomials, which are dense in $L^2(\mathbb{T})$, and the maximal estimate passes it to all of $L^2(\mathbb{T})$.
Carleson proved the maximal estimate in 1966 by a delicate decomposition of the function in time and frequency.
Later proofs were given by Fefferman and by Lacey and Thiele.

The theorem settles a conjecture of Lusin.
Since continuous periodic functions are square integrable, the Fourier series of a continuous function converges almost everywhere, although it can [[diverge at a point|FPDWWD12FE]].
The [[Kahane–Katznelson theorem|42DDDZHP7F]] shows that "almost everywhere" cannot be improved, even for continuous functions.
Square integrability cannot be weakened to integrability: [[Kolmogorov's example|25V2MHPHZ7]] is an integrable function whose Fourier series diverges everywhere.

## Explanations

### L1 human

The Fourier series of a periodic function is an infinite sum of waves meant to rebuild the function.
For a long time it was unknown whether this sum gives back the function at most points, even for continuous functions.
Carleson's theorem says yes for every square-integrable function: the sum converges to the right value except on a set of length zero.

### L2 human

Convergence in the $L^2$ norm follows from Parseval's identity and is easy.
Pointwise convergence is much harder because it needs control of all partial sums at once, through the Carleson maximal operator.
[[Hunt's extension|NAX51M6025]] proves the same for $L^p$ with $1 < p < \infty$.
The time-frequency methods behind the proof became a central tool of modern harmonic analysis.
