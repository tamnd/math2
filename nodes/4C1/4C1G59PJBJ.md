---
tag: 4C1G59PJBJ
kind: definition
name: Polytropic process
msc: [80A05, 80A10]
defines: 6YYBD15JCZ
uses: [PVDWD7HGFG, WYAY33ZVYQ, C9MM7GFRWN, ECAXF3AWWX, YT8APTNYD5, N7R0H2VNDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Polytropic_process
---

## Definition

Let $n$ be a real number.
A [[quasistatic process|PVDWD7HGFG]] of a fluid with pressure $p$ and volume $V$ is *polytropic with index* $n$ if $p V^n$ is constant along the process.

## Remarks

For an [[ideal gas|N7R0H2VNDJ]] with constant heat capacity ratio $\gamma$, the special cases are as follows.
The index $n = 0$ gives an [[isobaric process|WYAY33ZVYQ]].
The index $n = 1$ gives an [[isothermal process|C9MM7GFRWN]], since a constant product $pV$ means a constant temperature for an ideal gas.
The index $n = \gamma$ gives a reversible adiabatic, hence [[isentropic|ECAXF3AWWX]], process.
In the limit $n \to \infty$ one gets an [[isochoric process|YT8APTNYD5]].
For $n \ne 1$, the work done by the fluid from $(p_1, V_1)$ to $(p_2, V_2)$ is $(p_1 V_1 - p_2 V_2) / (n - 1)$.
A process with $p = a + bV$ for constants $a, b \ne 0$ is not polytropic, since $p V^n$ is not constant along it for any $n$.
