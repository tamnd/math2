---
tag: FVT2EA59S4
kind: example
name: Closure rules without the word smallest do not define a set
msc: ["00A35"]
topics: [EEH2F76CYQ]
audience: ug1
not_instance_of:
  - target: AM4GQQMZ3C
    note: the extremal clause is missing, so several sets satisfy the base and the rule, and no single set is defined
uses: [AM4GQQMZ3C, 0MWKJ44V5A]
sources:
  - url: https://en.wikipedia.org/wiki/Recursive_definition
    locator: Form of recursive definitions
  - book: isbn:9781108439534
    locator: Chapter 6
---

## Example

Here is an attempt to define a set $S$ of [[natural numbers|0MWKJ44V5A]] by a base and a rule.
The base says that $0 \in S$, and the rule says that if $n \in S$, then $n + 2 \in S$.
The attempt has no extremal clause: it does not say that $S$ is the smallest set with these properties.
We show that it is not an [[inductive definition|AM4GQQMZ3C]] of one set.

1. Let $E = \{0, 2, 4, 6, \ldots\}$ be the set of even natural numbers.
   Then $0 \in E$, and if $n = 2k$, then $n + 2 = 2(k + 1) \in E$, so $E$ satisfies the base and the rule.
2. The set $\mathbb{N}$ satisfies the base, because $0 \in \mathbb{N}$, and the rule, because $n + 2 \in \mathbb{N}$ for each $n \in \mathbb{N}$.
3. Let $F = E \cup \{5, 7, 9, \ldots\}$.
   It satisfies the base, because $0 \in E$.
   It satisfies the rule, because $n + 2$ is even when $n$ is even, and $n + 2$ is an odd number at least $7$ when $n$ is an odd number at least $5$.
4. The three sets differ: $1 \in \mathbb{N}$ but $1 \notin F$, and $5 \in F$ but $5 \notin E$.
5. So the base and the rule do not determine $S$, and the question "is $1 \in S$?" has no answer from the text.

## Remarks

Add the extremal clause "$S$ is the smallest set with these properties", and the definition fixes $S = E$.
The set $E$ is closed, so $S \subseteq E$.
Each $2k$ lies in every closed set, by induction on $k$, so $E \subseteq S$.

The base and the rule give only the "at least" half of a definition: they say which numbers must be in $S$.
The extremal clause gives the "at most" half: nothing else is in $S$.
Without it, proof by induction on the rules breaks down.
The property "$n$ is even" holds for $0$ and is kept by the rule, yet it fails for $1$, and $\mathbb{N}$ satisfies both clauses.
Books write the extremal clause as "nothing else is in $S$", "$S$ is the smallest such set" or "$S$ is the intersection of all such sets", and the three forms say the same thing.

## Explanations

### L1 human

Suppose that a club says: "Ann is a member, and every member may bring a friend, who is then a member."
This tells us that Ann, her friends, and their friends are members.
It does not tell us that nobody else is a member.
A stranger could also be a member, and the two rules would still be true.
To fix the club exactly, we must add: "and nobody else is a member".

### L2 human

Let us find all sets $S \subseteq \mathbb{N}$ that satisfy the two clauses.
Each such $S$ contains $E$: by induction on $k$, $2k \in S$, with the base for $k = 0$ and the rule for the step.
Let $O = S \setminus E$ be the odd members of $S$.
If $n \in O$, then $n + 2$ is odd and lies in $S$, so $n + 2 \in O$.
So the solutions are exactly the sets $E \cup O$, where $O$ is a set of odd numbers closed under $n \mapsto n + 2$.
Such an $O$ is empty, or it is $\{m, m + 2, m + 4, \ldots\}$, where $m$ is its least element.
So there are infinitely many solutions, one for each odd $m$ and one more for $O = \emptyset$.
The smallest solution is $E$, with $O = \emptyset$, and the extremal clause picks exactly that one.
The typical use of this check is to ask of any definition by rules which objects it excludes.
Watch out: a reader who takes the rules at their word may choose $\mathbb{N}$, and nothing in the rules says that this is wrong.
