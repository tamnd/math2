---
tag: KRK0SW60RE
kind: example
name: A family not closed under intersection breaks the K axiom
msc: ["03B45", "54A05"]
topics: [SPQVNPZDTB]
audience: research
not_instance_of:
  - target: HWJXMBNHQ0
    note: the family of sets is not a topology, so the induced operator is not an interior operator and the K axiom fails
uses: [HWJXMBNHQ0, 0CQHFPGJ45]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: Topological semantics
  - url: https://en.wikipedia.org/wiki/Interior_algebra
    locator: Topology
---

## Example

Let $X = \{a, b, c\}$ and $\mathcal{O} = \{ \emptyset, \{a, b\}, \{b, c\}, X \}$.
For $A \subseteq X$, let $I(A)$ be the union of the members of $\mathcal{O}$ that are contained in $A$, and read $\square$ as $I$.
We show that this is not an instance of [[topological semantics|HWJXMBNHQ0]], and that it refutes a theorem of $\mathsf{K}$.

1. The family $\mathcal{O}$ is not a [[topology|0CQHFPGJ45]], because $\{a, b\} \cap \{b, c\} = \{b\}$ is not in $\mathcal{O}$.
2. Let $V(p) = \{a, b\}$ and $V(q) = \{b, c\}$.
   Both sets are members of $\mathcal{O}$, so $I(V(p)) = \{a, b\}$ and $I(V(q)) = \{b, c\}$.
3. The conjunction has $V(p \wedge q) = \{b\}$, and the only member of $\mathcal{O}$ inside $\{b\}$ is $\emptyset$.
   So $I(V(p \wedge q)) = \emptyset$.
4. At $b$, the formulas $\square p$ and $\square q$ are true, and $\square(p \wedge q)$ is false.
5. So $\square p \wedge \square q \to \square(p \wedge q)$ fails at $b$.
   This formula is a theorem of $\mathsf{K}$: apply necessitation to $p \to (q \to p \wedge q)$, then the axiom $\mathrm{K}$ twice.

## Remarks

Closure of the open sets under finite intersections is exactly what makes $\square$ distribute over $\wedge$.
The operator $I$ keeps the other two properties of an interior.
It shrinks sets, $I(A) \subseteq A$, and it is idempotent, since $\mathcal{O}$ is closed under unions, so $I(A)$ is itself a member of $\mathcal{O}$.
Hence $\square p \to p$ and $\square p \to \square \square p$ still hold, and only the axiom $\mathrm{K}$ breaks.

If we add $\{b\}$ to $\mathcal{O}$, the family becomes a topology, and the formula of step 5 holds at every point.
Structures of this kind are monotone frames of [[neighborhood semantics|CN7HK9K1B6]], which model the non-normal modal logics.

## Explanations

### L1 human

Here only some regions count as neighborhoods.
The point $b$ lies inside a neighborhood where $p$ holds and inside one where $q$ holds.
But no neighborhood of $b$ has both $p$ and $q$, because the overlap of the two neighborhoods is missing from the list.

### L2 human

We compute the failure as an equation of sets.
The subsets of $\{b\}$ are $\emptyset$ and $\{b\}$, and only $\emptyset$ belongs to $\mathcal{O}$, so $I(\{b\}) = \emptyset$.
The two boxes separately give a larger set:
$$I(\{a, b\}) \cap I(\{b, c\}) = \{a, b\} \cap \{b, c\} = \{b\} \neq \emptyset = I(\{a, b\} \cap \{b, c\}).$$
So $I$ does not preserve intersections, and the law "if both are necessary, so is their conjunction" fails.
The typical use of such families is to separate normal from non-normal modal logics.
Watch out: checking $\square p \to p$ and $\square p \to \square \square p$ is not enough to recognize an interior operator.
