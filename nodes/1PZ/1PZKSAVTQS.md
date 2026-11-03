---
tag: 1PZKSAVTQS
kind: statement
role: theorem
name: Routh–Hurwitz theorem
msc: [26C10, 30C15, 93D20]
uses: [019MA1VTR2, 1G0B73WPX8, KJF8Y19BNV, Y631JTMMT5]
about: [019MA1VTR2]
sources:
  - url: https://en.wikipedia.org/wiki/Routh%E2%80%93Hurwitz_theorem
same_as:
  wikidata: Q4455015
  wikipedia: Routh–Hurwitz theorem
---

## Statement

Let $p(s) = a_0 s^n + a_1 s^{n-1} + \cdots + a_n$ be a real [[polynomial|1G0B73WPX8]] of degree $n \ge 1$ with $a_0 > 0$, and put $a_k = 0$ for $k > n$.
The *Routh array* of $p$ has rows $r_0, r_1, \ldots, r_n$, where row $r_k$ is a sequence $(r_{k,0}, r_{k,1}, \ldots)$:

1. $r_{0,j} = a_{2j}$ and $r_{1,j} = a_{2j+1}$ for $j \ge 0$;
2. for $k \ge 2$, if $r_{k-1,0} \ne 0$, then $r_{k,j} = \dfrac{r_{k-1,0}\, r_{k-2,j+1} - r_{k-2,0}\, r_{k-1,j+1}}{r_{k-1,0}}$ for $j \ge 0$.

Assume that the first column entries $r_{0,0}, r_{1,0}, \ldots, r_{n,0}$ are all defined and nonzero.
Then $p$ has no [[root|019MA1VTR2]] on the imaginary axis.
Moreover, the number of roots of $p$ with positive real part, counted with multiplicity, equals the number of sign changes in $r_{0,0}, r_{1,0}, \ldots, r_{n,0}$.

## Remarks

In particular, $p$ is a [[Hurwitz polynomial|Y631JTMMT5]] if and only if all entries of the first column are defined and positive.
This is Routh's form of the [[Routh–Hurwitz stability criterion|KJF8Y19BNV]].
One proof follows the change of the argument of $p(i\omega)$ as $\omega$ runs over $\R$.
This change is a Cauchy index of the ratio of the odd and even parts of $p$.
The rows of the array are the remainders of a Euclidean algorithm on these two parts, and Sturm's method counts the sign changes.

Example: for $p(s) = s^3 + s^2 + 2s + 8$, the rows start $(1, 2)$, $(1, 8)$, then $r_{2,0} = (1 \cdot 2 - 1 \cdot 8)/1 = -6$ and $r_{3,0} = ((-6) \cdot 8 - 1 \cdot 0)/(-6) = 8$.
The first column $1, 1, -6, 8$ has two sign changes, so $p$ has two roots with positive real part.
Indeed $p(s) = (s + 2)(s^2 - s + 4)$, and $s^2 - s + 4$ has roots $(1 \pm i\sqrt{15})/2$.

When a first column entry is $0$, the count needs extra care.
One may perturb the zero to a small $\varepsilon$, or use the derivative of an auxiliary polynomial when a whole row vanishes.

## Explanations

### L1 human

The theorem counts how many roots of a real polynomial lie in the right half-plane, the unstable side, without computing any root.
One builds a triangular table from the coefficients by a simple cross-multiplication rule.
The number of sign changes down its first column is the number of unstable roots.

### L2 human

For a linear system, the roots in the right half-plane are the unstable modes.
So the theorem tells not only whether the system is stable but how many unstable modes it has.
Treating a gain as a parameter in the array gives the range of gains for which a feedback loop is stable.
The determinant form of the same test uses the Hurwitz matrix and its leading principal minors.
