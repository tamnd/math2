---
tag: 9JDDFN8PT7
kind: concept
name: Essential undecidability
aliases: [essentially-undecidable-theory, hereditarily-undecidable-theory, hereditary-undecidability]
msc: ["03B25", "03D35"]
topics: [E4AVTNWE9E]
audience: grad
uses: [HWC687ES0Q, 92SWXST1ZM, VM8TQ70CVJ, 655K8Y7VS8, 3K1AKGXF8A, HZ7A7B2ERA]
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

A theory is essentially undecidable when no consistent set of new axioms can make it decidable.

Let $L$ be a signature with a computable coding of its sentences, and let $T$ be a [[consistent|VM8TQ70CVJ]] [[theory|92SWXST1ZM]] in $L$, closed under logical consequence.
$T$ is essentially undecidable when every consistent theory $T'$ in $L$ with $T \subseteq T'$ is undecidable, in the sense of [[decidable theories|HWC687ES0Q]].
$T$ is hereditarily undecidable when every theory $T''$ in $L$ with $T'' \subseteq T$ is undecidable.
An equivalent form: a consistent theory is essentially undecidable exactly when it has no complete, consistent, decidable extension.

## Motivation

Gödel's incompleteness theorem shows that a consistent axiomatizable theory that contains enough arithmetic is incomplete.
Tarski, Mostowski and Robinson asked which theories are undecidable in a form that survives new axioms.
Plain undecidability does not survive: the theory with no axioms in one binary relation is undecidable, but the theory of a one-element structure extends it and is decidable.
An essentially undecidable theory blocks every escape by new axioms.

