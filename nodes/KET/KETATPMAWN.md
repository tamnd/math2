---
tag: KETATPMAWN
kind: example
name: The present King of France
msc: ["03B10", "03A05"]
topics: [PSRDJXRW53]
audience: grad
instance_of: [PD2R4XT79Q]
uses: [PD2R4XT79Q]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_description
    locator: lead section
  - url: https://en.wikipedia.org/wiki/On_Denoting
    locator: lead section
---

## Example

Russell's example in "On Denoting" is the sentence "the present King of France is bald", together with "the present King of France is not bald".
Let $K(x)$ mean "$x$ is a present King of France" and $B(x)$ mean "$x$ is bald".
We write the two readings of the negative sentence by Russell's analysis of the [[definite description|PD2R4XT79Q]] $\iota x \, K(x)$.
Let $U(x)$ abbreviate $K(x) \land \forall y \, (K(y) \to y = x)$, "$x$ is the one present King of France".

1. Narrow scope, with the negation inside: $\exists x \, (U(x) \land \neg B(x))$.
   It says that there is exactly one present King of France and he is not bald.
2. Wide scope, with the negation outside: $\neg \exists x \, (U(x) \land B(x))$.
   It says that it is not the case that exactly one present King of France exists and is bald.
3. Today no object satisfies $K$, so no object satisfies $U$.
4. Then the narrow reading is false, because its $\exists x$ needs an object with $U(x)$.
5. The wide reading is true, because $\exists x \, (U(x) \land B(x))$ is false, and its negation is true.
6. "The present King of France is bald" is $\exists x \, (U(x) \land B(x))$, which is false by step 5.

So the positive sentence and the narrow reading of the negative one are both false, and the law of excluded middle is saved by the wide reading.

## Remarks

The puzzle that Russell solved is this: "the King of France is bald" and "the King of France is not bald" seem to be a sentence and its negation, yet both seem false.
On the analysis, the narrow reading of the second is not the negation of the first.
The true negation of "the King of France is bald" is the wide-scope sentence of step 2.
When exactly one object satisfies $K$, the two readings agree.

## Explanations

### L1 human

"The King of France is not bald" can mean two things.
It can mean "there is a King of France, and he is not bald", which is false today.
It can also mean "it is not true that there is a bald King of France", which is true today.
Russell's analysis makes the two meanings precise.

### L2 human

We check that the two readings agree when there is exactly one king.
Suppose $U(a)$ holds for one object $a$, and for no other.
Then the narrow reading $\exists x \, (U(x) \land \neg B(x))$ is equivalent to $\neg B(a)$.
The wide reading $\neg \exists x \, (U(x) \land B(x))$ is equivalent to $\neg B(a)$ as well.
So they agree, as the basic properties of [[descriptions|PD2R4XT79Q]] predict.
The typical use of the example is to show why scope must be marked when a description meets a negation.
Watch out: the narrow reading is not nonsense in Russell's analysis.
It is false when no king exists, by step 4 of the example.
