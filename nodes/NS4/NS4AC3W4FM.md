---
tag: NS4AC3W4FM
kind: example
name: A Euclidean relation that is neither reflexive nor symmetric
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [XBCYFDPS2F]
uses: [XBCYFDPS2F, FDFQFWPM4X, 0X8NMST0J2, 061J5VGSPT, 0GJZW9JFZQ, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

Take the frame with two worlds and the following [[accessibility relation|XBCYFDPS2F]]:
$$W = \{ a, b \}, \quad R = \{ (a, b), (b, b) \}.$$
A relation is Euclidean when $w R v$ and $w R u$ imply $v R u$.
The successor sets are $R[a] = \{ b \}$ and $R[b] = \{ b \}$.

1. $R$ is Euclidean.
   For $w = a$ the only choice is $v = u = b$, and $b R b$ holds; for $w = b$ the only choice is also $v = u = b$.
2. $R$ is [[transitive|0GJZW9JFZQ]].
   The paths of length two are $a R b R b$ and $b R b R b$, and their end pairs $a R b$ and $b R b$ hold.
3. $R$ is serial, because $R[a]$ and $R[b]$ are nonempty.
4. $R$ is not [[reflexive|0X8NMST0J2]], because the pair $(a, a)$ is missing.
5. $R$ is not [[symmetric|061J5VGSPT]], because $a R b$ holds and $b R a$ fails.
6. So the frame validates $\mathrm{D}$, $\mathrm{4}$ and $\mathrm{5}$, by [[common modal axiom schemata|FDFQFWPM4X]], and it is a frame of $\mathsf{KD45}$.
7. The axiom $\mathrm{T}$ fails at $a$ with $V(p) = \{ b \}$.
   The only successor $b$ has $p$, so $\square p$ is true at $a$, and $p$ is false at $a$.
8. The axiom $\mathrm{B}$ fails at $a$ with $V(p) = \{ a \}$.
   Here $p$ is true at $a$, and $b$ sees only $b$, so $\lozenge p$ is false at $b$ and $\square\lozenge p$ is false at $a$.

## Remarks

The Euclidean property does not imply reflexivity or symmetry.
The logic $\mathsf{KD45}$ is the usual logic of belief: beliefs are consistent ($\mathrm{D}$), and the agent is aware of what it believes and of what it does not believe ($\mathrm{4}$ and $\mathrm{5}$).
In the frame, $b$ is the only world compatible with the beliefs at $a$.
The world $a$ is not compatible with its own beliefs, so beliefs held at $a$ can be false.

With reflexivity the situation changes, because a reflexive Euclidean relation is an [[equivalence relation|0G8VEZ3WTK]].
For symmetry, $w R v$ and $w R w$ give $v R w$ by the Euclidean property.
For transitivity, $w R v$ gives $v R w$ by symmetry, and then $v R w$ and $v R u$ give $w R u$.
So if we add the pair $(a, a)$ and keep the Euclidean property, we must also add $(b, a)$, and we get the universal relation.

## Explanations

### L1 human

Picture two people, Ann at $a$ and Bob at $b$.
Ann trusts only Bob, and Bob trusts only himself.
Whenever someone trusts two people, these two trust each other, and here both are Bob.
Ann does not trust herself, and Bob does not trust Ann.
So the relation "trusts" has the Euclidean property, but it is not reflexive and not symmetric.

### L2 human

Read $\square p$ at $a$ as "the agent at $a$ believes $p$", and take $V(p) = \{ b \}$.
The agent believes $p$, since $b$ is the only world that it considers possible.
The real world is $a$, where $p$ is false, so the belief is false.
At $a$ the formula $\square\square p$ is also true, since $b$ sees only $b$, so the agent believes that it believes $p$.
The typical use of this frame is as a small countermodel that separates $\mathsf{KD45}$ from $\mathsf{S5}$.
Watch out: a Euclidean relation need not be symmetric, so without $\mathrm{T}$ the axiom $\mathrm{5}$ does not give $\mathrm{B}$.
