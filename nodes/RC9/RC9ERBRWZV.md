---
tag: RC9ERBRWZV
kind: example
name: Adding a new constant symbol is a conservative extension
msc: ["03B10", "03C07"]
topics: [H8QZY0RZXZ]
audience: grad
instance_of: [N238J43XNE]
uses: [N238J43XNE, 983GZBQYT4, MVCH6N9SNW, WQ1ZE255SF]
sources:
  - url: https://en.wikipedia.org/wiki/Conservative_extension
    locator: lead section
  - book: isbn:9780122384523
---

## Example

Every proof that begins "fix an arbitrary element $c$" adds a name to the language and then forgets it.
The step is safe because a new name with no axioms is a conservative extension.

Let $T$ be a theory in a first-order language $L$, and let $c$ be a constant symbol that is not in $L$.
Let $T'$ be the same set of sentences $T$, now read as a theory in the language $L' = L \cup \{ c \}$.
We show that $T'$ is a [[conservative extension|N238J43XNE]] of $T$.

1. $T'$ is an extension of $T$, because a derivation from $T$ in $L$ is also a derivation from $T'$ in $L'$.
2. Let $M$ be a [[model|MVCH6N9SNW]] of $T$.
   A [[structure|983GZBQYT4]] has a nonempty domain, so we can choose an element $a$ of $M$.
3. Let $(M, a)$ be the $L'$-structure that agrees with $M$ on $L$ and interprets $c$ as $a$.
4. The truth of an $L$-sentence in $(M, a)$ does not depend on the interpretation of $c$, so every sentence of $T$ is true in $(M, a)$, and $(M, a)$ is a model of $T'$.
5. Let $\sigma$ be an $L$-sentence with $T' \vdash \sigma$.
   By soundness $\sigma$ is true in $(M, a)$, and by the remark in step 4 it is true in $M$.
6. Since $M$ was an arbitrary model of $T$, $\sigma$ is true in every model of $T$, and [[Gödel's completeness theorem|WQ1ZE255SF]] gives $T \vdash \sigma$.

## Remarks

### A proof without models

There is also a purely syntactic proof.
In a derivation of $\sigma$ from $T'$, replace each occurrence of $c$ by a variable that occurs nowhere in the derivation.
The result is a derivation of $\sigma$ from $T$, because $c$ occurs neither in $\sigma$ nor in $T$.
This proof avoids the completeness theorem, so it also works in weak metatheories.

### Adding an axiom about the constant

The example changes when we add an axiom about $c$.
If $T \vdash \exists x\, P(x)$, then $T \cup \{ P(c) \}$ is still conservative over $T$, because $c$ can name a witness.
Henkin's proof of the completeness theorem takes this step many times.
If $T \nvdash \exists x\, P(x)$, then $T \cup \{ P(c) \}$ proves the new $L$-sentence $\exists x\, P(x)$, so it is not conservative.
For example, in the theory of fields the axiom $c \cdot c = 1 + 1$ proves $\exists x\, (x \cdot x = 1 + 1)$, which fails in $\mathbb{Q}$.

## Explanations

### L1 human

A theory about numbers does not change when you give a name, say "Bob", to one of the numbers and say nothing else about Bob.
Whatever you prove about numbers with the name Bob, you could have proved with "some number" instead.
The name is only a label, and labels add no facts.

### L2 human

Let $T$ be the theory of groups in the language $\{ \cdot, e \}$, and add a constant $c$ with no axioms.
In $T'$ we prove $c \cdot e = c$, an instance of the identity axiom.
This sentence uses $c$, so it is allowed to be new.
Replace $c$ by a fresh variable $x$ in the derivation, and it becomes a derivation of $x \cdot e = x$ from the group axioms.
Generalization then gives $\forall x\, (x \cdot e = x)$, a sentence of the old language and a theorem of $T$.
The typical use is in proofs that fix an arbitrary element, and the conservativity of new constants is what makes this step safe.
Watch out for an assumption about $c$ that is not provable for an arbitrary element, such as $c \neq e$ in a theory that has the trivial group as a model.
