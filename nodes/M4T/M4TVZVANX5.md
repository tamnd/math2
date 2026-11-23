---
tag: M4TVZVANX5
kind: example
name: Finiteness is definable in second-order logic
msc: ["03B16", "03C85"]
topics: [MDHDYV8QZW]
audience: grad
instance_of: [G6X7SZSNC5]
uses: [G6X7SZSNC5, 1NR3HAWG9D, 070R982G4B, 0PWE3BCHVJ, 09NWETVTNY]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: Expressive power
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: Metalogical results
---

## Example

A set is finite exactly when it cannot be mapped one-to-one into itself with an element left over.
Second-order logic can say this in one sentence, because it can quantify over all maps.
Let $L$ be any signature, and let $R$ be a binary relation variable.
Consider the sentence of [[second-order logic|G6X7SZSNC5]]
$$\mathrm{Inf} := \exists R \, \big( \alpha(R) \land \beta(R) \land \exists z \, \forall x \, \neg R(x, z) \big),$$
where $\alpha(R)$ and $\beta(R)$ are the following formulas:
$$\alpha(R) := \forall x \, \exists y \, R(x, y) \land \forall x \forall y \forall z \, (R(x, y) \land R(x, z) \to y = z),$$
$$\beta(R) := \forall x \forall y \forall z \, (R(x, z) \land R(y, z) \to x = y).$$
The formula $\alpha(R)$ says that $R$ is the graph of a function $g$ from the domain to itself.
The formula $\beta(R)$ says that $g$ is [[injective|09NWETVTNY]].
The last part says that some element $z$ is not a value of $g$.
Let $\mathrm{Fin} := \neg \mathrm{Inf}$.
We show that in the full semantics, a structure $\mathcal{M}$ satisfies $\mathrm{Fin}$ exactly when its domain $M$ is [[finite|070R982G4B]].

1. Let $M$ be finite with $n$ elements, and suppose $\mathcal{M} \models \mathrm{Inf}$.
   Then some injective $g \colon M \to M$ misses an element $z$.
2. Since $g$ is injective, its image has $n$ elements.
   A subset of $M$ with $n$ elements is $M$ itself, so $g$ is onto, which contradicts step 1.
   So $\mathcal{M} \models \mathrm{Fin}$.
3. Let $M$ be [[infinite|0PWE3BCHVJ]].
   Then $M$ contains distinct elements $a_0, a_1, a_2, \ldots$, by the axiom of countable choice in the metatheory.
4. Define $g(a_i) = a_{i+1}$ for each $i$, and $g(x) = x$ for each $x$ that is not of the form $a_i$.
5. The map $g$ is injective.
   Two elements $a_i \neq a_j$ go to $a_{i+1} \neq a_{j+1}$.
   Two other elements $x \neq y$ go to $x \neq y$.
   An element $a_i$ and an element $x$ of the other kind go to $a_{i+1}$ and $x$.
   These differ, because $x$ is not of the form $a_k$.
6. The element $a_0$ is not a value of $g$.
   It is not $a_{i+1}$ for any $i$, and it is not a value $g(x) = x$ with $x$ of the other kind.
7. In the full semantics, $R$ ranges over all subsets of $M^2$, so $R$ can be the graph of $g$.
   Then $\alpha$, $\beta$ and the last part hold, so $\mathcal{M} \models \mathrm{Inf}$ and $\mathcal{M} \not\models \mathrm{Fin}$.

Now we show that the [[compactness theorem|1NR3HAWG9D]] fails for the full semantics.
For $n \ge 1$, let $\lambda_n$ be the first-order sentence $\exists x_1 \cdots \exists x_n \bigwedge_{i < j} x_i \neq x_j$, which says that there are at least $n$ elements.
Let $\Gamma = \set{\mathrm{Fin}} \cup \set{\lambda_n : n \ge 1}$.

8. Let $\Gamma_0 \subseteq \Gamma$ be finite.
   Let $N$ be the largest $n$ with $\lambda_n \in \Gamma_0$, or $N = 1$ if there is none.
9. A structure with exactly $N$ elements satisfies $\lambda_n$ for each $n \le N$, and it satisfies $\mathrm{Fin}$ by step 2.
   So it is a model of $\Gamma_0$.
10. A model of $\Gamma$ satisfies $\mathrm{Fin}$, so it is finite by step 7, say with $n$ elements.
    It also satisfies $\lambda_{n+1}$, so it has at least $n + 1$ elements, a contradiction.
11. So every finite subset of $\Gamma$ has a model, but $\Gamma$ has none, and compactness fails.

## Remarks

One second-order sentence does here what no set of first-order sentences can do.
In first-order logic, compactness shows that no set of sentences has exactly the finite structures as its models.
Steps 8 to 11 are the same argument.

Step 3 uses countable choice.
Without any form of choice in the metatheory, $\mathrm{Fin}$ defines the Dedekind-finite sets, and these can differ from the finite sets.

With the [[Henkin semantics|KWEJFK5943]], $\Gamma$ has a model, because the Henkin semantics is compact.
The domain of this model is infinite.
Its family of binary relations contains no graph of an injective map that misses an element.
So the meaning of $\mathrm{Fin}$ depends on the semantics, and step 7 is the step that needs the full semantics.

## Explanations

### L1 human

A set is finite exactly when there is no way to shift its elements one-to-one so that a place stays empty.
For the set $\set{1, 2, 3}$, any one-to-one shift uses all three places, so no place stays empty.
For the natural numbers, the shift $n \mapsto n + 1$ is one-to-one and leaves $0$ empty.
Second-order logic can say "there is such a shift", because it can talk about all relations.
So one sentence says "the set is infinite", and its negation says "the set is finite".

### L2 human

We find the shift of step 4 for the set $M = \mathbb{Z}$.

1. Take $a_i = i$ for $i \ge 0$.
   These are distinct elements of $\mathbb{Z}$.
2. Then $g(i) = i + 1$ for $i \ge 0$, and $g(x) = x$ for $x < 0$.
3. The map $g$ is injective, because values from $i \ge 0$ are at least $1$, and values from $x < 0$ are negative.
4. The value $0$ is missed, because $i + 1 \ge 1$ for $i \ge 0$, and $g(x) = x < 0$ for $x < 0$.

Check: $g(-2) = -2$, $g(0) = 1$ and $g(1) = 2$ are distinct, and no input gives $0$.

We use $\mathrm{Fin}$ to show that second-order logic with the full semantics is not compact.
The trap is to believe that the map $g$ must be defined by a formula of the language.
In the full semantics, any relation counts, even one that no formula defines.

### L3 human

The sentence $\mathrm{Inf}$ is existential second-order, so $\mathrm{Fin}$ is universal second-order.
The categoricity of [[second-order Peano arithmetic|CKEG6B25AN]] shows that the full semantics also fails the upward Löwenheim-Skolem theorem.
[[Lindström's theorem|FYZ3CJGZYV]] says that a logic stronger than first-order logic loses compactness or the downward Löwenheim-Skolem property.
The logic with the generalized quantifier "there are infinitely many" also defines finiteness, and [[it also loses compactness|SD6TYGCEEB]].
