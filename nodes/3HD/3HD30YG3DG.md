---
tag: 3HD30YG3DG
kind: statement
role: theorem
name: Löb's theorem
msc: ["03F40", "03F45"]
topics: [HXHHWY3328]
audience: grad
uses: [MPSCREYC3M, MFJXPAF0R0, DKFGQTRYZE, 92SWXST1ZM, TN9G24VABN, NB2BCZR40F, F6H4STF9RG, 3PRW76471J]
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

Löb's theorem says that a theory proves "if $\varphi$ is provable, then $\varphi$" only when it proves $\varphi$ itself.

Let $T$ be a [[theory|92SWXST1ZM]] in the language of arithmetic that contains [[Peano arithmetic|MPSCREYC3M]], with axioms defined by a $\Sigma_1$ formula that defines a decidable set, so that its theorems form a [[computably enumerable|TN9G24VABN]] set.
Let $\mathrm{Prov}_T(x)$ be the standard [[provability predicate|NB2BCZR40F]] of $T$ for a [[Gödel numbering|MFJXPAF0R0]], and write $\square \varphi$ for $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$.

**Theorem (Löb).**

1. For every [[sentence|DKFGQTRYZE]] $\varphi$: if $T \vdash \square \varphi \to \varphi$, then $T \vdash \varphi$.
2. Formalized form: $T \vdash \square (\square \varphi \to \varphi) \to \square \varphi$ for every sentence $\varphi$.

