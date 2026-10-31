---
records:
    - id: XYV2CGF58K
      kind: problem-set
      title: Kvant 1992, no. 12
      date: "1992"
      expressions:
        - key: e1
          kind: edition
          date: "1992"
          structure: XYV2CGF58K/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1992-12
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: XYVSD6A7GV
      kind: preprint
      title: Spatially Explicit Optimal Harvesting and Adjoint-Based Diagnostics for Nonlinear Biomass Dynamics
      creators:
        - name: Tin Nwe Aye
          role: author
        - name: Wolfgang Bock
          role: author
      date: "2026-10-06"
      subjects:
        - system: arxiv
          code: math.OC
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-06"
          ids:
            arxiv: "2610.08374"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.08374"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
