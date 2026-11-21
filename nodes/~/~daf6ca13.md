---
tag: ~daf6ca13
kind: example
name: The classes of an equivalence relation with infinitely many infinite classes are imaginaries
aliases: [classes-of-equivalence-relation-are-imaginaries, imaginaries-not-eliminated-equivalence-relation]
msc: ["03C07", "03C45"]
topics: [SZRM3N6BXW]
audience: grad
instance_of: [~25317890]
uses: [~b9c87290, N232QBKCAA, DSQ17TNW1C, DKAGC639W9]
sources:
  - url: https://en.wikipedia.org/wiki/Imaginary_element
    locator: Examples
  - book: isbn:9780521763240
---

## Example

Let $T$ be the [[theory of an equivalence relation with infinitely many infinite classes|N232QBKCAA]], in the signature $\set{E}$, and let $M$ be a countable model of $T$.
Then $M$ has countably many classes, and each class is countably infinite.
For $a \in M$, the class $e = a / E$ is an element of the sort $S_E$ of $M^{\mathrm{eq}}$, so it is an [[imaginary element|~b9c87290]].
We show that $e$ is not interdefinable with any finite tuple of real elements.
In fact no real element is [[algebraic|DKAGC639W9]] over $e$.

1. Let $C = a / E$, as a subset of $M$. Each permutation of $C$, extended by the identity off $C$, preserves $E$. So it is an [[automorphism|DSQ17TNW1C]] of $M$ that fixes $e$.
2. Let $b \in M$. If $b \in C$, step 1 gives infinitely many images of $b$ under automorphisms that fix $e$, since $C$ is infinite.
3. If $b \notin C$, the same holds with the class of $b$ in place of $C$, and these automorphisms fix $C$ pointwise, so they fix $e$.
4. An element algebraic over $e$ has only finitely many images under the automorphisms that fix $e$. So by steps 2 and 3, $\operatorname{acl}^{\mathrm{eq}}(e) \cap M = \emptyset$.
5. The class $e$ is not in $\operatorname{dcl}^{\mathrm{eq}}(\emptyset)$: a permutation of $M$ that swaps $C$ with another class, by a bijection, is an automorphism that moves $e$.
6. Suppose $e$ and a real tuple $\bar b$ are interdefinable. By step 4, $\bar b$ is empty. Then $e \in \operatorname{dcl}^{\mathrm{eq}}(\emptyset)$, which contradicts step 5.

So $e$ is an imaginary that no real tuple codes, and $T$ does not eliminate imaginaries, even in the weak sense.

## Remarks

The example shows that $M^{\mathrm{eq}}$ can contain genuinely new elements.
The class $e$ is the canonical parameter of the definable set $E(M, a)$, and this set has no code among real tuples.

If instead $E$ has infinitely many classes, each with exactly $2$ elements, the class $\set{b_1, b_2}$ is in the definable closure of $b_1$, and $b_1$ is algebraic over it.
So weak elimination holds for these imaginaries, but the class is still not interdefinable with a real tuple, since swapping $b_1$ and $b_2$ fixes it.

If $E$ has only finitely many infinite classes, each class is in $\operatorname{acl}^{\mathrm{eq}}(\emptyset)$, and naming one element of each class as a constant makes every class definable.

## Explanations

### L1 human

Picture a crowd of people split into infinitely many teams, each with infinitely many members, where we only know who is on the same team.
A team is a natural object, but no finite list of people "names" a team in a way that the structure can see.
Any person on the team can be swapped with another member without changing the team.
So the team is a new kind of element, an imaginary one.

### L2 human

We test one candidate code for the class $e$ of $a$.

1. Try the tuple $(a)$ as a code. It is in the class, so $e = a / E$ is definable from $a$.
2. Now take an automorphism $\sigma$ that swaps $a$ with another element $a'$ of the same class and fixes everything else.
3. Then $\sigma(e) = e$, since $a$ and $a'$ have the same class, but $\sigma(a) = a' \neq a$.
4. So $a$ is not definable from $e$, and $(a)$ is not a code.

The typical use of this example is as the standard test case for elimination of imaginaries.
A trap is to think that every quotient is coded by a set of representatives: here no finite set of representatives is fixed by the automorphisms that fix $e$.
