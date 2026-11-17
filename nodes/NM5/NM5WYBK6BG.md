---
tag: NM5WYBK6BG
kind: statement
role: theorem
name: Kanamori–McAloon theorem
msc: ["03F30", "05D10"]
topics: [T6FK1E7GJ1]
audience: grad
uses: [4P2BAT6YC3, 509ZWA0R26, MPSCREYC3M, 00TQV3F5S4, YSZ82MRXT8]
about: [MPSCREYC3M, 00TQV3F5S4]
history:
  first_stated: "1987"
  notes: "Kanamori and McAloon, 'On Gödel incompleteness and finite combinatorics', Annals of Pure and Applied Logic 33 (1987), 23-41."
sources:
  - url: https://en.wikipedia.org/wiki/Kanamori–McAloon_theorem
    locator: lead section
---

## Statement

Let $X$ be a set of natural numbers and $n \ge 1$, and let $[X]^n$ be the set of the $n$-element subsets of $X$.
A function $f : [X]^n \to \N$ is *regressive* if $f(s) < \min s$ for every $s$ with $0 \notin s$.
A set $H \subseteq X$ is *min-homogeneous* for $f$ if $f(s) = f(t)$ for all $s, t \in [H]^n$ with $\min s = \min t$.

**Theorem** (Kanamori and McAloon).

1. For all $n, k \ge 1$ there is $m$ such that every regressive $f : [\set{0, \dots, m - 1}]^n \to \N$ has a min-homogeneous set $H$ with $\abs{H} = k$.
2. Statement 1, written as a $\Pi_2$ sentence of first-order arithmetic, is not provable in [[Peano arithmetic|MPSCREYC3M]] $\mathsf{PA}$.
3. Statement 1 is provable in [[second-order arithmetic|DC60FYCSPM]] and in $\mathsf{ZFC}$.

The [[proof|QENFV1NJGK]] derives statement 1 from the infinite [[Ramsey theorem|00TQV3F5S4]] by compactness, and it outlines part 2 with the cited lemma marked.

## Remarks

### Why each hypothesis is needed

- The theory in part 2 is $\mathsf{PA}$. Second-order arithmetic is a stronger theory, and it proves statement 1.
- The function must be regressive. The function that gives every $n$-set its own value has no min-homogeneous set with $n + 1$ elements, for $n \ge 2$.
- The sets $s$ that contain $0$ are free, because no value is below $\min s = 0$. A min-homogeneous set can avoid $0$, so this costs nothing.
- Homogeneity is asked only among sets with the same least element. Full homogeneity fails: for $n = 1$ the function $f(\set{x}) = x - 1$ is regressive, and no two points get the same value.
- The exponent $n$ must vary. For each fixed $n$ the proof uses the infinite Ramsey theorem for exponent $n - 1$ only, and then $\mathsf{PA}$ proves the statement.

### Consequences

- For $n = 1$, every set is min-homogeneous, so $m = k$ works.
- The least $m$, as a function of $n$ and $k$, is not [[provably total|Z742YPHPNS]] in $\mathsf{PA}$.
- Statement 1 is a second natural example after the [[Paris-Harrington theorem|509ZWA0R26]] of a true finite statement that $\mathsf{PA}$ does not prove.

### Converse

The converse question is whether $\mathsf{PA}$ proves the negation of statement 1.
It does not, because statement 1 is true in the standard model, and $\mathsf{PA}$ proves only true sentences.

### Generalizations

- The infinite form says that every regressive function on $[\N^+]^n$ has an infinite min-homogeneous set. It follows from the infinite Ramsey theorem for exponent $n - 1$.
- The [[strengthened finite Ramsey theorem|4P2BAT6YC3]] is a finite principle of the same kind, with "large" in place of "min-homogeneous for regressive functions".

### Examples

The case $n = 2$, $k = 4$, with the domain $\set{1, \dots, N}$, has least $N = 5$, by a computer search over all regressive functions.

1. For $N = 4$, let $f(\set{2, 4}) = 1$ and $f(s) = 0$ for the other pairs. The only $4$-set is $\set{1, 2, 3, 4}$, and $f(\set{2, 3}) \ne f(\set{2, 4})$.
2. For $N = 5$, every pair $\set{1, y}$ has the value $0$, because $f(\set{1, y}) < 1$.
3. The three values $f(\set{2, y})$ for $y = 3, 4, 5$ lie in $\set{0, 1}$, so two of them are equal, say for $y < y'$.
4. Then $H = \set{1, 2, y, y'}$ is min-homogeneous. The only pair with least element $y$ is $\set{y, y'}$.

## History

Akihiro Kanamori and Kenneth McAloon published the theorem in 1987, in "On Gödel incompleteness and finite combinatorics" in the Annals of Pure and Applied Logic.
Their proof uses the model-theoretic method of the Paris-Harrington theorem.

## Explanations

### L1 human

A regressive function gives each group of $n$ numbers a label smaller than the least number of the group.
The theorem says that among enough numbers there are always $k$ numbers on which the labels agree, as long as the groups start at the same number.
This is true, and set theory proves it.
But ordinary arithmetic cannot prove it, because the number of points that it needs grows too fast.

### L2 human

The proof of statement 1 has two parts.

1. On an infinite set, choose points one at a time, and keep an infinite set on which the labels of the groups that start at the chosen point agree.
2. The labels of such groups are below the chosen point, so there are finitely many labels, and the infinite Ramsey theorem applies.
3. The chosen points form an infinite min-homogeneous set.
4. A compactness argument, as for the strengthened finite Ramsey theorem, turns this into the finite statement.

The trap: the infinite Ramsey theorem used in step 2 has exponent $n - 1$, and it is the variation of $n$ that $\mathsf{PA}$ cannot follow.

### L3 human

Kanamori and McAloon define an [[indicator|JWTZ8NVVGK]] from the regressive principle on intervals $[a, b]$ of a non-standard model.
Its non-standard values give initial segments that are models of $\mathsf{PA}$, and the least-element argument of the Paris-Harrington proof applies.
Regressive functions are the finite analogue of the regressive functions in Fodor's lemma, and min-homogeneous sets are the finite analogue of indiscernibles in model theory.
