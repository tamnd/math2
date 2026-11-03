---
tag: WB7RND95F9
kind: definition
name: Heat exchanger theory
msc: [80A19, 80A20]
defines: 97ASA870TV
uses: [J821AD6YTE, SYYGZ18FF5, KK46Q2YV1D, CY4GJQGF06]
sources:
  - url: https://en.wikipedia.org/wiki/Heat_exchanger
---

## Definition

A two-stream heat exchanger is modelled as follows.
A hot stream and a cold stream flow steadily on the two sides of a wall of area $A$.
[[Heat|CY4GJQGF06]] passes through the wall from the hot to the cold stream.
Their mass flow rates are $\dot m_h$ and $\dot m_c$, and their specific [[heat capacities|SYYGZ18FF5]] $c_{p,h}$ and $c_{p,c}$ are constant.
The heat capacity rates are $C_h = \dot m_h c_{p,h}$ and $C_c = \dot m_c c_{p,c}$.
The inlet and outlet [[temperatures|KK46Q2YV1D]] are $T_{h,i}, T_{h,o}$ and $T_{c,i}, T_{c,o}$.
The model consists of three assumptions.

1. No heat is lost to the surroundings, and no phase change occurs.
2. The total heat rate $q$ satisfies $q = C_h (T_{h,i} - T_{h,o}) = C_c (T_{c,o} - T_{c,i})$.
3. Through each element $dA$ of the wall, the heat rate is $dq = U \, (T_h - T_c) \, dA$.
   Here $T_h$ and $T_c$ are the local stream temperatures and $U$ is the overall [[heat transfer coefficient|J821AD6YTE]].

*Heat exchanger theory* is the study of this model and of its solutions for given flow arrangements.

## Remarks

Example: counterflow with $C_h = C_c$.
Along the hot stream, $dT_h = -dq/C_h$, and the cold stream, which flows the other way, also changes by $dT_c = -dq/C_c$.
So $d(T_h - T_c) = 0$, and the temperature difference is the same along the whole exchanger.

Non-example: a pipe carrying hot water through a cold room, with heat lost to the room air, is not a two-stream exchanger in this sense; clause 1 fails.

For parallel flow and counterflow with constant $U$, integration of clauses 2 and 3 gives the log mean temperature difference formula.
The overall coefficient $U$ combines the convection coefficients $h_h$, $h_c$ on both sides and the conduction resistance of the wall.
For a thin plane wall of thickness $t_w$ and conductivity $k_w$, it satisfies $1/U = 1/h_h + t_w/k_w + 1/h_c$.
