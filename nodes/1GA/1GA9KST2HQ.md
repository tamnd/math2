---
tag: 1GA9KST2HQ
kind: example
name: Commutativity and the Church-Rosser property in product frames
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [JA2EBWVW8A]
uses: [JA2EBWVW8A, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Multimodal_logic
    locator: Overview
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Example

Take the $2 \times 2$ grid $\{0, 1\} \times \{0, 1\}$ with $0 < 1$ in both coordinates, and let $p$ be true only at $(1, 1)$.
At $(0, 0)$, $\lozenge_1 \square_2 p$ holds: go right to $(1, 0)$, whose only vertical successor is $(1, 1)$.
At $(0, 0)$, $\square_2 \lozenge_1 p$ holds too: the only vertical successor is $(0, 1)$, and it sees $(1, 1)$ horizontally.
We show that this is no accident, in every product frame.

Let $\mathfrak{F}_1 \times \mathfrak{F}_2 = (W_1 \times W_2, R_h, R_v)$ be a [[product frame|JA2EBWVW8A]] of two [[Kripke frames|NGHWZ9Y7ZV]].
We check that $\square_1 \square_2 p \leftrightarrow \square_2 \square_1 p$ and $\lozenge_1 \square_2 p \to \square_2 \lozenge_1 p$ are valid in it.

1. The path $(u, v) R_h (u', v) R_v (u', v')$ exists exactly when $u R_1 u'$ and $v R_2 v'$.
2. The path $(u, v) R_v (u, v') R_h (u', v')$ exists exactly when $v R_2 v'$ and $u R_1 u'$.
3. So $R_h \circ R_v = R_v \circ R_h$.
   Both $\square_1 \square_2 p$ and $\square_2 \square_1 p$ say that $p$ holds at all points reached by this relation, so they are equivalent.
4. Now let $(u, v) \models \lozenge_1 \square_2 p$.
   There is $u'$ with $u R_1 u'$ and $(u', v) \models \square_2 p$.
5. So $(u', v') \models p$ for every $v'$ with $v R_2 v'$.
6. Fix such a $v'$.
   Then $(u, v') R_h (u', v')$, so $(u, v') \models \lozenge_1 p$.
7. As $v'$ was arbitrary, $(u, v) \models \square_2 \lozenge_1 p$.

## Remarks

Step 6 uses the point $(u', v')$ that completes the square with corners $(u, v)$, $(u', v)$ and $(u, v')$.
This is the Church-Rosser property of product frames.
The two formulas are therefore theorems of every product logic $L_1 \times L_2$, while the fusion $\mathsf{K} \otimes \mathsf{K}$ proves neither.
For $\mathsf{K} \times \mathsf{K}$ they are the only interaction axioms needed.
By the theorem of Gabbay and Shehtman, $\mathsf{K} \times \mathsf{K} = \mathsf{K} \otimes \mathsf{K} \oplus \mathrm{com} \oplus \mathrm{chr}$.

## Explanations

### L1 human

On a grid, a step to the right followed by a step up lands on the same square as a step up followed by a step to the right.
Also, suppose one can go right to a column where every step up is safe.
Then after any step up one can still go right to a safe square.

### L2 human

Change the grid by deleting the point $(1, 1)$, and keep the other arrows.
Now $(0, 0)$ goes right to $(1, 0)$, and $(1, 0)$ has no vertical successor, so $\square_2 p$ holds there vacuously.
So $\lozenge_1 \square_2 p$ is true at $(0, 0)$ for every valuation.
The point $(0, 1)$ has no horizontal successor, so $\lozenge_1 p$ fails there, and $\square_2 \lozenge_1 p$ fails at $(0, 0)$.
The missing corner breaks step 6, and the frame is not a product.
The typical use of these formulas is to recognize frames that cannot be products.
Watch out: the formulas hold in every product, but frames that validate them need not be products.
