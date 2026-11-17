---
tag: 3HD30YG3DG
kind: statement
role: theorem
name: Löb's theorem
msc: ["03F40", "03F45"]
topics: [HXHHWY3328]
audience: grad
uses: [0QFT7Z76N5, MFJXPAF0R0, DKFGQTRYZE, 92SWXST1ZM, TN9G24VABN, NB2BCZR40F, ~abdd9e6a, 3PRW76471J]
about: [NB2BCZR40F]
history:
  first_stated: "Löb, 1955, Solution of a problem of Leon Henkin, Journal of Symbolic Logic"
  notes: "Henkin asked in 1952 whether a sentence that asserts its own provability is provable."
sources:
  - url: https://en.wikipedia.org/wiki/Löb's_theorem
    locator: lead section
  - book: isbn:9780521857840
  - book: isbn:9780521701464
same_as:
  wikidata: Q204884
  wikipedia: Löb's theorem
---

## Statement

Let $T$ be a [[theory|92SWXST1ZM]] in the language of arithmetic that contains the [[Peano axioms|0QFT7Z76N5]], with axioms given by a $\Sigma_1$ formula that defines a decidable set, so that its theorems form a [[computably enumerable|TN9G24VABN]] set.
Let $\mathrm{Prov}_T(x)$ be the standard [[provability predicate|NB2BCZR40F]] of $T$ for a [[Gödel numbering|MFJXPAF0R0]], and write $\square \varphi$ for $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$.

1. For every [[sentence|DKFGQTRYZE]] $\varphi$: if $T \vdash \square \varphi \to \varphi$, then $T \vdash \varphi$.
2. Formalized form: $T \vdash \square (\square \varphi \to \varphi) \to \square \varphi$ for every sentence $\varphi$.

The proof is in [[the proof of Löb's theorem|~e333036d]].

## Remarks

### Why each hypothesis is needed

1. The standard predicate: for the [[Rosser provability predicate|~55c1b89b]] $\square^R$, $T$ proves $\neg \square^R (0 = S0)$, so $T \vdash \square^R (0 = S0) \to 0 = S0$, while a consistent $T$ does not prove $0 = S0$.
2. The $\Sigma_1$ axiom formula: for Feferman's $\Pi_1$ formula $\alpha^*$, $\mathsf{PA}$ proves $\mathrm{Con}_{\alpha^*}$, and the same failure occurs with $\varphi := (0 = S0)$.
3. Enough arithmetic: the proof uses the [[derivability conditions|~abdd9e6a]] D2 and D3. They hold for extensions of $\mathsf{I}\Sigma_1$, so the theorem holds there too.

### Consequences

1. [[Gödel's second incompleteness theorem|~c79a35b5]]: if $T \vdash \mathrm{Con}(T)$, then $T \vdash \square (0 = S0) \to 0 = S0$, so $T \vdash 0 = S0$.
2. Every [[Henkin sentence|SBMQ5QHG9W]], a sentence $H$ with $T \vdash H \leftrightarrow \square H$, is provable in $T$.
3. $T$ proves the local reflection $\square \varphi \to \varphi$ only for the sentences $\varphi$ that it proves. So $T$ cannot prove its own soundness, even one sentence at a time.

### Converse

The converse holds and is immediate: if $T \vdash \varphi$, then $T \vdash \square \varphi \to \varphi$, by logic.
So $T \vdash \square \varphi \to \varphi$ exactly when $T \vdash \varphi$.

### Generalizations

1. The formalized form is the axiom of the modal logic $\mathsf{GL}$ of [[provability logic|WJK0YA4GP2]]; see [[Löb's theorem in provability logic|QQ6PZFGGB3]].
2. Solovay proved in 1976 that $\mathsf{GL}$ is exactly the set of modal formulas that $\mathsf{PA}$ proves under every interpretation of $\square$ as $\mathrm{Prov}_{\mathsf{PA}}$.
3. The proof works for any predicate that satisfies D1 to D3 in a theory where the diagonal lemma holds.

## History

Henkin asked in 1952 whether a sentence that asserts its own provability is provable.
Löb answered the question in 1955, in "Solution of a problem of Leon Henkin", by proving this theorem.
In the same paper he gave the derivability conditions in their present simple form.

## Explanations

### L1 human

A theory can never prove "if I prove $\varphi$, then $\varphi$ is true" unless it already proves $\varphi$ itself.
So a theory cannot vouch for its own soundness, even one sentence at a time.

### L2 human

1. Assume $T \vdash \square \varphi \to \varphi$.
2. The diagonal lemma gives $\psi$ that says "if I am provable, then $\varphi$".
3. The derivability conditions show that $T$ proves "if $\psi$ is provable, then $\varphi$ is provable", so with step 1, "if $\psi$ is provable, then $\varphi$".
4. That is $\psi$ itself, so $T \vdash \psi$, then $T \vdash \square \psi$, then $T \vdash \varphi$.

The typical use is to show that a sentence which refers to its own provability is provable, or that a reflection statement is not provable.
A trap: the hypothesis is provability of $\square \varphi \to \varphi$ in $T$, not its truth; it is true for every $\varphi$ when $T$ is sound.

### L3 human

Löb's theorem says that the provability operator obeys the induction principle of well-founded relations: the formalized form is the modal version of "every non-empty set has a minimal element".
This is why $\mathsf{GL}$ is valid on a Kripke frame exactly when the frame is transitive and has no infinite ascending chain.
The proof has the same form as Curry's paradox and as fixed point combinators in the lambda calculus.
