---
tag: XQMNJF241J
kind: statement
role: theorem
name: Goodstein's theorem
msc: ["03F30", "03F15"]
topics: [T6FK1E7GJ1]
audience: grad
uses: [0QFT7Z76N5, MPSCREYC3M, 0YSCSX5YZC, 6GD30FGYDZ, KT50SMH3EC, 0ZHQMQ2C1N]
about: [MPSCREYC3M, KT50SMH3EC]
history:
  first_stated: "1944"
  notes: "Goodstein proved termination in 1944 (J. Symbolic Logic, 'On the restricted ordinal theorem'). Kirby and Paris proved the unprovability in PA in 1982 (Bull. London Math. Soc., 'Accessible independence results for Peano arithmetic')."
sources:
  - url: https://en.wikipedia.org/wiki/Goodstein's_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Goodstein's_theorem
    locator: Sequence length as a function of the starting value
same_as:
  wikidata: Q1149185
  wikipedia: Goodstein's theorem
---

## Statement

Let $b \ge 2$ be an integer.
Every integer $n \ge 1$ has a unique expansion $n = b^{e_1} c_1 + b^{e_2} c_2 + \cdots + b^{e_r} c_r$ with $e_1 > e_2 > \cdots > e_r \ge 0$ and $0 < c_i < b$.
The *hereditary base-$b$ notation* of $n$ is this expansion, with each exponent $e_i$ again written in hereditary base-$b$ notation.
Let $B_b(n)$ be the number that we get when we replace every $b$ in the hereditary base-$b$ notation of $n$ by $b + 1$, and let $B_b(0) = 0$.
The *Goodstein sequence* of $m \in \N$ is defined by $G_1 = m$ and $G_{k+1} = B_{k+1}(G_k) - 1$ as long as $G_k > 0$.
So $G_k$ is read in base $k + 1$.

**Theorem.**

1. For every $m \in \N$ the Goodstein sequence of $m$ reaches $0$: there is a $k$ with $G_k = 0$.
2. Statement 1, written as a $\Pi_2$ sentence of first-order arithmetic, is not provable in [[Peano arithmetic|MPSCREYC3M]] $\mathsf{PA}$.
3. Statement 1 is provable in $\mathsf{PA}$ plus [[transfinite induction|0ZHQMQ2C1N]] up to [[epsilon nought|KT50SMH3EC]] $\varepsilon_0$, and so it is provable in $\mathsf{ZFC}$.

The [[proof|J1NTZCSPPM]] proves parts 1 and 3 in full, and gives part 2 with the cited lemmas marked.

## Remarks

### Why each hypothesis is needed

- The theory in part 2 is $\mathsf{PA}$ and not a stronger theory. Part 3 shows that $\mathsf{PA}$ plus transfinite induction up to $\varepsilon_0$ proves the statement, so "independent" always means "independent of $\mathsf{PA}$".
- The notation must be hereditary. If only the digits are written in base $b$ and the exponents are left alone, we get the *weak Goodstein sequence*, and $\mathsf{PA}$ proves that it reaches $0$.
- The bases must not decrease. A digit of base $b$ can be too large for a smaller base, and then the step is not defined. Every nondecreasing sequence of bases works, by the [[extended Goodstein theorem|3RVB1T9YDT]].
- The step "subtract $1$" is needed. Without it, $B_b$ alone never decreases a positive number, and the sequence $m, B_2(m), B_3(B_2(m)), \dots$ grows for ever when $m \ge 2$.

### Consequences

