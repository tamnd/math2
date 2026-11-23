---
tag: 655T2GTWNV
kind: example
name: The Geach-Kaplan sentence
msc: ["03A05", "03C62", "03B16"]
topics: [MDHDYV8QZW]
audience: research
uses: [DZVEFDYYZX, 1NR3HAWG9D, 1QWN5CV4CG, 086QKPF0A6]
instance_of: [DZVEFDYYZX]
sources:
  - url: https://en.wikipedia.org/wiki/Plural_quantification
    locator: History
  - url: https://en.wikipedia.org/wiki/Non-standard_model_of_arithmetic
    locator: lead section
---

## Example

The English sentence "some critics admire only one another" looks simple, but first-order logic cannot express it with its own predicates.
It uses a [[plural quantifier|DZVEFDYYZX]].
With $Cx$ for "$x$ is a critic" and $Axy$ for "$x$ admires $y$", it is this sentence:
$$\mathrm{GK} = \exists xx \, \big( \forall x \, (x \prec xx \to Cx) \land \forall x \, \forall y \, ((x \prec xx \land Axy) \to (x \neq y \land y \prec xx)) \big).$$
In monadic second-order form, $\exists xx$ becomes $\exists X$ with the extra condition $\exists x \, Xx$, and $X$ ranges over all subsets of the domain.
We show that no [[first-order|086QKPF0A6]] sentence $\psi$ in the vocabulary $\set{C, A}$ is true in exactly the same structures as $\mathrm{GK}$.

1. Let $\mathcal{N}$ be a model of the language of arithmetic with $0$ and the successor $S$.
   On the same domain, define the $\set{C, A}$-structure $\mathcal{N}^*$ by these rules:
   $$C = \text{the whole domain}, \qquad Axy \iff (x = 0 \lor x = Sy).$$
2. For a first-order $\psi$ in $\set{C, A}$, let $\psi'$ be $\psi$ with $Cx$ replaced by $x = x$ and $Axy$ replaced by $(x = 0 \lor x = Sy)$.
   Then $\mathcal{N} \models \psi'$ if and only if $\mathcal{N}^* \models \psi$, by induction on $\psi$.
3. $\mathrm{GK}$ is false in $\mathbb{N}^*$.
   Suppose that a nonempty $X \subseteq \mathbb{N}$ satisfies the condition, and let $m$ be its least element.
4. If $m = 0$, then $A00$ holds, so the condition demands $0 \neq 0$.
   If $m = k + 1$, then $Amk$ holds, so the condition puts $k$ into $X$, and $k < m$.
   Both cases contradict the choice of $m$.
5. Let $\mathcal{N}$ be a [[non-standard model of arithmetic|1QWN5CV4CG]] that satisfies all first-order sentences true in $\mathbb{N}$.
   Such a model exists by the [[compactness theorem|1NR3HAWG9D]].
   An element is standard when it is the value of a numeral $S^n 0$.
6. $\mathrm{GK}$ is true in $\mathcal{N}^*$.
   For $xx$, take the nonstandard elements, and there is at least one.
   Each of them is a critic, because $C$ is the whole domain.
7. Let $x$ be nonstandard with $Axy$.
   Then $x \neq 0$, so $x = Sy$, and $y$ is nonstandard, since $y = S^n 0$ would give $x = S^{n+1} 0$.
   Also $y \neq x$, because $\forall y \, (Sy \neq y)$ is true in $\mathbb{N}$ and so in $\mathcal{N}$.
8. Suppose a first-order $\psi$ were equivalent to $\mathrm{GK}$.
   By steps 2, 3 and 6, $\psi'$ is false in $\mathbb{N}$ and true in $\mathcal{N}$.
9. But $\neg \psi'$ is true in $\mathbb{N}$, and $\mathcal{N}$ satisfies every first-order sentence true in $\mathbb{N}$.
   This contradiction shows that no such $\psi$ exists.

Check: in $\mathbb{N}^*$ the number $3$ admires only $2$.
So a group that contains $3$ must contain $2$, then $1$, then $0$, and $0$ admires itself.

## Remarks

The sentence is the standard example of a plural sentence with no first-order paraphrase in its own vocabulary.
A set paraphrase avoids plurals by adding sets to the domain.
It reads: "there is a nonempty set of critics, each of whom admires only members of the set and not himself".

Step 6 uses a set that is not first-order definable in $\mathcal{N}$, namely the set of nonstandard elements.
So the argument needs the full semantics.
With a [[Henkin semantics|KWEJFK5943]] that offers only the definable sets, the set of step 6 need not be available.

If we weaken "only one another" to "only critics", that is, to $Axy \to Cy$, the sentence becomes first-order.
An example is $\exists x \, (Cx \land \forall y \, (Axy \to Cy))$, and it no longer needs a group.

## Explanations

### L1 human

Picture a group of critics in which each member admires only other members of the group, never themselves and never anyone outside.
The sentence says that such a group exists.
In arithmetic terms, let $0$ admire everybody, and let every other number admire only the number just below it.
Among the ordinary numbers $0, 1, 2, \ldots$ there is no such group: follow the admiration downward and you reach $0$, who admires itself.
In a model of arithmetic with extra "infinite" numbers, the infinite numbers form such a group, because you can go down forever among them.
First-order logic cannot tell the two models apart, so it cannot express the sentence.

### L2 human

We check step 4 for two candidate groups in $\mathbb{N}^*$.

1. Take $X = \set{3, 4, 5}$, with least element $m = 3$.
2. Since $3 = S2$, we have $A32$: the number $3$ admires $2$.
3. The condition asks $2 \in X$, which fails, so $X$ is not a group of the required kind.
4. Take $X = \set{0}$.
   Then $A00$ holds, and the condition asks $0 \neq 0$, which fails.

The typical use of the example is to show that some plural sentences of ordinary language go beyond first-order logic.
Watch out: if you write "only one another" as $Axy \to Cy$, you lose both the group and the condition $x \neq y$.
