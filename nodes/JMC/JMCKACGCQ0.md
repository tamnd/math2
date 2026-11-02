---
tag: JMCKACGCQ0
kind: statement
role: lemma
name: Four lemma
msc: ["18G35", "18E10"]
uses: [Y9CZ3MTNF1, JB7ZBFBA9C, WV898P4X16, Y2NP1JFR86, RVXDSY04KG, 8V296XR2M3, 1WV2THA6NY]
about: [JB7ZBFBA9C]
sources:
  - url: https://en.wikipedia.org/wiki/Five_lemma
---

## Statement

Let $\mathcal{A}$ be an [[abelian category|Y9CZ3MTNF1]], such as the category of modules over a ring.
Consider a [[commutative diagram|WV898P4X16]]
$$\begin{array}{ccccccc} A & \to & B & \to & C & \to & D \\ \downarrow{\scriptstyle \alpha} & & \downarrow{\scriptstyle \beta} & & \downarrow{\scriptstyle \gamma} & & \downarrow{\scriptstyle \delta} \\ A' & \to & B' & \to & C' & \to & D' \end{array}$$
in $\mathcal{A}$ whose two rows are [[exact|JB7ZBFBA9C]].

1. If $\alpha$ is an [[epimorphism|RVXDSY04KG]] and $\beta$ and $\delta$ are [[monomorphisms|Y2NP1JFR86]], then $\gamma$ is a monomorphism.
2. If $\delta$ is a monomorphism and $\alpha$ and $\gamma$ are epimorphisms, then $\beta$ is an epimorphism.

## Remarks

Part 1 is a diagram chase.
Let the row maps be $r \colon A \to B$, $s \colon B \to C$, $t \colon C \to D$ and $r', s', t'$ below.
If $\gamma(x) = 0$ for $x \in C$, then $\delta(t(x)) = t'(\gamma(x)) = 0$, so $t(x) = 0$ and $x = s(y)$ for some $y \in B$.
Then $s'(\beta(y)) = 0$, so $\beta(y) = r'(u')$ with $u' = \alpha(u)$ for some $u \in A$; now $\beta(y - r(u)) = 0$, so $y = r(u)$ and $x = s(r(u)) = 0$.
Part 2 is the dual statement, obtained by reversing all arrows.
Example: take $A = A' = 0$, so that the rows are exact sequences $0 \to B \to C \to D$ and $0 \to B' \to C' \to D'$.
If $\beta$ and $\delta$ are monomorphisms, part 1 shows that $\gamma$ is a monomorphism.

## Explanations

### L1 human

The four lemma is the five lemma split into two halves.
One half says when the third vertical map is one-to-one, and the other half says when the second vertical map is onto.
Each half needs only four columns of the ladder.

### L2 human

The two parts are proved by element chasing in modules, and hold in every abelian category by the [[Freyd–Mitchell embedding theorem|8V296XR2M3]] or by [[pseudo-elements|1WV2THA6NY]].
Applying part 1 to the left four columns and part 2 to the right four columns of a five-column ladder gives the five lemma.
The four lemma is useful when only one of injectivity or surjectivity is needed, so fewer hypotheses have to be checked.
