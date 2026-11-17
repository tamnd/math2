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

The claim refuted here is the [[deduction theorem for predicate logic|8M9ZFDR4DH]] for $\mathsf{H}_G$ with no condition on generalization: "if $\Gamma \cup \{\varphi\} \vdash_{\mathsf{H}_G} \psi$, then $\Gamma \vdash_{\mathsf{H}_G} \varphi \to \psi$".
Take a language with one unary relation symbol $P$, and let $\Gamma = \emptyset$, $\varphi = P(x)$ and $\psi = \forall x\, P(x)$.

1. The two lines $P(x)$ and $\forall x\, P(x)$ are a derivation of $\forall x\, P(x)$ from $\{P(x)\}$ in $\mathsf{H}_G$. The first line is a hypothesis and the second line follows by the rule of generalization.
2. So $\{P(x)\} \vdash_{\mathsf{H}_G} \forall x\, P(x)$.
3. Let $\mathcal{M}$ be the [[structure|983GZBQYT4]] with domain $\{0, 1\}$ in which $P$ holds of $0$ and not of $1$. Let $s$ be the assignment with $s(x) = 0$.
4. $\mathcal{M} \models P(x)[s]$, because $s(x) = 0$ and $P$ holds of $0$.
5. $\mathcal{M} \not\models \forall x\, P(x)[s]$, because $P$ does not hold of $1$.
6. So $\mathcal{M} \not\models (P(x) \to \forall x\, P(x))[s]$, by the definition of [[satisfaction|2RBQPV02AS]] for $\to$.
7. Every theorem of $\mathsf{H}_G$ is true in every structure under every assignment, by [[soundness|4A84VHDTHV]].
8. So $\nvdash_{\mathsf{H}_G} P(x) \to \forall x\, P(x)$, and the unrestricted claim fails.

The derivation in step 1 applies generalization with the variable $x$, which is free in the hypothesis $\varphi$, so the restricted theorem does not apply to it.

## Remarks

The counterexample shows that in $\mathsf{H}_G$ a hypothesis with a free variable means its universal closure: $\{P(x)\}$ and $\{\forall x\, P(x)\}$ derive the same formulas.
The formula $\varphi \to \psi$, in contrast, reads $x$ as one fixed object.
If $\varphi$ is replaced by its closure $\forall x\, P(x)$, the restriction holds, and the theorem gives the valid formula $\forall x\, P(x) \to \forall x\, P(x)$.
If the domain has one element, $P(x) \to \forall x\, P(x)$ is true under every assignment, so the countermodel needs at least two elements.
In Enderton's system $\mathsf{H}$, the first line of the counterexample fails instead: $\{P(x)\} \nvdash_{\mathsf{H}} \forall x\, P(x)$.

## Explanations

### L1 human

Let $x$ stand for one unknown person, and assume "$x$ is tall".
The rule of generalization in $\mathsf{H}_G$ lets us conclude "everybody is tall", because it reads the assumption as a claim about every person.
But the sentence "if $x$ is tall, then everybody is tall" is false when $x$ is a tall person in a room that also has a short person.
So we cannot always turn "from A we derive B" into "if A then B".

### L2 human

To check whether the deduction theorem applies to a derivation in $\mathsf{H}_G$, do three things.

1. List the free variables of the discharged hypothesis $\varphi$. Here the list is $x$.
2. Find each step of generalization that depends on $\varphi$. Here it is the step from $P(x)$ to $\forall x\, P(x)$.
3. Check whether its variable is in the list. Here it is, so the theorem does not apply.

A trap is to believe that the derivation is wrong: the derivation is correct, and only the step from it to $\vdash P(x) \to \forall x\, P(x)$ fails.
