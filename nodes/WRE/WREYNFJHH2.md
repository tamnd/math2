---
tag: WREYNFJHH2
kind: statement
role: proposition
name: Uniqueness of solutions given initial values
msc: [39A06, 11B37]
uses: [081THG13JZ, 0ZV2YKKZ58]
about: [06MJC8YDYR]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_recurrence_with_constant_coefficients
---

## Statement

Let $R$ be a commutative ring and let $d \ge 1$ be an integer.
Let $E$ be a [[linear recurrence with constant coefficients|081THG13JZ]] of order $d$ over $R$, with coefficients $c_0, \dots, c_{d-1} \in R$.
Let $u$ and $v$ be [[solutions|0ZV2YKKZ58]] of $E$, that is, sequences $\N \to R$ with $u_{n+d} = \sum_{i=0}^{d-1} c_i u_{n+i}$ and $v_{n+d} = \sum_{i=0}^{d-1} c_i v_{n+i}$ for all $n \in \N$.
If $u_i = v_i$ for $i = 0, 1, \dots, d-1$, then $u_n = v_n$ for all $n \in \N$.

## Remarks

The proof is a strong induction on $n$.
For $n < d$ the claim is the hypothesis.
For $n \ge d$, the recurrence writes $u_n$ and $v_n$ by the same formula in the $d$ previous terms, which agree by induction.
Existence also holds: for each choice of $u_0, \dots, u_{d-1}$ in $R$, the recurrence defines the later terms one by one.
So the map $u \mapsto (u_0, \dots, u_{d-1})$ is a bijection from the solutions onto $R^d$; see the [[space of solutions|099GXMHV40]].
Example: let $\varphi$ and $\psi$ be the roots of $X^2 - X - 1$, and let $v_n = (\varphi^n - \psi^n)/\sqrt{5}$.
Then $v$ solves $u_{n+2} = u_{n+1} + u_n$ over $\R$, and $v_0 = 0$, $v_1 = 1$.
The [[Fibonacci sequence|0GA9K57A39]] solves the same recurrence with the same two initial values, so it equals $v$; this proves Binet's formula.
Fewer initial values are not enough: $(0, 1, 1, 2, 3, \dots)$ and $(0, 2, 2, 4, 6, \dots)$ both solve $u_{n+2} = u_{n+1} + u_n$ and agree in the first term only.

## Explanations

### L1 human

A linear recurrence of order $d$ tells you how to compute each term from the $d$ terms before it.
So once the first $d$ terms are known, there is no freedom left: every later term is forced.
Two sequences that obey the same rule and start the same way are the same sequence.

### L2 human

This fact is the basic tool for proving closed formulas for recurrent sequences.
To check a formula, one checks that it satisfies the recurrence and that it has the right first $d$ terms.
Together with existence, it shows that the solutions form a free module of rank $d$ with the initial values as coordinates.
In Mathlib it is `LinearRecurrence.eq_mk_of_is_sol_of_eq_init`.
