---
tag: DYMYNTBWEE
kind: example
name: A composition of injective functions is injective
msc: ["00A35", "03E20"]
topics: [958EF46EYJ]
audience: ug1
instance_of: [V8ZB838JY5]
uses: [V8ZB838JY5, 09NWETVTNY, 0THBK9V825]
sources:
  - url: https://en.wikipedia.org/wiki/Injective_function
    locator: lead section
  - book: isbn:9781108439534
    locator: Chapter 3
---

## Example

We prove: if $f : A \to B$ and $g : B \to C$ are [[injective|09NWETVTNY]], then the [[composition|0THBK9V825]] $g \circ f : A \to C$ is injective.
We find the proof by the [[forward-backward method|V8ZB838JY5]], and then write it forward.

1. Backward: by definition, the goal says that for all $x, y \in A$, if $g(f(x)) = g(f(y))$, then $x = y$.
2. Backward: the goal is a universal statement about an implication.
   So let $x, y \in A$ be arbitrary and assume $g(f(x)) = g(f(y))$; the new goal is $x = y$.
3. Backward: how can we show $x = y$?
   The hypothesis that $f$ is injective gives $x = y$ from $f(x) = f(y)$, so the new goal is $f(x) = f(y)$.
4. Forward: apply the hypothesis that $g$ is injective to the elements $f(x)$ and $f(y)$ of $B$.
   The assumption $g(f(x)) = g(f(y))$ then gives $f(x) = f(y)$.
5. The chains meet at $f(x) = f(y)$, so $x = y$, and $g \circ f$ is injective.

Written forward, the proof reads: let $x, y \in A$ with $g(f(x)) = g(f(y))$; since $g$ is injective, $f(x) = f(y)$; since $f$ is injective, $x = y$.

## Remarks

The definition of the goal did most of the work.
Unfolding it in steps 1 and 2 told the proof how to start, and step 3 told it which hypothesis to use last.
Notice that the written proof uses the hypotheses in the opposite order to the search: $g$ first, then $f$.

A partial converse holds: if $g \circ f$ is injective, then $f$ is injective.
But $g$ need not be injective.
Take $A = \{1\}$, $B = \{1, 2\}$, $C = \{1\}$, $f(1) = 1$ and $g(1) = g(2) = 1$.
Then $g \circ f$ is injective, because $A$ has only one element, while $g$ sends $1$ and $2$ to the same point.

## Explanations

### L1 human

Think of $f$ as giving each student a different locker, and $g$ as giving each locker a different key.
Then each student ends up with a different key.
Two students with the same key would have the same locker, because different lockers have different keys.
And two students with the same locker would be the same student.
The proof follows the key back to the locker, and the locker back to the student.

### L2 human

The same plan proves that if $f : A \to B$ and $g : B \to C$ are surjective, then $g \circ f$ is surjective.
Backward, the goal is: for every $z \in C$ there is $x \in A$ with $g(f(x)) = z$, so we let $z \in C$ be arbitrary.
Forward, since $g$ is surjective, there is $y \in B$ with $g(y) = z$.
Forward again, since $f$ is surjective, there is $x \in A$ with $f(x) = y$.
Then
$$g(f(x)) = g(y) = z,$$
so this $x$ is the witness the goal needs.
The typical use is to unfold the definition in the goal and apply the hypotheses in the order that the unfolded goal asks for.
Watch out: the witness $x$ is chosen after $z$ and depends on $z$, so a proof that names one $x$ before $z$ is given has the quantifiers in the wrong order.