- The length of the sequence grows very fast. Let $L(m)$ be the least $k$ with $G_k = 0$; then $L(3) = 6$ and $L(4) = 3 \cdot 2^{402653211} - 2$, a number with $121210695$ decimal digits.
- In terms of the [[Hardy hierarchy|X8RKXQASR9]], $L(m) = H_{o_2(m)}(3) - 2$, where $o_2(m)$ replaces every $2$ in the hereditary base-$2$ notation of $m$ by $\omega$. Cichon gave a formula of this kind in 1983.
- The function $L$ is total but not [[provably total|Z742YPHPNS]] in $\mathsf{PA}$. It eventually dominates every function that $\mathsf{PA}$ proves total.
- The theorem gives a true $\Pi_2$ sentence of number theory with no mention of logic or coding that $\mathsf{PA}$ does not prove. It is a concrete case of [[Gödel's incompleteness theorems|X9WYNYE29C]].

### Converse

Part 1 has no hypothesis other than $m \in \N$, so it has no converse in the usual sense.
The related question is one of strength.
Over $\mathsf{PA}$, statement 1 implies the [[consistency|VM8TQ70CVJ]] of $\mathsf{PA}$, so its proof needs more than $\mathsf{PA}$.
Each single instance "the sequence of $m$ reaches $0$" for a fixed numeral $m$ is a true $\Sigma_1$ sentence, so $\mathsf{PA}$ proves it.

### Generalizations

- The [[extended Goodstein theorem|3RVB1T9YDT]]: the bases $2, 3, 4, \dots$ can be replaced by any nondecreasing sequence of bases $b_1 \ge 2$.
- The [[Kirby-Paris hydra|C028FF4TWM]] game and [[Beklemishev's worm principle|MHDZGDNEPS]] are other processes whose termination needs ordinals up to $\varepsilon_0$.
- The [[Buchholz hydra|9APRFM0G7F]] game needs much larger ordinals, and its termination is not provable even in $(\Pi^1_1\text{-}\mathsf{CA}) + \mathsf{BI}$.

### Examples

For $m = 3$: $G_1 = 3 = 2^1 + 1$, then $G_2 = (3 + 1) - 1 = 3$.
In base $3$, $3 = 3^1$, so $G_3 = 4 - 1 = 3$.
In base $4$ the number $3$ is a single digit, so $G_4 = 2$, $G_5 = 1$, $G_6 = 0$.
For $m = 4 = 2^{2^1}$ the sequence starts $4, 26, 41, 60, 83, 109, 139, 173$.
For example $G_2 = 26 = 2 \cdot 3^2 + 2 \cdot 3 + 2$ in base $3$, and $G_3 = (2 \cdot 4^2 + 2 \cdot 4 + 2) - 1 = 41$.

## History

Reuben Goodstein proved part 1 in 1944, in a paper on the "restricted ordinal theorem" in the Journal of Symbolic Logic.
Laurence Kirby and Jeff Paris proved part 2 in 1982, in "Accessible independence results for Peano arithmetic".
Their proof used non-standard models of arithmetic.
In 1983 Cichon gave a shorter proof through the Hardy hierarchy and the provably total functions of $\mathsf{PA}$.

## Explanations

### L1 human

Write $4$ with powers of $2$ only, even inside the exponents: $4 = 2^2$.
Change every $2$ into a $3$ and subtract $1$: $3^3 - 1 = 26$.
Write $26$ with powers of $3$, change every $3$ into a $4$ and subtract $1$, which gives $41$.
The numbers grow for a very long time, but the theorem says that they always come back to $0$ in the end.
For the start value $4$ this takes more steps than a number with over a hundred million digits.
The usual axioms of arithmetic cannot prove this fact, although it is true.

### L2 human

A worked check of the ordinal method for $m = 3$.

1. Write each $G_k$ in hereditary base $k + 1$ and replace the base by $\omega$. This gives an [[ordinal|0YSCSX5YZC]] $\alpha_k$ in [[Cantor normal form|6GD30FGYDZ]].
2. $G_1 = 2 + 1$ gives $\alpha_1 = \omega + 1$.
3. $G_2 = 3 = 3^1$ in base $3$ gives $\alpha_2 = \omega$.
4. $G_3 = 3$ in base $4$ is a digit, so $\alpha_3 = 3$.
5. Then $\alpha_4 = 2$, $\alpha_5 = 1$, $\alpha_6 = 0$.
6. The ordinals $\omega + 1 > \omega > 3 > 2 > 1 > 0$ strictly decrease, although the numbers $3, 3, 3$ do not.

The typical use: a process on numbers ends when it has a measure that strictly decreases in a well-ordered set.
The trap: the numbers $G_k$ themselves do not decrease, so no measure in $\N$ works directly.
A second trap: "unprovable" here means unprovable in $\mathsf{PA}$; the theorem is proved in $\mathsf{ZFC}$.

### L3 human

Goodstein's theorem is the arithmetic form of the well-foundedness of $\varepsilon_0$ along one primitive recursive descending path.
The length function equals a Hardy function $H_{\alpha}(3) - 2$ with $\alpha < \varepsilon_0$, and this calibrates the theorem against the [[proof-theoretic ordinal|C72RBH0CDR]] $\varepsilon_0$ of $\mathsf{PA}$.
The same pattern, termination by ordinals and unprovability by growth rate, appears for the [[Kirby-Paris hydra|C028FF4TWM]], for [[worms|MHDZGDNEPS]] and for the [[Paris-Harrington theorem|509ZWA0R26]].
Stronger theories match larger ordinals, as in the [[Buchholz hydra|9APRFM0G7F]] and [[Friedman's finite form of Kruskal's theorem|12XRGBWH59]].
The [[ordinal analysis|C5E5TG8PGP]] of $\mathsf{PA}$ by [[Gentzen|QPV0HNP22S]] is the background of all these results.
