---
tag: NB2BCZR40F
kind: concept
name: Provability predicate
msc: ["03F40"]
topics: [HXHHWY3328]
audience: grad
uses: [6M12VR1GT6, MFJXPAF0R0, 3K1AKGXF8A, 92SWXST1ZM]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section P
    note: adopted
    mention: wikipedia://en/76765067#O2L8
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Provability_predicate
    locator: lead section
  - book: isbn:9780521857840
inventory: [808MBHW2M1]
---

## Summary

Let $T$ be a [[first-order theory|92SWXST1ZM]] in the language $\set{0, S, +, \cdot}$ with a decidable set of axioms.
Let $\mathrm{Prf}_T(y, x)$ be a $\Sigma_1$ formula that represents in [[Robinson arithmetic|3K1AKGXF8A]] the relation "$y$ codes a proof in $T$ of the formula with code $x$", as given by [[arithmetization of syntax|6M12VR1GT6]].
The provability predicate of $T$ is the formula $\mathrm{Prov}_T(x) := \exists y \, \mathrm{Prf}_T(y, x)$.
For a sentence $\varphi$, $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$ says "$\varphi$ is provable in $T$", and it is true in $\N$ exactly when $T \vdash \varphi$.
The provability predicate lets $T$ speak about its own theorems, and every incompleteness theorem is about it.

## Motivation

To show that a theory cannot prove some sentence, Gödel needed a sentence that speaks about provability.
The proof relation is decidable, so a formula can express it, but the set of theorems is only computably enumerable.
The unbounded quantifier $\exists y$ in front of the proof relation is exactly what passes from proofs to provability.
This makes $\mathrm{Prov}_T$ a $\Sigma_1$ formula, and the step from $\Sigma_1$ to $\Pi_1$ is where incompleteness lives.

## Notation

1. Gödel wrote $\mathrm{Bew}(x)$, from the German "beweisbar" (provable); see also [[Bew|BF017NCXF4]].
2. Other notations are $\mathrm{Pr}_T(x)$, $\mathrm{Prov}_T(x)$ and $\square_T \varphi$ for $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$.
3. The modal shorthand $\square \varphi$ is set up in the node on the [[derivability conditions|F6H4STF9RG]].
4. We write $\ulcorner \varphi \urcorner$ for the numeral of the [[Gödel number|MFJXPAF0R0]] of $\varphi$.

## Remarks

### Examples

1. [[Robinson arithmetic proves that 0 + 0 = 0 is provable|SVMC76P884]]: an explicit proof gives an explicit witness for $\exists y$.
2. [[Non-standard proofs in a model of PA + ¬Con(PA)|JP0RVCPF38]]: a model can satisfy $\mathrm{Prov}_{\mathsf{PA}}(\ulcorner 0 = S0 \urcorner)$ with no real proof.
3. For $\mathsf{PA}$, the predicate $\mathrm{Prov}_{\mathsf{PA}}$ built from the [[decidable proof relation|QGR9FT4EHP]] is the standard one used in the [[second incompleteness theorem|4PZM5GJTR5]].
4. For a finite theory such as $\mathsf{Q}$, the formula $\mathrm{Ax}_{\mathsf{Q}}(x)$ can be a disjunction of seven equations $x = \underline{a_i}$.

### Non-examples