The [[proof of Löb's theorem|6GCSRKJ0SQ]] uses the [[diagonal lemma|3PRW76471J]] and the [[derivability conditions|F6H4STF9RG]].

## Remarks

### The sentence "if I am provable, then 0 = 1"

Write $\bot$ for $0 = S0$, the sentence $0 = 1$.
The diagonal lemma gives a sentence $L$ with
$$T \vdash L \leftrightarrow (\square L \to \bot).$$
So $L$ says "if this sentence is provable, then $0 = 1$".
Since $T$ refutes $\bot$, the right side is equivalent to $\neg \square L$, so $L$ is just a Gödel sentence: "this sentence is not provable".

Now look at the hypothesis of Löb's theorem for $\varphi := \bot$.
It reads $T \vdash \square \bot \to \bot$, and since $T \vdash \neg \bot$, this is the same as $T \vdash \neg \square \bot$, that is, $T \vdash \mathrm{Con}(T)$.
Löb's theorem then gives $T \vdash \bot$.
So if $T$ proves its own consistency, $T$ is inconsistent, which is [[Gödel's second incompleteness theorem|4PZM5GJTR5]].

### The general pattern

For a general $\varphi$, the proof uses the sentence $\psi$ with $T \vdash \psi \leftrightarrow (\square \psi \to \varphi)$, "if I am provable, then $\varphi$".
The derivability conditions show $T \vdash \square \psi \to \square \varphi$.
With the hypothesis $\square \varphi \to \varphi$ this gives $T \vdash \square \psi \to \varphi$, which is $\psi$ itself.
So $T$ proves $\psi$, then $\square \psi$, then $\varphi$.

### Why each hypothesis is needed

The theorem is about the standard predicate.
For the [[Rosser provability predicate|Z0H1KA8ZHT]] $\square^R$, the theory proves $\neg \square^R \bot$, so $T \vdash \square^R \bot \to \bot$, while a consistent $T$ does not prove $\bot$.

The axiom formula must be $\Sigma_1$.
For Feferman's $\Pi_1$ formula $\alpha^*$, $\mathsf{PA}$ proves the consistency statement built from $\alpha^*$, and the same failure occurs with $\varphi := \bot$.

The theory needs enough arithmetic, because the proof uses D2 and D3 inside $T$.
These hold in every extension of $\mathsf{I}\Sigma_1$, so the theorem holds there too.

### What it gives you

The second incompleteness theorem is the case $\varphi := \bot$.
Every [[Henkin sentence|SBMQ5QHG9W]], a sentence $H$ with $T \vdash H \leftrightarrow \square H$, is provable, since $T \vdash \square H \to H$.
And $T$ proves the reflection instance $\square \varphi \to \varphi$ only for the sentences $\varphi$ that it already proves.
So $T$ cannot prove its own soundness, not even one sentence at a time.

### The converse

The converse holds: if $T \vdash \varphi$, then $T \vdash \square \varphi \to \varphi$ by propositional logic.
So $T \vdash \square \varphi \to \varphi$ exactly when $T \vdash \varphi$.

### Generalizations

The formalized form is the axiom of the modal logic $\mathsf{GL}$ of [[provability logic|WJK0YA4GP2]], discussed in [[Löb's axiom in provability logic|QQ6PZFGGB3]].
Solovay proved in 1976 that $\mathsf{GL}$ is exactly the set of modal formulas that $\mathsf{PA}$ proves under every reading of $\square$ as $\mathrm{Prov}_{\mathsf{PA}}$ applied to arithmetic sentences.
The proof works for any predicate that satisfies D1 to D3 in a theory where the diagonal lemma holds.

### Watch out

The hypothesis is that $T$ proves $\square \varphi \to \varphi$, not that this sentence is true.
If $T$ is sound, $\square \varphi \to \varphi$ is true for every $\varphi$, yet $T$ proves it only for its theorems.
For example, $\square \bot \to \bot$ is true for $T = \mathsf{PA}$, and $\mathsf{PA}$ does not prove it.

### Try it

Let $\varphi := \mathrm{Con}(T)$ for a consistent $T$.
Does $T$ prove $\square \mathrm{Con}(T) \to \mathrm{Con}(T)$?
No: by Löb's theorem it would then prove $\mathrm{Con}(T)$, which the second theorem forbids.

Does $T$ prove $\square (0 = 0) \to (0 = 0)$?
Yes, because $T$ proves $0 = 0$, and an implication with a provable conclusion is provable.

## History

Henkin asked in 1952 whether a sentence that asserts its own provability is provable.
Löb answered the question in 1955, in "Solution of a problem of Leon Henkin", by proving this theorem.
Hilbert and Bernays had used conditions of this kind in 1939, and in the same paper Löb gave the derivability conditions their present short form.

## Explanations

### L1 human

Consider the sentence "if this sentence can be proved, then $0 = 1$".
If a theory could prove it, the theory could also follow the argument and conclude $0 = 1$.
Löb's theorem turns this into a general rule.
A theory can prove "if I prove $\varphi$, then $\varphi$ is true" only when it already proves $\varphi$.
So a theory cannot vouch for its own reliability, even about one sentence.

### L2 human

We follow the proof for a given $\varphi$, assuming $T \vdash \square \varphi \to \varphi$.
The diagonal lemma gives $\psi$ with $T \vdash \psi \leftrightarrow (\square \psi \to \varphi)$.
The derivability conditions let $T$ reason: "if $\psi$ is provable, then so is $\square \psi \to \varphi$, and so is $\square \psi$, hence so is $\varphi$".
That gives $T \vdash \square \psi \to \square \varphi$, and with the hypothesis, $T \vdash \square \psi \to \varphi$.
That sentence is $\psi$ itself, so $T \vdash \psi$, then $T \vdash \square \psi$ by D1, and $T \vdash \varphi$.
The typical use is to show that a sentence which refers to its own provability is provable, or that a reflection instance is not provable.
Watch out: the proof has the shape of Curry's paradox, "if this sentence is true, then $\varphi$", and the paradox is avoided only because provability is not truth.

### L3 human

Löb's theorem is the axiom $\square (\square p \to p) \to \square p$ of $\mathsf{GL}$.
A Kripke frame validates $\mathsf{GL}$ exactly when it is transitive and has no infinite chain $w_0 R w_1 R w_2 R \cdots$, so the theorem is a form of induction along a well-founded relation.
The fixed point used in the proof is the same trick as fixed point combinators in the lambda calculus.
