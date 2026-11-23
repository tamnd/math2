---
tag: C8ANFQQ843
kind: example
name: A derivation with the rule of generalization
msc: ["03B10"]
topics: [TTCRX3NFNY]
audience: ug2
instance_of: [N95HV0VWSM]
uses: [2B00FE6K5W, 0Y0MQYST0M]
sources:
  - book: isbn:9781482237726
    locator: Chapter 2
  - url: https://en.wikipedia.org/wiki/Hilbert_system
    locator: Predicate logic (example system)
---

## Example

We work in Mendelson's variant $\mathsf{H}_G$ of the [[Hilbert-style predicate calculus|2B00FE6K5W]].
Its quantifier axioms are $\forall x\, \varphi \to \varphi[t/x]$, with $t$ substitutable for $x$ in $\varphi$, and $\forall x\,(\varphi \to \psi) \to (\varphi \to \forall x\, \psi)$, with $x$ not free in $\varphi$.
Its rules are [[modus ponens|0Y0MQYST0M]] and generalization, which infers $\forall x\, \varphi$ from $\varphi$.
Let $\Gamma = \{ \forall x\,(P(x) \to Q(x)),\ \forall x\, P(x) \}$.
We check a derivation of $\forall x\, Q(x)$ from $\Gamma$.

1. $\forall x\,(P(x) \to Q(x))$, a member of $\Gamma$.
2. $\forall x\,(P(x) \to Q(x)) \to (P(x) \to Q(x))$, the instantiation axiom with $\varphi = P(x) \to Q(x)$ and $t = x$.
3. $P(x) \to Q(x)$, by modus ponens from lines 1 and 2.
4. $\forall x\, P(x)$, a member of $\Gamma$.
5. $\forall x\, P(x) \to P(x)$, the instantiation axiom with $\varphi = P(x)$ and $t = x$.
6. $P(x)$, by modus ponens from lines 4 and 5.
7. $Q(x)$, by modus ponens from lines 6 and 3.
8. $\forall x\, Q(x)$, by generalization of line 7 on the variable $x$.

So $\Gamma \vdash_{\mathsf{H}_G} \forall x\, Q(x)$.

## Remarks

### The informal argument behind it

The derivation follows the argument a mathematician writes: take an arbitrary $x$, use both hypotheses for this $x$, and conclude for all $x$.
Lines 1 to 6 remove the quantifiers, line 7 is propositional, and line 8 puts the quantifier back.
Most short derivations in $\mathsf{H}_G$ have this three-part shape.

### Discharging a hypothesis

Line 8 generalizes on $x$, and $x$ is not free in either hypothesis, because both are sentences.
So the [[deduction theorem for predicate logic|8M9ZFDR4DH]] applies, and it gives
$$\{ \forall x\,(P(x) \to Q(x)) \} \vdash_{\mathsf{H}_G} \forall x\, P(x) \to \forall x\, Q(x).$$
In Enderton's system $\mathsf{H}$ there is no rule of generalization, and the same consequence has a five-line deduction with the distribution axiom instead.

### When a hypothesis has a free variable

Replace the hypothesis $\forall x\, P(x)$ by the formula $P(x)$.
Then lines 4 to 6 shrink to the one line $P(x)$, and line 8 still gives $\forall x\, Q(x)$ in $\mathsf{H}_G$.
So in $\mathsf{H}_G$ a free variable in a hypothesis behaves as if it were universally quantified.
This derivation generalizes on $x$, which is now free in the hypothesis $P(x)$, so the deduction theorem can no longer discharge $P(x)$; [[the counterexample|D3SW6V4R1B]] shows what goes wrong.

## Explanations

### L1 human

The hypotheses say "every $P$ is a $Q$" and "everything is a $P$".
The derivation picks one object $x$, with no special property.
It shows that $x$ is a $P$, and then that $x$ is a $Q$.
Because $x$ was arbitrary, the last line says that everything is a $Q$.
For example, if every dog barks and everything in a room is a dog, then everything in the room barks.

### L2 human

The derivation is a template for many others.
First, remove the quantifiers from the hypotheses with the instantiation axiom, choosing $t = x$.
Second, reason with modus ponens about the single object $x$.
Third, put the quantifier back with generalization.
Watch out at the third step when a hypothesis contains $x$ free.
Generalization is then still a correct step in $\mathsf{H}_G$, but the deduction theorem can no longer discharge that hypothesis.
