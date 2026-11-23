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

The remainder in the β function can be written with one bounded quantifier, and Robinson arithmetic can compute it.
Let $\beta(c, d, i)$ be the remainder of $c$ on division by $1 + (i + 1) d$, as in [[Gödel's β-function lemma|BM6P0C2AC2]], and let
$$B(c, d, i, v) := \exists q \le c\,\bigl(c = q \cdot (1 + (i + 1) \cdot d) + v \land v < 1 + (i + 1) \cdot d\bigr),$$
with $1 = S 0$.

1. $B$ is a [[Δ0 formula|Y0JTZXBRT5]], and it defines the graph of $\beta$ in $\mathfrak{N}$: for all $c, d, i, v \in \mathbb{N}$, $\mathfrak{N} \models B(c, d, i, v)$ if and only if $v = \beta(c, d, i)$.
2. $B$ represents $\beta$ in [[Robinson arithmetic|TT8MXRTVBM]]: for all $c, d, i \in \mathbb{N}$,
$$\mathsf{Q} \vdash \forall v\,\bigl(B(\overline{c}, \overline{d}, \overline{i}, v) \leftrightarrow v = \overline{\beta(c, d, i)}\bigr).$$

## Remarks

### Why each clause is needed

The bound $q \le c$ makes $B$ a $\Delta_0$ formula.
It loses nothing in $\mathbb{N}$, because the quotient of $c$ by a positive number is at most $c$.

The clause $v < 1 + (i + 1) \cdot d$ makes the remainder unique.
Without it, $B(c, d, i, v)$ would hold for every $v$ of the form $c - q(1 + (i + 1) d)$ with $q \le c$ and $v \ge 0$.
For $c = 27001$, $d = 6$ and $i = 0$, the values $v = 2, 9, 16, \ldots$ would all qualify.

### What it gives you

With the β-function lemma, "there is a finite sequence $a_0, \ldots, a_n$ with property $P$" becomes "there are $c, d$ such that $\beta(c, d, 0), \ldots, \beta(c, d, n)$ have property $P$".
Written with $B$ and bounded quantifiers, this is a $\Sigma_1$ formula whenever $P$ is $\Delta_0$.

Part 2 is the case of $\beta$ in [[representability|BJF29XET83]].
Its proof is shorter than the general one, because the output $v$ is bounded inside $B$, so $\mathsf{Q}$ can list every candidate output.

## Explanations

### L1 human

The formula $B$ says "$v$ is the remainder of $c$ on division by $1 + (i + 1) d$" using only $+$, $\cdot$, $<$ and a search for the quotient below $c$.
Part 1 says that the formula means what it should in the natural numbers.
Part 2 says that even the weak axioms of $\mathsf{Q}$ prove, for each concrete input, that the formula picks out exactly one output.

### L2 human

We check Part 1 for $c = 3412752$, $d = 24$ and $i = 1$, where the modulus is $1 + 2 \cdot 24 = 49$.
Divide:
$$3412752 = 69648 \cdot 49 + 0,$$
so $\beta(3412752, 24, 1) = 0$, and $B(3412752, 24, 1, 0)$ holds with the witness $q = 69648 \le 3412752$, since $0 < 49$.
For $v = 1$, the equation $3412752 = q \cdot 49 + 1$ has no solution, since $3412751$ is not a multiple of $49$.
So $B(3412752, 24, 1, 1)$ fails.
Check the other entries with the moduli $25$, $73$ and $97$: the remainders are $2$, $2$ and $1$, so this $c$ and $d$ code the list $2, 0, 2, 1$.

The typical use of the lemma is to write "the $i$-th entry of the coded sequence is $v$" inside a $\Delta_0$ or $\Sigma_1$ formula.
Watch out: if you drop the clause $v < 1 + (i + 1) \cdot d$, then $B$ describes some number congruent to $c$, not the remainder.
