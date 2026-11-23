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
We build the sentence "I am provable in $\mathsf{PA}$", show that it is a [[Henkin sentence|SBMQ5QHG9W]], and show that it is provable and true.

1. Apply the [[diagonal lemma|3PRW76471J]] to the formula $\mathrm{Prov}_{\mathsf{PA}}(x)$.
   It gives a sentence $H$ with $\mathsf{PA} \vdash H \leftrightarrow \square H$, so $H$ is a Henkin sentence.
2. The direction from right to left in step 1 is $\mathsf{PA} \vdash \square H \to H$.
3. Step 2 is the hypothesis of [[Löb's theorem|3HD30YG3DG]] for $\varphi := H$, so $\mathsf{PA} \vdash H$.
4. $\mathbb{N}$ is a model of $\mathsf{PA}$, so $H$ is true in $\mathbb{N}$, by [[soundness|4A84VHDTHV]].
5. By step 3, a real proof of $H$ exists, so $\square H$ is true in $\mathbb{N}$ as well.
   So what $H$ says is true, as it must be for a true sentence that is equivalent to $\square H$.

## Remarks

The diagonal lemma gives $H$ explicitly.
In the usual construction, $H$ says that the number named by a fixed term is the code of a theorem, and that number is the code of $H$ itself.
So $H$ is a short sentence, but its proof in $\mathsf{PA}$ runs through the derivability conditions and is long.

Step 2 uses only one direction of step 1.
So any sentence $H$ with $\mathsf{PA} \vdash \square H \to H$ is provable, whether or not the other direction holds.
If the predicate is changed, for example to $\mathrm{Prov}_{\mathsf{PA}}(x) \wedge \mathrm{Con}(\mathsf{PA})$, step 3 is no longer available, and the diagonal sentence for that predicate is unprovable.

## Explanations

### L1 human

The sentence says "I am provable in Peano arithmetic".
Löb's theorem shows that Peano arithmetic does prove it.
So the sentence was telling the truth.

### L2 human

We run the three moves in order.
Diagonalize $\mathrm{Prov}_{\mathsf{PA}}(x)$ to get $H$ with $\mathsf{PA} \vdash H \leftrightarrow \square H$.
Read off the direction $\square H \to H$.
Apply Löb's theorem to get $\mathsf{PA} \vdash H$.
The typical use is as the standard first example of Löb's theorem.
Watch out: the argument "$H$ is provable because it says so" is not a proof, and the real proof needs Löb's theorem.
