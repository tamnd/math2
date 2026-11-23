---
tag: NM5WYBK6BG
kind: statement
role: theorem
name: Kanamori-McAloon theorem
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

The Kanamori-McAloon theorem is a second Ramsey-type statement that is true but unprovable in Peano arithmetic.
Its labels must be smaller than the least point of each group, and in return the labels need to agree only on groups that start at the same point.

Let $n \ge 1$, let $X$ be a set of positive integers, and let $[X]^n$ be the set of the $n$-element subsets of $X$.
A function $f : [X]^n \to \mathbb{N}$ is *regressive* if $f(s) < \min s$ for every $s \in [X]^n$.
A set $H \subseteq X$ is *min-homogeneous* for $f$ if $f(s) = f(t)$ for all $s, t \in [H]^n$ with $\min s = \min t$.

**Theorem** (Kanamori and McAloon).

1. For all $n, k \ge 1$ there is $N$ such that every regressive $f : [\{ 1, \dots, N \}]^n \to \mathbb{N}$ has a min-homogeneous set $H$ with $\lvert H \rvert = k$.
2. Statement 1, written as a $\Pi_2$ sentence of first-order arithmetic, is not provable in [[Peano arithmetic|MPSCREYC3M]] $\mathsf{PA}$.
3. Statement 1 is provable in [[second-order arithmetic|DC60FYCSPM]] and in $\mathsf{ZFC}$.

The [[proof|QENFV1NJGK]] derives statement 1 from the infinite [[Ramsey theorem|00TQV3F5S4]] by compactness, and it outlines part 2 with the cited lemma marked.

## Remarks

### A first case by hand

Take pairs, $n = 2$, and ask for $k = 4$ points.
On $\{ 1, 2, 3, 4 \}$, let $f(\{ 2, 4 \}) = 1$ and $f(s) = 0$ for the other five pairs.
This is regressive, because $1 < 2 = \min \{ 2, 4 \}$ and $0$ is below every least element.
The only $4$-element set is $\{ 1, 2, 3, 4 \}$, and its two pairs with least element $2$ get different values, $f(\{ 2, 3 \}) = 0$ and $f(\{ 2, 4 \}) = 1$.
So $N = 4$ is too small.

