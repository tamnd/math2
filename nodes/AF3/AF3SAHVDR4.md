---
tag: AF3SAHVDR4
kind: example
name: The empty set is a subset of every set
msc: ["03B10", "03E20"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0V4QXPGJQK]
uses: [0V4QXPGJQK, 0FE8Q5S42Y, 0ECVK59Y03, 0ZNX6DQ3EJ]
sources:
  - url: https://en.wikipedia.org/wiki/Vacuous_truth
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Empty_set
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.2
---

## Example

Let $B$ be a set.
We show that the [[empty set|0ECVK59Y03]] $\varnothing$ is a [[subset|0FE8Q5S42Y]] of $B$, and that this is a [[vacuous truth|0V4QXPGJQK]].

1. By the definition of a subset, $\varnothing \subseteq B$ means $\forall x \, (x \in \varnothing \to x \in B)$.
2. Let $x$ be any object.
   The empty set has no elements, so the statement $x \in \varnothing$ is false.
3. An [[implication|0ZNX6DQ3EJ]] with a false antecedent is true, so $x \in \varnothing \to x \in B$ is true for this $x$.
4. Step 3 holds for every object $x$, so $\forall x \, (x \in \varnothing \to x \in B)$ is true, and $\varnothing \subseteq B$.
5. The consequent $x \in B$ was never checked, so the truth does not depend on $B$, and this is what makes it vacuous.

The same fact has a proof by counterexample search.
A counterexample to $\varnothing \subseteq B$ would be an element $x \in \varnothing$ with $x \notin B$.
The empty set has no elements, so there is no counterexample.

## Remarks

The definition of a subset puts an implication inside a universal quantifier, and that choice settles the case of the empty set with no extra rule.

Three consequences follow at once.
With $B = \varnothing$ we get $\varnothing \subseteq \varnothing$.
The empty set is the only set that is a subset of every set: if $E \subseteq B$ for every set $B$, then $E \subseteq \varnothing$, so $E$ has no elements and $E = \varnothing$.
A set with $n$ elements has $2^n$ subsets, and $\varnothing$ is always one of them; for $\{1, 2\}$ the four subsets are $\varnothing$, $\{1\}$, $\{2\}$ and $\{1, 2\}$.

Replace $\varnothing$ by a nonempty set $A$, and step 2 fails.
For $x \in A$ the antecedent is true, so $x \in B$ must be checked; for example, $\{1\} \subseteq B$ holds exactly when $1 \in B$.

## Explanations

### L1 human

A set $A$ is inside a set $B$ when every member of $A$ is also a member of $B$.
The empty set has no members at all.
So no member of the empty set can fail to be in $B$.
That is why the empty set is inside every set, even inside $\{7\}$ and inside itself.

### L2 human

Check $\varnothing \subseteq \{1, 2, 3\}$ and $\{0\} \not\subseteq \{1, 2, 3\}$ with the same definition.
For $\varnothing$, each instance $x \in \varnothing \to x \in \{1, 2, 3\}$ has a false antecedent, so it is true, and $\varnothing \subseteq \{1, 2, 3\}$.
For $\{0\}$, the instance $x = 0$ has the true antecedent $0 \in \{0\}$ and the false consequent $0 \in \{1, 2, 3\}$.
That instance is false, so $\{0\} \not\subseteq \{1, 2, 3\}$.
Proofs about all subsets of a set, such as the count $2^n$, must include the empty subset for exactly this reason.
Watch out: $\varnothing \subseteq B$ is not $\varnothing \in B$.
The first is always true, and the second holds only when the empty set is an element of $B$, as in $B = \{\varnothing\}$.
