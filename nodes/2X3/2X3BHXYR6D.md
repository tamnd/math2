---
tag: 2X3BHXYR6D
kind: statement
role: lemma
name: The β function is represented in Robinson arithmetic by a Δ0 formula
msc: ["03F30", "03D20"]
topics: [QHCRN4JVG0]
audience: grad
uses: [BM6P0C2AC2, Y0JTZXBRT5, TT8MXRTVBM, 69234Z1V00]
sources:
  - wikipedia: en:24708433@r1334325217
    locator: Gödel's β function, section The β function lemma
    note: adopted
    mention: wikipedia://en/24708433#FTPA
    sections: [Statement]
  - book: isbn:9780521857840
inventory: [B96X42M79C]
---

## Statement

Let $\beta(c, d, i)$ be the remainder of $c$ on division by $1 + (i + 1) d$, as in [[Gödel's β-function lemma|BM6P0C2AC2]], and let
$$B(c, d, i, v) := \exists q \le c\,\bigl(c = q \cdot (1 + (i + 1) \cdot d) + v \land v < 1 + (i + 1) \cdot d\bigr),$$
with $1 = S 0$.

1. $B$ is a [[$\Delta_0$ formula|Y0JTZXBRT5]], and it defines the graph of $\beta$ in $\mathfrak{N}$: for all $c, d, i, v \in \N$, $\mathfrak{N} \models B(c, d, i, v)$ if and only if $v = \beta(c, d, i)$.
2. $B$ represents $\beta$ in [[Robinson arithmetic|TT8MXRTVBM]]: for all $c, d, i \in \N$,
$$\mathsf{Q} \vdash \forall v\,\bigl(B(\overline{c}, \overline{d}, \overline{i}, v) \leftrightarrow v = \overline{\beta(c, d, i)}\bigr).$$

## Remarks

### Why each hypothesis is needed

- The bound $q \le c$ makes $B$ a $\Delta_0$ formula. It loses nothing in $\N$, since the quotient of $c$ by a positive number is at most $c$.
- The clause $v < 1 + (i + 1) \cdot d$ makes the remainder unique. Without it, $B(c, d, i, v)$ would hold for every $v \le c$ of the form $c - q(1 + (i + 1) d)$, so for several values of $v$ in general.

### Consequences

- With the β-function lemma, the statement "there is a finite sequence $a_0, \ldots, a_n$ with property $P$" becomes "there are $c, d$ with property $P$ of $\beta(c, d, 0), \ldots, \beta(c, d, n)$", written with $B$ and bounded quantifiers.
- Part 2 is the case of $\beta$ in the [[representability theorem|BJF29XET83]], and its proof is shorter than the general one, because the output $v$ is bounded inside $B$.

## Explanations

### L1 human

The formula $B$ says "$v$ is the remainder of $c$ on division by $1 + (i + 1) d$" using only $+$, $\cdot$, $<$ and a search for the quotient below $c$.
Part 1 says that the formula means what it should in the natural numbers.
Part 2 says that even the weak axioms of $\mathsf{Q}$ prove, for each concrete input, that the formula picks out exactly one output.

### L2 human

We check Part 1 for $c = 3412752$, $d = 24$ and $i = 1$, where the modulus is $1 + 2 \cdot 24 = 49$.

1. $3412752 = 69648 \cdot 49 + 0$, so $\beta(3412752, 24, 1) = 0$.
2. $B(3412752, 24, 1, 0)$ holds with $q = 69648 \le 3412752$, since $0 < 49$.
3. For $v = 1$, the equation $3412752 = q \cdot 49 + 1$ has no solution, since $3412751$ is not a multiple of $49$; so $B(3412752, 24, 1, 1)$ fails.

The same $c$ and $d$ give $\beta = 2, 0, 2, 1$ for $i = 0, 1, 2, 3$, with the moduli $25$, $49$, $73$ and $97$.
The typical use of the lemma is to write "the $i$-th entry of the coded sequence is $v$" inside a $\Delta_0$ or $\Sigma_1$ formula.
A trap is to drop the clause $v < 1 + (i + 1) \cdot d$: then $B$ describes some number congruent to $c$, not the remainder.
