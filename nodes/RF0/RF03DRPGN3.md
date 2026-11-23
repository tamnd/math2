---
tag: RF03DRPGN3
kind: example
name: Negative introspection fails in an S4.2 model of knowledge
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [EA34W4ERRE]
uses: [N60RVXSA5W, VC3A2VWXND, FDFQFWPM4X, JDE7CN1C48, A2JGSWCMT5]
sources:
  - url: https://en.wikipedia.org/wiki/Epistemic_modal_logic
    locator: section The negative introspection axiom, section Axiom systems
  - url: https://plato.stanford.edu/entries/logic-epistemic/
    locator: Rendsvig and Symons, Epistemic Logic, Stanford Encyclopedia of Philosophy
---

## Example

A clock on the wall shows noon, and an agent reads it.
Let $p$ say "it is noon".
In the good world $x$ the clock works and it is noon.
In the bad world $u$ the clock stopped at noon, and it is really three o'clock.
At $u$ the agent cannot tell that she is not at $x$, because the clock looks the same.
At $x$ she reads a working clock, and we let that rule out $u$.

Let $W = \{u, x\}$ and $R = \{(u, u), (u, x), (x, x)\}$, with $p$ true at $x$ only.
We check that this is a model of knowledge in the sense of $\mathsf{S4.2}$, and that axiom $\mathsf{5}$ fails at $u$.

1. $R$ is reflexive, since $(u, u)$ and $(x, x)$ are in $R$.
2. $R$ is transitive.
   The composable pairs are $(u, u)$ then $(u, x)$, $(u, x)$ then $(x, x)$, and the loops, and each composite is already in $R$.
3. $R$ is directed: from $u$ the agent sees $u$ and $x$, and both see $x$; from $x$ she sees only $x$.
4. Reflexive, transitive and directed frames validate $\mathsf{S4.2}$, which is [[S4|N60RVXSA5W]] plus $\hat K K p \to K \hat K p$.
5. At $x$ the only world seen is $x$, where $p$ is true, so $K p$ is true at $x$.
6. At $u$ the world $u$ is seen and $p$ is false there, so $K p$ is false at $u$ and $\neg K p$ is true at $u$.
7. $K \neg K p$ at $u$ would need $\neg K p$ at $x$, because $u R x$.
   Step 5 gives $K p$ at $x$, so $K \neg K p$ is false at $u$.

So the instance $\neg K p \to K \neg K p$ of axiom $\mathsf{5}$ is false at $u$.
The agent does not know that it is noon, and she does not know that she does not know it.

## Remarks

The frame fails to be [[Euclidean|JDE7CN1C48]]: $u R u$ and $u R x$ hold, but $x R u$ does not.
That is the frame condition of axiom $\mathsf{5}$, as in [[the common modal axioms|FDFQFWPM4X]], and it fails at exactly the point where $\mathsf{5}$ fails.
So $\mathsf{5}$ is not a theorem of $\mathsf{S4.2}$, which sharpens [[the fact that 5 is not a theorem of S4|A2JGSWCMT5]].

The model is the standard picture against negative introspection: an agent in the bad case mistakes it for the good case.
If we add the pair $(x, u)$, the relation becomes the universal one, which is an equivalence relation.
Then the agent at $x$ also sees $u$, so she no longer knows $p$ even in the good case, and $\mathsf{5}$ holds again.
No smaller frame does the job: a one-world preorder is an equivalence relation, and the only two-world preorder that is not one is this chain.

## Explanations

### L1 human

You look at a clock that stopped at noon, and you think it is noon.
You do not know it is noon, because it is not.
You also do not know that you do not know, because the stopped clock looks just like a working one.
The logic $\mathsf{S5}$ says that you always know when you do not know.
This example is the main reason why many people reject $\mathsf{S5}$ as the logic of human knowledge.

### L2 human

To check axiom $\mathsf{5}$ at a world $w$, first ask whether $K p$ fails at $w$, by looking for a world seen from $w$ where $p$ is false.
If it does fail, then check $\neg K p$ at every world seen from $w$.
Here the first part succeeds at $u$ with the witness $u$ itself, and the second part fails at the seen world $x$, where the agent knows $p$.
The typical use is to show that a model satisfies $\mathsf{S4}$ or $\mathsf{S4.2}$ but not $\mathsf{S5}$.
Watch out: $\neg K p$ at $u$ comes from the truth axiom alone, since $p$ is false at $u$; the failure of $\mathsf{5}$ comes from the one-way arrow from $u$ to $x$.

### L3 human

The model is the two-element chain, the smallest directed preorder that is not an equivalence relation.
In philosophy it encodes externalism about knowledge: the good case rules out the bad case, but the bad case does not rule out the good one.
Combined logics of knowledge and belief, such as Stalnaker's, derive $\mathsf{S4.2}$ for knowledge from $\mathsf{KD45}$ for belief and a few bridge principles.
