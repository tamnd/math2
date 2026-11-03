---
tag: NS4N2EAKJ1
kind: statement
role: theorem
name: Tsfasman–Vlăduț–Zink bound
msc: [94B27, 94B65, 14G50]
uses: [GV8AGVP2F1, E85KREWV60, M2X88AXM17, XJM2MT4S3Y, 6W8TDV9VVN, SWJYG87QQH, 1NYCGYDNTX, 95CYGNRQQ6]
about: [DY3CHS08CT]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_geometry_code
---

## Statement

Let $q$ be the square of a prime power.
Let $0 < \delta < 1$.
Then there are [[linear codes|E85KREWV60]] $C_1, C_2, \dots$ over $\F_q$, of lengths $n_j \to \infty$, dimensions $k_j$ and [[minimum distances|M2X88AXM17]] $d_j$, such that
$$\liminf_{j \to \infty} \frac{d_j}{n_j} \ge \delta \quad \text{and} \quad \liminf_{j \to \infty} \frac{k_j}{n_j} \ge 1 - \delta - \frac{1}{\sqrt{q} - 1}.$$

## Remarks

The codes are [[algebraic geometry codes|DY3CHS08CT]].
For square $q$, there are [[curves|XJM2MT4S3Y]] $X_j$ over $\F_q$ of [[genus|6W8TDV9VVN]] $g_j \to \infty$ with $N_j$ [[rational points|SWJYG87QQH]] such that $N_j / g_j \to \sqrt{q} - 1$.
Modular curves give such sequences, and later Garcia and Stichtenoth gave explicit towers of function fields.
Take $n_j = N_j - 1$ of the points and a divisor $G$ of degree $a_j \approx (1 - \delta) n_j$ supported at the last point.
Then $d_j \ge n_j - a_j$ and $k_j \ge a_j + 1 - g_j$, which gives the two inequalities, since $g_j / n_j \to 1 / (\sqrt{q} - 1)$.

The bound is trivial for $q = 4$, since then $1/(\sqrt{q} - 1) = 1$.
For square $q \ge 49$, the line $R = 1 - \delta - 1/(\sqrt{q} - 1)$ lies above the [[Gilbert–Varshamov bound|1NYCGYDNTX]] $R = 1 - H_q(\delta)$ on an interval of values of $\delta$.
This gave the first known codes that beat the Gilbert–Varshamov bound for some alphabet size.

## Explanations

### L1 human

For long codes over a fixed alphabet, one wants both a good rate and a good fraction of correctable errors.
For a long time the best known trade-off came from random codes.
This theorem shows that codes built from algebraic curves with many points can do better when the alphabet is large enough.

### L2 human

For an algebraic geometry code from a curve of genus $g$, the rate $R$ and relative distance $\delta$ satisfy $R + \delta \ge 1 + 1/n - g/n$.
So the whole question is how small $g/n$ can be, that is how many rational points a curve can have relative to its genus.
The Drinfeld–Vlăduț bound shows that $\limsup N/g \le \sqrt{q} - 1$, so for square $q$ this construction cannot be pushed further with the same argument.
The comparison with the [[Gilbert–Varshamov bound|1NYCGYDNTX]] uses the [[$q$-ary entropy function|95CYGNRQQ6]] $H_q$.
