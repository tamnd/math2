---
tag: 2A7JZAYKR8
kind: statement
role: proposition
name: Logic formula minimization
sources:
  - wikipedia: en:89371@r1365055466
    locator: Combinational logic, section Logic formula minimization
    note: adopted
    mention: wikipedia://en/89371#JJNT
    sections: [Statement]
inventory: [9DJTNX062G]
---

## Statement

Minimization (simplification) of combinational logic formulas is done using the following rules based on the laws of Boolean algebra:

$$\begin{aligned} (A \vee B) \wedge (A \vee C) &= A \vee (B \wedge C) \\ (A \wedge B) \vee (A \wedge C) &= A \wedge (B \vee C) \end{aligned}$$

$$\begin{aligned} A \vee (A \wedge B) &= A \\ A \wedge (A \vee B) &= A \end{aligned}$$

$$\begin{aligned} A \vee (\lnot A \wedge B) &= A \vee B \\ A \wedge(\lnot A \vee B) &= A \wedge B \end{aligned}$$

$$\begin{aligned} (A \vee B)\wedge(\lnot A \vee B)&=B \\ (A \wedge B) \vee (\lnot A \wedge B)&=B \end{aligned}$$

$$\begin{aligned} (A \wedge B) \vee (\lnot A \wedge C) \vee (B \wedge C) &= (A \wedge B) \vee (\lnot A \wedge C) \\ (A \vee B) \wedge (\lnot A \vee C) \wedge (B \vee C) &= (A \vee B) \wedge (\lnot A \vee C) \end{aligned}$$

With the use of minimization (sometimes called logic optimization), a simplified logical function or circuit may be arrived upon, and the logic combinational circuit becomes smaller, and easier to analyse, use, or build.
