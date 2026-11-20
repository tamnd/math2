---
tag: RCGBM5KS25
kind: example
name: Iterated truth of 0 = 0 is grounded
aliases: [grounded-sentence-example]
msc: ["03A05", "03B50"]
topics: [6Q4JJ2MMV8]
audience: grad
not_instance_of:
  - target: 4CBCWZQZ12
    note: the sentence gets the value true at a finite stage of Kripke's construction, so it is true in every fixed point
illustrates: [ES71QTSTNV]
uses: [ES71QTSTNV, SZHA10A9X7]
sources:
  - url: https://plato.stanford.edu/entries/liar-paradox/
    locator: "Liar Paradox, 4.1.1 Paracomplete"
  - url: https://en.wikipedia.org/wiki/Semantic_theory_of_truth
    locator: Kripke's theory of truth
---

## Example

We use the stages $(E_\alpha, A_\alpha)$ of [[Kripke's theory of truth|ES71QTSTNV]], with $(E_0, A_0) = (\emptyset, \emptyset)$.
Let $\varphi_0 := (0 = 0)$ and $\varphi_{n+1} := T(\ulcorner \varphi_n \urcorner)$.
We show that each $\varphi_n$ gets value $1$ at stage $n$, so it is grounded and not a gap.

1. $\|\varphi_0\|_{(E, A)} = 1$ for every pair $(E, A)$, since $0 = 0$ is an arithmetical atomic sentence true in $\mathcal{N}$.
2. So $\ulcorner \varphi_0 \urcorner \in E_1$, by the definition of the jump.
3. Suppose $\ulcorner \varphi_n \urcorner \in E_{n+1}$. Then $\|\varphi_{n+1}\|_{(E_{n+1}, A_{n+1})} = 1$, by the clause for $T$.
4. So $\ulcorner \varphi_{n+1} \urcorner \in E_{n+2}$, by the definition of the jump.
5. By induction on $n$, $\ulcorner \varphi_n \urcorner \in E_{n+1}$ for every $n$.
6. The stages increase, so $\ulcorner \varphi_n \urcorner$ is in the least fixed point $E_\gamma$. So $\varphi_n$ is grounded and has value $1$.
7. The least fixed point is below every fixed point. So $\ulcorner \varphi_n \urcorner \in E$ for every fixed point $(E, A)$, by monotonicity.
8. So $\varphi_n$ is not a truth-value gap in any fixed point.

| stage | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|
| value of $\varphi_0$ | $1$ | $1$ | $1$ | $1$ |
| value of $\varphi_1$ | $\mathrm{u}$ | $1$ | $1$ | $1$ |
| value of $\varphi_2$ | $\mathrm{u}$ | $\mathrm{u}$ | $1$ | $1$ |

## Remarks

Groundedness means that the value comes from facts that do not mention truth, in finitely or transfinitely many steps.
Let $C(x, y)$ represent the function $n \mapsto \ulcorner \varphi_n \urcorner$.
The sentence $\forall x\, \forall y\, (C(x, y) \to T(y))$ has value $\mathrm{u}$ at every finite stage $m$, since $\ulcorner \varphi_m \urcorner \notin E_m \cup A_m$.
It first gets value $1$ at stage $\omega$, and its code enters $E_{\omega + 1}$.
So some grounded sentences need transfinite stages.
Compare the [[liar|XRRGJK0927]], which is a gap in every fixed point.

## Explanations

### L1 human

"$0 = 0$" is true without any talk of truth.
So in the first round, Kripke's construction puts it on the "true" list.
In the next round, "'$0 = 0$' is true" goes on the list, and so on.
Each sentence of this chain gets its value from a fact about numbers.

### L2 human

1. Stage $1$: $0 = 0$ enters $E_1$.
2. Stage $2$: $T(\ulcorner 0 = 0 \urcorner)$ enters $E_2$.
3. Stage $n + 1$: the sentence with $n$ nested $T$ enters $E_{n+1}$.

The typical use is to show what "grounded" means in practice.
The trap is to think that every sentence that contains $T$ is ungrounded.
