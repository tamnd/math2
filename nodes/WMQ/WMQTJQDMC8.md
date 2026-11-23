---
tag: WMQTJQDMC8
kind: example
name: A structured proof that a composition of injective functions is injective
msc: ["00A35", "03E20"]
topics: [STSM6PR7TX]
audience: research
instance_of: [H2W8D7BMSW]
uses: [H2W8D7BMSW, 09NWETVTNY, 0THBK9V825]
sources:
  - doi: 10.1080/00029890.1995.12004627
    locator: pages 600-608
  - url: https://en.wikipedia.org/wiki/Lean_(proof_assistant)
    locator: Examples (Lean 4)
---

## Example

The theorem: let $f \colon A \to B$ and $g \colon B \to C$ be [[injective functions|09NWETVTNY]]; then the [[composition|0THBK9V825]] $g \circ f \colon A \to C$ is injective.
A map $h \colon X \to Y$ is injective when, for all $x_1, x_2 \in X$, $h(x_1) = h(x_2)$ implies $x_1 = x_2$, and $(g \circ f)(a) = g(f(a))$ for each $a \in A$.
Here is the proof in the [[structured format|H2W8D7BMSW]].

- `<1>1.` ASSUME: $a_1, a_2 \in A$ and $g(f(a_1)) = g(f(a_2))$
  PROVE: $a_1 = a_2$
    - `<2>1.` $f(a_1) = f(a_2)$.
      PROOF: $f(a_1)$ and $f(a_2)$ lie in $B$, and $g$ is injective, so the assumption of `<1>1` gives the equality.
    - `<2>2.` Q.E.D.
      PROOF: by `<2>1`, since $f$ is injective.
- `<1>2.` Q.E.D.
  PROOF: by `<1>1` and the definition of an injective function, since $(g \circ f)(a) = g(f(a))$.

The top level has two steps: `<1>1` is the definition of injectivity for $g \circ f$, written as ASSUME/PROVE, and `<1>2` draws the conclusion.
The assumption of `<1>1` is in force only inside its proof, that is, in `<2>1` and `<2>2`.
Step `<2>1` uses the injectivity of $g$, and step `<2>2` uses the injectivity of $f$.
So each hypothesis of the theorem is used exactly once, and the citations show where.
Each leaf proof is one sentence that names its facts, so a reader can check each leaf without the rest.

The same proof in Lean 4 with Mathlib has the same tree, written backward from the goal.

```lean
-- The comments name the matching steps of the structured proof.
example {A B C : Type*} (f : A → B) (g : B → C)
    (hf : Function.Injective f) (hg : Function.Injective g) :
    Function.Injective (g ∘ f) := by  -- the theorem, proved backward.
  intro a₁ a₂ h  -- step <1>1.
  apply hf  -- step <2>2.
  apply hg  -- step <2>1.
  exact h  -- the assumption of step <1>1.
```

The line `intro a₁ a₂ h` is step `<1>1`: it brings in $a_1$, $a_2$ and the hypothesis `h`, and the goal becomes `a₁ = a₂`.
The line `apply hf` is step `<2>2` read backward, and it turns the goal into `f a₁ = f a₂`, the statement of `<2>1`.
The line `apply hg` is the proof of `<2>1` read backward, and the goal becomes `g (f a₁) = g (f a₂)`.
Finally `exact h` closes the goal, because `(g ∘ f) a` unfolds to `g (f a)`.
Mathlib states the theorem as `Function.Injective.comp`.

## Remarks

A structured proof makes the use of each hypothesis visible: $g$ is cited in `<2>1` and $f$ in `<2>2`.

The same format proves that a composition of surjective maps is surjective.
Step `<1>1` takes $c \in C$, then `<2>1` picks $b$ with $g(b) = c$, `<2>2` picks $a$ with $f(a) = b$, and `<2>3` concludes $g(f(a)) = c$.

If $f$ is not injective, step `<2>2` fails.
For $A = \{1, 2\}$, $B = \{0\}$ and $C = \{0\}$ with the constant maps, $g \circ f$ sends $1$ and $2$ to $0$, so it is not injective.
If only $f$ is injective, the proof breaks at `<2>1`, but the conclusion can still hold.
For $f \colon \{1\} \to \{1, 2\}$ with $f(1) = 1$ and $g$ constant on $\{1, 2\}$, the map $g \circ f$ is injective, because its domain has one element.

## Explanations

### L1 human

Two machines are joined: the first turns each input into a code, and the second turns each code into a label.
Each machine sends different inputs to different outputs.
Then the joined machine also sends different inputs to different labels.
The structured proof writes this in two levels.
The top step says what has to be shown, and the lower steps go back one machine at a time: equal labels give equal codes, and equal codes give equal inputs.

### L2 human

We test the proof on $f \colon \{1, 2, 3\} \to \{1, \dots, 6\}$ with $f(a) = 2a$, and $g \colon \{1, \dots, 6\} \to \mathbb{Z}$ with $g(b) = b + 10$.
Both maps are injective, since $2a_1 = 2a_2$ gives $a_1 = a_2$ and $b_1 + 10 = b_2 + 10$ gives $b_1 = b_2$.
Here $(g \circ f)(a) = 2a + 10$, with the values $12$, $14$ and $16$.
Step `<1>1` takes $a_1$ and $a_2$ with $2a_1 + 10 = 2a_2 + 10$.
Step `<2>1` uses $g$ to remove the $+10$, giving $2a_1 = 2a_2$, and step `<2>2` uses $f$ to remove the factor $2$, giving $a_1 = a_2$.

When a machine will check the proof, each step becomes a tactic or a lemma.
Watch out: citing $f$ in step `<2>1` is wrong, because the equation of `<1>1` is about values of $g$, and only the injectivity of $g$ can remove $g$ from it.
