---
tag: YPTNBRWRY7
kind: conjecture
name: Baker–Gammel–Wills conjecture
msc: [41A21, "30E10"]
uses: [1F16G4V64X, MDM8F48X18, 0ZZ7ZYDR8W, 066E7PJCYE, 08VZ57PT26]
about: [1F16G4V64X]
sources:
  - url: https://en.wikipedia.org/wiki/Pad%C3%A9_approximant
history:
  posed_by: "George A. Baker, John L. Gammel and J. G. Wills"
  first_stated: "1961"
---

## Statement

Let $D = \set{z \in \C : \abs{z} < 1}$ be the unit disc.
Let $f$ be a [[meromorphic function|0ZZ7ZYDR8W]] on $D$ that is analytic at $0$, and let $P$ be its set of [[poles|066E7PJCYE]] in $D$.
Let $[n/n]_f$ be the diagonal [[Padé approximants|1F16G4V64X]] of $f$ at $0$.
Then there is an infinite sequence $n_1 < n_2 < \cdots$ such that $[n_j/n_j]_f$ converges to $f$ [[uniformly|08VZ57PT26]] on every compact subset of $D \setminus P$.

## Remarks

The conjecture is false in this generality.
In 2003 D. S. Lubinsky published a counterexample built from the Rogers–Ramanujan continued fraction.
Convergence of the full diagonal fails in general, because the approximants can have spurious poles that wander through the disc; this is why the conjecture only asks for a subsequence.
A weaker form holds: for functions meromorphic in the whole plane, the diagonal sequence converges in logarithmic capacity (the Nuttall–Pommerenke theorem).
For columns of the [[Padé table|MDM8F48X18]] with a fixed number of poles, [[Montessus de Ballore's theorem|XQQWP9ZPEW]] gives uniform convergence.

## Explanations

### L1 human

Diagonal Padé approximants, with equal degrees of numerator and denominator, are the most used rational approximations to a power series.
They often converge very well in practice, but sometimes an approximant has an unwanted pole in a bad place.
The conjecture predicted that one can always skip the bad approximants and keep infinitely many good ones that converge uniformly.
This turned out to be false, although convergence holds in a weaker averaged sense.
