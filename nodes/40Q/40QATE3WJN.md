---
tag: 40QATE3WJN
kind: example
name: The proof of the Kepler conjecture and its formal verification
aliases: [flyspeck-project]
msc: ["52C17", "00A35"]
topics: [1BTHSHST4M]
audience: research
instance_of: [MC18C7BMFT]
uses: [MC18C7BMFT, AFMBQT06ZV, HF32CBN5MA, VNMXB0J2KA]
sources:
  - url: https://en.wikipedia.org/wiki/Kepler_conjecture
    locator: Hales' proof
  - url: https://en.wikipedia.org/wiki/Kepler_conjecture
    locator: A formal proof
---

## Example

The [[Kepler conjecture|AFMBQT06ZV]] says that no [[packing|HF32CBN5MA]] of equal balls in space has a density greater than
$$\frac{\pi}{\sqrt{18}} \approx 0.7405,$$
the density of the usual stack of oranges on a market stall.
Johannes Kepler stated it in 1611.
Thomas Hales proved it with a large computation, and the proof was fully accepted only after a formal verification.
We check that the proof is a [[computer-assisted proof|MC18C7BMFT]], and then we follow its acceptance.

1. The written reduction. Hales reduced the problem to a statement about finitely many local configurations of balls. The written argument shows that a packing of higher density would give a configuration that breaks one of a finite set of inequalities.
2. The computer part. From 1992 Hales, with his graduate student Samuel Ferguson, checked these inequalities by computer. The work applied [[linear programming|VNMXB0J2KA]] to more than $5000$ configurations and solved about $100000$ linear programs.
3. The size. When Hales announced the proof in August 1998, it consisted of about $250$ pages of notes and about $3$ gigabytes of programs, data and results.
4. Step 1 is a written proof, and the computations of step 2 are far beyond a check by hand, so the proof is computer-assisted.

## Remarks

The *Annals of Mathematics* agreed to publish the proof if a panel of twelve referees accepted it.
In 2003 the head of the panel, Gábor Fejes Tóth, reported that the referees were "99% certain" of the proof, because they could not certify all of the computer calculations.
The *Annals* published Hales's article in 2005, and *Discrete and Computational Geometry* published the computational parts, by Hales and Ferguson, in 2006.

To remove the remaining doubt, Hales announced the Flyspeck project in January 2003, with the aim of a complete formal proof.
In 2012 he published a blueprint that rewrote the proof in a form suited to formalization.
The project announced the completion of the formal proof on 10 August 2014, checked with the proof assistants HOL Light and Isabelle.
The paper on the formal proof, with Hales and many collaborators as authors, was published in *Forum of Mathematics, Pi* in 2017.

The example shows the limit of traditional refereeing.
Twelve expert referees worked for years and still could not reach full certainty, because the proof was too large for them.
The formal proof changed what a reader must trust: no longer the many programs of 1998, but only the kernels of two proof assistants and the formal statement.

## Explanations

### L1 human

Grocers stack oranges in layers, each orange in a dip of the layer below, and the oranges fill about $74\%$ of the space.
Kepler guessed in 1611 that no arrangement of equal balls fills more.
Thomas Hales announced a proof in 1998, with a computer that checked thousands of cases.
The referees of the journal worked for years, and in the end they were "99% certain" that the proof was right.
To remove the last doubt, Hales led a team that wrote the whole proof in a form that a proof-checking program could check.
The work took more than ten years and was finished in 2014.

### L2 human

We first check the density of the orange stack, the face-centered cubic packing.
A cube of side $a$ in this packing contains $4$ whole balls, and the balls touch along the diagonals of the faces, so $4r = a\sqrt{2}$.
The fraction of the cube that the balls fill is
$$\frac{4 \cdot \tfrac{4}{3}\pi r^3}{a^3} = \frac{\tfrac{16}{3}\pi r^3}{(2\sqrt{2}\, r)^3} = \frac{16 \pi}{3 \cdot 16 \sqrt{2}} = \frac{\pi}{3\sqrt{2}} = \frac{\pi}{\sqrt{18}}.$$
Check: $\pi / \sqrt{18} \approx 3.1416 / 4.2426 \approx 0.7405$.

Next we read the stages of acceptance as answers to the question "what must a reader trust?".
Before 2003 a reader had to trust the written argument, the programs of Hales and Ferguson, and the machines that ran them.
After the report of 2003 the written argument had been checked by experts, but the programs only in part.
After 2014 the argument and the computations had both been checked by HOL Light and Isabelle, so a reader must trust only their kernels and the formal statement.

The typical use of this pattern is a proof whose size exceeds what referees can check, so that a machine check becomes part of acceptance.
Watch out for the idea that the formal proof copies the proof of 1998 line by line, since it follows the blueprint of 2012, which reorganized the argument.
