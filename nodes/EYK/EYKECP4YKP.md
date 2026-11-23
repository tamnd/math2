---
tag: EYKECP4YKP
kind: example
name: Peano arithmetic is essentially undecidable
aliases: [essential-undecidability-of-peano-arithmetic]
msc: ["03B25", "03F30"]
topics: [E4AVTNWE9E]
audience: grad
instance_of: [9JDDFN8PT7]
uses: [9JDDFN8PT7, 0QFT7Z76N5, 3K1AKGXF8A, RZ42PP37MD, HZ7A7B2ERA]
sources:
  - url: https://en.wikipedia.org/wiki/Peano_axioms
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
    locator: lead section
---

## Example

Peano arithmetic $\mathsf{PA}$ is the theory in the signature $L_A = \{0, S, +, \cdot\}$ given by the first-order [[Peano axioms|0QFT7Z76N5]].
Its axioms are axioms 1, 2 and 4 to 7 of [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$, together with the induction scheme.
The induction scheme contains, for each $L_A$-formula $\varphi(x, \vec{z})$, the universal closure of $(\varphi(0) \wedge \forall x \, (\varphi(x) \to \varphi(S x))) \to \forall x \, \varphi(x)$.
We check that $\mathsf{PA}$ is [[essentially undecidable|9JDDFN8PT7]].

1. $\mathsf{PA}$ is consistent, because the standard structure $(\mathbb{N}, 0, S, +, \cdot)$ satisfies all its axioms.
   Induction holds in $\mathbb{N}$, since every nonempty subset of $\mathbb{N}$ has a least element.
2. Axioms 1, 2 and 4 to 7 of $\mathsf{Q}$ are axioms of $\mathsf{PA}$.
3. Axiom 3 of $\mathsf{Q}$ is $\forall x \, (x \ne 0 \to \exists y \, (x = S y))$.
   We prove it in $\mathsf{PA}$ by induction on $\varphi(x) = (x = 0 \vee \exists y \, (x = S y))$.
4. $\varphi(0)$ holds by its first disjunct.
   For every $x$, $\varphi(S x)$ holds with the witness $y = x$.
5. By the induction axiom for $\varphi$, $\forall x \, \varphi(x)$ holds, and this gives axiom 3.
   So $\mathsf{Q} \subseteq \mathsf{PA}$.
6. Let $T$ be a consistent $L_A$-theory with $\mathsf{PA} \subseteq T$.
   Then $\mathsf{Q} \subseteq T$ by step 5.
7. By the theorem that [[Robinson arithmetic is essentially undecidable|RZ42PP37MD]], $T$ is undecidable.

So every consistent extension of $\mathsf{PA}$ is undecidable, and $\mathsf{PA}$ is essentially undecidable.

## Remarks

The example gives the first incompleteness theorem for $\mathsf{PA}$ in the form of Rosser.
If $T \supseteq \mathsf{PA}$ were consistent, complete and axiomatizable, then $T$ would be decidable by the theorem on [[complete axiomatizable theories|HZ7A7B2ERA]], against step 7.
The example also shows that $\mathsf{PA}$ is hereditarily undecidable, since $\mathsf{Q}$ is finitely axiomatized and every theory contained in a consistent extension of $\mathsf{Q}$ is undecidable.

Drop multiplication and keep the induction scheme for formulas in $0$, $S$ and $+$.
The result is [[Presburger arithmetic|4W0E9G7PPV]], and it is decidable.
So the multiplication axioms 6 and 7, and not induction, carry the undecidability.

## Explanations

### L1 human

Peano arithmetic is the usual list of rules for whole numbers, with "plus one", addition, multiplication and the rule of induction.
No computer can decide all statements that follow from these rules.
Adding more rules does not help, as long as the rules do not contradict each other.
The reason is that the rules contain the seven basic rules of Robinson arithmetic, which already have this property.

### L2 human

We show that $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is undecidable, where $\mathrm{Con}(\mathsf{PA})$ is an arithmetic sentence that expresses the consistency of $\mathsf{PA}$.

1. By Gödel's second incompleteness theorem, $\mathsf{PA}$ does not prove $\mathrm{Con}(\mathsf{PA})$.
   So $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is consistent.
2. It contains $\mathsf{PA}$, hence $\mathsf{Q}$ by step 5.
3. By step 7, it is undecidable.
4. The theory is false in $\mathbb{N}$, so this shows that essential undecidability does not need true axioms.

The typical use is to transfer undecidability to every consistent theory that contains $\mathsf{PA}$, with true or false extra axioms.
Watch out: essential undecidability of $\mathsf{PA}$ does not use the induction scheme, only the axioms of $\mathsf{Q}$.
