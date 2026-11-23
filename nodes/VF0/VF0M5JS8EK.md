---
tag: VF0M5JS8EK
kind: example
name: A serial strict order has no finite model
msc: ["03B45", "03C13"]
topics: [SKY7AQFG1V]
audience: grad
not_instance_of:
  - target: 3NT8RCA6HE
    note: the sentence is satisfiable, but it has no finite model, so first-order logic lacks the finite model property
uses: [3NT8RCA6HE, 086QKPF0A6, 0GJZW9JFZQ, NGHWZ9Y7ZV, YW6YGBMVQY]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_model_property
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

We show that [[first-order logic|086QKPF0A6]] does not have the [[finite model property|3NT8RCA6HE]].
Let $\sigma$ be the conjunction of three sentences in one binary relation symbol $R$.

- Irreflexivity: $\forall x\, \neg Rxx$.
- Transitivity: $\forall x \forall y \forall z\, (Rxy \wedge Ryz \to Rxz)$.
- Seriality: $\forall x \exists y\, Rxy$.

The structure $(\mathbb{N}, <)$ satisfies $\sigma$: no $n$ has $n < n$, the order $<$ is [[transitive|0GJZW9JFZQ]], and $n < n + 1$.
So $\sigma$ is satisfiable.

Now let $(A, R)$ be a finite structure with $A$ nonempty that satisfies irreflexivity and transitivity.
Pick $a_0 \in A$, and as long as $a_i$ has an $R$-successor, pick one and call it $a_{i+1}$.
By transitivity, $a_i R a_j$ holds for all $i < j$ in the sequence.
If $a_i = a_j$ with $i < j$, then $a_i R a_i$, which irreflexivity forbids, so the $a_i$ are pairwise distinct.
$A$ is finite, so the sequence stops at some $a_k$, and $a_k$ has no $R$-successor.
So seriality fails at $a_k$, and $(A, R)$ does not satisfy $\sigma$.
Hence $\sigma$ is satisfiable but has no finite model.

Check with three points: on $\{ 0, 1, 2 \}$ with the strict order $<$, the points $0$ and $1$ have successors, but $2$ has none.

## Remarks

### The modal side

The property that fails is the one in the definition: every satisfiable formula has a finite model.
Modal formulas cannot express irreflexivity in this way.
The modal formula $\lozenge\top \wedge \square\lozenge\top$ is true at $0$ in $(\mathbb{N}, <)$, which is serial and transitive.
It is also true in the one-point reflexive model, which is finite, serial and transitive.
So the modal description of $(\mathbb{N}, <)$ by seriality and transitivity has a finite model, while the first-order description $\sigma$ has none.

### The two-variable fragment

The [[standard translation|YW6YGBMVQY]] lands in the two-variable fragment of first-order logic.
That fragment does have the finite model property, by a theorem of Mortimer of 1975.
The sentence $\sigma$ uses three variables in its transitivity clause, which is why it escapes this theorem.

### Modal logics without the property

Normal modal logics can also lack the property.
Makinson gave a normal logic between $\mathsf{T}$ and $\mathsf{S4}$ without it in 1969.

### Watch out

The example is about the one sentence $\sigma$.
It does not say that the modal logic of serial transitive frames lacks the finite model property, and in fact that logic, $\mathsf{KD4}$, has it.

## Explanations

### L1 human

Imagine a line of people where each person must point to someone strictly ahead.
Pointing passes on: if you point at someone, you also point at everyone they point at.
Nobody may point at themselves.
With finitely many people, the last one has nobody to point at.
So such a line must be endless.

### L2 human

Follow successors from any point of a finite set with an irreflexive transitive relation.
Transitivity and irreflexivity forbid a repeat, so the path must end, and its end point has no successor.
So the relation is not serial.
The typical use is to see that first-order logic can force infinite models, while basic modal logic over Kripke frames cannot.

### L3 human

Trakhtenbrot's theorem of 1950 says that the set of first-order sentences with a finite model is not decidable.
So no Harrop-style argument can work for full first-order logic.
In modal logic the finite model property, together with finite axiomatization, gives decidability by [[Harrop's theorem|VSYQ1AZ9G7]].
