---
tag: ~c0b3bb9c
kind: concept
name: Essential undecidability
aliases: [essentially-undecidable-theory, hereditarily-undecidable-theory, hereditary-undecidability]
msc: ["03B25", "03D35"]
topics: [E4AVTNWE9E]
audience: grad
uses: [HWC687ES0Q, 92SWXST1ZM, VM8TQ70CVJ, 655K8Y7VS8, 3K1AKGXF8A, ~269dc6e7]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Decidability_(logic)
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Undecidability
  - book: isbn:9780521701464
---

## Summary

Let $L$ be a signature with a computable coding of its sentences, and let $T$ be a [[consistent|VM8TQ70CVJ]] [[theory|92SWXST1ZM]] in $L$, closed under logical consequence.
$T$ is essentially undecidable when every consistent theory $T'$ in $L$ with $T \subseteq T'$ is undecidable, in the sense of [[decidable theories|HWC687ES0Q]].
$T$ is hereditarily undecidable when every theory $T''$ in $L$ with $T'' \subseteq T$ is undecidable.
Essential undecidability is the property that survives the addition of axioms, so it is the tool to show that whole families of theories, such as all theories of arithmetic, are undecidable.

## Motivation

Gödel's incompleteness theorem shows that a consistent axiomatizable theory that contains enough arithmetic is incomplete.
Tarski, Mostowski and Robinson asked which theories have this property in a form that survives new axioms.
If a theory is undecidable, one cannot conclude that its extensions are undecidable: the empty theory of a binary relation is undecidable, but the theory of a one-element structure extends it and is decidable.
An essentially undecidable theory blocks every escape by new axioms.
Combined with interpretations, it then gives the undecidability of group theory, ring theory and field theory from one source, [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$.

## Notation

Tarski, Mostowski and Robinson write $\mathsf{Q}$ for Robinson arithmetic and $\mathsf{R}$ for a weaker theory with infinitely many axioms.
The theory $\mathsf{R}$ is in the signature $\set{0, S, +, \cdot, \le}$, and for natural numbers $n, m$ it has the axioms $\bar{n} + \bar{m} = \overline{n + m}$, $\bar{n} \cdot \bar{m} = \overline{n m}$, $\bar{n} \ne \bar{m}$ for $n \ne m$, $\forall x \, (x \le \bar{n} \to x = \bar{0} \vee \cdots \vee x = \bar{n})$ and $\forall x \, (x \le \bar{n} \vee \bar{n} \le x)$.
Here $\bar{n}$ is the numeral $S \cdots S 0$ with $n$ copies of $S$.
Some books use "strongly undecidable" for hereditarily undecidable.

## Remarks

### Examples

1. [[Robinson arithmetic is essentially undecidable|~2685d084]]. This is the basic example, and it is proved by diagonalization.
2. [[Peano arithmetic is essentially undecidable|~5914e62b]], because each consistent extension of $\mathsf{PA}$ is a consistent extension of $\mathsf{Q}$.
3. [[True arithmetic is essentially and hereditarily undecidable|~0d1ea341]]. It is complete, so its only consistent extension in its signature is itself.
4. Robinson's theory $\mathsf{R}$ is essentially undecidable, because every computable relation is representable in it, and the proof for $\mathsf{Q}$ applies.
5. The theory of the ring $\Z$ is hereditarily undecidable, by the [[transfer theorem|~e4c9e250]] and Lagrange's four-square theorem.

### Non-examples

1. [[The theory of groups is not essentially undecidable|~55bc8a72]]. It is undecidable, but the theory of the trivial group is a decidable consistent extension.
2. [[Presburger arithmetic|~14d8268c]] is decidable, so it is not essentially undecidable. The condition fails at $T' = T$.
3. An inconsistent theory is not essentially undecidable in the sense here, which requires consistency of $T$.

### Basic properties

1. An essentially undecidable theory is undecidable, by taking $T' = T$.
2. A consistent theory $T$ is essentially undecidable exactly when it has no complete, consistent, decidable extension. If $T'$ is decidable and consistent, list the sentences and add each one or its negation, keeping consistency; this is computable, since each stage adds finitely many sentences.
3. By the theorem on [[complete axiomatizable theories|~269dc6e7]], an essentially undecidable theory has no complete, consistent, axiomatizable extension. So it is essentially incomplete, which is the Gödel-Rosser theorem for $\mathsf{Q}$.
4. If $T$ is essentially undecidable and finitely axiomatizable, then every theory $T''$ such that $T'' \cup T$ is consistent is undecidable. In particular every consistent extension of $T$ is hereditarily undecidable.
5. If an essentially undecidable theory is interpretable in a consistent theory $T_2$, then $T_2$ is essentially undecidable; see the [[transfer theorem for undecidability|~e4c9e250]].

### History

Tarski, Mostowski and Robinson introduced essential and hereditary undecidability in their book Undecidable Theories of 1953.
They introduced the theories $\mathsf{Q}$ and $\mathsf{R}$ there, and they developed the method of interpretations.
Julia Robinson proved in 1949 that the field of rational numbers defines the integers, which gives the undecidability of the theory of fields.

### Common errors

- Confusing essential undecidability with undecidability. The theory of groups is undecidable, but some of its consistent extensions are decidable.
- Forgetting consistency. Every theory has the inconsistent theory, the set of all sentences, as an extension, and that theory is decidable.
- Extending the signature. Essential undecidability is about extensions in the same signature; in a larger signature, one reduces to the original signature as in the transfer theorem.

## Explanations

### L1 human

Some collections of rules are so strong that no computer can sort all statements into "follows" and "does not follow".
For most such collections, adding more rules can help, for example a rule that says "there is only one object".
An essentially undecidable collection is one where no addition of rules helps, as long as the rules do not contradict each other.
Seven simple rules about $0$, "plus one", addition and multiplication already have this property.

### L2 human

We show that the theory $T$ of commutative rings is undecidable, with the transfer theorem.

1. Robinson arithmetic $\mathsf{Q}$ is essentially undecidable and has seven axioms.
2. By Lagrange's four-square theorem, an integer $x$ is a natural number exactly when $x = a^2 + b^2 + c^2 + d^2$ for some integers $a, b, c, d$.
3. So the natural numbers, with $0$, $x \mapsto x + 1$, $+$ and $\cdot$, are defined inside the ring $\Z$ by first-order formulas.
4. This structure is a model of $\mathsf{Q}$, so $\mathsf{Q}$ is interpretable in the ring $\Z$.
5. The ring $\Z$ is commutative, so the theory $T$ of commutative rings is true in $\Z$.
6. The transfer theorem now says that $T$ is undecidable, and so is every theory true in $\Z$.

The typical use of essential undecidability is this chain: find an interpretation of $\mathsf{Q}$, then conclude undecidability.
A trap is to conclude essential undecidability of $T$ from step 6; the theory of commutative rings has the decidable extension of the theory of the field with two elements.

### L3 human

Essential undecidability is the computational form of incompleteness: a consistent theory is essentially undecidable exactly when it has no consistent, complete, decidable extension.
For theories that interpret $\mathsf{Q}$, it explains at once Gödel's first incompleteness theorem, Church's theorem, and the undecidability of many algebraic theories.
The search for minimal essentially undecidable theories led to $\mathsf{R}$, to theories of concatenation, and to the study of the lattice of interpretability degrees.
A related notion is a theory whose theorems and refutable sentences form a pair of computably inseparable sets; $\mathsf{Q}$ has this stronger property.
