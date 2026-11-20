---
tag: H3EK7YJ0B4
kind: example
name: The theory TB is conservative over PA
aliases: [tb-conservative, disquotational-truth-conservative]
msc: ["03F25", "03A05"]
topics: [6Q4JJ2MMV8]
audience: grad
instance_of: [KE8ZX8KVA3]
uses: [KE8ZX8KVA3, HACXBCM7SS, 3K1AKGXF8A]
sources:
  - url: https://plato.stanford.edu/entries/truth-axiomatic/
    locator: "Axiomatic Theories of Truth, 3.2 The T-sentences"
  - book: isbn:9780521115810
---

## Example

Let $\mathsf{TB}$ be [[Peano arithmetic|HACXBCM7SS]] in $\mathcal{L}_T$, with induction for all formulas of $\mathcal{L}_T$.
Its truth axioms are the typed T-sentences $T(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$, for $\varphi$ a sentence without $T$.
It is an [[axiomatic theory of truth|KE8ZX8KVA3]].
We check that every sentence $\chi$ without $T$ that $\mathsf{TB}$ proves is already a theorem of $\mathsf{PA}$.

1. Fix a proof of $\chi$ in $\mathsf{TB}$. It uses T-sentences only for finitely many distinct sentences $\varphi_1, \dots, \varphi_k$.
2. Define the arithmetical formula $\sigma(x) := \bigvee_{i=1}^{k} (x = \ulcorner \varphi_i \urcorner \wedge \varphi_i)$.
3. For a formula $\psi$ of $\mathcal{L}_T$, let $\psi^*$ be the result of replacing each atom $T(t)$ by $\sigma(t)$. We rename bound variables of $\sigma$ where needed.
4. This replacement maps logical axioms to logical axioms. It keeps modus ponens and generalization.
5. An axiom of $\mathsf{PA}$ without $T$ is unchanged by step 3.
6. The induction axiom for $\psi(x)$ becomes the induction axiom for $\psi^*(x)$. This formula has no $T$, so it is an axiom of $\mathsf{PA}$.
7. The T-sentence for $\varphi_j$ becomes $\sigma(\ulcorner \varphi_j \urcorner) \leftrightarrow \varphi_j$.
8. For $i \ne j$, the codes differ, and [[Robinson arithmetic|3K1AKGXF8A]] proves $\ulcorner \varphi_j \urcorner \ne \ulcorner \varphi_i \urcorner$ for distinct numerals.
9. So $\mathsf{PA} \vdash \sigma(\ulcorner \varphi_j \urcorner) \leftrightarrow (\ulcorner \varphi_j \urcorner = \ulcorner \varphi_j \urcorner \wedge \varphi_j)$, and hence $\mathsf{PA} \vdash \sigma(\ulcorner \varphi_j \urcorner) \leftrightarrow \varphi_j$.
10. By steps 4 to 9, the translated proof is a proof in $\mathsf{PA}$ from theorems of $\mathsf{PA}$. Its last line is $\chi^*$.
11. Since $\chi$ has no $T$, $\chi^* = \chi$. So $\mathsf{PA} \vdash \chi$.

## Remarks

The SEP entry states this conservativity, and adds that it holds with induction for $\mathcal{L}_T$; it mentions the compactness theorem as a method.
The argument above is a syntactic version of the same idea: each proof sees only finitely many T-sentences, and these have a definable truth predicate.
Step 8 is the only place where the base theory matters.
The SEP entry notes that over the empty base theory the T-sentences are not conservative.
They prove that $\ulcorner 0 = 0 \urcorner$ and $\ulcorner \neg\, 0 = 0 \urcorner$ differ, so at least two objects exist.
The same argument with the uniform T-sentences gives the conservativity of $\mathsf{UTB}$, which the SEP entry also reports.

## Explanations

### L1 human

The theory $\mathsf{TB}$ adds the word "true" for sentences about numbers.
Any one proof uses only a few of the new axioms.
For a few sentences, an ordinary formula can say "true".
The formula says: "it is the first sentence and it holds, or it is the second sentence and it holds".
Replacing "true" by this formula turns the proof into a proof in plain arithmetic.

### L2 human

1. Suppose a proof uses the T-sentences for $0 = 0$ and $\forall x\, (x = x)$ only.
2. Define $\sigma(x) := (x = \ulcorner 0 = 0 \urcorner \wedge 0 = 0) \vee (x = \ulcorner \forall x (x = x) \urcorner \wedge \forall x (x = x))$.
3. Then $\sigma(\ulcorner 0 = 0 \urcorner)$ is provably equivalent to $0 = 0$, since the two codes are distinct numbers.
4. Replace every $T$ by $\sigma$ in the proof. Each line is now a theorem of $\mathsf{PA}$.

The typical use is the deflationist claim that typed disquotation adds no new content about numbers.
The trap is to think that $\mathsf{TB}$ is as strong as $\mathsf{CT}$; the compositional axioms with induction are not conservative.
