---
tag: BNCS8H51B2
kind: example
name: Hypersequent derivation of the prelinearity axiom
msc: ["03F05", "03B55"]
topics: [R10RMQCJQX]
audience: grad
instance_of: [73J7F0FN4A]
uses: [3PR9PEMXJ4, P4T18C5736]
sources:
  - url: https://en.wikipedia.org/wiki/Hypersequent
    locator: Intermediate logics
  - url: https://en.wikipedia.org/wiki/Intermediate_logic
    locator: Syntactics
---

## Example

We derive $\Rightarrow (p \to q) \vee (q \to p)$ without cut in Avron's calculus HLC from the [[definition of hypersequent calculus|3PR9PEMXJ4]].
The formula is an instance of the [[prelinearity axiom|P4T18C5736]], the extra axiom of Gödel-Dummett logic.
Recall the communication rule:
$$\dfrac{G \mid \Gamma_1, \Delta_1 \Rightarrow \Pi_1 \qquad G \mid \Gamma_2, \Delta_2 \Rightarrow \Pi_2}{G \mid \Gamma_1, \Gamma_2 \Rightarrow \Pi_1 \mid \Delta_1, \Delta_2 \Rightarrow \Pi_2} \ (\mathsf{com})$$

1. The sequents $q \Rightarrow q$ and $p \Rightarrow p$ are axioms.
2. Apply $\mathsf{com}$ to them with $G$ empty, $\Gamma_1 = \emptyset$, $\Delta_1 = q$, $\Pi_1 = q$, $\Gamma_2 = p$, $\Delta_2 = \emptyset$ and $\Pi_2 = p$.
   The premises are $\Gamma_1, \Delta_1 \Rightarrow \Pi_1$, which is $q \Rightarrow q$, and $\Gamma_2, \Delta_2 \Rightarrow \Pi_2$, which is $p \Rightarrow p$.
3. The conclusion $\Gamma_1, \Gamma_2 \Rightarrow \Pi_1 \mid \Delta_1, \Delta_2 \Rightarrow \Pi_2$ is $p \Rightarrow q \mid q \Rightarrow p$.
4. Apply ${\to}$R to the first component, with side hypersequent $q \Rightarrow p$.
   This gives $\Rightarrow p \to q \mid q \Rightarrow p$.
5. Apply ${\to}$R to the second component, with side hypersequent $\Rightarrow p \to q$.
   This gives $\Rightarrow p \to q \mid \Rightarrow q \to p$.
6. Apply ${\vee}$R to the first component, and ${\vee}$R in its second form to the second component.
   This gives $\Rightarrow (p \to q) \vee (q \to p) \mid \Rightarrow (p \to q) \vee (q \to p)$.
7. The two components of step 6 are equal, so external contraction gives $\Rightarrow (p \to q) \vee (q \to p)$.

Each step uses an axiom or one rule of HLC, and no step uses cut.
Every formula in the derivation is a subformula of $(p \to q) \vee (q \to p)$.

## Remarks

The derivation shows exactly where the communication rule is needed.
Without step 2, every derivable hypersequent would have a component that is derivable on its own, as the [[non-example of HLJ|805SVAZ350]] proves.
But neither $\Rightarrow p \to q$ nor $\Rightarrow q \to p$ is derivable, because each formula fails in a one-world model.
So the derivation must keep both alternatives open until step 7, and only the bar allows that.

What changes if we replace $p$ and $q$ by formulas $A$ and $B$?
The same steps derive $\Rightarrow (A \to B) \vee (B \to A)$, with the axioms $B \Rightarrow B$ and $A \Rightarrow A$ in step 1.
If the axioms are restricted to variables, we first derive $A \Rightarrow A$ for each formula $A$ by induction on $A$, and the rest is unchanged.

## Explanations

### L1 human

The goal is the statement "$p$ gives $q$, or $q$ gives $p$".
We start from two basic facts, "$q$ gives $q$" and "$p$ gives $p$".
The communication rule lets the two facts swap their assumptions, and it keeps both results as alternatives.
This gives "$p$ gives $q$, or $q$ gives $p$".
The other steps only rewrite each alternative as a formula and then merge the two equal alternatives.

### L2 human

The derivation has three phases.
First, communication swaps the antecedents of $q \Rightarrow q$ and $p \Rightarrow p$ and gives $p \Rightarrow q \mid q \Rightarrow p$.
Second, the logical rules work inside each component: ${\to}$R twice and ${\vee}$R twice.
Third, external contraction merges the two equal components.
The typical use of the example is as a test: any calculus for LC must derive the prelinearity axiom without cut.
Watch out in backward search: if you undo ${\vee}$R first, on the single sequent, you must derive $p \to q$ or $q \to p$ alone, and both fail.
Undo external contraction first, so that each disjunct gets its own component.
