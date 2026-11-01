---
records:
    - id: XYV2CGF58K
      kind: problem-set
      title: Kvant 1992, no. 12
      creators:
        - name: Kvant editorial board
          role: editor
      date: "1992"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "1992"
          structure: XYV2CGF58K/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
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
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
    - id: XYVSD6A7GV
      kind: preprint
      title: Spatially Explicit Optimal Harvesting and Adjoint-Based Diagnostics for Nonlinear Biomass Dynamics
      creators:
        - name: Tin Nwe Aye
          role: author
        - name: Wolfgang Bock
          role: author
      date: "2026-10-06"
      msc:
        - code: 49-XX
          from: arxiv
        - code: 90-XX
          from: arxiv
        - code: 93-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.OC
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-10-06"
          ids:
            arxiv: "2610.08374"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.08374"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2610.08374"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