1. [[The Rosser provability predicate|Z0H1KA8ZHT]] defines the same set of theorems in $\N$ when $T$ is consistent, but it has an extra clause. It cannot satisfy all three derivability conditions, since $T$ proves its consistency statement.
2. For consistent $T \supseteq \mathsf{PA}$, the formula $\mathrm{Prov}_T(x) \wedge \mathrm{Con}(T)$ defines the set of theorems in $\N$. But $T$ proves none of its instances, by the [[second incompleteness theorem|4PZM5GJTR5]], so the first derivability condition fails.
3. The formula $\mathrm{Tr}(x)$, "the sentence with code $x$ is true", is not a provability predicate; by [[Tarski's undefinability theorem|YRV6SYK2BY]] no formula of arithmetic defines truth.

### Basic properties

1. $\mathrm{Prov}_T$ is a $\Sigma_1$ formula, since $\mathrm{Prf}_T$ can be taken $\Delta_0$ or $\Sigma_1$.
2. If $T \vdash \varphi$, then $\mathsf{Q} \vdash \mathrm{Prov}_T(\ulcorner \varphi \urcorner)$. Indeed $\mathsf{Q}$ proves $\mathrm{Prf}_T(\underline{p}, \ulcorner \varphi \urcorner)$ for the code $p$ of a proof. This is the first [[derivability condition|F6H4STF9RG]].
3. The converse of property 2 holds when $T$ is $\Sigma_1$-sound, and it fails for some consistent theories. An example is $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$; see [[ω-consistency|4S29X1GTV4]].
4. The predicate depends on the chosen axiom set, not only on the set of theorems. Two axiom sets with the same theorems can give predicates that $T$ cannot prove equivalent.
5. In a [[non-standard model|1QWN5CV4CG]] of $T$, a witness $y$ of $\mathrm{Prf}_T(y, x)$ can be a non-standard number, which codes no real proof.
6. For $T \supseteq \mathsf{PA}$, the standard predicate satisfies the [[derivability conditions|F6H4STF9RG]], which give the [[second incompleteness theorem|4PZM5GJTR5]] and [[Löb's theorem|3HD30YG3DG]].

### History

Gödel's 1931 paper defined the provability formula $\mathrm{Bew}(x)$ as the last step of its list of arithmetized notions.
Hilbert and Bernays isolated the properties of the predicate that the second incompleteness theorem uses, in the second volume of their Grundlagen der Mathematik (1939).
Feferman studied in 1960 how the second theorem depends on the choice of the formula that defines the axioms.

### Common errors

1. A student reads $T \vdash \mathrm{Prov}_T(\ulcorner \varphi \urcorner)$ as $T \vdash \varphi$. The two are different when $T$ is not $\Sigma_1$-sound.
2. A student thinks that the predicate is determined by the set of theorems. It depends on the formula that presents the axioms.
3. A student forgets the quantifier $\exists y$, and treats $\mathrm{Prov}_T$ as decidable. Only $\mathrm{Prf}_T$ is decidable.

## Explanations

### L1 human

A provability predicate is a formula of arithmetic that says "this statement has a proof".
It speaks about code numbers: "there is a number that codes a proof of the statement with code $n$".
For example, the statement $0 + 0 = 0$ has a short proof, so the formula holds for its code.
The formula cannot be checked by a finite search, since the proof may be very long.

### L2 human

1. Take $T = \mathsf{Q}$ and the sentence $\varphi := 0 + 0 = 0$.
2. A three-line proof of $\varphi$ exists, with code $p$.
3. The relation "$p$ codes a proof of $\varphi$" is true, so by representability $\mathsf{Q} \vdash \mathrm{Prf}_{\mathsf{Q}}(\underline{p}, \ulcorner \varphi \urcorner)$.
4. By the rule for $\exists$, $\mathsf{Q} \vdash \mathrm{Prov}_{\mathsf{Q}}(\ulcorner \varphi \urcorner)$.

The typical use is in a fixed point $G \leftrightarrow \neg \mathrm{Prov}_T(\ulcorner G \urcorner)$ of the [[diagonal lemma|3PRW76471J]].
A trap: $\neg \mathrm{Prov}_T(\ulcorner \varphi \urcorner)$ is a $\Pi_1$ statement, and $T$ need not prove it even when it is true.

### L3 human

The provability predicate is a $\Sigma_1$-definition of a computably enumerable set that is not decidable, and its behaviour inside $T$ is studied by [[provability logic|WJK0YA4GP2]].
For the standard predicate of $\mathsf{PA}$, the modal logic GL describes exactly the schemes that $\mathsf{PA}$ proves about it, by Solovay's theorem.
Non-standard predicates, such as Rosser's or Feferman's, are extensionally the same in $\N$ but satisfy other modal laws.
The idea extends to interpretability predicates and to provability in stronger systems, such as $\omega$-provability, which lead to other modal logics.
