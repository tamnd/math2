---
tag: NBFNXA2WFM
kind: statement
role: lemma
name: Osgood's lemma
msc: [32A10]
uses: [0DG0Z72CQD, 0DG10TVYPN, 0VP56B4EMX]
about: [0NAHXR1FRH]
sources:
  - url: https://en.wikipedia.org/wiki/Osgood%27s_lemma
same_as:
  wikidata: Q7106530
  wikipedia: Osgood's lemma
---

## Statement

Let $n \ge 1$, let $U \subseteq \C^n$ be an open set, and let $f \colon U \to \C$ be continuous.
Assume that $f$ is holomorphic in each variable separately: for each $j$ and each fixed value of the other variables, $z_j \mapsto f(z_1, \dots, z_n)$ is [[holomorphic|0DG0Z72CQD]].
Then $f$ is holomorphic on $U$.
That is, near each point $c \in U$, $f$ is the sum of a convergent [[power series|0VP56B4EMX]] in $z_1 - c_1, \dots, z_n - c_n$.

## Remarks

Proof idea: on a closed polydisc $\prod_j \set{\abs{z_j - c_j} \le r_j}$ in $U$, apply the one-variable [[Cauchy integral formula|0DG10TVYPN]] in each variable in turn.
Continuity makes the iterated integral an integral over the torus $\prod_j \set{\abs{\zeta_j - c_j} = r_j}$.
Expanding the kernel $\prod_j (\zeta_j - z_j)^{-1}$ as a geometric series gives the power series.
Hartogs's theorem on separate analyticity shows that the continuity hypothesis can be dropped, but its proof is much harder.
For real variables the analogue fails: $xy/(x^2 + y^2)$, set to $0$ at the origin, is real-analytic in each variable but not continuous.

## Explanations

### L1 human

In several complex variables a function can be tested one variable at a time.
If it is continuous and holomorphic in each variable when the others are frozen, it is holomorphic in all of them together.
This makes it easy to check that many functions of several variables are holomorphic.

### L2 human

Osgood's lemma is often the first step in a course on several complex variables.
With it, the Cauchy formula on polydiscs gives power series expansions, Cauchy estimates and Weierstrass convergence theorems in $\C^n$.
It also lets one define holomorphic functions of several variables either by power series or by separate holomorphy plus continuity.
