---
tag: 6FWPDEK05X
kind: example
name: The sentence 0 = 0 is a Henkin sentence
msc: ["03F40"]
topics: [HXHHWY3328]
audience: grad
instance_of: [SBMQ5QHG9W]
uses: [SBMQ5QHG9W, F6H4STF9RG, NB2BCZR40F, MPSCREYC3M]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%E2%80%93Bernays_provability_conditions
    locator: lead section
  - book: isbn:9780521857840
---

## Example

Let $T \supseteq \mathsf{PA}$ have the standard [[provability predicate|NB2BCZR40F]], and write $\square \varphi$ for $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$.
The sentence $0 = 0$ does not mention itself, yet it is a [[Henkin sentence|SBMQ5QHG9W]] of $T$.
We check the defining biconditional
$$T \vdash (0 = 0) \leftrightarrow \square (0 = 0).$$

1. $0 = 0$ is an axiom of equality, so $T \vdash 0 = 0$.
2. The [[derivability condition|F6H4STF9RG]] D1 turns a proof into a proof of provability.
   Applied to step 1, it gives $T \vdash \square (0 = 0)$.
3. If $T$ proves $\alpha$ and $\beta$, it proves $\alpha \leftrightarrow \beta$, because $\alpha \to \beta$ and $\beta \to \alpha$ follow from the conclusions $\beta$ and $\alpha$.
   With steps 1 and 2, $T \vdash (0 = 0) \leftrightarrow \square (0 = 0)$.

## Remarks

The same three steps show that every theorem of $T$ is a Henkin sentence.
Löb's theorem gives the converse, so the Henkin sentences of $T$ are exactly its theorems.
So being a Henkin sentence is a property of what a sentence is provably equivalent to, not of the way it is written.

Change the sentence and the example breaks.
For $0 = S0$, step 1 fails, and the biconditional would be equivalent in $T$ to $\mathrm{Con}(T)$, which a consistent $T$ does not prove.
Step 2 is where the theory matters: D1 holds for every theory with a $\Sigma_1$ axiom formula that contains $\mathsf{Q}$, so the example works already for such theories.

## Explanations

### L1 human

The statement "$0 = 0$" can be proved.
So the statement "$0 = 0$ can be proved" can also be proved, by pointing at the proof.
Two statements that can both be proved count as equivalent, so "$0 = 0$" says, up to equivalence, "I can be proved".

### L2 human

We go through the three steps once more with the names of the rules.
The axiom of equality gives $T \vdash 0 = 0$.
D1 gives $T \vdash \square (0 = 0)$, because a real proof of $0 = 0$ has a code, and $\mathsf{Q}$ proves that this code is a proof.
Propositional logic combines the two theorems into the biconditional.
The typical use is to show that a Henkin sentence need not refer to itself.
Watch out: the converse, that every Henkin sentence is a theorem, needs Löb's theorem and is much deeper.
