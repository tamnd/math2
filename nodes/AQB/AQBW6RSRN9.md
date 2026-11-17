---
tag: AQBW6RSRN9
kind: example
name: Being an interval is not a generalized quantifier
msc: ["03C80"]
topics: [MDHDYV8QZW]
audience: grad
uses: [MFV98WTF4G, 0SNQEF7Z53]
not_instance_of:
  - target: MFV98WTF4G
    note: a bijection of the real line maps the interval [0, 1] to a set that is not an interval, so the family is not closed under isomorphism
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_quantifier
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Lindström_quantifier
    locator: Generalization of first-order quantifiers
---

## Example

Let $\mathcal{I}$ be the family of all intervals of $\mathbb{R}$, that is, of all sets $A \subseteq \mathbb{R}$ such that $a, b \in A$ and $a < c < b$ imply $c \in A$.
Consider the rule "$Qx \, \varphi(x)$ is true over the domain $\mathbb{R}$ when the set defined by $\varphi$ is an interval".
This rule looks like a quantifier of type $\langle 1 \rangle$.
We show that there is no [[generalized quantifier|MFV98WTF4G]] $Q$ of type $\langle 1 \rangle$ with $Q_{\mathbb{R}} = \mathcal{I}$.

1. A generalized quantifier of type $\langle 1 \rangle$ is a class $Q$ of structures $(M, A)$ with $A \subseteq M$, closed under isomorphism.
2. For $M' = M = \mathbb{R}$, an isomorphism from $(\mathbb{R}, A)$ to $(\mathbb{R}, A')$ is a [[bijection|0SNQEF7Z53]] $\pi \colon \mathbb{R} \to \mathbb{R}$ with $\pi[A] = A'$. So closure under isomorphism requires: $A \in Q_{\mathbb{R}}$ implies $\pi[A] \in Q_{\mathbb{R}}$ for every bijection $\pi$ of $\mathbb{R}$.
3. Let $A = [0, 1]$, an interval, and let $\pi$ be the bijection that swaps $\tfrac{1}{2}$ and $2$ and fixes every other real number.
4. Then $\pi[A] = \big( [0, 1] \setminus \{ \tfrac{1}{2} \} \big) \cup \{ 2 \}$.
5. The set $\pi[A]$ contains $0$ and $1$ but not $\tfrac{1}{2}$, so it is not an interval.
6. So $\mathcal{I}$ is not closed under bijections of $\mathbb{R}$, and by step 2 no generalized quantifier $Q$ has $Q_{\mathbb{R}} = \mathcal{I}$.

## Remarks

The example shows that a generalized quantifier may look only at the structure that its arguments provide, and not at extra structure of the domain.
Being an interval uses the order of $\mathbb{R}$, which is not one of the arguments.
If we make the order an argument, the problem disappears.
Let $\mathrm{Conv}$ be the class of all structures $(M, R, A)$ such that $R$ is a linear order of $M$ and $A$ is convex for $R$.
Then $\mathrm{Conv}$ is a generalized quantifier of type $\langle 2, 1 \rangle$.
An isomorphism of such structures preserves the order and maps $A$ onto $A'$, so it maps convex sets to convex sets.
On a pure set, a type $\langle 1 \rangle$ quantifier can depend only on $|A|$ and $|M \setminus A|$, as [[this example|HPA3BKNZE1]] shows.
The sets $[0, 1]$ and $\pi[A]$ both have the cardinality of the continuum, and so do their complements.

## Explanations

### L1 human

A quantifier in the sense of logic may only count.
"Is an interval" does not count: it asks whether the points of a set lie next to each other on the number line.
Suppose that we exchange two numbers: the point $\tfrac{1}{2}$ inside $[0, 1]$ and the point $2$ outside it.
The counts stay the same, but the set gets a hole.
So the answer changed although no count changed, and "is an interval" is not a quantifier.

### L2 human

We test a second set and a second bijection, to see that the failure is typical.

1. Let $A = (0, 3)$ and let $\pi$ swap $1$ and $5$ and fix all other reals.
2. Then $\pi[A] = \big( (0, 3) \setminus \{1\} \big) \cup \{5\}$.
3. This set contains $\tfrac{1}{2}$ and $2$ but not $1$, so it is not an interval.

The typical use of the test is to decide whether a proposed operator on sets is a logical quantifier.
A trap is to test only order-preserving bijections: they map intervals to intervals, but closure under isomorphism in type $\langle 1 \rangle$ asks for all bijections.
