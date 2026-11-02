---
tag: CTVVXCWTX7
kind: definition
name: Exact category
msc: ["18E05", "18E10"]
defines: TFADSC9YPZ
uses: [B2VP96NJSK, S417YNEJ6M, H8W38933NC, Q05K04QJ71, Q699KKMVJD, Y9CZ3MTNF1]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_category
---

## Definition

Let $\mathcal{E}$ be an [[additive category|B2VP96NJSK]].
A *kernel–cokernel pair* is a pair of composable morphisms $A \xrightarrow{i} B \xrightarrow{p} C$ such that $i$ is a [[kernel|S417YNEJ6M]] of $p$ and $p$ is a [[cokernel|H8W38933NC]] of $i$.
An *exact structure* on $\mathcal{E}$ is a class $\mathcal{S}$ of kernel–cokernel pairs, closed under isomorphism of pairs, whose members are called *conflations*.
In a conflation $(i, p)$, the morphism $i$ is called an *inflation* and $p$ a *deflation*.
The class $\mathcal{S}$ must satisfy:

1. For every object $A$, the identity $1_A$ is an inflation and a deflation.
2. A composite of two inflations is an inflation, and a composite of two deflations is a deflation.
3. For every inflation $i \colon A \to B$ and every morphism $f \colon A \to A'$, the [[pushout|Q699KKMVJD]] of $i$ along $f$ exists and is an inflation $A' \to B'$.
4. For every deflation $p \colon B \to C$ and every morphism $g \colon C' \to C$, the [[pullback|Q05K04QJ71]] of $p$ along $g$ exists and is a deflation $B' \to C'$.

An *exact category* is an additive category together with an exact structure.

## Remarks

This is Quillen's notion, in the streamlined form of Keller.
Inflations are also called admissible monomorphisms, and deflations admissible epimorphisms.

Example: every [[abelian category|Y9CZ3MTNF1]] with the class of all short exact sequences is an exact category.
Every morphism has a kernel and a cokernel, pushouts and pullbacks exist, and pushouts of monomorphisms are monomorphisms while pullbacks of epimorphisms are epimorphisms.
Example: every additive category with the class of split exact sequences $A \to A \oplus C \to C$ is an exact category.

Non-example: in the category of abelian groups, the class of short exact sequences whose three terms are finite groups fails clause 1.
The identity of $\Z$ is not an inflation, because the only kernel–cokernel pair $\Z \xrightarrow{1} \Z \to 0$ that contains it has an infinite term.
