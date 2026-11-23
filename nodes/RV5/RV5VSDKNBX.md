---
tag: RV5VSDKNBX
kind: example
name: A satisfiable set that is not a Hintikka set
msc: ["03B10", "03F03"]
topics: [TTCRX3NFNY]
audience: ug2
not_instance_of:
  - target: RJNDEG07R1
    fails: [4, 5]
    note: the set is satisfiable, but the γ sentence lacks its instance ¬Q(c) and the δ sentence has no instance P(t)
uses: [RJNDEG07R1, 2A6QP78XN3, QN7M1JCGT9, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Hintikka_set
    locator: lead section
---

## Example

Let $L$ be the language with one constant symbol $c$ and two unary relation symbols $P$ and $Q$, so its only closed term is $c$.
Let
$$\Gamma = \{ \exists x\, P(x),\ \forall x\, \neg Q(x) \}.$$

1. $\Gamma$ is [[satisfiable|QN7M1JCGT9]].
   The [[structure|983GZBQYT4]] with domain $\{ 1 \}$, $c$ read as $1$, $P = \{ 1 \}$ and $Q = \varnothing$ makes both members true.
2. Condition 1 of a [[Hintikka set|RJNDEG07R1]] holds, because $\Gamma$ has no literal.
3. Conditions 2 and 3 hold, because $\Gamma$ has no $\alpha$ and no $\beta$ sentence.
4. Condition 4 fails.
   The $\gamma$ sentence $\forall x\, \neg Q(x)$ needs its instance $\neg Q(c)$, and $\neg Q(c) \notin \Gamma$.
5. Condition 5 fails.
   The $\delta$ sentence $\exists x\, P(x)$ needs an instance $P(t)$ at a closed term, the only candidate is $P(c)$, and $P(c) \notin \Gamma$.

So $\Gamma$ is satisfiable, and it is not a Hintikka set.

## Remarks

### The converse of Hintikka's lemma fails

[[Hintikka's lemma|2A6QP78XN3]] turns every Hintikka set into a model, but satisfiable sets need not be Hintikka sets.
The conditions are really needed for the construction.
The term structure that the lemma would build from $\Gamma$ has domain $\{ c \}$ and makes every atom false, since $\Gamma$ has no atomic member.
In that structure $\exists x\, P(x)$ is false, so the construction fails for $\Gamma$.

### Repairing the set

The set $\Gamma \cup \{ P(c), \neg Q(c) \}$ is a Hintikka set.
The $\gamma$ sentence has its only instance, the $\delta$ sentence has the instance $P(c)$, and the literals do not clash.
Its term model is the structure of step 1, with $c$ in place of $1$.
This is the general pattern: a satisfiable set extends to a Hintikka set, and a tableau finds the extension.

## Explanations

### L1 human

The list "some ball is red; no ball is blue" correctly describes a possible world.
But it does not name the red ball, and it does not say of ball $c$ that it is not blue.
A Hintikka set must give these simple facts, so this list is not one yet.
Adding "ball $c$ is red" and "ball $c$ is not blue" completes it.

### L2 human

To repair a set that is not saturated, add the missing pieces one condition at a time.

1. The $\gamma$ sentence $\forall x\, \neg Q(x)$ needs $\neg Q(c)$, so we add it.
2. The $\delta$ sentence $\exists x\, P(x)$ needs some instance, so we add $P(c)$.
3. The new members are literals and do not clash, so the repair stops.

Watch out: the repair does not always succeed in the old language.
For $\{ \exists x\, P(x), \neg P(c) \}$ the only closed term $c$ cannot be the witness, so a Hintikka set that contains this set needs a new constant, just as the $\delta$ rule of a tableau does.
