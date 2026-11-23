---
tag: SD6TYGCEEB
kind: example
name: Logic with the quantifier there are infinitely many is not compact
msc: ["03C80"]
topics: [MDHDYV8QZW]
audience: grad
uses: [MFV98WTF4G, 1NR3HAWG9D, FYZ3CJGZYV, 0PWE3BCHVJ]
instance_of: [MFV98WTF4G]
sources:
  - url: https://en.wikipedia.org/wiki/Lindström_quantifier
    locator: As precursors to Lindström's theorem
  - url: https://en.wikipedia.org/wiki/Generalized_quantifier
    locator: Examples
---

## Example

The word "infinitely many" makes logic stronger, and the price is the compactness theorem.
Let $Q_0$ be the [[generalized quantifier|MFV98WTF4G]] of type $\langle 1 \rangle$ given by this class:
$$Q_0 = \{ (M, A) : A \text{ is an infinite subset of } M \}.$$
In the logic $L(Q_0)$, the formula $Q_0 x \, \varphi(x)$ is true in $\mathcal{M}$ when infinitely many elements of $M$ satisfy $\varphi$.
We show that $L(Q_0)$ does not have the compactness property of first-order logic.

1. First we check that $Q_0$ is a generalized quantifier.
   A bijection $f \colon M \to M'$ maps each [[infinite subset|0PWE3BCHVJ]] $A$ of $M$ to an infinite subset $f[A]$ of $M'$.
   So the class $Q_0$ is closed under isomorphism.
2. For $n \geq 2$, let $\lambda_n$ be the first-order sentence that says "there are at least $n$ elements":
   $$\lambda_n = \exists x_1 \cdots \exists x_n \bigwedge_{i < j} x_i \neq x_j.$$
   It is true in $\mathcal{M}$ exactly when $|M| \geq n$.
3. In the empty vocabulary, let $\Sigma$ be this set of sentences:
   $$\Sigma = \{ \neg Q_0 x \, (x = x) \} \cup \{ \lambda_n : n \geq 2 \}.$$
4. Let $\Sigma_0$ be a finite subset of $\Sigma$.
   Then there is a number $N \geq 2$ such that $\Sigma_0$ contains $\lambda_n$ only for $n \leq N$.
   The set $\{1, \ldots, N\}$ has $N$ elements, so it satisfies these $\lambda_n$.
5. The set $\{1, \ldots, N\}$ is finite, so the set that $x = x$ defines in it is finite.
   So $\neg Q_0 x \, (x = x)$ is true in it, and $\Sigma_0$ has a model.
6. Now suppose that $\mathcal{M}$ is a model of $\Sigma$.
   By step 2, $|M| \geq n$ for every $n$, so $M$ is infinite.
7. Then the set that $x = x$ defines is the infinite set $M$, so $Q_0 x \, (x = x)$ is true in $\mathcal{M}$.
   This contradicts $\neg Q_0 x \, (x = x) \in \Sigma$.
8. So every finite subset of $\Sigma$ has a model, and $\Sigma$ has none.
   Thus $L(Q_0)$ is not compact.

## Remarks

The [[compactness theorem|1NR3HAWG9D]] of first-order logic is exactly what fails.
Read in first-order logic, the same argument shows that no first-order sentence says "the domain is finite".
In $L(Q_0)$ the sentence $\neg Q_0 x \, (x = x)$ says it, and compactness has to go.

[[Lindström's theorem|FYZ3CJGZYV]] shows that this failure is not an accident of the example.
The logic $L(Q_0)$ is a regular logic, and it is strictly stronger than first-order logic, because $Q_0 x \, (x = x)$ has no first-order equivalent.
Each formula $Q_0 x \, \varphi$ is equivalent to the countable conjunction of the formulas "at least $n$ elements satisfy $\varphi$".
So $L(Q_0)$ is a part of the infinitary logic $L_{\omega_1 \omega}$, and it has the downward Löwenheim-Skolem property of $L_{\omega_1 \omega}$.
Then Lindström's theorem says that $L(Q_0)$ must fail compactness, and the example shows one failure.

The quantifier $Q_1$, "uncountably many", behaves the other way.
If we write $\neg Q_1$ in place of $\neg Q_0$ in $\Sigma$, the new set has a model, the countable set $\mathbb{N}$.
In fact $L(Q_1)$ is countably compact by Keisler's completeness theorem, and it fails the downward Löwenheim-Skolem property instead.

## Explanations

### L1 human

Compactness says this: if every finite part of a list of demands can be met, then the whole list can be met.
Here the demands are "there are at least $2$ things", "there are at least $3$ things", and so on, together with "there are not infinitely many things".
A large enough finite collection meets any finite part of the list.
The whole list asks for a collection that is larger than every number and still finite, and no such collection exists.
So the new word "infinitely many" breaks compactness.

### L2 human

We check steps 4 and 5 on one finite subset.

1. Take $\Sigma_0 = \{ \neg Q_0 x \, (x = x), \lambda_2, \lambda_5, \lambda_9 \}$.
2. The largest index is $N = 9$, so we take the domain $\{1, \ldots, 9\}$.
3. The domain has $9$ elements, so $\lambda_2$, $\lambda_5$ and $\lambda_9$ hold.
   Check: $9 \geq 2$, $9 \geq 5$ and $9 \geq 9$.
4. The domain is finite, so $\neg Q_0 x \, (x = x)$ holds, and $\Sigma_0$ has a model.

The typical use of this example is as a first test of a new logic: we ask whether the logic can say "infinite" or "finite".
Watch out: the failure does not come from the size of $\Sigma$.
The set $\Sigma$ is countable, so even countable compactness fails for $L(Q_0)$.
