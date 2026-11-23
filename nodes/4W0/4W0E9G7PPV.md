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

Arithmetic with addition but without multiplication is decidable: a machine can settle every sentence about the natural numbers that uses only $0$, $1$ and $+$.
For example, it confirms that every number is even or odd, $\forall x \, \exists y \, (x = y + y \vee x = y + y + 1)$, by removing the quantifiers one at a time.

Presburger arithmetic is the [[theory|92SWXST1ZM]] $\operatorname{Th}(\mathbb{N}, 0, 1, +)$ of the [[natural numbers|0MWKJ44V5A]] with zero, one and addition.
Let $L_{\mathbb{Z}}$ be the signature with constants $0, 1$, binary function symbols $+$ and $-$, the binary relation symbol $<$, and a unary relation symbol $D_n$ for each integer $n \ge 2$.
Interpret $L_{\mathbb{Z}}$ in the [[integers|0C4JS9RF5M]] $\mathbb{Z}$ in the usual way, with $D_n(x)$ meaning that $n$ divides $x$, that is, $x \equiv 0$ [[modulo $n$|0WAY5WX8NY]].

1. Quantifier elimination.
   For every $L_{\mathbb{Z}}$-formula $\varphi(x_1, \ldots, x_k)$ there is a quantifier-free $L_{\mathbb{Z}}$-formula $\psi(x_1, \ldots, x_k)$ such that $\mathbb{Z} \models \forall \vec{x} \, (\varphi \leftrightarrow \psi)$.
   The formula $\psi$ can be computed from $\varphi$.
2. Decidability.
   The theory $\operatorname{Th}(\mathbb{Z}, 0, 1, +, -, <, (D_n)_{n \ge 2})$ is a [[decidable theory|HWC687ES0Q]].
3. Presburger's theorem.
   The theory $\operatorname{Th}(\mathbb{N}, 0, 1, +)$ is decidable.

The [[proof|FSX4D0YCTJ]] uses Cooper's elimination procedure.

## Remarks

### A first decision

Take the sentence of the opening, $\forall x \, \exists y \, (x = y + y \vee x = y + y + 1)$, read in $\mathbb{N}$.
We eliminate the inner $\exists y$ first.
Over $\mathbb{Z}$, the equation $x = 2y$ has a solution exactly when $D_2(x)$, and $x = 2y + 1$ has one exactly when $D_2(x - 1)$.
For $x \ge 0$ the solutions $x / 2$ and $(x - 1) / 2$ are not negative, so in $\mathbb{N}$ the inner formula is equivalent to $D_2(x) \vee D_2(x - 1)$.

What remains is a sentence with one quantifier, and its negation is
$$\exists x \, (x \ge 0 \wedge \neg D_2(x) \wedge \neg D_2(x - 1)).$$
In $\mathbb{Z}$ exactly one of $x$ and $x - 1$ is even, so $\neg D_2(x)$ is the same as $D_2(x - 1)$, and the negation asks for $D_2(x - 1) \wedge \neg D_2(x - 1)$.
That is impossible, so the negation is false and the sentence is true.
Check: $7 = 3 + 3 + 1$ and $8 = 4 + 4$.

### Why each hypothesis is needed

The divisibility symbols $D_n$ are needed for [[quantifier elimination|7FDDXV3JK7]].
In $\mathbb{Z}$, the formula $\exists y \, (x = y + y)$ says that $x$ is even.
Without $D_n$, a quantifier-free formula in $x$ is a Boolean combination of conditions $a x + b = 0$ and $a x + b > 0$, so it defines a finite union of intervals.
The even numbers are not such a union, so the quantifier cannot be removed in the smaller signature.

Multiplication must be absent.
The theory of $(\mathbb{N}, 0, 1, +, \cdot)$ is undecidable, because it is a consistent extension of Robinson arithmetic $\mathsf{Q}$, which is [[essentially undecidable|9JDDFN8PT7]].

### What it gives you

$\operatorname{Th}(\mathbb{N}, 0, 1, +)$ is [[complete|655K8Y7VS8]], as is the theory of any single structure.
It is axiomatized by $x + 1 \ne 0$, $x + 1 = y + 1 \to x = y$, $x + 0 = x$, $x + (y + 1) = (x + y) + 1$ and the induction scheme for formulas in $0, 1, +$; the proof here does not cover this axiomatization.

Multiplication is not definable in $(\mathbb{N}, 0, 1, +)$.
If it were, the theory of $(\mathbb{N}, 0, 1, +, \cdot)$ would reduce to Presburger arithmetic and would be decidable.

The subsets of $\mathbb{N}$ definable in $(\mathbb{N}, 0, 1, +)$ are exactly the eventually periodic sets.
This follows from part 1, since a quantifier-free formula in one variable is a Boolean combination of half-lines, points and congruence classes.
So the set of squares, $\{ 0, 1, 4, 9, \ldots \}$, is not definable, because its gaps grow without bound.

In practice, questions about integer linear constraints with quantifiers, as they arise in program verification, have an algorithm.

### The converse and the cost

