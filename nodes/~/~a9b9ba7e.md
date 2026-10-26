---
tag: ~a9b9ba7e
kind: definition
name: Subset
msc: ["03E20"]
defines: ~a26615cd
uses: [~bd92ceee, ~6dec28e3, ~787b9755, ~06eaf3d7]
sources:
  - url: https://en.wikipedia.org/wiki/Subset
    locator: lead section
---

## Definition

Let $A$ and $B$ be [[sets|~bd92ceee]].
The set $A$ is a subset of $B$, written $A \subseteq B$, when each [[element|~6dec28e3]] of $A$ is an element of $B$:
$$\forall x \, (x \in A \to x \in B).$$
Then $B$ is a superset of $A$.
The set $A$ is a proper subset of $B$, written $A \subsetneq B$, when $A \subseteq B$ and $A \neq B$.

## Remarks

Some authors write $A \subset B$ for $A \subseteq B$, and others write it for a proper subset.
Two sets are equal if and only if each is a subset of the other. This follows from the [[axiom of extensionality|~4ca8988d]].
The [[empty set|~8354c914]] is a subset of every set, and every set is a subset of itself.

## Explanations

### L1 human

$A \subseteq B$ means that $A$ fits inside $B$.
The set of even numbers is a subset of the set of integers.
To prove $A \subseteq B$, take an arbitrary $x \in A$ and show $x \in B$.
