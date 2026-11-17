---
tag: Y8G800QGAZ
kind: example
name: The diagonal Henkin sentence of PA is provable
msc: ["03F40"]
topics: [HXHHWY3328]
audience: grad
instance_of: [SBMQ5QHG9W]
illustrates: [3HD30YG3DG, 3PRW76471J]
uses: [SBMQ5QHG9W, 3HD30YG3DG, 3PRW76471J, NB2BCZR40F, MPSCREYC3M, 4A84VHDTHV]
sources:
  - url: https://en.wikipedia.org/wiki/Löb's_theorem
    locator: lead section
  - book: isbn:9780521857840
---

## Example

Let $T = \mathsf{PA}$, with the standard [[provability predicate|NB2BCZR40F]], and write $\square \varphi$ for $\mathrm{Prov}_{\mathsf{PA}}(\ulcorner \varphi \urcorner)$.
We build a [[Henkin sentence|SBMQ5QHG9W]] and show that it is provable and true.

1. Apply the [[diagonal lemma|3PRW76471J]] to the formula $\mathrm{Prov}_{\mathsf{PA}}(x)$. It gives a sentence $H$ with $\mathsf{PA} \vdash H \leftrightarrow \square H$. So $H$ is a Henkin sentence.
2. From step 1, $\mathsf{PA} \vdash \square H \to H$.
3. By [[Löb's theorem|3HD30YG3DG]], step 2 gives $\mathsf{PA} \vdash H$.
4. $\N$ is a model of $\mathsf{PA}$, so $H$ is true by [[soundness|4A84VHDTHV]].
5. By step 3, $\square H$ is true as well, so what $H$ says is true.

## Remarks

The diagonal lemma gives $H$ explicitly: in the usual construction, $H$ says that the number defined by a fixed formula is the code of a theorem, and that number is the code of $H$.
The proof of $H$ in $\mathsf{PA}$ goes through the derivability conditions, so it is long, although $H$ is short.

## Explanations

### L1 human

The sentence says "I am provable in Peano arithmetic".
Löb's theorem shows that Peano arithmetic does prove it, so what it says is true.

### L2 human

1. Diagonalize $\mathrm{Prov}_{\mathsf{PA}}(x)$.
2. Read off $\square H \to H$.
3. Apply Löb's theorem.

The typical use is as the standard example of Löb's theorem.
A trap: step 2 uses only one direction of the equivalence of step 1.
