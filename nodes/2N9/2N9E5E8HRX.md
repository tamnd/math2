---
tag: 2N9E5E8HRX
kind: example
name: Labeled derivation of the axiom 4
msc: ["03F05", "03B45"]
topics: [R10RMQCJQX]
audience: grad
instance_of: [F46GV42XCE]
uses: [VW8XP95XCB, 0GJZW9JFZQ, FDFQFWPM4X]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Common modal axiom schemata
---

## Example

We derive the axiom 4, $\Box p \to \Box\Box p$, in the calculus G3K4 of the [[definition of labeled sequent calculus|VW8XP95XCB]].
G3K4 is G3K with the frame rule for [[transitivity|0GJZW9JFZQ]]:
$$\dfrac{x R z, x R y, y R z, \Gamma \Rightarrow \Delta}{x R y, y R z, \Gamma \Rightarrow \Delta} \ (\mathrm{Trans})$$
The goal is the sequent $\Rightarrow x : \Box p \to \Box\Box p$.

### The derivation

1. The sequent $z : p, x : \Box p, x R z, x R y, y R z \Rightarrow z : p$ is initial, because $z : p$ occurs on both sides.
2. Apply ${\Box}$L with principal formula $x : \Box p$ and atom $x R z$. The conclusion is $x : \Box p, x R z, x R y, y R z \Rightarrow z : p$.
3. Apply Trans with $\Gamma = x : \Box p$ and $\Delta = z : p$. The conclusion is $x : \Box p, x R y, y R z \Rightarrow z : p$.
4. Apply ${\Box}$R with eigenvariable $z$. The conclusion is $x : \Box p, x R y \Rightarrow y : \Box p$.
5. Apply ${\Box}$R with eigenvariable $y$. The conclusion is $x : \Box p \Rightarrow x : \Box\Box p$.
6. Apply ${\to}$R. The conclusion is $\Rightarrow x : \Box p \to \Box\Box p$.

Each step is an initial sequent or one rule of G3K4, and no step uses cut.

### The eigenvariable conditions

7. Step 4 is ${\Box}$R with $\Gamma = x : \Box p, x R y$ and $\Delta$ empty, so the premise is $y R z, \Gamma \Rightarrow z : p$. Its eigenvariable $z$ does not occur in the conclusion $\Gamma \Rightarrow y : \Box p$.
8. Step 5 is ${\Box}$R with $\Gamma = x : \Box p$ and $\Delta$ empty, so the premise is $x R y, \Gamma \Rightarrow y : \Box p$. Its eigenvariable $y$ does not occur in the conclusion $\Gamma \Rightarrow x : \Box\Box p$.

### Without transitivity

We check that G3K alone does not derive the sequent.

9. Take the frame with worlds $a, b, c$ and $a R b$, $b R c$ only. It is not transitive.
10. Let $p$ be true at $b$ only. Then $\Box p$ holds at $a$, because $b$ is the only world that $a$ reaches.
11. $\Box p$ fails at $b$, because $b R c$ and $p$ fails at $c$. So $\Box\Box p$ fails at $a$.
12. So $\Box p \to \Box\Box p$ fails at $a$, and the sound calculus G3K does not derive it.

## Remarks

The rule Trans is the only step that uses transitivity.
In the backward reading it adds $x R z$ from $x R y$ and $y R z$, so that ${\Box}$L can send $x : \Box p$ two steps along $R$.
In the countermodel of steps 9 to 12, $a R c$ fails, and that is the missing atom.

The two ${\Box}$R steps need different fresh labels.
The label $y$ occurs in the conclusion of step 4, so step 4 cannot reuse $y$ as its eigenvariable, and it takes $z$.

Combining Ref and Trans gives G3S4, which derives both T and 4.

## Explanations

### L1 human

The axiom 4 says: if $p$ is necessary, then "$p$ is necessary" is itself necessary.
Read with worlds: if $p$ holds at every world one step away, then it holds at every world two steps away.
That is true when every world two steps away is also one step away, which is what transitivity says.
The proof uses the rule Trans at the point where a two-step path must be turned into a one-step path.

### L2 human

We read the derivation as a backward proof search.
Backward ${\to}$R reduces the goal to $x : \Box p \Rightarrow x : \Box\Box p$.
Backward ${\Box}$R with a new world $y$ gives $x : \Box p, x R y \Rightarrow y : \Box p$.
Backward ${\Box}$R with a new world $z$ gives $x : \Box p, x R y, y R z \Rightarrow z : p$.
Then Trans adds $x R z$, and ${\Box}$L adds $z : p$, which closes the branch.
The typical use of this pattern is in proofs for S4 and its extensions.
Watch out: ${\Box}$L cannot use the atom $y R z$ here, because the principal formula is $x : \Box p$, and the rule needs an atom that starts at $x$.
