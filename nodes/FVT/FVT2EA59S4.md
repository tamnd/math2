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

Consider the following attempt to define a set $S$ of [[natural numbers|0MWKJ44V5A]].

- Base: $0 \in S$.
- Rule: if $n \in S$, then $n + 2 \in S$.

The attempt has no extremal clause: it does not say that $S$ is the smallest set with these properties.
We show that it is not an [[inductive definition|AM4GQQMZ3C]] of one set.

1. Let $E = \{0, 2, 4, 6, \ldots\}$ be the set of even natural numbers. Then $0 \in E$, and if $n = 2k$, then $n + 2 = 2(k + 1) \in E$. So $E$ satisfies the base and the rule.
2. The set $\mathbb{N}$ satisfies the base, because $0 \in \mathbb{N}$, and the rule, because $n + 2 \in \mathbb{N}$ for each $n \in \mathbb{N}$.
3. The set $F = E \cup \{5, 7, 9, \ldots\}$ satisfies the base, because $0 \in E$. It satisfies the rule, because $n + 2$ is even when $n$ is even, and $n + 2$ is an odd number at least $7$ when $n$ is an odd number at least $5$.
4. The three sets differ: $1 \in \mathbb{N}$ but $1 \notin F$, and $5 \in F$ but $5 \notin E$.
5. So the base and the rule do not determine $S$. The question "is $1 \in S$?" has no answer from the text.

## Remarks

1. With the extremal clause "$S$ is the smallest set with these properties", the definition fixes $S = E$. The set $E$ is closed, so $S \subseteq E$. Each $2k$ is in every closed set, by induction on $k$, so $E \subseteq S$.
2. The two clauses give only the "at least" half of the definition: they say which numbers must be in $S$. The extremal clause gives the "at most" half: nothing else is in $S$.
3. Without the extremal clause, proof by induction on the rules fails. The property "$n$ is even" holds for $0$ and is kept by the rule, but it is false for $1 \in \mathbb{N}$, and $\mathbb{N}$ satisfies both clauses.
4. Textbooks write the extremal clause in several forms: "nothing else is in $S$", "$S$ is the smallest such set", or "$S$ is the intersection of all such sets". All three say the same thing.

## Explanations

### L1 human

Suppose that a club says: "Ann is a member, and every member may bring a friend who is then a member."
This tells us that Ann and her friends, and their friends, are members.
It does not tell us that nobody else is a member.
A stranger could also be a member, and the two rules would still be true.
To fix the club exactly, we must add: "and nobody else is a member".

### L2 human

We find all sets $S \subseteq \mathbb{N}$ that satisfy the two clauses.

1. Each such $S$ contains $E$: by induction on $k$, $2k \in S$, using the base for $k = 0$ and the rule for the step.
2. Let $O = S \setminus E$, the odd members of $S$. If $n \in O$, then $n + 2$ is odd and in $S$, so $n + 2 \in O$.
3. So the sets that satisfy the clauses are exactly $E \cup O$, where $O$ is a set of odd numbers closed under $n \mapsto n + 2$.
4. Such an $O$ is empty or of the form $\{m, m + 2, m + 4, \ldots\}$, where $m$ is the least element of $O$. So there are infinitely many solutions, one for each choice of $O$.
5. The smallest solution is $E$, with $O = \emptyset$.

The typical use of this observation is to check whether a definition says which objects are excluded.
A trap is to read the rules as if they said "the smallest set": a reader can take the rules at their word, and then $\mathbb{N}$ fits too.