Combined with interpretations, one essentially undecidable theory gives the undecidability of many others.
From [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$ alone one gets the undecidability of group theory, ring theory, field theory and set theory.
The same idea returns in computability as pairs of computably inseparable sets, and in proof theory as the study of weak arithmetics.

## Notation

Tarski, Mostowski and Robinson write $\mathsf{Q}$ for Robinson arithmetic and $\mathsf{R}$ for a weaker theory with infinitely many axioms.
The theory $\mathsf{R}$ is in the signature $\{0, S, +, \cdot, \le\}$, and $\bar{n}$ is the numeral $S \cdots S 0$ with $n$ copies of $S$.
For all natural numbers $n, m$ it has the axioms $\bar{n} + \bar{m} = \overline{n + m}$, $\bar{n} \cdot \bar{m} = \overline{n m}$, $\bar{n} \ne \bar{m}$ for $n \ne m$, $\forall x \, (x \le \bar{n} \to x = \bar{0} \vee \cdots \vee x = \bar{n})$ and $\forall x \, (x \le \bar{n} \vee \bar{n} \le x)$.
Some books say "strongly undecidable" for hereditarily undecidable.

## Remarks

### A first example: arithmetic

[[Robinson arithmetic is essentially undecidable|RZ42PP37MD]], and this is the basic example, proved by diagonalization.
Its seven axioms prove every true equation between numerals, such as $\bar{2} \cdot \bar{3} = \bar{6}$, and this is enough to represent every computable function.
[[Peano arithmetic is essentially undecidable|EYKECP4YKP]], because each consistent extension of $\mathsf{PA}$ is a consistent extension of $\mathsf{Q}$.
[[True arithmetic is essentially and hereditarily undecidable|2XXRT73422]].
It is complete, so its only consistent extension in its signature is itself.
Robinson's theory $\mathsf{R}$ is essentially undecidable too, because every computable relation is representable in it, and the proof for $\mathsf{Q}$ applies.

### More examples by interpretation

The theory of the ring $\mathbb{Z}$ is hereditarily undecidable, by the [[transfer theorem|FMB2C20G8W]].
The key is Lagrange's four-square theorem: an integer is a natural number exactly when it is a sum of four squares.
For example $7 = 2^2 + 1^2 + 1^2 + 1^2$, while $-1$ is no such sum, since squares are not negative.
So the natural numbers are first-order definable in the ring $\mathbb{Z}$, and $\mathsf{Q}$ is interpretable in it.

### What it is not

[[The theory of groups is not essentially undecidable|8FYX4VNRW8]].
It is undecidable, but the theory of the trivial group is a decidable consistent extension.
[[Presburger arithmetic|4W0E9G7PPV]] is decidable, so the condition already fails at $T' = T$.
An inconsistent theory is not essentially undecidable here, since the definition asks for consistency of $T$.

### The rules you can use

An essentially undecidable theory is undecidable, by taking $T' = T$.

The equivalent form in the Summary holds by an effective Lindenbaum construction.
If $T'$ is a decidable consistent extension, list the sentences and add each one or its negation, keeping consistency.
Each test asks whether $T'$ proves the negation of a finite conjunction, which is decidable, so the complete extension is decidable too.

By the theorem on [[complete axiomatizable theories|HZ7A7B2ERA]], an essentially undecidable theory has no complete, consistent, axiomatizable extension.
So it is essentially incomplete, and for $\mathsf{Q}$ this is the Gödel-Rosser theorem.

If $T$ is essentially undecidable and finitely axiomatizable with axiom $A$, then every theory $T''$ such that $T'' \cup T$ is consistent is undecidable.
Indeed, if $T''$ were decidable, then the sentences $\sigma$ with $(A \to \sigma) \in T''$ would form a decidable consistent extension of $T$.
In particular every consistent extension of $T$ is hereditarily undecidable.

If an essentially undecidable theory is interpretable in a consistent theory $T_2$, then $T_2$ is essentially undecidable, by the [[transfer theorem for undecidability|FMB2C20G8W]].

### Watch out

Do not confuse essential undecidability with undecidability.
The theory of groups is undecidable, but its extension by the axiom $\forall x \, (x = e)$ is decidable.

Do not forget consistency.
Every theory has the inconsistent theory, the set of all sentences, as an extension, and that theory is decidable.

### History

Tarski, Mostowski and Robinson introduced essential and hereditary undecidability in their book Undecidable Theories of 1953.
They introduced the theories $\mathsf{Q}$ and $\mathsf{R}$ there, and they developed the method of interpretations.
Julia Robinson proved in 1949 that the field of rational numbers defines the integers, which gives the undecidability of the theory of fields.

### Try it

Is the theory of the field $\mathbb{F}_2$ with two elements essentially undecidable?
No: it is complete and decidable by evaluation in the finite field, so it is its own decidable consistent extension.

Does essential undecidability pass to extensions in a larger signature $L' \supseteq L$?
Yes: if $T'$ in $L'$ were decidable and consistent, the sentences of $L$ in $T'$ would form a decidable consistent extension of $T$.

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
3. So the natural numbers, with $0$, $x \mapsto x + 1$, $+$ and $\cdot$, are defined inside the ring $\mathbb{Z}$ by first-order formulas.
4. This structure is a model of $\mathsf{Q}$, so $\mathsf{Q}$ is interpretable in the ring $\mathbb{Z}$.
5. The ring $\mathbb{Z}$ is commutative, so the theory $T$ of commutative rings is true in $\mathbb{Z}$.
6. The transfer theorem now says that $T$ is undecidable, and so is every theory true in $\mathbb{Z}$.

The typical use of essential undecidability is this chain: find an interpretation of $\mathsf{Q}$, then conclude undecidability.
Watch out: step 6 does not make $T$ essentially undecidable, since the theory of the field with two elements is a decidable extension of it.

### L3 human

Essential undecidability is the computational form of incompleteness: a consistent theory is essentially undecidable exactly when it has no consistent, complete, decidable extension.
For theories that interpret $\mathsf{Q}$, it explains at once Gödel's first incompleteness theorem, Church's theorem and the undecidability of many algebraic theories.
The search for minimal essentially undecidable theories led to $\mathsf{R}$, to theories of concatenation, and to the study of the lattice of interpretability degrees.
A related notion is a theory whose theorems and refutable sentences form a pair of computably inseparable sets, and $\mathsf{Q}$ has this stronger property.
