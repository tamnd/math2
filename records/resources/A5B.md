---
records:
    - id: A5BNSFPM3K
      kind: problem-set
      title: Kvant 1981, no. 6
      creators:
        - name: Kvant editorial board
          role: editor
      date: "1981"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "1981"
          structure: A5BNSFPM3K/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
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
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
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
      msc:
        - code: 81-XX
          from: arxiv
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
          language: en
          date: "2024-03-07"
          ids:
            arxiv: "2403.04887"
            doi: 10.1088/1751-8121/ad6c02
            zbl: "1547.35736"
            zbl_id: "7909764"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2403.04887"
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "7909764"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
---
