---
tag: CAA7K3VF59
kind: example
name: The full structure on the natural numbers is a model of second-order arithmetic
msc: ["03F35", "03B30"]
topics: [BY8AAFN7C5]
audience: grad
instance_of: [DC60FYCSPM, MKB74TX3Z8, T21WETAHN5, J0Z2GNJZ2W]
uses: [DC60FYCSPM, Y92NXGEQBD]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: Models
---

## Example

Let $\mathcal{N} = (\mathbb{N}, \mathcal{P}(\mathbb{N}))$ be the $L_2$-structure whose numbers are the natural numbers with the usual $0, 1, +, \cdot, <$, and whose sets are all subsets of $\mathbb{N}$.
We check that $\mathcal{N}$ is a model of [[second-order arithmetic|DC60FYCSPM]], axiom by axiom, with the axioms of the [[definition|Y92NXGEQBD]].

1. The basic axioms are true statements about the natural numbers.
   For example, $n + 1 \ne 0$ holds because $0$ is not a successor in $\mathbb{N}$.
   The axiom $m < n + 1 \leftrightarrow (m < n \vee m = n)$ holds because no natural number lies strictly between $n$ and $n + 1$.
2. The induction axiom holds.
   Let $X \subseteq \mathbb{N}$ contain $0$ and be closed under $n \mapsto n + 1$, and suppose that $X \ne \mathbb{N}$.
   Then $\mathbb{N} \setminus X$ has a least element $n_0$, and $n_0 \ne 0$, so $n_0 = m + 1$ with $m \in X$.
   Closure gives $n_0 \in X$, a contradiction, so $X = \mathbb{N}$.
3. The comprehension scheme holds.
   Let $\varphi(n)$ be any $L_2$-formula, with parameters in $\mathbb{N}$ and in $\mathcal{P}(\mathbb{N})$.
   The set $A = \{ n \in \mathbb{N} : \mathcal{N} \models \varphi(n) \}$ is a subset of $\mathbb{N}$, so $A \in \mathcal{P}(\mathbb{N})$, and $A$ witnesses the instance $\exists X \, \forall n \, (n \in X \leftrightarrow \varphi(n))$.
4. The number part of $\mathcal{N}$ is standard, so $\mathcal{N}$ is an $\omega$-model of $\mathsf{Z}_2$.
5. Each subsystem, such as [[ATR0|MKB74TX3Z8]] or [[Π¹₁-CA0|T21WETAHN5]], has only axioms that are theorems of $\mathsf{Z}_2$, so $\mathcal{N}$ is a model of each subsystem.
6. A $\Sigma^1_1$ formula with parameters in $\mathcal{N}$ asks for a set, and the sets of $\mathcal{N}$ are all subsets of $\mathbb{N}$.
   So the formula is true in $\mathcal{N}$ exactly when it is true, and $\mathcal{N}$ is a [[β-model|J0Z2GNJZ2W]].

## Remarks

$\mathcal{N}$ is the intended model of $\mathsf{Z}_2$, and it is the largest $\omega$-model, since every $\omega$-model has a family $\mathcal{S} \subseteq \mathcal{P}(\mathbb{N})$.
Step 3 is the only step that uses the full power set.
The formula $\varphi$ may contain set quantifiers, and these range over all subsets, so the set $A$ is always available.

In a structure with fewer sets, step 3 can fail.
In the structure of [[computable sets|W4J2H41PB7]], the halting set is defined by a formula with one unbounded number quantifier, and it is missing.
Steps 1 and 2 hold in every $\omega$-structure, because they speak about the standard numbers and about each set separately.

The set of sentences true in $\mathcal{N}$ is not arithmetical.
By the incompleteness theorems, no theory with a computable set of axioms proves exactly the sentences true in $\mathcal{N}$.

## Explanations

### L1 human

Here every set of natural numbers is allowed.
So for every property that the theory can express, the set of numbers with that property is there.
Induction holds because the natural numbers have no gaps: each number is reached from $0$ by adding $1$ again and again.

### L2 human

Step 2 uses the least number principle in the metatheory, where we reason about the true natural numbers.
Step 3 needs no work, but it hides a definition of truth by recursion on formulas, and truth of a formula with set quantifiers refers to all subsets of $\mathbb{N}$.

A typical use is to show that $\mathsf{Z}_2$ and all its subsystems are consistent, under the assumption that $\mathcal{P}(\mathbb{N})$ exists.
Watch out: $\mathcal{N}$ is not the only model.
By the compactness theorem, $\mathsf{Z}_2$ also has models with non-standard numbers, and by the Löwenheim-Skolem theorem it has countable $\omega$-models with far fewer sets.
