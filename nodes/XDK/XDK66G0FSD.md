---
tag: XDK66G0FSD
kind: proof
name: Proof of Chang's completeness theorem by linear chains and rational solutions
msc: ["03B50", "06D35"]
topics: [WZP584JQ06]
audience: research
proves: QM0F33QE9P
uses: [JQ713VVD0G, AJNZJD8442, 88WN3AD2VQ, 1P8087YGYQ, NCZZ90R5Y6]
methods: [0NTF6DMVAP, 12MQ2NJ29A, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/MV-algebra
    locator: Examples of MV-algebras; Definitions
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 7. Algebraic semantics
  - book: isbn:9780792360094
---

## Proof

This is a structured proof.
Lemmas A and B are cited with their sources; Lemma C and the assembly are proved in full.
The direction from all MV-algebras to $[0, 1]$ holds because $[0, 1]$ is an MV-algebra.
We prove the other direction by contraposition.

**Lemma A (cited).**
Every MV-algebra is a [[subdirect product|88WN3AD2VQ]] of linearly ordered MV-algebras.
Source: SEP, section 7, states that every MTL-algebra is a subdirect product of MTL-chains.
Wikipedia states that MV-algebras are exactly the prelinear bounded integral commutative residuated lattices with $x \lor y = (x \to y) \to y$.
So every MV-algebra is an MTL-algebra.
Its subdirect factors are quotients, so they are again MV-algebras, because MV-algebras form a [[variety|AJNZJD8442]].

**Lemma B (cited).**
Let $C$ be a linearly ordered MV-algebra.
Then there are a [[totally ordered abelian group|1P8087YGYQ]] $G$ and $u \in G$, $u \ge 0$, with $C \cong \Gamma(G, u)$.
Here $\Gamma(G, u) = \set{x \in G : 0 \le x \le u}$, with $x \oplus y = \min(u, x + y)$ and $\neg x = u - x$.
Source: Wikipedia, "Examples of MV-algebras", attributes this representation to Chang.

**Lemma C (proved).**
Let $\Sigma$ be a finite system of inequalities $\ell > 0$ and $\ell \ge 0$.
Each $\ell$ is a linear form with integer coefficients and no constant term, in variables $z_1, \dots, z_k$.
If $\Sigma$ has a solution in a totally ordered abelian group $G$, then $\Sigma$ has a solution in $\mathbb{Q}$.

Proof of Lemma C, by induction on $k$.

1. Case $k = 0$: each $\ell$ is the form $0$, and the $G$-solution shows that each inequality is $0 \ge 0$, which holds in $\mathbb{Q}$.
2. Case $k > 0$: write each inequality as $a z_k + m > 0$ or $a z_k + m \ge 0$, with $a \in \mathbb{Z}$.
3. Here $m$ is an integer form in $z_1, \dots, z_{k-1}$.
4. Split $\Sigma$ into lower bounds ($a > 0$), upper bounds ($a < 0$) and the rest ($a = 0$).
5. Write a lower bound as $a z_k \rhd -m$ and an upper bound as $b z_k \lhd m'$, with $a, b > 0$.
6. For each such pair, form $b(-m) \lhd' a m'$, that is, $a m' + b m \rhd' 0$.
7. Here $\rhd'$ is strict iff one of the two given inequalities is strict.
8. Let $\Sigma'$ be these new inequalities together with the rest, a system in $k - 1$ variables.
9. $\Sigma'$ holds at the $G$-solution: in $G$, $p < q$ implies $n p < n q$ for every integer $n \ge 1$.
10. So $-bm \le ab z_k \le a m'$ in $G$, with strict inequality where needed.
11. By induction, $\Sigma'$ has a rational solution $(q_1, \dots, q_{k-1})$.
12. At this solution, every lower bound $-m/a$ is below every upper bound $m'/b$, strictly where needed, by step 6.
13. Choose a rational $q_k$ between the largest lower bound and the smallest upper bound.
14. If a bound is strict, choose $q_k$ strictly inside, which is possible since $\mathbb{Q}$ is dense.
15. If there are no lower or no upper bounds, choose $q_k$ far enough from the others.
16. Then $(q_1, \dots, q_k)$ solves $\Sigma$, by the elimination step of [[Fourier-Motzkin|NCZZ90R5Y6]].

**Assembly.**

1. Let $s = t$ fail in an MV-algebra $A$, at elements $a_1, \dots, a_n$.
2. By Lemma A, $A$ embeds in a product of chains $C_i$, and $s(a) \neq t(a)$ differs in some coordinate $i$.
3. So $s = t$ fails in a linearly ordered MV-algebra $C$.
4. By Lemma B, $C \cong \Gamma(G, u)$, and $u > 0$ since $\Gamma(G, 0)$ is trivial and satisfies every equation.
5. For each subterm $r$ of $s$ and $t$, define an integer linear form $\ell_r$ in $x_1, \dots, x_n, u$.
6. Set $\ell_{x_i} = x_i$, $\ell_0 = 0$ and $\ell_{\neg r} = u - \ell_r$.
7. For $r = r_1 \oplus r_2$, test $\ell_{r_1} + \ell_{r_2} \le u$ at $(a, u)$ in $G$.
8. If it holds, set $\ell_r = \ell_{r_1} + \ell_{r_2}$; otherwise set $\ell_r = u$.
9. By induction on $r$, $r(a) = \ell_r(a, u)$ in $\Gamma(G, u)$.
10. Collect into $\Sigma$: $u > 0$, $x_i \ge 0$, $u - x_i \ge 0$, and each test result from step 7.
11. A failed test enters as $\ell_{r_1} + \ell_{r_2} - u > 0$, since $G$ is totally ordered.
12. Add $\ell_t - \ell_s > 0$ or $\ell_s - \ell_t > 0$, whichever holds at $(a, u)$.
13. $\Sigma$ is homogeneous with integer coefficients, and $(a, u)$ solves it in $G$.
14. By Lemma C, $\Sigma$ has a rational solution $(b_1, \dots, b_n, v)$, with $v > 0$.
15. Put $c_i = b_i / v$; all forms are homogeneous, so $(c, 1)$ also solves $\Sigma$.
16. So $c_i \in [0, 1]$, and every test of step 7 has the same result at $(c, 1)$ in $\mathbb{R}$.
17. By induction on $r$, as in step 9, $r(c) = \ell_r(c, 1)$ in the standard MV-algebra.
18. By step 12, $s(c) \neq t(c)$, so $s = t$ fails in $[0, 1]$, at rational arguments.
19. This proves item 1, and item 2 is item 1 restated, since a variety is determined by its equations.
20. For item 3, a formula $\varphi$ has value $1$ everywhere iff the equation $\varphi = \neg 0$ holds.
21. So item 3 is item 1 for the equation $\varphi = \neg 0$. $\blacksquare$

## Idea

An equation that fails somewhere fails in a chain.
A chain is an interval of an ordered group.
The failure is a finite set of linear facts, and these facts can be realized by rational numbers.

## Variants

1. Rose and Rosser gave a syntactic proof of the completeness of the Łukasiewicz axioms in 1958, as SEP reports.
2. Instead of Lemma C, one can use that the divisible hull of $G$ is elementarily equivalent to $\mathbb{Q}$.
   This needs the completeness of the theory of divisible ordered abelian groups, which is not proved here.
