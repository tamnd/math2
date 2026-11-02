---
tag: KX2XY7S3X6
kind: statement
role: theorem
name: Spectral radius formula
msc: [47A10, 46H05]
uses: [06GZ956657, 03TM135G0N, 06EKW1AKXF, BMKATJ802A, J5YNNKSB9P, 8QJ91709V2, 3KX0KQ7V05, 9V7YQA85PC]
about: [BMKATJ802A]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_radius
    locator: Gelfand's formula
---

## Statement

Let $X \ne \set{0}$ be a complex [[Banach space|06GZ956657]], and let $T \colon X \to X$ be a [[continuous linear map|03TM135G0N]] with [[spectrum|BMKATJ802A]] $\sigma(T)$.
Then $\sigma(T)$ is nonempty and compact, and its *spectral radius* $r(T) = \max \set{\abs{\lambda} : \lambda \in \sigma(T)}$ satisfies
$$r(T) = \lim_{n \to \infty} \norm{T^n}^{1/n} = \inf_{n \ge 1} \norm{T^n}^{1/n},$$
where $\norm{\cdot}$ is the [[operator norm|06EKW1AKXF]].

## Remarks

Proof idea: if $\lambda \in \sigma(T)$, then $\lambda^n \in \sigma(T^n)$, and the [[Neumann series|8QJ91709V2]] shows $\abs{\lambda}^n \le \norm{T^n}$; this gives $r(T) \le \inf_n \norm{T^n}^{1/n}$.
For $\abs{\lambda} > \norm{T}$, the [[resolvent|J5YNNKSB9P]] has the expansion $R(\lambda, T) = -\sum_{n \ge 0} T^n / \lambda^{n+1}$.
The resolvent is analytic on $\abs{\lambda} > r(T)$, so this Laurent series converges there, and the uniform boundedness principle with the Cauchy estimates gives $\limsup_n \norm{T^n}^{1/n} \le r(T)$.
Nonemptiness of $\sigma(T)$ follows from Liouville's theorem applied to $\lambda \mapsto f(R(\lambda, T))$ for continuous linear functionals $f$.

Example: the Volterra operator $(Vf)(x) = \int_0^x f(t) \, dt$ on $C[0, 1]$ with the supremum norm satisfies $\norm{V^n} = 1/n!$, attained at $f = 1$.
So $r(V) = \lim (1/n!)^{1/n} = 0$ and $\sigma(V) = \set{0}$, although $V \ne 0$.

The field must be $\C$.
The rotation $T(x, y) = (-y, x)$ of the real plane has $\norm{T^n} = 1$ for all $n$, but $T - \lambda I$ is invertible for every real $\lambda$, so its real spectrum is empty.

For matrices this is [[Gelfand's formula|3KX0KQ7V05]] for the [[spectral radius|9V7YQA85PC]].
The same statement, with the same proof, holds for every element of a unital complex Banach algebra.

## Explanations

### L1 human

The spectral radius is the size of the largest point in the spectrum.
The formula says it can be read off from the norms of the powers $T^n$: these grow, or shrink, like $r(T)^n$.
So the long-run growth rate of $T^n$ is fixed by the spectrum, even though a single norm $\norm{T}$ can be much larger than $r(T)$.

### L2 human

The formula shows that $T^n \to 0$ in norm if and only if $r(T) < 1$, and that $\sum T^n$ converges in that case, which sharpens the Neumann series.
It also shows that $r(T)$ depends only on the algebra, not on the choice of an equivalent norm.
A quasinilpotent operator, with $r(T) = 0$, need not be nilpotent, as the Volterra operator shows.
For normal operators on a Hilbert space, $\norm{T^{2^k}} = \norm{T}^{2^k}$, so $r(T) = \norm{T}$; this is a key step in the theory of C*-algebras.
