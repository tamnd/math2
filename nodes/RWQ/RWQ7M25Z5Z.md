---
tag: RWQ7M25Z5Z
kind: example
name: The informal proof that divisibility is transitive
msc: ["00A35", "11A05"]
topics: [1BTHSHST4M]
audience: ug1
instance_of: [8VZ77R4R8S]
uses: [8VZ77R4R8S, 0PG2H7WKGG, 0MSRQHCNN9]
sources:
  - url: https://en.wikipedia.org/wiki/Divisor
    locator: Further notions and facts
  - url: https://en.wikipedia.org/wiki/Formal_proof
    locator: lead section
---

## Example

Claim: for integers $a, b, c$, if $a \mid b$ and $b \mid c$, then $a \mid c$.
Here $a \mid b$ means that $b = ak$ for some integer $k$; this is the definition of [[divisibility|0PG2H7WKGG]].

The informal proof found in books has three lines.

> Write $b = ak$ and $c = bm$ with integers $k, m$.
> Then $c = (ak)m = a(km)$.
> Since $km$ is an integer, $a \mid c$.

This is an [[informal proof|8VZ77R4R8S]]: it is correct and complete for its reader, and it leaves out steps of logic and arithmetic.
We list the steps that a formal proof must write.

1. Unfold the definition: $a \mid b$ is the statement $\exists k \in \mathbb{Z},\ b = ak$, with an [[existential quantifier|0MSRQHCNN9]].
2. Existential elimination: from $\exists k,\ b = ak$, introduce a new name $k$ with $b = ak$. The name must not occur elsewhere in the proof.
3. The same for $b \mid c$: introduce a new name $m$ with $c = bm$.
4. Substitution of equals: from $c = bm$ and $b = ak$, derive $c = (ak)m$.
5. Associativity of multiplication: $(ak)m = a(km)$. With step 4 and the transitivity of $=$, this gives $c = a(km)$.
6. Closure: $k, m \in \mathbb{Z}$ gives $km \in \mathbb{Z}$.
7. Existential introduction: from step 6 and $c = a(km)$, derive $\exists j \in \mathbb{Z},\ c = aj$.
8. Fold the definition: this is $a \mid c$.
9. Implication introduction: discharge the assumptions $a \mid b$ and $b \mid c$, and conclude the implication of the claim. Then generalize over $a, b, c$.

## Remarks

The three informal lines carry all nine steps.
The first line does steps 1 to 3, the second does steps 4 and 5, and the third does steps 6 to 8.
Step 9 is not written at all: the words "if" and "then" in the claim make it implicit.

A reader with a first course in proofs fills in these steps without effort.
This is why the three-line proof is [[rigorous|E1PE9R8DBB]] for that reader, even though it is not formal.

Proof assistants have this lemma in their libraries.
In Lean's Mathlib it is called `dvd_trans`, and its proof there is short because tactics perform steps 1 to 9.

## Explanations

### L1 human

"$3$ divides $12$" means that $12$ is $3$ times a whole number, namely $4$.
"$12$ divides $60$" means that $60$ is $12$ times a whole number, namely $5$.
Then $60 = 12 \times 5 = (3 \times 4) \times 5 = 3 \times 20$, so $3$ divides $60$.
The informal proof says this in three lines for all numbers.
A formal proof also writes the small steps, such as "regroup the product" and "$4 \times 5$ is a whole number".

### L2 human

We run the nine steps with $a = 3$, $b = 12$ and $c = 60$.

1. Steps 2 and 3 give $k = 4$, since $12 = 3 \cdot 4$, and $m = 5$, since $60 = 12 \cdot 5$.
2. Step 4 gives $60 = (3 \cdot 4) \cdot 5$.
3. Step 5 gives $(3 \cdot 4) \cdot 5 = 3 \cdot (4 \cdot 5) = 3 \cdot 20$.
4. Steps 6 and 7 give $j = 20$, an integer with $60 = 3j$, so $3 \mid 60$.

The typical use of the list is to see which axioms the proof needs: here, associativity, closure of $\mathbb{Z}$ under multiplication, and the rules for $\exists$.
A trap is in step 3 of the formal list: the name $m$ must be new, and reusing $k$ would claim that both quotients are equal.
