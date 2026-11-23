---
tag: MEKKHHQTKB
kind: topic
name: Proof patterns for common goals
msc: ["00A35"]
topics: [SGSVYFDSYK]
---

## Summary

Many proofs in a first course have the same shape, because the goals repeat: two sets are equal, a function is injective, a relation is an equivalence relation, two expressions agree, a limit exists.
This part of [[reasoning and proof|SGSVYFDSYK]] collects the standard pattern for each such goal, and each page opens with one short goal proved by its pattern.
The story starts with goals about sets and functions, where the pattern is a pair of checks: two inclusions for set equality, the injective and surjective templates for a function, and the three properties of an equivalence relation.
Two inequalities give an equality of numbers in the same way, and identities are proved by chains of reversible steps.
Analysis brings estimates: the epsilon-delta proof finds $\delta$ in scratch work and writes it forward, the epsilon over three argument splits one distance into three small pieces, and the density argument proves a fact on a dense set and extends it by continuity.
Symmetry and reduction to a special case cut the work before it starts.
The last patterns spread a property over a whole space or a whole interval of time: the open-closed argument on a connected space, bootstrapping from a weak estimate to a stronger one, and the proof by algorithm, where a procedure that stops with a correct output proves that the output exists.
Each page also shows the slips that break its pattern, with a non-example where the pattern seems to apply and fails.

## Remarks

### Reading order

1. [[Set equality by double inclusion|MKHVRNW68H]]: how to prove $A = B$ by element chasing in both directions, and why one inclusion is never enough.
2. [[Proving injectivity and surjectivity|DD2P85Y8E9]]: the two templates for a function, and how a one-sided inverse gives each property at once.
3. [[Proving a relation is an equivalence relation|RGNF33GVHX]]: the three checks, and the shortcut through a function whose fibers are the classes.
4. [[Equality by two inequalities|S3QADD13E9]]: how $a \le b$ and $b \le a$ prove $a = b$ when a direct computation is out of reach.
5. [[Proving identities|XP5SDYKJX0]]: how to chain reversible steps from one side to the other, and why squaring both sides can mislead.
6. [[Writing epsilon-delta proofs|RXG5JTZ2PZ]]: how to find $\delta$ in scratch work and then write the proof forward.
7. [[Epsilon over three argument|VXV7M0QDH6]]: how to split one estimate into three small terms, and why the approximation must be uniform.
8. [[Density argument|J2J35J3055]]: how to prove a result on a dense set and extend it by continuity.
9. [[Symmetry arguments|H840D9TM2X]]: how a symmetry of the problem cuts the work, and why it does not place an extremum at the symmetric point.
10. [[Reduction to a special case|DX2H7AD66G]]: how to prove a normalized case and transfer it, once the statement is checked to survive the transfer.
11. [[Open-closed argument|1JJCDJB7FM]]: why a non-empty set that is open and closed in a connected space is the whole space.
12. [[Bootstrapping|YKA0ADKYFR]]: how a weak estimate that improves itself becomes a strong one, and why continuity is needed.
13. [[Proof by algorithm|X5HG1RNWQX]]: how termination and an invariant turn a procedure into an existence proof.

### Prerequisites

1. [[Mathematical proof|0B94TKFQJX]]: what a proof is and how it is written.
2. [[The language of mathematical statements|WMY13MXY3W]]: quantifiers, implications and negations.
3. [[Basic proof methods|958EF46EYJ]]: direct proof, contradiction, contrapositive and cases, which each pattern here uses.
4. [[Proof methods|G9JFJGY4TQ]]: the list of all proof methods, for the context of each pattern.
5. Sets, functions and relations for items 1 to 3, and limits and continuity of real functions for items 6 to 8, 11 and 12.
