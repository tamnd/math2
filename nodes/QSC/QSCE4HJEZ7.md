---
tag: QSCE4HJEZ7
kind: statement
role: theorem
name: Extensions by definitions are conservative
msc: ["03B10", "03C07"]
topics: [H8QZY0RZXZ]
audience: grad
about: [GCK0NN60E4, N238J43XNE]
uses: [GCK0NN60E4, N238J43XNE, MVCH6N9SNW, WQ1ZE255SF, CY1TXHF6KQ]
sources:
  - url: https://en.wikipedia.org/wiki/Extension_by_definition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Conservative_extension
    locator: lead section
  - book: isbn:9780122384523
---

## Statement

Let $T$ be a theory, a set of sentences, in a first-order language $L$.
Let $T' = T \cup D$ be an [[extension by definitions|GCK0NN60E4]] of $T$ in the language $L' \supseteq L$.
So $D$ has, for each new relation symbol $R$, an axiom $\forall \bar x\, (R(\bar x) \leftrightarrow \psi_R(\bar x))$.
For each new function symbol $f$, $D$ has an axiom $\forall \bar x\, \forall y\, (f(\bar x) = y \leftrightarrow \psi_f(\bar x, y))$ with $T \vdash \forall \bar x\, \exists ! y\, \psi_f(\bar x, y)$.
The new symbols come in an order in which each definiens uses only symbols of $L$ and earlier new symbols.
The condition on $\psi_f$ is then required in the theory built so far.
Then the following hold.

1. Unique expansion: every [[model|MVCH6N9SNW]] of $T$ has exactly one expansion to an $L'$-structure that is a model of $T'$.
2. Conservativity: for every $L$-sentence $\sigma$, $T' \vdash \sigma$ if and only if $T \vdash \sigma$.
   So $T'$ is a [[conservative extension|N238J43XNE]] of $T$.
3. Eliminability: for every $L'$-formula $\varphi$ there is an $L$-formula $\varphi^*$ with the same free variables such that $T' \vdash \forall \bar z\, (\varphi \leftrightarrow \varphi^*)$.
   Here $\bar z$ lists the free variables of $\varphi$.

## Remarks

### A first case

In arithmetic, define $x \le y$ by $\exists z\, (x + z = y)$.
Part 1 says that $\mathbb{N}$ has only one way to read $\le$, the usual order.
Part 3 turns $\forall x\, (0 \le x)$ into $\forall x\, \exists z\, (0 + z = x)$.
Part 2 says that a theorem with $\le$ and without it in its statement is a theorem of the original theory.

### Why existence and uniqueness are needed

Existence matters for function symbols.
Over the theory of fields, a symbol $s$ with $\forall x\, (s(x) \cdot s(x) = x)$ gives a [[non-conservative extension|ZC5ZTHCPKH]], because $2$ has no square root in $\mathbb{Q}$.

Uniqueness matters too.
Let $T = \{ \exists x\, \exists y\, (x \neq y) \}$ in the pure language of equality.
The formula $y = y$ has existence but not uniqueness, and the axiom $\forall y\, (c = y \leftrightarrow y = y)$ contradicts $T$.

### Why the other hypotheses are needed

The definiens must not use the symbol that it defines.
The "definition" $\forall x\, (R(x) \leftrightarrow \lnot R(x))$ is inconsistent, so it proves every $L$-sentence.

Existence and uniqueness must be provable in $T$, not only true in one model.
Let $T = \varnothing$ in the language $\{ P \}$ and $\psi(y) = P(y)$.
Then the axiom $\forall y\, (c = y \leftrightarrow P(y))$ proves the new $L$-sentence $\exists ! y\, P(y)$.

### Consequences

A theorem proved with defined symbols has a translation into the original language, and the translation is a theorem of $T$.
Defined symbols can be used freely in the instances of a later schema.
For example, the induction schema of PA with $\le$ is equivalent to the induction schema without it.
By part 3, the sets and functions definable in a model of $T$ do not change when $T$ is replaced by $T'$.

### Converse

Part 1 has a converse, by [[Beth's definability theorem|RJBDSA2ETP]].
Let $T'$ be any $L'$-theory that contains $T$, such that every model of $T$ has exactly one expansion to a model of $T'$.
Then each new symbol has an explicit definition in $T'$, and $T'$ has the same models as an extension by definitions of $T$.
Conservativity alone has no such converse: adding a constant with no axioms is conservative, but it is not an extension by definitions.

### Generalizations

The theorem holds for many-sorted logic.
It also holds for new sorts defined as quotients of definable sets by definable equivalence relations.
This gives the construction $T^{\mathrm{eq}}$ of model theory; see [[interpretations and imaginaries|SZRM3N6BXW]].

## History

Shoenfield's textbook *Mathematical Logic* of 1967 states the theorem for first-order theories and proves it syntactically.
Beth proved the definability theorem, which gives the converse of part 1, in 1953.

## Explanations

### L1 human

A definition gives a new word for something we can already describe.
The theorem says three things about such new words.
Every situation that obeys the old rules gives the new word exactly one meaning.
The new word proves no new facts in the old words.
Every sentence with the new word can be rewritten in the old words.

### L2 human

Take the theory of groups and define $i(x)$ as the unique $y$ with $x \cdot y = e \land y \cdot x = e$.

1. Part 1: in the group $\mathbb{Z}$ with $+$ and $0$, the only possible reading of $i$ is $n \mapsto -n$.
2. Part 3: the sentence $\forall x\, (i(i(x)) = x)$ becomes $\forall x\, \exists y\, (x \cdot y = e \land y \cdot x = e \land y \cdot x = e \land x \cdot y = e)$.
   The [[example on group inverses|SZRQRQ5FE9]] does this computation.
3. Part 2: the translation is equivalent to the inverse axiom of groups.
   So it is a theorem of group theory, and the original sentence is a theorem of $T'$.

The typical use is to prove a statement with convenient notation and then to know that it holds in the original theory.
Watch out: do not apply the theorem to a function symbol before the uniqueness proof is done.

### L3 human

The three parts are the semantic, the proof-theoretic and the syntactic faces of one fact: a defined symbol is determined by the old structure.
The semantic face is unique expansion, the proof-theoretic face is conservativity, and the syntactic face is the translation $\varphi \mapsto \varphi^*$.
The same pattern returns in [[relative consistency proofs|X3G0RG2GPZ]], where an interpretation translates one theory into another, and in the definitional equivalence of theories.
