---
tag: HVHEKG9FA5
kind: example
name: Peano arithmetic is not conservative over Heyting arithmetic for Pi-0-3 sentences
msc: ["03F30", "03F55"]
topics: [8XY7JYZKFW]
audience: grad
not_instance_of:
  - target: TNZ995J8AP
    note: "PA proves a Pi-0-3 sentence that HA does not prove, so PA is not Pi-0-3-conservative over HA."
uses: [RXHJPVMPJH, 0QFT7Z76N5, E6MB6B3YQ0, S9DK13K5PS, Z7TN2B35B0, PY679V9MVR]
sources:
  - url: https://en.wikipedia.org/wiki/Heyting_arithmetic
    locator: Conservativity
  - url: https://en.wikipedia.org/wiki/Realizability
    locator: lead section
---

## Example

In this example PA and HA have function symbols and defining equations for all primitive recursive functions.
Let $T(e, x, y)$ be [[Kleene's T predicate|S9DK13K5PS]], a quantifier-free formula: "$y$ codes a halting computation of program $e$ on input $x$".
Let $B$ be the $\Pi^0_3$ sentence
$$\forall x\, \exists y\, \forall z\, (T(x, x, y) \vee \neg T(x, x, z)).$$
We show that [[Peano arithmetic|0QFT7Z76N5]] proves $B$ and [[Heyting arithmetic|RXHJPVMPJH]] does not.
So the [[Pi-0-2 conservativity|PY679V9MVR]] does not extend to $\Pi^0_3$ sentences.

1. PA proves $B$. Fix $x$ and use excluded middle on $\exists y\, T(x, x, y)$.
2. If $T(x, x, y_0)$ for some $y_0$, take $y = y_0$: the first disjunct holds for every $z$.
3. If $\neg \exists y\, T(x, x, y)$, take $y = 0$: then $\neg T(x, x, z)$ for every $z$.
4. Assume, for a contradiction, that HA proves $B$. By the soundness theorem of [[realizability|E6MB6B3YQ0]], which extends to the primitive recursive symbols, some number $e$ realizes $B$.
5. For each $x$, $\{e\}(x)$ is defined, and $f(x) = (\{e\}(x))_0$ is a computable function of $x$.
6. The second part realizes $\forall z\, (T(x, x, f(x)) \vee \neg T(x, x, z))$, so for every $z$ some disjunct is realized.
7. A realized equation is true, and a realized negation $\neg T(x, x, z)$ means that $T(x, x, z)$ is not realized, so it is false.
8. Hence for every $z$: $T(x, x, f(x))$ is true or $T(x, x, z)$ is false.
9. If program $x$ halts on input $x$, take $z$ with $T(x, x, z)$ true. Step 8 gives $T(x, x, f(x))$.
10. So $x$ halts on $x$ if and only if $T(x, x, f(x))$, which is decidable by computing $f(x)$.
11. This decides the [[halting problem|Z7TN2B35B0]], which is impossible. So HA does not prove $B$.

## Remarks

The example shows that PA and HA differ on $\Pi^0_3$ sentences, so the $\Pi^0_2$ bound in the conservation theorem is optimal.
The matrix of $B$ is quantifier-free, and the sentence is classically equivalent to $\forall x\, (\exists y\, T(x, x, y) \vee \neg \exists y\, T(x, x, y))$.
The failure comes from the alternation $\exists y\, \forall z$: a witness $y$ must be found without knowing all $z$.
The [[no-counterexample interpretation|4BCD1EM542]] replaces the quantifier $\forall z$ by a function and so gives a weaker, computable reading of $B$.
For $\Pi^0_1$ and $\Pi^0_2$ sentences, the two theories agree.

## Explanations

### L1 human

Classical arithmetic proves the statement "every program either halts or does not halt", written in a special form.
Intuitionistic arithmetic does not prove it, because each intuitionistic proof contains a method of computation.
Here the method would tell, for each program, whether it halts, and no such method exists.
So the two theories prove different statements, as soon as the statements have three alternating quantifiers.

### L2 human

We look at the realizer for one program $x$ that halts after a computation coded by $y_0 = 17$.

1. The classical proof chooses $y = 17$, because $T(x, x, 17)$ is true.
2. A realizer would have to output $f(x)$ with $T(x, x, f(x))$ true, so $f(x)$ would also code a halting computation.
3. For a program that never halts, any $f(x)$ works.
4. So the function $f$ tells the two cases apart, which no program can do for all $x$.

The typical use of this example is to show that a conservation result is optimal.
A trap is to read the classical proof as a method to find $y$: it finds $y$ only after a case distinction that no program can decide.
