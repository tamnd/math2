---
tag: ZMRFSYVWQT
kind: statement
role: theorem
name: Bieberbach conjecture
msc: [30C50, 30C55]
uses: [R91E83SDBD, EZQFWKF03Q, 51G4QJZ345]
about: [R91E83SDBD]
sources:
  - url: https://en.wikipedia.org/wiki/De_Branges%27s_theorem
same_as:
  wikidata: Q857089
  wikipedia: De Branges's theorem
---

## Statement

Let $f$ be a [[univalent function|R91E83SDBD]] on the unit disc $\mathbb{D}$ with $f(0) = 0$ and $f'(0) = 1$, and write
$$f(z) = z + \sum_{n=2}^{\infty} a_n z^n, \qquad \abs{z} < 1.$$
Then $\abs{a_n} \le n$ for every $n \ge 2$.
If $\abs{a_n} = n$ for some $n \ge 2$, then $f(z) = e^{-i\theta} k(e^{i\theta} z)$ for some $\theta \in \R$, where $k(z) = z/(1-z)^2$ is the [[Koebe function|EZQFWKF03Q]].

## Remarks

Bieberbach proved the case $n = 2$ and stated the general bound as a conjecture.
Loewner proved the case $n = 3$ with his [[differential equation|51G4QJZ345]].
Louis de Branges proved the full statement, which is therefore also called de Branges's theorem.
The conjecture was known to follow from the Robertson conjecture on odd univalent functions, which in turn follows from the Milin conjecture on the logarithmic coefficients of $f$.
De Branges proved the Milin conjecture, using the Loewner equation and an inequality on sums of Jacobi polynomials that had been proved by Askey and Gasper.
The bound is sharp for every $n$ at once, because the Koebe function has $a_n = n$.

## Explanations

### L1 human

Normalise a univalent function on the unit disc so that it starts like $z$.
The theorem says that its $n$-th Taylor coefficient has absolute value at most $n$.
The Koebe function, which maps the disc onto the plane minus a slit, is the extreme case with coefficients exactly $n$.

### L2 human

The case $n = 2$, Bieberbach's inequality $\abs{a_2} \le 2$, is a short consequence of the [[Grönwall area theorem|BYZDAZNHP4]] and implies the [[Koebe quarter theorem|WX0HMW4GT7]] and the distortion theorems.
For larger $n$ the problem resisted for a long time, and partial results such as $\abs{a_n} < e\,n$ and the proofs for small $n$ produced many methods of univalent function theory.
The final proof goes through the stronger Milin inequality and the [[Loewner equation|51G4QJZ345]].
