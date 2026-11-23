---
tag: E007FEBHYD
kind: example
name: An equivalence over ACA0 is not a reverse mathematics result
msc: ["03B30"]
topics: [BY8AAFN7C5]
audience: grad
not_instance_of:
  - target: 7SQS69T17R
    note: the base theory ACA0 already proves the theorem, so the equivalence measures no strength
uses: [7SQS69T17R, TQTDKMBJ0F, HV153Y95MQ, KRS3VTWCHJ, 3P2J5NWCM1, 8B045KSKW5]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: General principles
---

## Example

Let $\mathrm{HB}$ be the Heine-Borel theorem for countable covers of $[0, 1]$ by open intervals, and let $\mathrm{BW}$ be the Bolzano-Weierstrass theorem, both coded in $L_2$.
We check that $\mathsf{ACA}_0 \vdash \mathrm{HB} \leftrightarrow \mathrm{BW}$, and that this equivalence is not a classification in the sense of [[reverse mathematics|TQTDKMBJ0F]].

1. $\mathsf{ACA}_0$ proves $\mathrm{BW}$, by the [[Bolzano-Weierstrass equivalence|HV153Y95MQ]].
2. $\mathsf{ACA}_0$ proves [[König's lemma|3P2J5NWCM1]], and König's lemma gives weak König's lemma.
   Weak König's lemma proves $\mathrm{HB}$, by the [[Heine-Borel equivalence|KRS3VTWCHJ]].
3. A theory that proves two sentences proves that each implies the other.
   So $\mathsf{ACA}_0 \vdash \mathrm{HB} \leftrightarrow \mathrm{BW}$.
4. Over $\mathsf{RCA}_0$, $\mathrm{HB}$ does not imply $\mathrm{BW}$.
   There is an [[ω-model of WKL0 in which every set is low|8B045KSKW5]], and it satisfies $\mathrm{HB}$.
5. That model does not contain the halting set, so it is not a model of $\mathsf{ACA}_0$.
   Since $\mathsf{RCA}_0 + \mathrm{BW}$ proves $\mathsf{ACA}_0$, the sentence $\mathrm{BW}$ fails in it.
6. So the equivalence of step 3 hides a real difference in strength.

The base $\mathsf{ACA}_0$ is too strong, and the result is not an equivalence over $\mathsf{RCA}_0$.

## Remarks

The example shows why the base system must be weak.
A reverse mathematics equivalence is informative only when the base theory proves neither side.
Over $\mathsf{ACA}_0$, every theorem between $\mathsf{RCA}_0$ and $\mathsf{ACA}_0$ collapses into one class, together with every theorem of $\mathsf{ACA}_0$ itself.

What changes with a weaker base?
Over $\mathsf{RCA}_0$ the two theorems separate, and the low model in step 4 is the witness.
Over $\mathsf{WKL}_0$, the theorem $\mathrm{HB}$ becomes provable, and $\mathrm{BW}$ is still equivalent to $\mathsf{ACA}_0$, so the strength of $\mathrm{BW}$ is still visible there.

## Explanations

### L1 human

If a theory proves two statements, it also proves that each one implies the other.
So the theory sees them as equivalent, even when one is much stronger than the other.
To compare strength, one must use a base theory that proves neither statement.

### L2 human

The test is to look for a model of the base theory in which one side holds and the other fails.
Over $\mathsf{ACA}_0$ no such model exists for $\mathrm{HB}$ and $\mathrm{BW}$, because both hold in every model of $\mathsf{ACA}_0$.
Over $\mathsf{RCA}_0$, the low model of $\mathsf{WKL}_0$ is one.

Watch out: an equivalence proved in a textbook of analysis is usually an equivalence over a strong background, such as set theory.
Before such a result counts in reverse mathematics, its proof must be redone inside $\mathsf{RCA}_0$.
