---
tag: 163A2WQQJX
kind: statement
role: theorem
name: Abel–Ruffini theorem
msc: [12F10, "12E12"]
uses: [J7YS0DA3HQ, 0RJMNEN3BJ, 0P3KZK0FTV, 0J53NE674D, VHCWCFA3MX]
about: [J7YS0DA3HQ]
sources:
  - url: https://en.wikipedia.org/wiki/Abel–Ruffini_theorem
same_as:
  wikidata: Q657482
  wikipedia: Abel–Ruffini theorem
---

## Statement

Let $n \ge 5$ be an integer.

1. Let $t_1, \dots, t_n$ be indeterminates and $K = \Q(t_1, \dots, t_n)$. The general polynomial $x^n + t_1 x^{n-1} + \dots + t_{n-1} x + t_n \in K[x]$ is not [[solvable by radicals|J7YS0DA3HQ]] over $K$.
2. There is a polynomial of degree $n$ with rational coefficients that is not solvable by radicals over $\Q$.

## Remarks

By [[Galois' theorem on solvability|VHCWCFA3MX]], it suffices to find a Galois group that is not [[solvable|0P3KZK0FTV]].
The Galois group of the general polynomial of degree $n$ is the full [[symmetric group|0RJMNEN3BJ]] $S_n$, and [[$S_n$ is not solvable for $n \ge 5$|0J53NE674D]].
For clause 2, the polynomial $x^5 - 4x + 2$ has Galois group $S_5$ over $\Q$; see the [[quintic equation|S1WS18QEGJ]].
Multiplying it by $x^{n-5}$ gives a polynomial of degree $n$ with the same nonsolvable roots.
The bound $n \ge 5$ is necessary: every polynomial of degree at most $4$ is solvable by radicals, by the [[cubic formula|FB6J5WAT5V]] and the [[quartic formula|4CDFMKKZ01]].

## Explanations

### L1 human

For equations of degree $2$, $3$ and $4$ there are formulas that give the roots from the coefficients using arithmetic and roots.
The theorem says that no such formula can exist for degree $5$ or more.
Worse, some single equations of degree $5$ with whole-number coefficients have roots that cannot be written with radicals at all.

### L2 human

The theorem does not say that quintic equations have no solutions: by the fundamental theorem of algebra, each has five complex roots.
It says only that these roots are not always radical expressions in the coefficients.
Many quintics, such as $x^5 - 2$, are still solvable by radicals; Galois theory decides which ones.
The roots can be expressed with other functions, for instance with the [[Bring radical|BSDCDJR6RQ]] or with elliptic modular functions.
