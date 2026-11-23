---
tag: KZEDH1C6M6
kind: example
name: The predecessor as a description
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: grad
instance_of: [PD2R4XT79Q]
uses: [PD2R4XT79Q, 0QFT7Z76N5, GCK0NN60E4]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_description
    locator: Mathematical logic
---

## Example

Take the signature $\{ 0, S \}$ and the structure $\mathbb{N}$ with $S(n) = n + 1$.
For a variable $x$, consider the [[definite description|PD2R4XT79Q]] $\iota y \, (S(y) = x)$, "the predecessor of $x$".
We check when it denotes, and we eliminate it from the formula $\iota y \, (S(y) = x) = 0$.

1. Uniqueness: if $S(y) = x$ and $S(z) = x$, then $y + 1 = z + 1$, so $y = z$.
   This holds for every $x$.
2. Existence for $x \neq 0$: the natural number $y = x - 1$ satisfies $S(y) = x$.
3. Existence fails for $x = 0$: $S(y) = y + 1 \geq 1$ for every $y$, so no $y$ satisfies $S(y) = 0$.
4. So for $x \neq 0$ the description denotes $x - 1$, and for $x = 0$ it has no referent.
5. By Russell's analysis, $\iota y \, (S(y) = x) = 0$ abbreviates
   $$\exists y \, \big( S(y) = x \land \forall z \, (S(z) = x \to z = y) \land y = 0 \big).$$
6. At $x = 1$ this is true, with $y = 0$.
   At $x = 0$ it is false, by step 3.

So the description works as a term away from $0$, and Russell's analysis gives a definite truth value also at $0$.

## Remarks

The [[Peano axioms|0QFT7Z76N5]] prove $\forall x \, (x \neq 0 \to \exists! y \, (S(y) = x))$.
Because of the hypothesis $x \neq 0$, this does not give a total predecessor function as an [[extension by definition|GCK0NN60E4]].
The usual fix chooses a value at $0$.
The function $p$ with $p(0) = 0$ and $p(S(y)) = y$ is defined by the description
$$\iota y \, \big( S(y) = x \lor (x = 0 \land y = 0) \big),$$
whose condition has exactly one witness for every $x$.

## Explanations

### L1 human

"The number just before $x$" makes sense for $x = 5$: it is $4$.
For $x = 0$ there is no natural number just before it, so the phrase names nothing.
On Russell's analysis, a simple statement about "the number before $0$", such as "it equals $0$", is false.

### L2 human

We check that the condition in the remark has one witness for each $x$.
For $x = 0$, the equation $S(y) = 0$ never holds, so the condition reduces to $y = 0$, and the one witness is $0$.
For $x \neq 0$, the disjunct $x = 0 \land y = 0$ is false, so the condition is $S(y) = x$, which has the one witness $x - 1$ by steps 1 and 2.
The typical use is to turn a partial description into a total function by a default value, in the spirit of Frege's treatment.
Watch out: the formula $\neg (\iota y \, (S(y) = x) = 0)$ at $x = 0$ is ambiguous until the scope of the description is fixed.
With narrow scope it is false, and with wide scope it is true.
