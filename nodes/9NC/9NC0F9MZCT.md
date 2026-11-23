---
tag: 9NC0F9MZCT
kind: example
name: A Henkin witness for an existential sentence must be a new constant
msc: ["03C07", "03B10"]
topics: [FBWW4J1XWG]
audience: ug2
instance_of: [RY8KRKR097]
uses: [RY8KRKR097, AVD7T7J063, SC0BSJ3GT6, VM8TQ70CVJ, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem
    locator: Proofs
  - book: isbn:9780122384523
    locator: Section 2.5
---

## Example

A theory says that something has the property $P$ and that the object named $a$ does not.
We add a witness for the existential sentence, as in the [[Henkin construction|RY8KRKR097]], and see that the witness has to be a fresh name.

Let $L$ have one constant symbol $a$ and one unary relation symbol $P$.
Let $\Gamma = \{ \exists x \, P(x), \neg P(a) \}$, where $\exists x \, P(x)$ abbreviates $\neg \forall x \, \neg P(x)$.

1. The set $\Gamma$ is [[consistent|VM8TQ70CVJ]].
   The [[structure|983GZBQYT4]] with universe $\{ 0, 1 \}$, $a = 0$ and $P = \{ 1 \}$ satisfies it, and the [[soundness theorem|AVD7T7J063]] turns a model into consistency.
2. Try the old constant $a$ as the witness.
   The witness axiom is $\exists x \, P(x) \to P(a)$, and modus ponens with $\exists x \, P(x) \in \Gamma$ derives $P(a)$.
   The set also contains $\neg P(a)$, so it is inconsistent.
3. Take instead a new constant $c$ and the witness axiom $\exists x \, P(x) \to P(c)$.
   The structure of step 1 with $c = 1$ satisfies $\Gamma$ together with this axiom, so the set is consistent.
4. Let $\Delta$ be a maximal consistent extension in $L \cup \{ c \}$, from [[Lindenbaum's lemma|SC0BSJ3GT6]].
   It derives $P(c)$ by modus ponens, so it contains $P(c)$, and it contains $\neg P(a)$.
5. Suppose $c = a$ were in $\Delta$.
   The equality axiom $c = a \to (P(c) \to P(a))$ and two uses of modus ponens would put $P(a)$ into $\Delta$, next to $\neg P(a)$, which is impossible.
6. So $\neg (c = a) \in \Delta$, and the term model has two different elements $[a]$ and $[c]$, with $[c] \in P$ and $[a] \notin P$.

## Remarks

The witness axiom is consistent with $\Gamma$ exactly because $\Gamma$ says nothing about $c$.
Any model of $\Gamma$ can interpret $c$ as one of its elements in $P$, and step 3 does exactly that.
The old constant $a$ has no such freedom, since $\Gamma$ already says $\neg P(a)$.

Step 5 shows that the new constant is not a copy of an old term: the Henkin set can force it to differ from every old term.
If we change $\Gamma$ to $\{ \exists x \, P(x) \}$ alone, the witness $a$ would happen to be consistent, but the construction cannot know this in general, so it always takes a fresh constant.

## Explanations

### L1 human

The facts say "something has property $P$" and "the thing called $a$ does not have $P$".
We cannot name $a$ as the thing with $P$, because that contradicts the second fact.
So we invent a fresh name $c$ and say "$c$ has $P$".
Then $c$ and $a$ must be different things.

### L2 human

The witness axiom $\exists x \, P(x) \to P(c)$ adds a name for an element that the theory says exists.
The freshness of $c$ is the only hypothesis that makes the axiom safe, and step 2 shows what happens without it.
This is the step "add witness axioms" in the proof of the [[model existence theorem|G0DTR159RN]].
Watch out: it is tempting to reuse a constant of $\Gamma$ to keep the language small, and that is exactly the move that fails here.

### L3 human

The axiom $\exists x \, P(x) \to P(c)$ with fresh $c$ gives a conservative extension, since $c$ can be interpreted by any witness in any model of $\Gamma$.
In the sequent calculus the same freshness appears as the eigenvariable condition of the left rule for $\exists$.
In Hilbert's epsilon calculus, the term $\varepsilon x \, P(x)$ plays the role of $c$.
