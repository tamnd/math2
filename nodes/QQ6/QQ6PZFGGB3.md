---
tag: QQ6PZFGGB3
kind: statement
role: theorem
name: Löb's theorem in provability logic
sources:
  - wikipedia: en:693002@r1343042369
    locator: Löb's theorem, section Löb's theorem in provability logic
    note: adopted
    mention: wikipedia://en/693002#SMBU
    sections: [Statement]
inventory: [1WWMN5M6CY]
---

## Statement

Provability logic abstracts away from the details of encodings used in Gödel's incompleteness theorems by expressing the provability of $\phi$ in the given system in the language of modal logic, by means of the modality $\Box \phi$. That is, when $\phi$ is a logical formula, another formula can be formed by placing a box in front of $\phi$, and is intended to mean that $\phi$ is provable.

Then we can formalize Löb's theorem by the axiom

$$\Box(\Box P\rightarrow P)\rightarrow \Box P,$$

known as axiom GL, for Gödel–Löb. This is sometimes formalized by means of the inference rule:

If

$$\vdash \Box P \rightarrow P$$

then

$$\vdash P.$$

The provability logic **GL** that results from taking the modal logic **K4** (or **K**, since the axiom schema 4, $\Box A\rightarrow\Box\Box A$, then becomes redundant) and adding the above axiom GL is the most intensely investigated system in provability logic.
