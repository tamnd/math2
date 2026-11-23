---
tag: PD9NCAT86M
kind: example
name: Two independent agents in a STIT model
msc: ["03B45"]
topics: [CQM9SRN8PM]
audience: research
instance_of: [WYY2JXWMYY]
uses: [WYY2JXWMYY, 2S27CNRV3S]
sources:
  - url: https://en.wikipedia.org/wiki/STIT_logic
    locator: Group agency and joint action
---

## Example

Two agents $1$ and $2$ must each press button $0$ or button $1$ at a moment $m$.
There are four histories $h_{ab}$ for $a, b \in \{0, 1\}$, where $a$ is the button of agent 1 and $b$ is the button of agent 2.
The partitions are as follows.
$$\mathrm{Choice}^m_1 = \{\{h_{00}, h_{01}\}, \{h_{10}, h_{11}\}\}, \qquad \mathrm{Choice}^m_2 = \{\{h_{00}, h_{10}\}, \{h_{01}, h_{11}\}\}$$
The door opens, written $p$, only on $h_{11}$.
We evaluate the operators of [[STIT logic|WYY2JXWMYY]] at $m$, as in [[the one-agent model|2S27CNRV3S]].

1. Independence holds: a cell of agent 1 fixes $a$, a cell of agent 2 fixes $b$, and their intersection is $\{h_{ab}\}$, which is nonempty.
2. At $m/h_{11}$ the cell of agent 1 is $\{h_{10}, h_{11}\}$, and $p$ fails at $m/h_{10}$.
   So $[1]p$ is false.
3. At $m/h_{11}$ the cell of agent 2 is $\{h_{01}, h_{11}\}$, and $p$ fails at $m/h_{01}$.
   So $[2]p$ is false.
4. The group cell at $m/h_{11}$ is $\{h_{10}, h_{11}\} \cap \{h_{01}, h_{11}\} = \{h_{11}\}$.
   So $[\{1, 2\}]p$ is true.
5. Let $q$ be true on $h_{10}$ and $h_{11}$ (agent 1 presses $1$), and let $r$ be true on $h_{01}$ and $h_{11}$ (agent 2 presses $1$).
   Then $[1]q$ holds at $m/h_{10}$ and $m/h_{11}$, and $[2]r$ holds at $m/h_{01}$ and $m/h_{11}$.
6. So $\lozenge[1]q \wedge \lozenge[2]r$ is true at $m/h_{00}$.
7. At $m/h_{11}$ both $[1]q$ and $[2]r$ hold, so $\lozenge([1]q \wedge [2]r)$ is true at $m/h_{00}$, as the independence axiom predicts.
8. At $m/h_{10}$ the cell of agent 2 is $\{h_{00}, h_{10}\}$, and $\neg p$ holds on both.
   So $[2]\neg p$ is true there: agent 2 alone keeps the door shut.

## Remarks

The model shows joint agency.
The door opens only by the action of both agents, and neither agent alone sees to it.
Each agent alone can prevent the result, since pressing $0$ guarantees $\neg p$.
If $p$ were true on $h_{10}$ and $h_{11}$, then agent 1 alone would see to $p$ by pressing $1$, and the choice of agent 2 would not matter.
The product form of the histories, one coordinate per agent, is the standard way to make choices independent.

## Explanations

### L1 human

A door has two locks, and each of two people holds one key.
The door opens only if both turn their keys.
Neither person alone can make the door open.
Together they can, and either of them alone can keep it shut.

### L2 human

List the four histories as pairs of buttons, $00, 01, 10, 11$, in a two by two table.
A cell of agent 1 is a row of the table, and a cell of agent 2 is a column.
A row and a column always meet in one square, and that is independence.
To test $[G]p$, intersect the cells of the agents in $G$ and check $p$ on the result.
The typical use of such a model is to analyze shared responsibility.
Watch out: the group operator is not the conjunction $[1]p \wedge [2]p$.
At $m/h_{11}$ that conjunction is false, while $[\{1, 2\}]p$ is true.
