---
tag: PWRQX8JKYQ
kind: example
name: Convention T for a propositional language
msc: ["03A05", "03B05"]
topics: [6Q4JJ2MMV8]
audience: grad
instance_of: [8FBF0EFFC9]
uses: [8FBF0EFFC9, TT7WT5HPN9, H31CS3HK5P, 0DSHAVH45F, EDRV3N0SA3]
sources:
  - url: https://plato.stanford.edu/entries/tarski-truth/
    locator: "Tarski's Truth Definitions, 1.3 Material adequacy"
  - url: https://en.wikipedia.org/wiki/Semantic_theory_of_truth
    locator: Criteria for a definition of truth
---

## Example

Let $L$ be the propositional language with atoms $p_0, p_1, p_2, \dots$ and the connectives $\neg$ and $\wedge$.
Fix a [[truth valuation|H31CS3HK5P]] of the atoms, $v \colon \{p_0, p_1, \dots\} \to \{0, 1\}$.
The metalanguage $M$ is informal set theory, with names $\ulcorner A \urcorner$ for the [[formulas|TT7WT5HPN9]] $A$ of $L$.
Each formula of $L$ is a sentence, since $L$ has no variables.
By [[definition by recursion|0DSHAVH45F]] on formulas, let $h$ be the unique function from formulas to $\{0, 1\}$ with $h(p_i) = v(p_i)$, $h(\neg A) = 1 - h(A)$ and $h(A \wedge B) = \min(h(A), h(B))$.
Define
$$\mathrm{True}(x) :\iff x \text{ is a formula of } L \text{ and } h(x) = 1.$$
We check that this is a truth definition in the sense of the [[semantic conception of truth|8FBF0EFFC9]].

1. *Metalanguage.* The definition uses only the syntax of $L$, the valuation $v$ and set theory. It uses no semantic primitive such as "denotes".
2. *Formal correctness.* The definition has the form $\forall x\,(\mathrm{True}(x) \leftrightarrow \varphi(x))$, and $\mathrm{True}$ does not occur in $\varphi$.
3. *Material adequacy, atoms.* For an atom, $\mathrm{True}(\ulcorner p_i \urcorner)$ holds if and only if $v(p_i) = 1$. In this metalanguage, "$p_i$" translates as "$v(p_i) = 1$", so the T-sentence holds.
4. *Material adequacy, negation.* Assume the T-sentence for $A$. Then $\mathrm{True}(\ulcorner \neg A \urcorner)$ iff $h(A) = 0$ iff not $\mathrm{True}(\ulcorner A \urcorner)$ iff not $A^{*}$.
5. *Material adequacy, conjunction.* Assume the T-sentences for $A$ and $B$. Then $\mathrm{True}(\ulcorner A \wedge B \urcorner)$ iff $h(A) = h(B) = 1$ iff $A^{*}$ and $B^{*}$.
6. By [[induction on formulas|EDRV3N0SA3]], steps 3 to 5 give the T-sentence for every formula of $L$.

A concrete case: let $v(p_0) = 1$ and $v(p_1) = 0$.
Then $h(p_0 \wedge \neg p_1) = \min(1, 1 - 0) = 1$.
So $\mathrm{True}(\ulcorner p_0 \wedge \neg p_1 \urcorner)$ holds, and the translation "$v(p_0) = 1$ and $v(p_1) \neq 1$" is also true.

## Remarks

The example shows the two conditions of Tarski in the simplest setting.
Material adequacy is proved one sentence at a time in step 6, by an induction in the meta-theory.
If the metalanguage proves the induction principle for formulas, it also proves the uniform statement "for every formula $x$, $\mathrm{True}(x)$ iff $h(x) = 1$".
Suppose we add to $L$ a predicate $T$ and names for the sentences of $L$.
Then the recursion has no base case for $T(\ulcorner A \urcorner)$, and the [[liar paradox|KBYY281V8T]] blocks any definition of this kind.

## Explanations

### L1 human

Take two simple statements, "it rains" (false today) and "it is cold" (true today).
The rules say: "not A" is true when A is false, and "A and B" is true when both are true.
With these rules we find that "it is cold and it does not rain" is true.
Tarski's test asks that such rules give the right answer for every sentence, and here they do.

### L2 human

1. Let $v(p_0) = 0$, $v(p_1) = 1$, and take $A := \neg(p_0 \wedge p_1)$.
2. Compute $h(p_0 \wedge p_1) = \min(0, 1) = 0$.
3. Compute $h(A) = 1 - 0 = 1$, so $\mathrm{True}(\ulcorner A \urcorner)$.
4. The translation $A^{*}$ is "not ($v(p_0) = 1$ and $v(p_1) = 1$)", and it is true because $v(p_0) = 0$.
5. So both sides of the T-sentence for $A$ are true.

The typical use is as a model for truth definitions of richer languages, such as first-order languages, where satisfaction replaces $h$.
The trap is to confuse the formula $A$ with its name $\ulcorner A \urcorner$.
The predicate $\mathrm{True}$ applies to names, and the right side of the T-sentence uses the sentence itself.