A decidable theory need not have quantifier elimination.
Every complete theory with a computable set of axioms is decidable by [[proof search|HZ7A7B2ERA]], with or without elimination, so elimination is a method, not a necessary condition.

The algorithm exists, but it is slow on some inputs.
Fischer and Rabin proved in 1974 that there is a constant $c > 0$ such that every decision procedure, even a nondeterministic one, needs more than $2^{2^{c n}}$ steps on some sentence of length $n$, for infinitely many $n$.
Oppen proved in 1978 that Cooper's procedure runs within $2^{2^{2^{p n}}}$ steps, for a constant $p$.

### Watch out

The constant multiples $2x = x + x$ and $3x = x + x + x$ are allowed, because they are sums.
A product $x \cdot y$ of two variables is not, and adding it changes the answer from decidable to undecidable.

Be careful whether you read a sentence in $\mathbb{N}$ or in $\mathbb{Z}$.
The sentence $\forall x \, \exists y \, (y + x = 0)$ is true in $\mathbb{Z}$ and false in $\mathbb{N}$, where $x = 1$ has no partner.
The proof works in $\mathbb{Z}$ and then relativizes every quantifier to $x \ge 0$.

### Generalizations

The elimination works in every $\mathbb{Z}$-group: a discretely ordered abelian group with least positive element $1$ in which $G / nG$ has exactly $n$ elements for each $n \ge 2$.
So the theory of $\mathbb{Z}$-groups is complete.
[[Büchi arithmetic|NSTECGT93D]] adds the function $V_k$, where $V_k(x)$ is the largest power of $k$ that divides $x$, and it is still decidable, by finite automata.
Real closed fields also have quantifier elimination, by the [[Tarski-Seidenberg theorem|3W5JGDZAN0]], and their theory is decidable for the same reason.

### Try it

Is $\exists x \, (x + x + x = 7)$ true in $\mathbb{N}$?
No: the formula says $D_3(7)$, and $7 = 2 \cdot 3 + 1$.

Write a quantifier-free formula equivalent in $\mathbb{N}$ to $\exists y \, (x = y + y + y + 1)$.
It is $D_3(x - 1) \wedge 0 < x$, since $y = (x - 1)/3$ must be a natural number.

## History

Mojżesz Presburger proved in 1929 that the theory of the natural numbers with addition is complete and decidable, by quantifier elimination.
Büchi showed in 1960 that the definable relations of $(\mathbb{N}, +)$ are recognized by finite automata, which gives a second decision procedure.
Cooper published in 1972 an elimination procedure that avoids the disjunctive normal form, and it is the procedure of the proof.
Fischer and Rabin proved the doubly exponential lower bound in 1974, and Oppen proved the triply exponential upper bound for Cooper's procedure in 1978.

## Explanations

### L1 human

Presburger arithmetic is arithmetic with whole numbers and addition, but without multiplication.
A statement such as "every number is even or one more than an even number" belongs to it.
Presburger proved that a computer can decide every such statement.
The method removes each "there is" from a statement, if we also allow the words "smaller than" and "divisible by 3".
In the end only a calculation with fixed numbers remains.

### L2 human

We run Cooper's method on $\varphi(x) = \exists y \, (x < y + y \wedge y + y + y < x + 4)$ over $\mathbb{Z}$.
The coefficients of $y$ are $2$ and $3$, with least common multiple $6$, so we scale the bounds to $3x < 6y$ and $6y < 2x + 8$.
With $z = 6y$, the formula becomes the following:
$$\exists z \, (D_6(z) \wedge 3x < z \wedge z < 2x + 8).$$
The lower bound is $3x$, and the period is $\delta = 6$.
Far to the left the lower bound fails, so only the test points $z = 3x + i$ for $i = 1, \ldots, 6$ count:
$$\bigvee_{i=1}^{6} \bigl( D_6(3x + i) \wedge x + i < 8 \bigr).$$
Since $3x + i$ must be a multiple of $3$, only $i = 3$ and $i = 6$ survive, and $\varphi(x)$ is equivalent to "$x$ is odd and $x < 5$, or $x$ is even and $x < 2$".
Check: for $x = 3$ the witness is $y = 2$, since $3 < 4$ and $6 < 7$, and for $x = 4$ no $y$ works, since $y \ge 3$ gives $3y \ge 9 > 8$.

The typical use is to turn a question about integer constraints with quantifiers into one without.
Watch out: the method is exact but costly, as the Fischer-Rabin bound shows.

### L3 human

Presburger arithmetic is the standard example of a theory proved decidable by quantifier elimination, together with the real closed fields.
Cooper's method shows that every formula about integers with addition reduces to finitely many test points: values just above a lower bound, within one full period of the congruences.
A second proof uses automata, since in binary notation the relation $x + y = z$ is recognized by a finite automaton with a carry bit.
The relations definable in Presburger arithmetic are exactly those recognized by automata in every base, by the theorem of Cobham and Semenov for [[Büchi arithmetic|NSTECGT93D]].
The doubly exponential lower bound of Fischer and Rabin is one of the first lower bounds proved for a natural decision problem.
