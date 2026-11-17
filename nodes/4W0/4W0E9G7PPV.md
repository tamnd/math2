---
tag: 4W0E9G7PPV
kind: statement
role: theorem
name: Presburger arithmetic
aliases: [decidability-of-presburger-arithmetic, presburgers-theorem]
msc: ["03B25", "03C10", "11U09"]
topics: [E4AVTNWE9E]
audience: grad
about: [HWC687ES0Q, 7FDDXV3JK7]
uses: [0MWKJ44V5A, 0C4JS9RF5M, 0WAY5WX8NY, 655K8Y7VS8, 0QFT7Z76N5, 7FDDXV3JK7, HWC687ES0Q, 92SWXST1ZM]
history:
  first_stated: "1929"
  notes: Mojżesz Presburger proved the completeness and decidability of the theory of addition of natural numbers in 1929. David Cooper gave the elimination procedure used in the proof here in 1972.
sources:
  - url: https://en.wikipedia.org/wiki/Presburger_arithmetic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Presburger_arithmetic
    locator: Decidability of Presburger arithmetic
  - url: https://en.wikipedia.org/wiki/Quantifier_elimination
    locator: lead section
same_as:
  wikidata: Q956059
  wikipedia: Presburger arithmetic
---

## Statement

Presburger arithmetic is the [[theory|92SWXST1ZM]] $\operatorname{Th}(\N, 0, 1, +)$ of the [[natural numbers|0MWKJ44V5A]] with zero, one and addition.

Let $L_{\Z}$ be the signature with constants $0, 1$, binary function symbols $+$ and $-$, the binary relation symbol $<$, and a unary relation symbol $D_n$ for each integer $n \ge 2$.
Interpret $L_{\Z}$ in the [[integers|0C4JS9RF5M]] $\Z$ in the usual way, with $D_n(x)$ meaning that $n$ divides $x$, that is, $x \equiv 0$ [[modulo $n$|0WAY5WX8NY]].

1. Quantifier elimination. For every $L_{\Z}$-formula $\varphi(x_1, \ldots, x_k)$ there is a quantifier-free $L_{\Z}$-formula $\psi(x_1, \ldots, x_k)$ such that $\Z \models \forall \vec{x} \, (\varphi \leftrightarrow \psi)$. The formula $\psi$ can be computed from $\varphi$.
2. Decidability. The theory $\operatorname{Th}(\Z, 0, 1, +, -, <, (D_n)_{n \ge 2})$ is a [[decidable theory|HWC687ES0Q]].
3. Presburger's theorem. The theory $\operatorname{Th}(\N, 0, 1, +)$ is decidable.

## Remarks

### Why each hypothesis is needed

- The divisibility predicates are needed for [[quantifier elimination|7FDDXV3JK7]]. In $\Z$, the formula $\exists y \, (x = y + y)$ says that $x$ is even. A quantifier-free formula in $x$ without $D_n$ is a Boolean combination of conditions $a x + b = 0$ and $a x + b > 0$. So it defines a finite union of intervals, some of them possibly unbounded, and the even numbers are not such a union.
- Multiplication must be absent. The theory of $(\N, 0, 1, +, \cdot)$ is undecidable, because it is a consistent extension of the [[essentially undecidable|9JDDFN8PT7]] theory $\mathsf{Q}$.

### Consequences

1. $\operatorname{Th}(\N, 0, 1, +)$ is [[complete|655K8Y7VS8]], as the theory of one structure. It is axiomatized by the axioms $x + 1 \ne 0$, $x + 1 = y + 1 \to x = y$, $x + 0 = x$, $x + (y + 1) = (x + y) + 1$ and the induction scheme for formulas in $\set{0, 1, +}$. We do not prove this axiomatization here.
2. Multiplication is not definable in $(\N, 0, 1, +)$. If it were, the theory of $(\N, 0, 1, +, \cdot)$ would reduce to Presburger arithmetic and would be decidable.
3. The subsets of $\N$ definable in $(\N, 0, 1, +)$ are exactly the eventually periodic sets: finite unions of finite sets and of arithmetic progressions. This follows from part 1, since a quantifier-free formula in one variable is a Boolean combination of half-lines, points and congruence classes.
4. Questions about integer linear constraints with quantifiers, as they arise in program verification, have an algorithm.

