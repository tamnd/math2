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
Let $T(e, x, y)$ be [[Kleene's T predicate|S9DK13K5PS]], a quantifier-free formula that says "$y$ codes a halting computation of program $e$ on input $x$".
Let $B$ be the $\Pi^0_3$ sentence
$$\forall x\, \exists y\, \forall z\, (T(x, x, y) \vee \neg T(x, x, z)).$$
We show that [[Peano arithmetic|0QFT7Z76N5]] proves $B$ and [[Heyting arithmetic|RXHJPVMPJH]] does not, so the [[Pi-0-2 conservativity|PY679V9MVR]] does not extend to $\Pi^0_3$ sentences.

1. PA proves $B$.
   Fix $x$ and use the excluded middle on $\exists y\, T(x, x, y)$.
2. If $T(x, x, y_0)$ for some $y_0$, take $y = y_0$, and the first disjunct holds for every $z$.
3. If $\neg \exists y\, T(x, x, y)$, take $y = 0$, and then $\neg T(x, x, z)$ holds for every $z$.
4. Assume, for a contradiction, that HA proves $B$.
   By the soundness theorem of Kleene [[realizability|E6MB6B3YQ0]], which extends to the primitive recursive symbols, some number $e$ realizes $B$.
5. For each $x$, $\{e\}(x)$ is defined, and $f(x) = (\{e\}(x))_0$ is a computable function of $x$.
6. The second component of $\{e\}(x)$ realizes $\forall z\, (T(x, x, f(x)) \vee \neg T(x, x, z))$, so for every $z$ some disjunct is realized.
7. A realized equation is true, and a realized negation $\neg T(x, x, z)$ means that $T(x, x, z)$ has no realizer, so it is false.
   Hence for every $z$, $T(x, x, f(x))$ is true or $T(x, x, z)$ is false.
8. If program $x$ halts on input $x$, take $z$ with $T(x, x, z)$ true, and step 7 gives $T(x, x, f(x))$.
   So $x$ halts on $x$ if and only if $T(x, x, f(x))$, which we can decide by computing $f(x)$.
9. This decides the [[halting problem|Z7TN2B35B0]], which is impossible, so HA does not prove $B$.

## Remarks

PA and HA differ on $\Pi^0_3$ sentences, so the $\Pi^0_2$ bound in the conservation theorem is the best possible.
The sentence $B$ is classically equivalent to $\forall x\, (\exists y\, T(x, x, y) \vee \neg \exists y\, T(x, x, y))$, the excluded middle for halting.
The failure comes from the alternation $\exists y\, \forall z$: a witness $y$ must be chosen before all the $z$ are known.

What if we weaken $B$?
Drop the $\forall z$ and fix $z$ as a variable, and the sentence $\forall x\, \forall z\, \exists y\, (T(x, x, y) \vee \neg T(x, x, z))$ is $\Pi^0_2$.
HA proves it with the witness $y = z$, because $T(x, x, z) \vee \neg T(x, x, z)$ is decidable.
The [[no-counterexample interpretation|4BCD1EM542]] makes this idea systematic: it lets $y$ depend on a function that proposes $z$.

## Explanations

### L1 human

Classical arithmetic proves the statement "every program either halts or does not halt", written in a special form.
Intuitionistic arithmetic does not prove it, because each intuitionistic proof contains a method of computation.
Here the method would tell, for each program, whether it halts, and no such method exists.
So the two theories prove different statements as soon as the statements have three alternating quantifiers.

### L2 human

We look at what a realizer would have to do for two programs.
Let program $x_1$ halt on its own code, with the computation coded by $y_0 = 17$.
The classical proof chooses $y = 17$, and a realizer would have to output an $f(x_1)$ with $T(x_1, x_1, f(x_1))$ true.
Let program $x_2$ never halt on its own code.
Then any value $f(x_2)$ works, because $\neg T(x_2, x_2, z)$ holds for every $z$.
So checking $T(x, x, f(x))$ tells the two kinds of program apart, and no algorithm can do that for every $x$.

The typical use of the example is to show that a conservation result is optimal.
Watch out: the classical proof does say how to choose $y$, but only after a case distinction that no program can decide.
