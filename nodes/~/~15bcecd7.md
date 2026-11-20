---
tag: ~15bcecd7
kind: statement
role: theorem
name: The sorites argument is valid
aliases: [sorites-validity, sorites-inconsistency]
msc: ["03A05", "03B05"]
topics: [6Q4JJ2MMV8]
audience: ug2
about: [~44206687]
uses: [~44206687, PDFBXAN9CC]
proofs: [~f5263999]
sources:
  - url: https://plato.stanford.edu/entries/sorites-paradox/
    locator: "Sorites Paradox, 2. Different Formulations of the Paradox"
  - url: https://plato.stanford.edu/entries/sorites-paradox/
    locator: "Sorites Paradox, 3.3.1 Supervaluationism"
---

## Statement

Let $N \ge 2$, and let $p_1, \ldots, p_N$ be propositional variables; in the example, $p_n$ is $H(n)$, "$n$ grains make a heap".
Let $\Gamma_N$ be the set of the following $N + 1$ premises.

- (P1) $p_N$.
- (P2) $\neg p_1$.
- (C$_n$) $p_{n + 1} \to p_n$, for each $n$ with $1 \le n \le N - 1$. These are the [[tolerance conditionals|~44206687]].

Then the following hold.

1. *(Conditional form.)* (P1) and the conditionals C$_1$ to C$_{N-1}$ derive $p_1$ by exactly $N - 1$ applications of modus ponens.
2. *(Inconsistency.)* $\Gamma_N$ is inconsistent: it derives both $p_1$ and $\neg p_1$. So no valuation makes all of $\Gamma_N$ true.
3. *(Line-drawing form.)* In classical logic, (P1) and (P2) derive $\bigvee_{n = 1}^{N - 1} (p_{n + 1} \wedge \neg p_n)$.

Parts 1 and 2 hold in intuitionistic logic as well.

## Remarks

### Why each hypothesis is needed

1. Without (P1), the valuation with every $p_n$ false makes all other premises true.
2. Without (P2), the valuation with every $p_n$ true makes all other premises true.
3. Without one conditional C$_k$, the valuation "$p_n$ true iff $n \ge k + 1$" makes all other premises true. Only C$_k$ fails, since $p_{k+1}$ is true and $p_k$ is false.

### Consequences

1. Any account of "heap" that accepts (P1) and (P2) in classical logic must reject some tolerance conditional; see the [[sorites paradox|~13b952b1]].
2. The proof uses only modus ponens. So a response to the paradox must reject a premise or restrict modus ponens across many steps.

### Converse

Each proper subset of $\Gamma_N$ is consistent, by the three valuations above.
So $\Gamma_N$ is a minimal inconsistent set.

### Generalizations

1. The SEP entry gives an induction form: from $\Phi\alpha_1$ and $\forall n\, (\Phi\alpha_n \to \Phi\alpha_{n + 1})$, infer $\forall n\, \Phi\alpha_n$.
2. The same proof works for any [[sorites series|PDFBXAN9CC]] and any predicate.

## History

The SEP entry describes the conditional form, the induction form and the line-drawing form, and it uses the conditional form as the main one.
It credits the first formulation of the puzzle to Eubulides.

## Explanations

### L1 human

Start with $10000$ grains: that is a heap.
Remove a grain: still a heap.
Do this again and again, $9999$ times.
At the end, a single grain is a "heap", which is false.
The theorem says that the reasoning has no logical gap: each step is the same simple rule.

### L2 human

Take $N = 4$.

1. (P1) gives $p_4$.
2. C$_3$ is $p_4 \to p_3$. Modus ponens gives $p_3$.
3. C$_2$ is $p_3 \to p_2$. Modus ponens gives $p_2$.
4. C$_1$ is $p_2 \to p_1$. Modus ponens gives $p_1$.
5. (P2) is $\neg p_1$. Steps 4 and 5 give a contradiction, after $3 = N - 1$ steps of modus ponens.

The typical use of the theorem is to show that the paradox is not a logical mistake.
The trap is to think that a long chain is less valid than a short one: validity does not depend on the length.

### L3 human

The theorem is a propositional fact, and it does not use vagueness.
The paradox lies in the joint plausibility of the premises.
In a degree semantics such as [[Łukasiewicz logic|EP8J937EQC]], each premise can have value close to $1$, while the conclusion has value $0$.
