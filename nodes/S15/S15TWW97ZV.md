---
tag: S15TWW97ZV
kind: conjecture
name: Bochner–Riesz conjecture
msc: [42B15, 42B08]
uses: [AFS2DCWCD3, DPVM34ADZV, SASP14MA1Z, ZQEFCY61T7, CG9JEATW3Q]
about: [AFS2DCWCD3]
sources:
  - url: https://en.wikipedia.org/wiki/Bochner%E2%80%93Riesz_mean
history:
  posed_by: "Salomon Bochner"
  first_stated: "1936"
  notes: "Bochner introduced these means in 1936 to study spherical summation of Fourier integrals; the sharp conjecture arose later from the necessary condition found by Herz and has no single documented originator, so the attribution is to the earliest known source. Carleson and Sjölin proved the case n = 2 in 1972."
---

## Statement

Let $n \ge 2$, let $\delta > 0$ and let $1 \le p \le \infty$.
For a [[Schwartz function|CG9JEATW3Q]] $f$ on $\R^n$, let $S^\delta f$ be the function whose [[Fourier transform|DPVM34ADZV]] is
$$\widehat{S^\delta f}(\xi) = (1 - \abs{\xi}^2)_+^\delta \, \hat f(\xi),$$
where $t_+ = \max(t, 0)$.
Then $S^\delta$ extends to a bounded operator on [[$L^p(\R^n)$|SASP14MA1Z]] if and only if
$$\abs{\frac{1}{p} - \frac{1}{2}} < \frac{2\delta + 1}{2n}.$$

## Remarks

The operator $S^\delta$ is the [[Bochner–Riesz mean|AFS2DCWCD3]] of order $\delta$ at radius $1$.
By scaling, the bound for radius $1$ gives the same bound for every radius $R > 0$.
So the conjecture describes the pairs $(\delta, p)$ for which $S^\delta_R f \to f$ in $L^p$ as $R \to \infty$.
It says exactly which [[Fourier multipliers|ZQEFCY61T7]] $(1 - \abs{\xi}^2)_+^\delta$ are bounded on $L^p$.

The condition is known to be necessary.
The kernel of $S^\delta$ decays like $\abs{x}^{-(n+1)/2 - \delta}$ and no faster, so it lies in $L^p$ only for $p > 2n/(n + 1 + 2\delta)$.
This range, together with its dual range for $p' = p/(p-1)$, is exactly the stated condition.
For $\delta > (n-1)/2$ the kernel is integrable, and $S^\delta$ is bounded on every $L^p$.
For $p = 2$ every $\delta \ge 0$ works, by Plancherel's theorem.

Status: the conjecture holds for $n = 2$, a theorem of Carleson and Sjölin.
It is open for every $n \ge 3$, with partial ranges of $p$ known.
For $\delta = 0$, the ball multiplier, Fefferman proved that $S^0$ is unbounded on $L^p(\R^n)$ for every $p \ne 2$ and $n \ge 2$.
His proof uses a [[Kakeya set|6PEN7AKC7M]] construction, which shows the link with Kakeya problems.
The Bochner–Riesz conjecture is known to imply the [[restriction conjecture|9CE11G48JY]].

## Explanations

### L1 human

To rebuild a function from its frequencies, one keeps the frequencies inside a ball and fades them out near the edge of the ball.
The number $\delta$ measures how smooth the fade is.
A smoother fade gives a better-behaved operator.
The conjecture says exactly how smooth the fade must be for the operator to be bounded in the $L^p$ norm.
In the plane the answer is known, and in higher dimensions it is a major open problem.
