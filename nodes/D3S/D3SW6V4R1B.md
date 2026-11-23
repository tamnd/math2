---
tag: D3SW6V4R1B
kind: counterexample
name: The deduction theorem fails without the restriction on generalization
msc: ["03B10"]
topics: [TTCRX3NFNY]
audience: ug2
uses: [8M9ZFDR4DH, 2B00FE6K5W, 983GZBQYT4, 2RBQPV02AS, 4A84VHDTHV]
sources:
  - url: https://en.wikipedia.org/wiki/Deduction_theorem
    locator: The deduction theorem in predicate logic
  - book: isbn:9781482237726
    locator: Chapter 2
---

## Counterexample

In Mendelson's calculus $\mathsf{H}_G$ the hypothesis $P(x)$ derives $\forall x\, P(x)$, but $P(x) \to \forall x\, P(x)$ is not a theorem.
So the [[deduction theorem for predicate logic|8M9ZFDR4DH]] fails for $\mathsf{H}_G$ if we drop its condition on generalization.
The claim that fails is "if $\Gamma \cup \{ \varphi \} \vdash_{\mathsf{H}_G} \psi$, then $\Gamma \vdash_{\mathsf{H}_G} \varphi \to \psi$".
Take a language with one unary relation symbol $P$, and let $\Gamma = \emptyset$, $\varphi = P(x)$ and $\psi = \forall x\, P(x)$.

1. The two lines $P(x)$ and $\forall x\, P(x)$ are a derivation of $\forall x\, P(x)$ from $\{ P(x) \}$ in $\mathsf{H}_G$, as defined in the [[Hilbert-style predicate calculus|2B00FE6K5W]].
   The first line is a hypothesis, and the second line follows by the rule of generalization.
2. So $\{ P(x) \} \vdash_{\mathsf{H}_G} \forall x\, P(x)$.
3. Let $\mathcal{M}$ be the [[structure|983GZBQYT4]] with domain $\{ 0, 1 \}$ in which $P$ holds of $0$ and not of $1$.
   Let $s$ be the assignment with $s(x) = 0$.
4. $\mathcal{M} \models P(x)[s]$, because $s(x) = 0$ and $P$ holds of $0$.
5. $\mathcal{M} \not\models \forall x\, P(x)[s]$, because $P$ does not hold of $1$.
6. So $\mathcal{M} \not\models (P(x) \to \forall x\, P(x))[s]$, by the definition of [[satisfaction|2RBQPV02AS]] for $\to$.
7. Every theorem of $\mathsf{H}_G$ is true in every structure under every assignment, by [[soundness|4A84VHDTHV]].
8. So $\nvdash_{\mathsf{H}_G} P(x) \to \forall x\, P(x)$, and the unrestricted claim fails.

The derivation in step 1 applies generalization to the variable $x$, which is free in the hypothesis $\varphi$.
So the restricted theorem makes no claim about it.

## Remarks

### What a free variable in a hypothesis means

In $\mathsf{H}_G$ a hypothesis with a free variable acts like its universal closure.
The sets $\{ P(x) \}$ and $\{ \forall x\, P(x) \}$ derive the same formulas: generalization gives one direction, and the axiom $\forall x\, P(x) \to P(x)$ gives the other.
The formula $P(x) \to \forall x\, P(x)$ reads $x$ in a different way, as one fixed object.
The deduction theorem would identify these two readings, and that is why it fails.

### How to repair it

If we replace $\varphi$ by its closure $\forall x\, P(x)$, the variable $x$ is no longer free in the hypothesis, and the restriction holds.
The theorem then gives $\vdash_{\mathsf{H}_G} \forall x\, P(x) \to \forall x\, P(x)$, which is valid.

### Why the countermodel has two elements

If the domain has one element, then $P(x) \to \forall x\, P(x)$ is true under every assignment, because $P$ holds of the one element or of nothing.
So every countermodel needs at least two elements, one with $P$ and one without.

### The other Hilbert system

In Enderton's system $\mathsf{H}$ the failure happens at step 2 instead.
The same structure $\mathcal{M}$ and assignment $s$ satisfy $P(x)$ and not $\forall x\, P(x)$, so soundness gives $\{ P(x) \} \nvdash_{\mathsf{H}} \forall x\, P(x)$.
This is why the deduction theorem for $\mathsf{H}$ needs no condition.

## Explanations

### L1 human

Let $x$ stand for one unknown person, and assume "$x$ is tall".
The rule of generalization in $\mathsf{H}_G$ lets us conclude "everybody is tall", because it reads the assumption as a claim about every person.
But the sentence "if $x$ is tall, then everybody is tall" is false when $x$ is a tall person in a room that also has a short person.
So we cannot always turn "from A we derive B" into "if A then B".

### L2 human

To check whether the deduction theorem applies to a derivation in $\mathsf{H}_G$, we first list the free variables of the hypothesis $\varphi$ that we want to discharge.
Here the list is $x$.
Next we find each step of generalization that depends on $\varphi$.
Here there is one, the step from $P(x)$ to $\forall x\, P(x)$.
Last we check whether the variable of that step is in the list.
Here it is, so the theorem does not apply.
Watch out: the derivation in step 1 is correct.
Only the step from it to $\vdash P(x) \to \forall x\, P(x)$ fails.