Now let $f$ be any regressive function on the pairs of $\{ 1, \dots, 5 \}$.
Every pair $\{ 1, y \}$ has $f(\{ 1, y \}) = 0$, since the only natural number below $1$ is $0$.
The three values $f(\{ 2, y \})$ for $y = 3, 4, 5$ lie in $\{ 0, 1 \}$, so two of them agree, say for $y < y'$.
Then $H = \{ 1, 2, y, y' \}$ is min-homogeneous:
$$f(\{ 1, 2 \}) = f(\{ 1, y \}) = f(\{ 1, y' \}) = 0, \qquad f(\{ 2, y \}) = f(\{ 2, y' \}),$$
and $\{ y, y' \}$ is the only pair of $H$ with least element $y$.
So the least $N$ for $n = 2$ and $k = 4$ is $5$.

### Why each hypothesis is needed

The theory in part 2 is $\mathsf{PA}$.
Second-order arithmetic is a stronger theory, and it proves statement 1.

The function must be regressive.
Let $n \ge 2$ and give every $n$-set its own value.
A set $H$ with $n + 1$ elements has $n \ge 2$ subsets of size $n$ that contain $\min H$, and they get different values, so no min-homogeneous set has $n + 1$ elements.

Only groups with the same least element must agree.
Full homogeneity would fail: for $n = 1$ the function $f(\{ x \}) = x - 1$ is regressive, and no two points get the same value.

The exponent $n$ must vary.
For each fixed $n$ the proof uses the infinite Ramsey theorem for exponent $n - 1$ only, and then $\mathsf{PA}$ proves the statement.

### What it gives you

For $n = 1$ every set is min-homogeneous, because two one-element sets with the same least element are equal, so $N = k$ works.
For larger $n$ the least $N$, as a function of $n$ and $k$, grows so fast that it is not [[provably total|Z742YPHPNS]] in $\mathsf{PA}$; this is part 2 in other words.
After the [[Paris-Harrington theorem|509ZWA0R26]], the theorem is a second natural example of a true finite statement that $\mathsf{PA}$ does not prove.

### The converse, other forms, generalizations

$\mathsf{PA}$ does not prove the negation of statement 1 either, because statement 1 is true in the standard model and every theorem of $\mathsf{PA}$ is true there.

A common variant uses the domain $\{ 0, \dots, m - 1 \}$ and ask $f(s) < \min s$ only when $0 \notin s$.
The two forms are equivalent, because a min-homogeneous set can always avoid $0$, so $m = N + 1$ works.

The infinite form says that every regressive function on $[\mathbb{N}^+]^n$ has an infinite min-homogeneous set, and it follows from the infinite Ramsey theorem for exponent $n - 1$.
The [[strengthened finite Ramsey theorem|4P2BAT6YC3]] is a finite principle of the same kind, with largeness in place of regressive labels.

### Watch out

A common slip is to confuse min-homogeneous with homogeneous.
In the set $\{ 1, 2, y, y' \}$ above, the pairs that start at $1$ have value $0$, and the pairs that start at $2$ may both have value $1$.
That is allowed, because only pairs with the same least element are compared.

A second slip is to check regressiveness against the largest element.
The value $f(\{ 2, 4 \}) = 3$ is not allowed, although $3 < 4$, because the bound is $\min \{ 2, 4 \} = 2$.

### Try it

First, is $f(\{ x, y \}) = y - x$, for $x < y$, regressive on the pairs of $\{ 1, \dots, 5 \}$?
No: $f(\{ 1, 3 \}) = 2$, and $2 \ge 1 = \min \{ 1, 3 \}$.

Second, find the least $N$ for $n = 2$ and $k = 3$.
On $\{ 1, 2, 3 \}$ all pairs with least element $1$ have value $0$, and $\{ 2, 3 \}$ is the only pair with least element $2$, so $\{ 1, 2, 3 \}$ is min-homogeneous and the answer is $3$.

## History

Akihiro Kanamori and Kenneth McAloon published the theorem in 1987, in "On Gödel incompleteness and finite combinatorics" in the Annals of Pure and Applied Logic.

## Explanations

### L1 human

A regressive function gives each group of $n$ numbers a label smaller than the least number of the group.
The theorem says that among enough numbers there are always $k$ numbers on which the labels agree, as long as the groups start at the same number.
For pairs and $k = 4$, five numbers are enough, and four are not.
The statement is true, and set theory proves it.
But ordinary arithmetic cannot prove it, because the number of points that it needs grows too fast.

### L2 human

We sketch how the infinite form is proved for $n = 2$.
Let $f$ be regressive on the pairs of an infinite set $A$, and let $a_1 = \min A$.
The values $f(\{ a_1, y \})$ lie below $a_1$, so there are at most $a_1$ of them, and infinitely many $y$ share one value.
Keep only those $y$, let $a_2$ be the least of them, and repeat.

After infinitely many rounds, the points $a_1 < a_2 < a_3 < \cdots$ have this property: for each $i$, all pairs $\{ a_i, a_j \}$ with $j > i$ have the same value.
That is exactly min-homogeneity of $\{ a_1, a_2, \dots \}$.
For larger $n$ the same rounds use the infinite Ramsey theorem for exponent $n - 1$, and a compactness argument turns the infinite form into statement 1.
The trap is that the number of labels in round $i$ grows with $a_i$, and only the bound $f(s) < \min s$ keeps it finite.

### L3 human

Kanamori and McAloon define an [[indicator|JWTZ8NVVGK]] from the regressive principle on intervals $[a, b]$ of a non-standard model.
Its non-standard values give initial segments that are models of $\mathsf{PA}$, and the least-element argument of the [[Paris-Harrington proof|D0Q498H0R5]] applies.
Regressive functions are the finite analogue of the regressive functions in [[Fodor's lemma|55W1M20Q3F]], and min-homogeneous sets play the role of indiscernibles in model theory.
