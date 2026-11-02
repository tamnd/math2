---
tag: XQQWP9ZPEW
kind: statement
role: theorem
name: Montessus de Ballore's theorem
msc: [41A21, "30E10"]
uses: [1F16G4V64X, 0ZZ7ZYDR8W, 066E7PJCYE, 08VZ57PT26]
about: [1F16G4V64X]
sources:
  - url: https://en.wikipedia.org/wiki/Pad%C3%A9_approximant
---

## Statement

Let $R > 0$ and let $n \ge 1$ be an integer.
Let $f$ be a [[meromorphic function|0ZZ7ZYDR8W]] on the disc $D = \set{z \in \C : \abs{z} < R}$ that is analytic at $0$ and has exactly $n$ [[poles|066E7PJCYE]] in $D$, counted with multiplicity.
Let $P$ be the set of these poles.
Let $[m/n]_f$ be the [[Padé approximant|1F16G4V64X]] of $f$ at $0$ with numerator degree at most $m$ and denominator degree at most $n$.
Then:

1. as $m \to \infty$, $[m/n]_f$ converges to $f$ [[uniformly|08VZ57PT26]] on every compact subset of $D \setminus P$;
2. for $m$ large, $[m/n]_f$ has exactly $n$ poles counted with multiplicity, and as $m \to \infty$ they converge to the poles of $f$, each with its multiplicity.

## Remarks

The idea of the proof: let $Q(z) = \prod_{p \in P} (z - p)$, so that $Qf$ is analytic on $D$.
The denominators $q_m$ of $[m/n]_f$ are determined by $n$ linear conditions on the Taylor coefficients of $f$ of high order.
The asymptotics of these coefficients are dominated by the poles in $P$, and one shows that $q_m \to Q$ after normalization, at a geometric rate.
Then $q_m f - p_m$ is small by construction, and dividing by $q_m$ gives the convergence away from $P$.
Example: $f(z) = e^z / (1 - z)$ has exactly one pole in every disc of radius $R > 1$.
So the column $[m/1]_f$ converges to $f$ on compact subsets of $\C \setminus \set{1}$, and the pole of $[m/1]_f$ tends to $1$.
The hypothesis that the number of poles equals $n$ matters.
With fewer poles the approximants may have spurious poles, and with more poles a denominator of degree $n$ cannot capture them all.
The theorem was proved by Robert de Montessus de Ballore in 1902.

## Explanations

### L1 human

A Taylor polynomial cannot see beyond the first pole of a function: it converges only in a disc that stops there.
Suppose the function has exactly $n$ poles in a larger disc, and the approximations may have $n$ poles.
Then the Padé approximants find those poles and converge in the whole larger disc.
So rational approximation extends the reach of power series past their singularities.

### L2 human

This is the basic convergence theorem for columns of the [[Padé table|MDM8F48X18]], where the denominator degree is fixed and the numerator degree grows.
It gives a practical way to locate the poles of a function from its Taylor coefficients, as the limits of the poles of the approximants.
For diagonal sequences $[n/n]_f$, where both degrees grow, convergence is much harder; uniform convergence can fail, which is the subject of the [[Baker–Gammel–Wills conjecture|YPTNBRWRY7]].
