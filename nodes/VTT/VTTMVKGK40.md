---
tag: VTTMVKGK40
kind: example
name: A liar attempt at level one of the Tarskian hierarchy
msc: ["03A05", "03F40"]
topics: [6Q4JJ2MMV8]
audience: grad
instance_of: [Z6MCGB0ZFX]
uses: [Z6MCGB0ZFX, 3PRW76471J, 4A84VHDTHV, 151M7YHAQV]
sources:
  - url: https://plato.stanford.edu/entries/liar-paradox/
    locator: "Liar Paradox, 4.3.1 Typed restrictionist approaches"
---

## Example

Use the languages $\mathcal{L}_0 \subset \mathcal{L}_1 \subset \mathcal{L}_2$ and the models $\mathcal{N}_1, \mathcal{N}_2$ of [[the first levels of the hierarchy|151M7YHAQV]].
We try to build a liar for the predicate $T_1$ and see what the [[Tarskian hierarchy|Z6MCGB0ZFX]] does with it.

1. The [[diagonal lemma|3PRW76471J]] holds in $\mathcal{L}_2$, since its proof uses only arithmetic. Apply it to the formula $\neg T_1(x)$.
2. It gives a sentence $\lambda$ of $\mathcal{L}_2$ with $\mathsf{Q} \vdash \lambda \leftrightarrow \neg T_1(\ulcorner \lambda \urcorner)$, where $\mathsf{Q}$ is taken in $\mathcal{L}_2$.
3. $\mathcal{N}_2$ is a model of $\mathsf{Q}$, so $\mathcal{N}_2 \models \lambda \leftrightarrow \neg T_1(\ulcorner \lambda \urcorner)$ by [[soundness|4A84VHDTHV]].
4. $\lambda$ is built from $\neg T_1(x)$, so it contains $T_1$, and it is not a sentence of $\mathcal{L}_1$.
5. $T_1$ holds in $\mathcal{N}_2$ only of codes of sentences of $\mathcal{L}_1$. By step 4, $\mathcal{N}_2 \models \neg T_1(\ulcorner \lambda \urcorner)$.
6. Steps 3 and 5 give $\mathcal{N}_2 \models \lambda$. So the "liar" is simply true at level 2.
7. In the next model $\mathcal{N}_3$, with $T_2$ for the sentences of $\mathcal{L}_2$, step 6 gives $\mathcal{N}_3 \models T_2(\ulcorner \lambda \urcorner)$.

There is no contradiction.
The T-sentence $T_1(\ulcorner \lambda \urcorner) \leftrightarrow \lambda$ is not an axiom of the hierarchy, because $\lambda$ is not in $\mathcal{L}_1$.
In fact it is false in $\mathcal{N}_2$: its left side is false by step 5 and its right side is true by step 6.

## Remarks

The example shows how the hierarchy blocks the [[liar paradox|KBYY281V8T]]: it allows the liar sentence, but not the T-sentence that would make it paradoxical.
If we apply the diagonal lemma to $\neg T_0(x)$ in $\mathcal{L}_1$ instead, the same steps show that the sentence is true in $\mathcal{N}_1$.
At every level the liar for $T_n$ is a true sentence of level $n + 1$.

## Explanations

### L1 human

At level 2 we can write a sentence that says "I am not true-1".
The word "true-1" only applies to sentences of level 1.
Our sentence contains "true-1", so it is a level-2 sentence, and it is not true-1.
So what it says is correct, and the sentence is true, but only "true-2", not "true-1".
No paradox comes up.

### L2 human

1. Suppose the hierarchy also had the T-sentence $T_1(\ulcorner \lambda \urcorner) \leftrightarrow \lambda$.
2. Together with step 2 of the example, this gives $T_1(\ulcorner \lambda \urcorner) \leftrightarrow \neg T_1(\ulcorner \lambda \urcorner)$.
3. As in the liar paradox, this gives a contradiction.
4. So the restriction of the T-sentences to $\mathcal{L}_1$ is exactly what keeps the theory consistent.

The typical use is to explain why the typed T-sentences are safe.
The trap is to think that the hierarchy forbids the sentence $\lambda$; it only forbids its T-sentence at level 1.
