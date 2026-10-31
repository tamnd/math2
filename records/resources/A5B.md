---
records:
    - id: A5BNSFPM3K
      kind: problem-set
      title: Kvant 1981, no. 6
      date: "1981"
      expressions:
        - key: e1
          kind: edition
          date: "1981"
          structure: A5BNSFPM3K/e1.json
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
          native_id: 1981-6
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: A5BW1KBV63
      kind: preprint
      title: Fractional diffusion equations interpolate between damping and waves
      creators:
        - name: Andy Manapany
          role: author
        - name: Sébastien Fumeron
          role: author
        - name: Malte Henkel
          role: author
      date: "2024-03-07"
      subjects:
        - system: arxiv
          code: math-ph
        - system: arxiv
          code: cond-mat.stat-mech
        - system: arxiv
          code: hep-th
        - system: arxiv
          code: math.MP
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2024-03-07"
          ids:
            arxiv: "2403.04887"
            doi: 10.1088/1751-8121/ad6c02
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2403.04887"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