### Converse

The converse direction asks whether a decidable theory must have quantifier elimination; it does not.
Every complete theory with a computable set of axioms is decidable by [[proof search|HZ7A7B2ERA]], with or without quantifier elimination.
Quantifier elimination is a method to prove decidability and completeness, not a necessary condition.

### Generalizations

- The elimination works in every $\Z$-group: a discretely ordered abelian group with least positive element $1$ in which $G / nG$ has exactly $n$ elements for each $n \ge 2$. So the theory of $\Z$-groups is complete.
- Fischer and Rabin proved in 1974 a lower bound: there is a constant $c > 0$ such that every decision procedure for Presburger arithmetic needs more than $2^{2^{c n}}$ steps on some sentence of length $n$, for infinitely many $n$. The bound holds for nondeterministic algorithms as well.
- Oppen proved in 1978, by an analysis of Cooper's procedure, a deterministic upper bound of $2^{2^{2^{p n}}}$ steps, for a constant $p$.
- [[Büchi arithmetic|NSTECGT93D]] adds the function $V_k$, where $V_k(x)$ is the largest power of $k$ that divides $x$. It is still decidable, by finite automata.
- Real closed fields have quantifier elimination as well, by the [[Tarski-Seidenberg theorem|3W5JGDZAN0]], and their theory is decidable for the same reason.

## History

Mojżesz Presburger proved in 1929 that the theory of the natural numbers with addition is complete and decidable, by quantifier elimination.
Cooper published in 1972 an elimination procedure that avoids the disjunctive normal form, and it is the procedure in the proof here.
Fischer and Rabin proved the doubly exponential lower bound in 1974, and Oppen the triply exponential upper bound for Cooper's procedure in 1978.
Büchi observed in 1960 that the definable relations of $(\N, +)$ are recognized by finite automata, which gives a second decision procedure.

## Explanations

### L1 human

Presburger arithmetic is arithmetic with whole numbers and addition, but without multiplication.
A statement such as "every number is even or one more than an even number" belongs to it.
Presburger proved that a computer can decide every such statement.
The method removes each "there is" from a statement, if one also allows the words "smaller than" and "divisible by 3".
In the end only a simple calculation with fixed numbers remains.

### L2 human

We decide the sentence $\forall x \, \exists y \, (x = y + y \vee x = y + y + 1)$ in $\N$.

1. The inner formula is $\varphi(x) = \exists y \, (x = y + y \vee x = y + y + 1)$.
2. Over $\Z$, with $y$ allowed to be negative, the equation $x = 2 y$ has a solution exactly when $D_2(x)$ holds, and $x = 2 y + 1$ exactly when $D_2(x - 1)$ holds.
3. For $x \ge 0$ the solution $y$ is $x / 2$ or $(x - 1) / 2$, which is at least $0$. So in $\N$ the formula $\varphi(x)$ is equivalent to $D_2(x) \vee D_2(x - 1)$.
4. The formula $\forall x \, (x \ge 0 \to D_2(x) \vee D_2(x - 1))$ remains. Its negation is $\exists x \, (x \ge 0 \wedge \neg D_2(x) \wedge \neg D_2(x - 1))$.
5. Since $\neg D_2(x) \leftrightarrow D_2(x - 1)$ in $\Z$, the negation asks for $D_2(x - 1) \wedge \neg D_2(x - 1)$, which is false.
6. So the sentence is true in $\N$.

The typical use of Presburger's theorem is to settle questions about integer linear inequalities with quantifiers by machine.
A trap is the cost: the algorithm exists, but by the Fischer-Rabin bound it is very slow on some short sentences.

### L3 human

Presburger arithmetic is the standard example of a decidable theory proved by quantifier elimination, together with the real closed fields.
The proof here, by Cooper's method, shows that every formula about integers with addition reduces to finitely many test points: values just above a lower bound, within one full period of the congruences.
A second proof is by automata: in binary notation the relation $x + y = z$ is recognized by a finite automaton with a carry bit.
The definable relations are exactly those recognized by automata over all bases, by the theorem of Cobham and Semenov for [[Büchi arithmetic|NSTECGT93D]].
The complexity is known precisely in terms of alternating machines, and the doubly exponential lower bound is one of the first lower bounds for a natural decision problem.
