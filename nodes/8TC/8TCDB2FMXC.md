---
tag: 8TCDB2FMXC
kind: example
name: Deciding a monadic sentence by types
msc: ["03B10", "03B25"]
topics: [E4AVTNWE9E]
audience: ug2
instance_of: [SERN6CRVWW]
uses: [SERN6CRVWW, AS0NHQMAKA, QN7M1JCGT9, MVCH6N9SNW]
sources:
  - url: https://en.wikipedia.org/wiki/Monadic_predicate_calculus
    locator: lead section
---

## Example

A monadic sentence turns into a list of conditions on how many elements each region of a Venn diagram holds, and we solve those conditions by hand.
Consider the following sentence $\sigma$ with two unary predicates $P$ and $Q$.

$$\forall x \, (P(x) \to Q(x)) \wedge \exists x \, P(x) \wedge \exists x \, \neg Q(x) \wedge \exists x \, \exists y \, (x \neq y \wedge \neg P(x) \wedge \neg P(y))$$

We check that $\sigma$ is a monadic sentence, and we decide whether it is [[satisfiable|QN7M1JCGT9]].

1. The symbols $P$ and $Q$ are unary, and the only other atomic formulas are equations.
   So $\sigma$ is a sentence of the [[monadic predicate calculus|SERN6CRVWW]] with equality, with $k = 2$.
2. The quantifier rank of $\sigma$ is $q = 2$, from the last conjunct.
   By the [[finite model property|AS0NHQMAKA]], if $\sigma$ has a model, it has one with at most $2 \cdot 2^2 = 8$ elements.
3. We read the conjuncts as conditions on the four types $PQ$, $P\bar{Q}$, $\bar{P}Q$ and $\bar{P}\bar{Q}$.
   The first conjunct says that type $P\bar{Q}$ is empty.
4. The second conjunct says that $PQ$ or $P\bar{Q}$ is nonempty, so by step 3, type $PQ$ is nonempty.
5. The third conjunct says that $P\bar{Q}$ or $\bar{P}\bar{Q}$ is nonempty, so type $\bar{P}\bar{Q}$ is nonempty.
6. The last conjunct says that the types $\bar{P}Q$ and $\bar{P}\bar{Q}$ together have at least $2$ elements.
7. A candidate [[model|MVCH6N9SNW]] is $\mathcal{A}$ with domain $\{ a, b, c \}$, $P = \{ a \}$ and $Q = \{ a \}$.
   Then $a$ has type $PQ$, and $b$ and $c$ have type $\bar{P}\bar{Q}$.
8. In $\mathcal{A}$, $P \subseteq Q$, $a \in P$, $b \notin Q$, and $b \neq c$ with $b, c \notin P$.
   So all four conjuncts hold, and $\sigma$ is satisfiable.
9. No model has fewer than $3$ elements.
   Step 4 needs an element in $P$, and step 6 needs two other elements outside $P$.

## Remarks

Each conjunct became a condition on the number of elements of each type.
The conditions are linear inequalities on the sizes of the four types, and a sentence of rank $q$ only counts up to $q$.

Small changes move the answer.
If the last conjunct asks for three distinct elements outside $P$, the rank becomes $3$, and the smallest model has $4$ elements.
If the second conjunct is changed to $\forall x \, P(x)$, the sentence becomes unsatisfiable, because every element is then in $P$ and the last conjunct needs elements outside $P$.

Try it: decide whether $\forall x \, (P(x) \leftrightarrow Q(x)) \wedge \exists x \, \neg P(x) \wedge \exists x \, Q(x)$ is satisfiable, and find the smallest model.
(Answer: yes, with $2$ elements, one of type $PQ$ and one of type $\bar{P}\bar{Q}$.)

## Explanations

### L1 human

Think of two properties, "plays piano" and "plays guitar", and a group of people.
The statement says: every pianist plays guitar, someone plays piano, someone does not play guitar, and at least two people do not play piano.
A group of three people works: one plays both instruments, and two play neither.
We found it by sorting people into the four kinds and asking how many of each kind we need.

### L2 human

We repeat the method on a sentence that has no model.
Let $\rho = \forall x \, (P(x) \to Q(x)) \wedge \forall x \, (Q(x) \to P(x)) \wedge \exists x \, (P(x) \wedge \neg Q(x))$.

1. The first conjunct makes type $P\bar{Q}$ empty.
2. The second conjunct makes type $\bar{P}Q$ empty.
3. The third conjunct makes type $P\bar{Q}$ nonempty.
4. Steps 1 and 3 contradict each other, so $\rho$ has no model.

The typical use is to decide a monadic sentence by hand: translate each conjunct into a condition on the types, then solve the conditions.
A trap is to treat the types of different quantifiers as independent: one element has exactly one type, so the conditions interact.
