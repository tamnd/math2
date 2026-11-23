---
tag: HPA3BKNZE1
kind: example
name: Cardinality quantifiers are permutation invariant
msc: ["03A05", "03C80"]
topics: [H8QZY0RZXZ]
audience: research
uses: [05RWFKVTJ7, 0SNQEF7Z53, MFV98WTF4G]
instance_of: [2QQ7Q5SKP8]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_quantifier
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Logical_constant
    locator: lead section
---

## Example

Let $D$ be a nonempty set.
A unary quantifier on $D$ is a set $Q$ of subsets of $D$, and $Qx \, \varphi(x)$ is true when the set of $x$ that satisfy $\varphi$ is in $Q$.
This is the simplest kind of [[generalized quantifier|MFV98WTF4G]].
A [[permutation|05RWFKVTJ7]] $\pi$ of $D$ acts by $\pi[Q] = \{\pi[X] : X \in Q\}$, and $Q$ is permutation invariant when $\pi[Q] = Q$ for every $\pi$.
We show that $Q$ is permutation invariant if and only if $X \in Q \Leftrightarrow Y \in Q$ for all $X, Y \subseteq D$ with $|X| = |Y|$ and $|D \setminus X| = |D \setminus Y|$.

1. Let $\pi$ be a permutation and $X \subseteq D$.
   The map $\pi$ restricts to a [[bijection|0SNQEF7Z53]] from $X$ onto $\pi[X]$, so $|\pi[X]| = |X|$.
2. Since $\pi$ is a bijection of $D$, it also restricts to a bijection from $D \setminus X$ onto $D \setminus \pi[X]$, so $|D \setminus \pi[X]| = |D \setminus X|$.
3. Suppose $Q$ satisfies the cardinality condition, and let $X \in Q$.
   By steps 1 and 2, $\pi[X]$ has the same two cardinalities as $X$, so $\pi[X] \in Q$, and $\pi[Q] \subseteq Q$.
4. Step 3 for $\pi^{-1}$ gives $\pi^{-1}[Q] \subseteq Q$, so $Q \subseteq \pi[Q]$ and $\pi[Q] = Q$.
5. Conversely, suppose $Q$ is invariant, and let $|X| = |Y|$ and $|D \setminus X| = |D \setminus Y|$.
6. Choose bijections $f \colon X \to Y$ and $g \colon D \setminus X \to D \setminus Y$.
   Their union $\pi = f \cup g$ is a permutation of $D$ with $\pi[X] = Y$.
7. If $X \in Q$, then $Y = \pi[X] \in \pi[Q] = Q$, and the same argument with $\pi^{-1}$ gives the other direction.

So these quantifiers are permutation invariant and logical by Tarski's criterion: $\forall$, with $Q = \{D\}$, that is, $|D \setminus X| = 0$; $\exists$, with $|X| \geq 1$; "at least two", with $|X| \geq 2$; "infinitely many", with $X$ infinite; and "more than half", with $|X| > |D \setminus X|$.

## Remarks

The criterion admits many quantifiers that first-order logic cannot express.
"Infinitely many" is not first-order definable, by the [[compactness theorem|1NR3HAWG9D]], and "more than half" is not first-order definable even on finite domains.

On a finite $D$ with $n$ elements the second cardinality is $n - |X|$, so an invariant quantifier depends on $|X|$ alone.
It is fixed by the set of sizes among $0, 1, \ldots, n$ for which it holds, so there are exactly $2^{n+1}$ invariant quantifiers.
On an infinite $D$ both cardinalities are needed.
In $\mathbb{N}$ the even numbers and the numbers at least $1$ both have size $\aleph_0$, but their complements have sizes $\aleph_0$ and $1$.
A quantifier such as "contains the number $0$", $Q = \{X : 0 \in X\}$, is not invariant, because a permutation can move $0$.

## Explanations

### L1 human

The word "some" in "some cats are black" asks only whether the set of black cats is empty.
The phrase "most cats" asks only whether there are more black cats than other cats.
Neither cares which cats they are, only how many.
If we exchange one cat for another, the answers stay the same.
That is why these words count as logical: they look only at numbers of objects.

### L2 human

We take $D = \{1, 2, 3\}$ and test two quantifiers.

1. Let $Q_{\text{most}} = \{X \subseteq D : |X| > 3 - |X|\} = \{X \subseteq D : |X| \geq 2\}$.
2. So $Q_{\text{most}} = \{\{1, 2\}, \{1, 3\}, \{2, 3\}, \{1, 2, 3\}\}$.
3. A permutation maps each $2$-element set to a $2$-element set and $D$ to $D$, so it maps $Q_{\text{most}}$ to itself.
4. Let $Q_1 = \{X \subseteq D : 1 \in X\}$, the quantifier "the object $1$ has the property".
5. The permutation $\sigma$ that swaps $1$ and $2$ maps $\{1\} \in Q_1$ to $\{2\}$, and $\{2\} \notin Q_1$.
6. So $Q_{\text{most}}$ is invariant and $Q_1$ is not.

The same test classifies natural language quantifiers such as "most", "few" and "at least three" by the sizes of sets.
The trap is to forget the complement on infinite domains: on $\mathbb{N}$ the quantifier "all but finitely many", $\{X : D \setminus X \text{ is finite}\}$, is invariant, but it does not depend on $|X|$ alone.
