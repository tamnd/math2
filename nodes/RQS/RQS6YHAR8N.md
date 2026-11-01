---
tag: RQS6YHAR8N
kind: statement
role: theorem
name: Mazur's torsion theorem
msc: [11G05, 14H52, 11G18]
uses: [427N6S6QQW, P7V1BQJPSS, 0DBWXQRXQJ, 0KVGH0J5B3]
about: [427N6S6QQW, 0DBWXQRXQJ]
sources:
  - url: https://en.wikipedia.org/wiki/Torsion_conjecture
---

## Statement

Let $E$ be an [[elliptic curve|427N6S6QQW]] over $\Q$, and let $E(\Q)_{\mathrm{tors}}$ be the [[torsion subgroup|0DBWXQRXQJ]] of the [[group of rational points|P7V1BQJPSS]].
Then $E(\Q)_{\mathrm{tors}}$ is isomorphic to one of the following $15$ groups:

1. the [[cyclic group|0KVGH0J5B3]] $\Z/N\Z$ with $1 \le N \le 10$ or $N = 12$;
2. $\Z/2\Z \times \Z/2N\Z$ with $1 \le N \le 4$.

## Remarks

Each of the $15$ groups occurs for infinitely many curves with different $j$-invariants; this part was known before Mazur, from explicit families.
The hard part is that no other group occurs.
A rational point of order $N$ on $E$ gives a non-cuspidal rational point on the modular curve $X_1(N)$.
Mazur proved in 1977, with his study of the Eisenstein ideal, that for primes $N > 7$ the curve $X_1(N)$ has no such points.
Together with earlier results on the composite orders, this gives the list.
Example: on $y^2 = x^3 + 1$ the torsion subgroup is cyclic of order $6$.
Over larger number fields, the list of possible torsion groups is different, but it is still finite for each degree, by a theorem of Merel.

## Explanations

### L1 human

The points of finite order on an elliptic curve over the rationals form a small finite group.
Mazur's theorem gives the complete list of what that group can be: never more than $16$ points, and only $15$ shapes.

### L2 human

Together with the [[Nagell–Lutz theorem|G38B7E4ESW]], it makes the torsion part of [[Mordell's theorem|BZHGKN6Q3K]] fully explicit.
The method, through rational points on modular curves, is an early deep use of modular curves in arithmetic.
