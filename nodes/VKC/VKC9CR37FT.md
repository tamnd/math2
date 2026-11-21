---
tag: VKC9CR37FT
kind: statement
role: theorem
name: Quantifier elimination for Z-groups
aliases: [presburger-quantifier-elimination, quantifier-elimination-for-z-groups, presburger-arithmetic-quantifier-elimination]
msc: ["03C10", "03B25", "11U09"]
topics: [1A9JSC5YG8]
audience: grad
uses: [082GHNPJ53, A49BATWQEH, RE5TFTDP4D, 92SWXST1ZM, 0C4JS9RF5M]
about: [4W0E9G7PPV, 7FDDXV3JK7]
sources:
  - url: https://en.wikipedia.org/wiki/Presburger_arithmetic
  - book: isbn:9780387987606
    locator: Chapter 3
---

## Statement

Let $L = \set{0, 1, +, -, <} \cup \set{D_n : n \ge 2}$, with each $D_n$ a unary relation symbol.
A *$\Z$-group* is an $L$-structure $G$ with these properties:

1. $(G, 0, +, -, <)$ is an [[ordered abelian group|A49BATWQEH]], and $1$ is its least positive element.
2. For each $n \ge 2$, $D_n(x)$ holds if and only if $x = n y$ for some $y \in G$.
3. For each $n \ge 2$ and each $x \in G$, exactly one of $x, x - 1, \dots, x - (n - 1)$ satisfies $D_n$.

Let $T_\Z$ be the $L$-[[theory|92SWXST1ZM]] whose models are the $\Z$-groups; it is axiomatized by these properties, one axiom or one scheme each.
Then $T_\Z$ has [[quantifier elimination|RE5TFTDP4D]].
A proof is [[the proof by the embedding test|PAJZHRYE6K]].

## Remarks

### Why each hypothesis is needed

- The predicates $D_n$. In the signature $\set{0, 1, +, -, <}$, the theory of $\Z$ has no quantifier elimination: $\exists y \, (x = y + y)$ defines the even numbers, and a quantifier-free set in one variable is a finite union of intervals; see [[Presburger arithmetic|4W0E9G7PPV]].
- Discreteness. Drop "$1$ is the least positive element". Then $\Z \times \Q$ with the lexicographic order, $1 = (1, 0)$ and $D_n$ meaning divisibility of the first coordinate by $n$, is a model of the rest, and so is $\Z$. The sentence $\exists x \, (0 < x \land x < 1)$ separates them, so the weaker theory is not complete, while a theory of this kind with quantifier elimination is complete, since its quantifier-free sentences only compare integers.
- The residue axioms in 3. Drop them. Then $\Z \times \Z$ with the lexicographic order and $1 = (0, 1)$ is a discretely ordered group. The element $(1, 0)$ satisfies neither $D_2(x)$ nor $D_2(x - 1)$, so $\forall x \, (D_2(x) \lor D_2(x - 1))$ fails there and holds in $\Z$.

### Consequences

- $T_\Z$ is complete, so it equals the theory of the [[integers|0C4JS9RF5M]] in $L$, and the $\Z$-groups are exactly the models of this theory.
- $T_\Z$ has a computable set of axioms and is complete, so it is decidable. This gives Presburger's theorem for $(\N, 0, 1, +)$, as in [[this statement|4W0E9G7PPV]].
- $T_\Z$ is model complete, and $\Z$ is its prime model: it embeds into every $\Z$-group by $k \mapsto k \cdot 1$.
- The definable subsets of a $\Z$-group in one variable are finite Boolean combinations of intervals and congruence classes.

### Converse

Every model of the theory of $(\Z, 0, 1, +, -, <)$ is a $\Z$-group after interpreting $D_n$ by divisibility by $n$, since the three properties are first-order and true in $\Z$.

### Generalizations

- Divisible ordered abelian groups have quantifier elimination in $\set{0, +, -, <}$; this is the dense analogue, with no need for $D_n$.
- Szmielew's invariants classify the [[complete theories of abelian groups|Y0753DF5R9]]. In the theory of modules, every formula is equivalent to a Boolean combination of positive primitive formulas and invariant sentences.

The name "$\Z$-group" also denotes, in finite group theory, a group with cyclic Sylow subgroups; see [[this concept|9VYFXJQ3DE]].
The two notions are unrelated.

## History

Mojżesz Presburger proved in 1929, by eliminating quantifiers with the help of congruences, that arithmetic with addition alone is complete and decidable.

## Explanations

### L1 human

The integers with addition and order behave like the real numbers in one respect: every statement can be simplified until no "there is" is left.
The only extra words needed are "divisible by $n$".
For example, "there is $y$ with $x = 3y + 1$" becomes "$x - 1$ is divisible by $3$".

### L2 human

We eliminate $\exists y \, (x < 2 y \land 2y < z)$ in $\Z$.

1. Put $w = 2y$. The formula says that some even $w$ lies strictly between $x$ and $z$.
2. The even numbers have period $2$, so it suffices to test $w = x + 1$ and $w = x + 2$, the first two values above $x$.
3. So the formula is equivalent to $(D_2(x + 1) \land x + 1 < z) \lor (D_2(x + 2) \land x + 2 < z)$.
4. Check with $x = 0$, $z = 2$: the first disjunct fails since $1$ is odd, and the second fails since $2 < 2$ is false. Indeed no even number lies strictly between $0$ and $2$.

The typical use is to decide statements about integer linear constraints with parameters.
A trap is to forget the predicates $D_n$: without them, step 3 has no quantifier-free form.

### L3 human

Quantifier elimination for $\Z$-groups is the integer counterpart of quantifier elimination for divisible ordered groups and for real closed fields.
The witnesses are found within one period of the congruences above a lower bound, which is the idea of Cooper's procedure in [[the proof of Presburger's theorem|FSX4D0YCTJ]].
The same idea gives quantifier elimination for other discretely ordered structures with congruence predicates.
