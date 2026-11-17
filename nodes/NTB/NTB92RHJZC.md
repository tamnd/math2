---
tag: NTB92RHJZC
kind: example
name: Factoring is needed in first-order resolution
msc: ["03B10", "03B35"]
topics: [TTCRX3NFNY]
audience: grad
instance_of: [DEB3CF4Z2D]
uses: [DEB3CF4Z2D, T3SXVH3ZZC, RJJ9D0WF53, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: Factoring
---

## Example

Let $S$ consist of the two [[clauses|T3SXVH3ZZC]]
$$C_1 = \{P(x), P(y)\}, \qquad C_2 = \{\neg P(u), \neg P(v)\}.$$
We show that $S$ is unsatisfiable and that binary resolution alone never derives $\square$ from $S$.
Then one factoring step on each clause gives a refutation.
So the factoring rule of [[first-order resolution|DEB3CF4Z2D]] cannot be dropped.

1. $S$ is unsatisfiable. The clause $C_1$ means $\forall x\,\forall y\,(P(x) \lor P(y))$, and the instance $y = x$ gives $\forall x\, P(x)$. The clause $C_2$ gives $\forall u\, \neg P(u)$ in the same way. A structure has a non-empty domain, so the two sentences contradict each other at any element.
2. The invariant. Call a clause good when it has two literals of the form $P(z)$ or $\neg P(z)$, with two different variables $z$. Both $C_1$ and $C_2$ are good.
3. Binary resolution keeps the invariant. Let $\{L_1, M_1\}$ and $\{L_2, M_2\}$ be good and renamed apart, and resolve on $L_1$ and $L_2$. The four variables $z_1, z_2, z_3, z_4$ of $L_1, M_1, L_2, M_2$ are then all different.
4. The [[unification|RJJ9D0WF53]] of the atoms $P(z_1)$ and $P(z_3)$ gives the single equation $z_1 = z_3$ and the mgu $\{z_1 \mapsto z_3\}$. This mgu does not move $z_2$ or $z_4$.
5. So the resolvent is $\{M_1, M_2\}$, with the different variables $z_2$ and $z_4$. It has two literals and it is good.
6. By [[structural induction|12MQ2NJ29A]] on derivations, every clause derived from $S$ by binary resolution alone is good. A good clause has two literals, so it is never $\square$.
7. Factoring $C_1$. The atoms $P(x)$ and $P(y)$ have the mgu $\{x \mapsto y\}$, and the factor is $\{P(x), P(y)\}\{x \mapsto y\} = \{P(y)\}$.
8. Factoring $C_2$. The atoms $P(u)$ and $P(v)$ have the mgu $\{u \mapsto v\}$, and the factor is $\{\neg P(v)\}$.
9. Resolution. The factors $\{P(y)\}$ and $\{\neg P(v)\}$ have no common variable. The atoms $P(y)$ and $P(v)$ have the mgu $\{y \mapsto v\}$, and the resolvent is $\square$.

## Remarks

The example shows where variables change the propositional picture.
In ground resolution a clause is a set, so two equal literals are one literal, and factoring is never needed.
With variables, $P(x)$ and $P(y)$ are different literals that have a common instance, and only factoring merges them.
This is also the point where the lifting lemma of the completeness proof needs factors.
A ground instance of $C_1$, such as $\{P(a)\}$, has one literal where $C_1$ has two.

Robinson's original resolution rule resolves on sets of literals and has factoring built in.
With that rule the refutation is one step: unify all of $P(x)$, $P(y)$, $P(u)$, $P(v)$ with the mgu $\{x \mapsto v, y \mapsto v, u \mapsto v\}$.

If the clause $C_2$ is replaced by the unit clause $\{\neg P(u)\}$, factoring is not needed.
Then $C_1$ and $\{\neg P(u)\}$ give $\{P(y)\}$ with the mgu $\{x \mapsto u\}$, and $\{P(y)\}$ and a renamed copy $\{\neg P(w)\}$ give $\square$.

## Explanations

### L1 human

The first clause says "everything has property $P$", written twice with two letters.
The second clause says "nothing has property $P$", also written twice.
The rule of resolution cancels one item of each list at a time.
Each cancellation leaves one item from each list, so a list of two items always remains.
Factoring first notices that the two items in one list say the same thing and merges them.
Then a single cancellation leaves nothing, which shows the contradiction.

### L2 human

To decide whether factoring helps, look for two literals of one clause with the same sign whose atoms unify.

1. In $\{P(x), P(y)\}$ the atoms $P(x)$ and $P(y)$ unify, with the mgu $\{x \mapsto y\}$.
2. In $\{\neg P(u), \neg P(v)\}$ the atoms unify, with the mgu $\{u \mapsto v\}$.
3. In a clause such as $\{P(a), P(b)\}$ with distinct constants, no factor exists, since $a$ and $b$ do not unify.

The typical use: provers add all factors of each new clause, which is one reason for the size of the search.
A trap is to expect binary resolution alone to be complete, as it is for ground clauses.
Here every resolvent has two literals, like its parents, so the clauses never shrink.
