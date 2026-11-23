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

We move a failing equation from an arbitrary MV-algebra to a chain, then to an ordered group, then to rational numbers, and finally to $[0, 1]$.
Lemmas A and B are cited, and Lemma C and the assembly are proved in full.
The direction from all MV-algebras to $[0, 1]$ holds because $[0, 1]$ is an MV-algebra, so we prove the other direction by contraposition.

### Two cited lemmas

**Lemma A.**
Every MV-algebra is a [[subdirect product|88WN3AD2VQ]] of linearly ordered MV-algebras.
Chang proved this in 1959.
It also follows from the subdirect representation of MTL-algebras by MTL-chains, since every MV-algebra is an MTL-algebra and the factors are quotients, hence MV-algebras, because MV-algebras form a [[variety|AJNZJD8442]].

**Lemma B.**
Let $C$ be a linearly ordered MV-algebra.
Then there are a [[totally ordered abelian group|1P8087YGYQ]] $G$ and an element $u \ge 0$ of $G$ with $C \cong \Gamma(G, u)$.
Here $\Gamma(G, u) = \{x \in G : 0 \le x \le u\}$, with $x \oplus y = \min(u, x + y)$ and $\neg x = u - x$.
This representation is also due to Chang.

### Lemma C: rational solutions

**Lemma C.**
Let $\Sigma$ be a finite system of inequalities $\ell > 0$ and $\ell \ge 0$, where each $\ell$ is a linear form with integer coefficients and no constant term in the variables $z_1, \dots, z_k$.
If $\Sigma$ has a solution in a totally ordered abelian group $G$, then $\Sigma$ has a solution in $\mathbb{Q}$.

We argue by induction on $k$, following [[Fourier-Motzkin elimination|NCZZ90R5Y6]].

1. For $k = 0$ each $\ell$ is the zero form.
   The $G$-solution shows that no inequality is $0 > 0$, so each one is $0 \ge 0$, which holds in $\mathbb{Q}$.
2. For $k > 0$ write each inequality as $a z_k + m > 0$ or $a z_k + m \ge 0$, with $a \in \mathbb{Z}$ and $m$ an integer form in $z_1, \dots, z_{k-1}$.
3. Call it a lower bound when $a > 0$, an upper bound when $a < 0$, and neutral when $a = 0$.
   Write a lower bound as $a z_k \rhd -m$ and an upper bound as $b z_k \lhd m'$, with $a, b > 0$.
4. For each pair of a lower and an upper bound, form $a m' + b m \rhd' 0$, where $\rhd'$ is strict when one of the two bounds is strict.
   Let $\Sigma'$ consist of these new inequalities and the neutral ones, a system in $k - 1$ variables.
5. The $G$-solution satisfies $\Sigma'$.
   In $G$, $p < q$ implies $np < nq$ for each integer $n \ge 1$, so $-bm \le ab z_k \le am'$, strictly where needed.
6. By induction, $\Sigma'$ has a rational solution $(q_1, \dots, q_{k-1})$.
   At it, every lower bound $-m/a$ lies below every upper bound $m'/b$, strictly where needed, by step 4.
7. Since $\mathbb{Q}$ is dense, choose a rational $q_k$ above all lower bounds and below all upper bounds, strictly where needed.
   If there are no bounds of one kind, choose $q_k$ far enough in that direction.
8. Then $(q_1, \dots, q_k)$ solves $\Sigma$.

### Assembly: from a chain to the rationals

1. Let $s = t$ fail in an MV-algebra $A$ at elements $a_1, \dots, a_n$.
   By Lemma A, $A$ embeds in a product of chains, and $s(a) \neq t(a)$ in some coordinate, so $s = t$ fails in a linearly ordered MV-algebra $C$.
2. By Lemma B, $C \cong \Gamma(G, u)$, and $u > 0$, because $\Gamma(G, 0)$ has one element and satisfies every equation.
3. For each subterm $r$ of $s$ and $t$ we define an integer linear form $\ell_r$ in $x_1, \dots, x_n, u$.
   Put $\ell_{x_i} = x_i$, $\ell_0 = 0$ and $\ell_{\neg r} = u - \ell_r$.
4. For $r = r_1 \oplus r_2$, test whether $\ell_{r_1} + \ell_{r_2} \le u$ holds at $(a, u)$ in $G$.
   If it holds, put $\ell_r = \ell_{r_1} + \ell_{r_2}$, and otherwise put $\ell_r = u$.
5. Induction on $r$ gives $r(a) = \ell_r(a, u)$ in $\Gamma(G, u)$, because $\oplus$ is the sum cut at $u$.
6. Let $\Sigma$ contain $u > 0$, $x_i \ge 0$, $u - x_i \ge 0$, and each test result of step 4.
   A passed test enters as $u - \ell_{r_1} - \ell_{r_2} \ge 0$, and a failed test as $\ell_{r_1} + \ell_{r_2} - u > 0$, since $G$ is totally ordered.
7. Add $\ell_t - \ell_s > 0$ or $\ell_s - \ell_t > 0$, whichever holds at $(a, u)$; one does, by step 5 and $s(a) \neq t(a)$.

### Assembly: from the rationals to the interval

8. The system $\Sigma$ is homogeneous with integer coefficients, and $(a, u)$ solves it in $G$.
   By Lemma C it has a rational solution $(b_1, \dots, b_n, v)$, with $v > 0$.
9. Put $c_i = b_i / v$.
   All forms are homogeneous and $v > 0$, so $(c, 1)$ also solves $\Sigma$.
10. So each $c_i$ lies in $[0, 1]$, and every test of step 4 has the same result at $(c, 1)$ in $\mathbb{R}$.
11. The induction of step 5, repeated in the standard MV-algebra, gives $r(c) = \ell_r(c, 1)$.
12. By step 7, $s(c) \neq t(c)$, so $s = t$ fails in $[0, 1]$, at rational arguments.

This proves item 1.
Item 2 is item 1 restated, because a variety is determined by the equations that hold in it.
For item 3, write $x \to y = \neg x \oplus y$, so that each formula $\varphi$ is a term.
Then $\varphi$ takes the value $1$ under every valuation in an algebra exactly when the equation $\varphi = \neg 0$ holds there, and item 3 is item 1 for that equation.

## Idea

An equation that fails somewhere fails in a chain, and a chain is an interval of an ordered group.
Inside the group, the failure is a finite list of linear facts: which sums were cut at the top, and which side of the equation is larger.
Linear facts with integer coefficients that hold in some ordered group already hold in the rationals, by eliminating one variable at a time.
Dividing by the top element then moves the counterexample into $[0, 1]$.

## Variants

Rose and Rosser gave a syntactic proof of the completeness of the Łukasiewicz axioms in 1958, without MV-algebras.
In place of Lemma C one can use model theory: the divisible hull of $G$ is elementarily equivalent to $\mathbb{Q}$ as an ordered group.
That route needs the completeness of the theory of divisible ordered abelian groups, which Lemma C avoids.
